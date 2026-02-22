"""
Tests for domain modeling framework
"""

import pytest
from datetime import datetime

from domain_modeling import (
    DomainInvariant, EdgeCase, EntityLifecycle, EntityLifecycleState,
    DomainModel, DomainModelBuilder, create_authentication_model
)


class TestDomainInvariant:
    
    def test_create_invariant(self):
        invariant = DomainInvariant(
            name="unique_email",
            description="Each user must have unique email",
            rule="No duplicate emails allowed",
            priority=1
        )
        assert invariant.name == "unique_email"
        assert invariant.priority == 1
    
    def test_invariant_validation(self):
        with pytest.raises(ValueError, match="name cannot be empty"):
            DomainInvariant("", "desc", "rule")
        
        with pytest.raises(ValueError, match="description cannot be empty"):
            DomainInvariant("name", "", "rule")


class TestEdgeCase:
    
    def test_create_edge_case(self):
        case = EdgeCase(
            scenario="High traffic spike",
            impact="critical",
            likelihood=3,
            mitigation="Auto-scaling"
        )
        assert case.scenario == "High traffic spike"
        assert case.mitigation == "Auto-scaling"
    
    def test_risk_score_calculation(self):
        case = EdgeCase(
            scenario="System failure",
            impact="critical", 
            likelihood=4
        )
        # critical = 5, likelihood = 4, so 5 * 4 = 20
        assert case.risk_score() == 20
    
    def test_risk_score_unknown_impact(self):
        case = EdgeCase(
            scenario="Unknown issue",
            impact="unknown_severity",
            likelihood=3
        )
        # Should default to medium = 3, so 3 * 3 = 9
        assert case.risk_score() == 9


class TestEntityLifecycle:
    
    def test_create_entity(self):
        entity = EntityLifecycle("User")
        assert entity.entity_name == "User"
        assert EntityLifecycleState.CREATED in entity.states
        assert EntityLifecycleState.ACTIVE in entity.states
    
    def test_add_transition(self):
        entity = EntityLifecycle("Order")
        entity.add_transition(EntityLifecycleState.CREATED, EntityLifecycleState.ACTIVE)
        
        assert entity.can_transition(EntityLifecycleState.CREATED, EntityLifecycleState.ACTIVE)
        assert not entity.can_transition(EntityLifecycleState.ACTIVE, EntityLifecycleState.CREATED)
    
    def test_empty_entity_name(self):
        with pytest.raises(ValueError, match="Entity name cannot be empty"):
            EntityLifecycle("")


class TestDomainModel:
    
    def test_create_model(self):
        model = DomainModel("Test System", "A test system")
        assert model.name == "Test System"
        assert len(model.invariants) == 0
        assert len(model.edge_cases) == 0
    
    def test_add_invariant(self):
        model = DomainModel("Test", "Test")
        invariant = DomainInvariant("test", "test desc", "test rule")
        
        model.add_invariant(invariant)
        assert len(model.invariants) == 1
        assert model.invariants[0] == invariant
    
    def test_add_invalid_invariant(self):
        model = DomainModel("Test", "Test")
        
        with pytest.raises(TypeError):
            model.add_invariant("not an invariant")
    
    def test_add_edge_case(self):
        model = DomainModel("Test", "Test")
        case = EdgeCase("scenario", "impact", 3)
        
        model.add_edge_case(case)
        assert len(model.edge_cases) == 1
    
    def test_add_assumption(self):
        model = DomainModel("Test", "Test")
        model.add_assumption("Users prefer simple interfaces")
        
        assert len(model.assumptions) == 1
        assert "Users prefer simple interfaces" in model.assumptions
    
    def test_add_empty_assumption(self):
        model = DomainModel("Test", "Test")
        
        with pytest.raises(ValueError, match="Assumption cannot be empty"):
            model.add_assumption("   ")
    
    def test_get_critical_invariants(self):
        model = DomainModel("Test", "Test")
        critical = DomainInvariant("critical", "critical desc", "rule", priority=1)
        important = DomainInvariant("important", "important desc", "rule", priority=2)
        
        model.add_invariant(critical)
        model.add_invariant(important)
        
        critical_list = model.get_critical_invariants()
        assert len(critical_list) == 1
        assert critical_list[0] == critical
    
    def test_get_high_risk_cases(self):
        model = DomainModel("Test", "Test")
        high_risk = EdgeCase("high risk", "critical", 5)  # 5 * 5 = 25
        low_risk = EdgeCase("low risk", "low", 2)  # 2 * 2 = 4
        
        model.add_edge_case(high_risk)
        model.add_edge_case(low_risk)
        
        high_risk_list = model.get_high_risk_cases(threshold=20)
        assert len(high_risk_list) == 1
        assert high_risk_list[0] == high_risk
    
    def test_to_dict(self):
        model = DomainModel("Test System", "Test description")
        model.add_assumption("Test assumption")
        
        dict_repr = model.to_dict()
        assert dict_repr['name'] == "Test System"
        assert dict_repr['description'] == "Test description"
        assert len(dict_repr['assumptions']) == 1
        assert 'created_at' in dict_repr
    
    def test_to_json(self):
        model = DomainModel("Test", "Test")
        json_str = model.to_json()
        
        assert isinstance(json_str, str)
        assert "Test" in json_str


class TestDomainModelBuilder:
    
    def test_builder_basic(self):
        model = (DomainModelBuilder("Test System", "Description")
                .with_assumption("Test assumption")
                .build())
        
        assert model.name == "Test System"
        assert len(model.assumptions) == 1
    
    def test_builder_with_invariant(self):
        model = (DomainModelBuilder("Test", "Test")
                .with_invariant("test_inv", "test desc", "test rule", priority=2)
                .build())
        
        assert len(model.invariants) == 1
        assert model.invariants[0].name == "test_inv"
        assert model.invariants[0].priority == 2
    
    def test_builder_with_edge_case(self):
        model = (DomainModelBuilder("Test", "Test")
                .with_edge_case("scenario", "high", 4, "mitigation")
                .build())
        
        assert len(model.edge_cases) == 1
        assert model.edge_cases[0].scenario == "scenario"
        assert model.edge_cases[0].mitigation == "mitigation"
    
    def test_builder_with_entity(self):
        model = (DomainModelBuilder("Test", "Test")
                .with_entity("User")
                    .with_states(EntityLifecycleState.CREATED, EntityLifecycleState.ACTIVE)
                    .with_transition(EntityLifecycleState.CREATED, EntityLifecycleState.ACTIVE)
                    .with_business_event("UserCreated")
                    .and_model()
                .build())
        
        assert len(model.entities) == 1
        entity = model.entities[0]
        assert entity.entity_name == "User"
        assert len(entity.states) == 3  # CREATED, ACTIVE, ARCHIVED (default states)
        assert EntityLifecycleState.CREATED in entity.states
        assert EntityLifecycleState.ACTIVE in entity.states
        assert "UserCreated" in entity.business_events
    
    def test_entity_builder_chain(self):
        builder = DomainModelBuilder("Test", "Test")
        entity_builder = builder.with_entity("Order")
        
        # Should be able to chain entity builder methods
        final_builder = (entity_builder
                        .with_states(EntityLifecycleState.CREATED)
                        .with_business_event("OrderCreated")
                        .and_model())
        
        assert final_builder == builder  # Should return to original builder


class TestCreateAuthenticationModel:
    
    def test_create_auth_model(self):
        model = create_authentication_model()
        
        assert model.name == "User Authentication"
        assert len(model.invariants) >= 2  # Should have unique_email and password_strength
        assert len(model.edge_cases) >= 2  # Should have some edge cases
        assert len(model.entities) >= 1   # Should have User entity
        assert len(model.assumptions) >= 2 # Should have assumptions
    
    def test_auth_model_has_critical_invariants(self):
        model = create_authentication_model()
        critical = model.get_critical_invariants()
        
        assert len(critical) >= 2
        invariant_names = [inv.name for inv in critical]
        assert "unique_email" in invariant_names
        assert "password_strength" in invariant_names
    
    def test_auth_model_user_entity(self):
        model = create_authentication_model()
        
        # Should have a User entity
        user_entities = [e for e in model.entities if e.entity_name == "User"]
        assert len(user_entities) == 1
        
        user_entity = user_entities[0]
        assert EntityLifecycleState.CREATED in user_entity.states
        assert EntityLifecycleState.ACTIVE in user_entity.states
        assert "UserRegistered" in user_entity.business_events
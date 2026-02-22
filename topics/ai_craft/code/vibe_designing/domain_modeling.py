"""
Domain Modeling Framework for Vibe Designing

This module implements the core concepts from TAM4: From Vibe Coding to Vibe Designing,
focusing on tools for deeper problem modeling and design thinking before code generation.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Set, Optional, Any, Callable
from enum import Enum
import json
from datetime import datetime


class EntityLifecycleState(Enum):
    """States in an entity's lifecycle"""
    CREATED = "created"
    ACTIVE = "active" 
    SUSPENDED = "suspended"
    ARCHIVED = "archived"
    DELETED = "deleted"


@dataclass
class DomainInvariant:
    """A business rule or constraint that must always hold true"""
    name: str
    description: str
    rule: str  # Natural language description of the rule
    validation_function: Optional[Callable] = None
    priority: int = 1  # 1=critical, 2=important, 3=nice-to-have
    
    def __post_init__(self):
        if not self.name:
            raise ValueError("Invariant name cannot be empty")
        if not self.description:
            raise ValueError("Invariant description cannot be empty")


@dataclass 
class EdgeCase:
    """A potential edge case or failure mode"""
    scenario: str
    impact: str  # What happens if this occurs
    likelihood: int  # 1-5 scale
    mitigation: Optional[str] = None
    
    def risk_score(self) -> int:
        """Calculate risk score based on likelihood and impact severity"""
        impact_levels = {
            "critical": 5, "high": 4, "medium": 3, "low": 2, "minimal": 1
        }
        severity = impact_levels.get(self.impact.lower(), 3)
        return self.likelihood * severity


@dataclass
class EntityLifecycle:
    """Models the lifecycle and state transitions of a domain entity"""
    entity_name: str
    states: Set[EntityLifecycleState] = field(default_factory=set)
    transitions: Dict[str, Set[EntityLifecycleState]] = field(default_factory=dict)
    business_events: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        if not self.entity_name:
            raise ValueError("Entity name cannot be empty")
        
        # Add default states if none provided
        if not self.states:
            self.states = {
                EntityLifecycleState.CREATED,
                EntityLifecycleState.ACTIVE,
                EntityLifecycleState.ARCHIVED
            }
    
    def add_transition(self, from_state: EntityLifecycleState, to_state: EntityLifecycleState):
        """Add a valid state transition"""
        if from_state not in self.transitions:
            self.transitions[from_state.value] = set()
        self.transitions[from_state.value].add(to_state)
    
    def can_transition(self, from_state: EntityLifecycleState, to_state: EntityLifecycleState) -> bool:
        """Check if a state transition is valid"""
        return to_state in self.transitions.get(from_state.value, set())


@dataclass
class DomainModel:
    """A comprehensive model of a problem domain before coding"""
    name: str
    description: str
    invariants: List[DomainInvariant] = field(default_factory=list)
    edge_cases: List[EdgeCase] = field(default_factory=list)
    entities: List[EntityLifecycle] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    
    def add_invariant(self, invariant: DomainInvariant):
        """Add a domain invariant with validation"""
        if not isinstance(invariant, DomainInvariant):
            raise TypeError("Expected DomainInvariant instance")
        self.invariants.append(invariant)
    
    def add_edge_case(self, edge_case: EdgeCase):
        """Add an edge case with validation"""
        if not isinstance(edge_case, EdgeCase):
            raise TypeError("Expected EdgeCase instance")
        self.edge_cases.append(edge_case)
    
    def add_entity(self, entity: EntityLifecycle):
        """Add an entity lifecycle"""
        if not isinstance(entity, EntityLifecycle):
            raise TypeError("Expected EntityLifecycle instance")
        self.entities.append(entity)
    
    def add_assumption(self, assumption: str):
        """Add a domain assumption to be validated"""
        if not assumption.strip():
            raise ValueError("Assumption cannot be empty")
        self.assumptions.append(assumption.strip())
    
    def get_critical_invariants(self) -> List[DomainInvariant]:
        """Get all critical priority invariants"""
        return [inv for inv in self.invariants if inv.priority == 1]
    
    def get_high_risk_cases(self, threshold: int = 15) -> List[EdgeCase]:
        """Get edge cases above risk threshold"""
        return [case for case in self.edge_cases if case.risk_score() >= threshold]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        return {
            'name': self.name,
            'description': self.description,
            'invariants': [
                {
                    'name': inv.name,
                    'description': inv.description,
                    'rule': inv.rule,
                    'priority': inv.priority
                } for inv in self.invariants
            ],
            'edge_cases': [
                {
                    'scenario': case.scenario,
                    'impact': case.impact,
                    'likelihood': case.likelihood,
                    'mitigation': case.mitigation,
                    'risk_score': case.risk_score()
                } for case in self.edge_cases
            ],
            'entities': [
                {
                    'name': entity.entity_name,
                    'states': [state.value for state in entity.states],
                    'transitions': {k: [s.value for s in v] for k, v in entity.transitions.items()},
                    'business_events': entity.business_events
                } for entity in self.entities
            ],
            'assumptions': self.assumptions,
            'created_at': self.created_at.isoformat()
        }
    
    def to_json(self) -> str:
        """Convert to JSON string"""
        return json.dumps(self.to_dict(), indent=2)


class DomainModelBuilder:
    """Builder pattern for creating domain models step by step"""
    
    def __init__(self, name: str, description: str):
        self.model = DomainModel(name=name, description=description)
    
    def with_invariant(self, name: str, description: str, rule: str, priority: int = 1) -> 'DomainModelBuilder':
        """Add a domain invariant"""
        invariant = DomainInvariant(
            name=name,
            description=description, 
            rule=rule,
            priority=priority
        )
        self.model.add_invariant(invariant)
        return self
    
    def with_edge_case(self, scenario: str, impact: str, likelihood: int, mitigation: str = None) -> 'DomainModelBuilder':
        """Add an edge case"""
        edge_case = EdgeCase(
            scenario=scenario,
            impact=impact,
            likelihood=likelihood,
            mitigation=mitigation
        )
        self.model.add_edge_case(edge_case)
        return self
    
    def with_entity(self, name: str) -> 'EntityBuilder':
        """Start building an entity lifecycle"""
        return EntityBuilder(self, name)
    
    def with_assumption(self, assumption: str) -> 'DomainModelBuilder':
        """Add a domain assumption"""
        self.model.add_assumption(assumption)
        return self
    
    def build(self) -> DomainModel:
        """Build the final domain model"""
        return self.model


class EntityBuilder:
    """Builder for entity lifecycles within a domain model"""
    
    def __init__(self, parent_builder: DomainModelBuilder, entity_name: str):
        self.parent_builder = parent_builder
        self.entity = EntityLifecycle(entity_name=entity_name)
    
    def with_states(self, *states: EntityLifecycleState) -> 'EntityBuilder':
        """Add lifecycle states"""
        self.entity.states.update(states)
        return self
    
    def with_transition(self, from_state: EntityLifecycleState, to_state: EntityLifecycleState) -> 'EntityBuilder':
        """Add a state transition"""
        self.entity.add_transition(from_state, to_state)
        return self
    
    def with_business_event(self, event: str) -> 'EntityBuilder':
        """Add a business event"""
        self.entity.business_events.append(event)
        return self
    
    def and_model(self) -> DomainModelBuilder:
        """Finish building entity and return to model builder"""
        self.parent_builder.model.add_entity(self.entity)
        return self.parent_builder


def create_authentication_model() -> DomainModel:
    """Example: Create a domain model for user authentication system"""
    return (DomainModelBuilder("User Authentication", "System for managing user login and security")
        .with_invariant(
            "unique_email",
            "Each user must have a unique email address",
            "No two active users can have the same email address",
            priority=1
        )
        .with_invariant(
            "password_strength", 
            "Passwords must meet minimum security requirements",
            "Password must be at least 8 characters with uppercase, lowercase, number, and symbol",
            priority=1
        )
        .with_edge_case(
            "Email enumeration attack",
            "high",
            3,
            "Return consistent response times regardless of email existence"
        )
        .with_edge_case(
            "Account locked due to failed attempts",
            "medium", 
            4,
            "Implement exponential backoff and admin unlock capability"
        )
        .with_assumption("Users will remember their passwords most of the time")
        .with_assumption("Email delivery is reliable within 5 minutes")
        .with_entity("User")
            .with_states(
                EntityLifecycleState.CREATED,
                EntityLifecycleState.ACTIVE,
                EntityLifecycleState.SUSPENDED,
                EntityLifecycleState.DELETED
            )
            .with_transition(EntityLifecycleState.CREATED, EntityLifecycleState.ACTIVE)
            .with_transition(EntityLifecycleState.ACTIVE, EntityLifecycleState.SUSPENDED)
            .with_transition(EntityLifecycleState.SUSPENDED, EntityLifecycleState.ACTIVE)
            .with_transition(EntityLifecycleState.ACTIVE, EntityLifecycleState.DELETED)
            .with_business_event("UserRegistered")
            .with_business_event("EmailVerified")
            .with_business_event("PasswordChanged")
            .with_business_event("AccountLocked")
            .and_model()
        .build())
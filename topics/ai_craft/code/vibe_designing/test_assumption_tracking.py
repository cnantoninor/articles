"""
Tests for assumption tracking system
"""

import pytest
from datetime import datetime, timedelta

from assumption_tracking import (
    Evidence, ValidationTask, Assumption, AssumptionStatus, ValidationMethod,
    AssumptionRegistry, create_sample_registry
)


class TestEvidence:
    
    def test_create_evidence(self):
        evidence = Evidence(
            description="Study shows 80% user satisfaction",
            source="User Research Team",
            supports=True,
            confidence=4,
            url_or_reference="https://example.com/study"
        )
        
        assert evidence.description == "Study shows 80% user satisfaction"
        assert evidence.supports is True
        assert evidence.confidence == 4
        assert evidence.url_or_reference == "https://example.com/study"
    
    def test_evidence_validation(self):
        with pytest.raises(ValueError, match="Evidence description cannot be empty"):
            Evidence("", "source", True, 3)
        
        with pytest.raises(ValueError, match="Evidence source cannot be empty"):
            Evidence("description", "", True, 3)
        
        with pytest.raises(ValueError, match="Confidence must be 1-5"):
            Evidence("description", "source", True, 6)


class TestValidationTask:
    
    def test_create_task(self):
        task = ValidationTask(
            description="Survey users about notification preferences",
            method=ValidationMethod.USER_RESEARCH,
            assigned_to="UX Team"
        )
        
        assert task.description == "Survey users about notification preferences"
        assert task.method == ValidationMethod.USER_RESEARCH
        assert task.assigned_to == "UX Team"
        assert not task.completed
    
    def test_mark_complete(self):
        task = ValidationTask("Test task", ValidationMethod.DATA_ANALYSIS)
        evidence = [Evidence("Test evidence", "Test source", True, 3)]
        
        task.mark_complete("Task completed successfully", evidence)
        
        assert task.completed
        assert task.results == "Task completed successfully"
        assert len(task.evidence_found) == 1


class TestAssumption:
    
    def test_create_assumption(self):
        assumption = Assumption(
            id="user_engagement",
            description="Users will engage with notifications",
            context="Feature planning discussion",
            impact_if_wrong="Low adoption rates",
            priority=1
        )
        
        assert assumption.id == "user_engagement"
        assert assumption.priority == 1
        assert assumption.status == AssumptionStatus.UNVALIDATED
    
    def test_assumption_validation(self):
        with pytest.raises(ValueError, match="Assumption ID cannot be empty"):
            Assumption("", "description", "context", "impact")
        
        with pytest.raises(ValueError, match="Assumption description cannot be empty"):
            Assumption("id", "", "context", "impact")
        
        with pytest.raises(ValueError, match="Priority must be 1-3"):
            Assumption("id", "description", "context", "impact", priority=4)
    
    def test_add_evidence_supporting(self):
        assumption = Assumption("test", "test desc", "context", "impact")
        evidence = Evidence("Supporting evidence", "source", supports=True, confidence=4)
        
        assumption.add_evidence(evidence)
        
        assert len(assumption.evidence) == 1
        assert assumption.status == AssumptionStatus.CONFIRMED
    
    def test_add_evidence_contradicting(self):
        assumption = Assumption("test", "test desc", "context", "impact")
        evidence = Evidence("Contradicting evidence", "source", supports=False, confidence=5)
        
        assumption.add_evidence(evidence)
        
        assert assumption.status == AssumptionStatus.REFUTED
    
    def test_add_evidence_mixed(self):
        assumption = Assumption("test", "test desc", "context", "impact")
        
        # Add supporting evidence
        assumption.add_evidence(Evidence("Support", "source", True, 3))
        # Add contradicting evidence of similar strength
        assumption.add_evidence(Evidence("Contradict", "source", False, 3))
        
        # Should be conditional when evidence is mixed
        assert assumption.status == AssumptionStatus.CONDITIONAL
    
    def test_add_validation_task(self):
        assumption = Assumption("test", "test desc", "context", "impact")
        task = ValidationTask("Validate this", ValidationMethod.USER_RESEARCH)
        
        assumption.add_validation_task(task)
        
        assert len(assumption.validation_tasks) == 1
        assert assumption.status == AssumptionStatus.VALIDATING
    
    def test_is_stale_no_review(self):
        assumption = Assumption("test", "test desc", "context", "impact")
        assert assumption.is_stale(days=30)  # Never reviewed, should be stale
    
    def test_is_stale_recent_review(self):
        assumption = Assumption("test", "test desc", "context", "impact")
        assumption.last_reviewed = datetime.now() - timedelta(days=10)
        
        assert not assumption.is_stale(days=30)  # Recently reviewed
    
    def test_is_stale_old_review(self):
        assumption = Assumption("test", "test desc", "context", "impact")
        assumption.last_reviewed = datetime.now() - timedelta(days=45)
        
        assert assumption.is_stale(days=30)  # Old review
    
    def test_validation_progress_no_tasks(self):
        assumption = Assumption("test", "test desc", "context", "impact")
        assert assumption.get_validation_progress() == 0.0
    
    def test_validation_progress_partial(self):
        assumption = Assumption("test", "test desc", "context", "impact")
        
        task1 = ValidationTask("Task 1", ValidationMethod.USER_RESEARCH)
        task2 = ValidationTask("Task 2", ValidationMethod.DATA_ANALYSIS) 
        task1.completed = True
        
        assumption.validation_tasks = [task1, task2]
        
        assert assumption.get_validation_progress() == 0.5


class TestAssumptionRegistry:
    
    def test_create_registry(self):
        registry = AssumptionRegistry("Test Project")
        
        assert registry.project_name == "Test Project"
        assert len(registry.assumptions) == 0
    
    def test_add_assumption(self):
        registry = AssumptionRegistry("Test")
        assumption = Assumption("test_id", "test desc", "context", "impact")
        
        registry.add_assumption(assumption)
        
        assert len(registry.assumptions) == 1
        assert registry.assumptions["test_id"] == assumption
    
    def test_add_duplicate_assumption(self):
        registry = AssumptionRegistry("Test")
        assumption1 = Assumption("test_id", "desc1", "context", "impact")
        assumption2 = Assumption("test_id", "desc2", "context", "impact")
        
        registry.add_assumption(assumption1)
        
        with pytest.raises(ValueError, match="Assumption with ID 'test_id' already exists"):
            registry.add_assumption(assumption2)
    
    def test_get_assumption(self):
        registry = AssumptionRegistry("Test")
        assumption = Assumption("test_id", "test desc", "context", "impact")
        registry.add_assumption(assumption)
        
        retrieved = registry.get_assumption("test_id")
        assert retrieved == assumption
        
        not_found = registry.get_assumption("nonexistent")
        assert not_found is None
    
    def test_remove_assumption(self):
        registry = AssumptionRegistry("Test")
        assumption = Assumption("test_id", "test desc", "context", "impact")
        registry.add_assumption(assumption)
        
        registry.remove_assumption("test_id")
        
        assert len(registry.assumptions) == 0
        assert registry.get_assumption("test_id") is None
    
    def test_get_by_status(self):
        registry = AssumptionRegistry("Test")
        
        unvalidated = Assumption("unval", "desc", "context", "impact")
        confirmed = Assumption("conf", "desc", "context", "impact")
        confirmed.status = AssumptionStatus.CONFIRMED
        
        registry.add_assumption(unvalidated)
        registry.add_assumption(confirmed)
        
        unvalidated_list = registry.get_by_status(AssumptionStatus.UNVALIDATED)
        assert len(unvalidated_list) == 1
        assert unvalidated_list[0] == unvalidated
        
        confirmed_list = registry.get_by_status(AssumptionStatus.CONFIRMED)
        assert len(confirmed_list) == 1
        assert confirmed_list[0] == confirmed
    
    def test_get_by_priority(self):
        registry = AssumptionRegistry("Test")
        
        critical = Assumption("crit", "desc", "context", "impact", priority=1)
        important = Assumption("imp", "desc", "context", "impact", priority=2)
        
        registry.add_assumption(critical)
        registry.add_assumption(important)
        
        critical_list = registry.get_by_priority(1)
        assert len(critical_list) == 1
        assert critical_list[0] == critical
    
    def test_get_stale_assumptions(self):
        registry = AssumptionRegistry("Test")
        
        stale = Assumption("stale", "desc", "context", "impact")
        fresh = Assumption("fresh", "desc", "context", "impact")
        fresh.last_reviewed = datetime.now() - timedelta(days=10)
        
        registry.add_assumption(stale)
        registry.add_assumption(fresh)
        
        stale_list = registry.get_stale_assumptions(days=30)
        assert len(stale_list) == 1
        assert stale_list[0] == stale
    
    def test_get_critical_unvalidated(self):
        registry = AssumptionRegistry("Test")
        
        critical_unval = Assumption("crit_unval", "desc", "context", "impact", priority=1)
        critical_val = Assumption("crit_val", "desc", "context", "impact", priority=1)
        critical_val.status = AssumptionStatus.CONFIRMED
        
        important_unval = Assumption("imp_unval", "desc", "context", "impact", priority=2)
        
        registry.add_assumption(critical_unval)
        registry.add_assumption(critical_val)
        registry.add_assumption(important_unval)
        
        critical_unvalidated = registry.get_critical_unvalidated()
        assert len(critical_unvalidated) == 1
        assert critical_unvalidated[0] == critical_unval
    
    def test_get_refuted_assumptions(self):
        registry = AssumptionRegistry("Test")
        
        refuted = Assumption("refuted", "desc", "context", "impact")
        refuted.status = AssumptionStatus.REFUTED
        
        confirmed = Assumption("confirmed", "desc", "context", "impact")
        confirmed.status = AssumptionStatus.CONFIRMED
        
        registry.add_assumption(refuted)
        registry.add_assumption(confirmed)
        
        refuted_list = registry.get_refuted_assumptions()
        assert len(refuted_list) == 1
        assert refuted_list[0] == refuted
    
    def test_create_assumption(self):
        registry = AssumptionRegistry("Test")
        
        assumption = registry.create_assumption(
            "new_id",
            "New assumption", 
            "Context",
            "Impact if wrong",
            priority=1
        )
        
        assert assumption.id == "new_id"
        assert assumption.priority == 1
        assert len(registry.assumptions) == 1
        assert registry.get_assumption("new_id") == assumption
    
    def test_add_dependency(self):
        registry = AssumptionRegistry("Test")
        
        parent = registry.create_assumption("parent", "Parent", "context", "impact")
        child = registry.create_assumption("child", "Child", "context", "impact")
        
        registry.add_dependency("child", "parent")
        
        assert "parent" in child.dependencies
    
    def test_get_dependency_chain(self):
        registry = AssumptionRegistry("Test")
        
        a = registry.create_assumption("a", "A", "context", "impact")
        b = registry.create_assumption("b", "B", "context", "impact")
        c = registry.create_assumption("c", "C", "context", "impact")
        
        # Chain: c -> b -> a
        registry.add_dependency("c", "b")
        registry.add_dependency("b", "a")
        
        chain = registry.get_dependency_chain("c")
        assert chain == {"a", "b"}  # c depends on both a and b (transitively)
    
    def test_to_dict(self):
        registry = AssumptionRegistry("Test Project")
        assumption = registry.create_assumption("test", "Test assumption", "context", "impact")
        
        dict_repr = registry.to_dict()
        
        assert dict_repr['project_name'] == "Test Project"
        assert 'created_at' in dict_repr
        assert len(dict_repr['assumptions']) == 1
        assert 'summary' in dict_repr
        
        summary = dict_repr['summary']
        assert summary['total_assumptions'] == 1
        assert 'by_status' in summary
    
    def test_to_json(self):
        registry = AssumptionRegistry("Test")
        json_str = registry.to_json()
        
        assert isinstance(json_str, str)
        assert "Test" in json_str


class TestCreateSampleRegistry:
    
    def test_create_sample_registry(self):
        registry = create_sample_registry()
        
        assert registry.project_name == "E-commerce Platform"
        assert len(registry.assumptions) >= 3  # Should have several sample assumptions
    
    def test_sample_registry_has_evidence(self):
        registry = create_sample_registry()
        
        # Should have at least one assumption with evidence
        assumptions_with_evidence = [
            a for a in registry.assumptions.values() 
            if len(a.evidence) > 0
        ]
        assert len(assumptions_with_evidence) > 0
    
    def test_sample_registry_has_tasks(self):
        registry = create_sample_registry()
        
        # Should have at least one assumption with validation tasks
        assumptions_with_tasks = [
            a for a in registry.assumptions.values() 
            if len(a.validation_tasks) > 0
        ]
        assert len(assumptions_with_tasks) > 0
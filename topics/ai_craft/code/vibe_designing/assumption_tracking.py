"""
Assumption Tracking for Vibe Designing

This module implements tools for tracking, validating, and managing assumptions
throughout the design process, as outlined in TAM4's vibe designing approach.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Any
from enum import Enum
import json
from datetime import datetime, timedelta


class AssumptionStatus(Enum):
    """Status of an assumption in the validation process"""
    UNVALIDATED = "unvalidated"  # Initial state
    VALIDATING = "validating"    # In process of validation
    CONFIRMED = "confirmed"      # Evidence supports assumption
    REFUTED = "refuted"         # Evidence contradicts assumption  
    CONDITIONAL = "conditional"  # True under certain conditions
    UNKNOWN = "unknown"         # Cannot be validated


class ValidationMethod(Enum):
    """Methods for validating assumptions"""
    USER_RESEARCH = "user_research"
    DATA_ANALYSIS = "data_analysis"
    PROTOTYPE_TESTING = "prototype_testing"
    EXPERT_CONSULTATION = "expert_consultation"
    MARKET_RESEARCH = "market_research"
    TECHNICAL_SPIKE = "technical_spike"
    A_B_TESTING = "a_b_testing"


@dataclass
class Evidence:
    """A piece of evidence supporting or refuting an assumption"""
    description: str
    source: str  # Where this evidence came from
    supports: bool  # True if supports assumption, False if contradicts
    confidence: int  # 1-5 scale of confidence in this evidence
    date_collected: datetime = field(default_factory=datetime.now)
    url_or_reference: Optional[str] = None
    
    def __post_init__(self):
        if not self.description.strip():
            raise ValueError("Evidence description cannot be empty")
        if not self.source.strip():
            raise ValueError("Evidence source cannot be empty")
        if self.confidence not in range(1, 6):
            raise ValueError("Confidence must be 1-5")


@dataclass
class ValidationTask:
    """A task to validate a specific assumption"""
    description: str
    method: ValidationMethod
    assigned_to: Optional[str] = None
    due_date: Optional[datetime] = None
    completed: bool = False
    results: Optional[str] = None
    evidence_found: List[Evidence] = field(default_factory=list)
    
    def mark_complete(self, results: str, evidence: List[Evidence] = None):
        """Mark the validation task as complete"""
        self.completed = True
        self.results = results
        if evidence:
            self.evidence_found.extend(evidence)


@dataclass  
class Assumption:
    """A trackable assumption with validation state"""
    id: str
    description: str
    context: str  # Where/why this assumption arose
    impact_if_wrong: str  # What happens if assumption is false
    priority: int = 1  # 1=critical, 2=important, 3=nice-to-have
    status: AssumptionStatus = AssumptionStatus.UNVALIDATED
    evidence: List[Evidence] = field(default_factory=list)
    validation_tasks: List[ValidationTask] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    last_reviewed: Optional[datetime] = None
    dependencies: Set[str] = field(default_factory=set)  # IDs of related assumptions
    
    def __post_init__(self):
        if not self.id.strip():
            raise ValueError("Assumption ID cannot be empty")
        if not self.description.strip():
            raise ValueError("Assumption description cannot be empty")
        if self.priority not in range(1, 4):
            raise ValueError("Priority must be 1-3")
    
    def add_evidence(self, evidence: Evidence):
        """Add evidence for or against this assumption"""
        self.evidence.append(evidence)
        self._update_status_from_evidence()
    
    def add_validation_task(self, task: ValidationTask):
        """Add a task to validate this assumption"""
        self.validation_tasks.append(task)
        if self.status == AssumptionStatus.UNVALIDATED:
            self.status = AssumptionStatus.VALIDATING
    
    def _update_status_from_evidence(self):
        """Update assumption status based on collected evidence"""
        if not self.evidence:
            return
            
        supporting_evidence = [e for e in self.evidence if e.supports]
        contradicting_evidence = [e for e in self.evidence if not e.supports]
        
        # Weight evidence by confidence
        support_score = sum(e.confidence for e in supporting_evidence)
        contradict_score = sum(e.confidence for e in contradicting_evidence)
        
        if support_score > contradict_score * 2:
            self.status = AssumptionStatus.CONFIRMED
        elif contradict_score > support_score * 2:
            self.status = AssumptionStatus.REFUTED
        elif abs(support_score - contradict_score) <= 2:
            self.status = AssumptionStatus.CONDITIONAL
        else:
            self.status = AssumptionStatus.VALIDATING
    
    def is_stale(self, days: int = 30) -> bool:
        """Check if assumption hasn't been reviewed recently"""
        if not self.last_reviewed:
            return True
        return datetime.now() - self.last_reviewed > timedelta(days=days)
    
    def get_validation_progress(self) -> float:
        """Get percentage of validation tasks completed"""
        if not self.validation_tasks:
            return 0.0
        completed = sum(1 for task in self.validation_tasks if task.completed)
        return completed / len(self.validation_tasks)


class AssumptionRegistry:
    """Registry for managing all assumptions in a project"""
    
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.assumptions: Dict[str, Assumption] = {}
        self.created_at = datetime.now()
    
    def add_assumption(self, assumption: Assumption):
        """Add an assumption to the registry"""
        if assumption.id in self.assumptions:
            raise ValueError(f"Assumption with ID '{assumption.id}' already exists")
        self.assumptions[assumption.id] = assumption
    
    def get_assumption(self, assumption_id: str) -> Optional[Assumption]:
        """Get an assumption by ID"""
        return self.assumptions.get(assumption_id)
    
    def remove_assumption(self, assumption_id: str):
        """Remove an assumption from registry"""
        if assumption_id in self.assumptions:
            del self.assumptions[assumption_id]
    
    def get_by_status(self, status: AssumptionStatus) -> List[Assumption]:
        """Get all assumptions with specific status"""
        return [a for a in self.assumptions.values() if a.status == status]
    
    def get_by_priority(self, priority: int) -> List[Assumption]:
        """Get all assumptions with specific priority"""
        return [a for a in self.assumptions.values() if a.priority == priority]
    
    def get_stale_assumptions(self, days: int = 30) -> List[Assumption]:
        """Get assumptions that haven't been reviewed recently"""
        return [a for a in self.assumptions.values() if a.is_stale(days)]
    
    def get_critical_unvalidated(self) -> List[Assumption]:
        """Get critical assumptions that are unvalidated"""
        return [
            a for a in self.assumptions.values() 
            if a.priority == 1 and a.status == AssumptionStatus.UNVALIDATED
        ]
    
    def get_refuted_assumptions(self) -> List[Assumption]:
        """Get assumptions that have been refuted by evidence"""
        return self.get_by_status(AssumptionStatus.REFUTED)
    
    def create_assumption(self, 
                         assumption_id: str,
                         description: str, 
                         context: str,
                         impact_if_wrong: str,
                         priority: int = 2) -> Assumption:
        """Create and add a new assumption"""
        assumption = Assumption(
            id=assumption_id,
            description=description,
            context=context,
            impact_if_wrong=impact_if_wrong,
            priority=priority
        )
        self.add_assumption(assumption)
        return assumption
    
    def add_dependency(self, assumption_id: str, depends_on: str):
        """Add dependency between assumptions"""
        if assumption_id in self.assumptions and depends_on in self.assumptions:
            self.assumptions[assumption_id].dependencies.add(depends_on)
    
    def get_dependency_chain(self, assumption_id: str) -> Set[str]:
        """Get all assumptions this one depends on (recursively)"""
        if assumption_id not in self.assumptions:
            return set()
        
        chain = set()
        to_check = {assumption_id}
        
        while to_check:
            current = to_check.pop()
            if current in self.assumptions:
                deps = self.assumptions[current].dependencies
                new_deps = deps - chain  # Avoid cycles
                chain.update(deps)
                to_check.update(new_deps)
        
        return chain
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert registry to dictionary for serialization"""
        return {
            'project_name': self.project_name,
            'created_at': self.created_at.isoformat(),
            'assumptions': {
                aid: {
                    'id': a.id,
                    'description': a.description,
                    'context': a.context,
                    'impact_if_wrong': a.impact_if_wrong,
                    'priority': a.priority,
                    'status': a.status.value,
                    'evidence_count': len(a.evidence),
                    'validation_progress': a.get_validation_progress(),
                    'is_stale': a.is_stale(),
                    'dependencies': list(a.dependencies),
                    'created_at': a.created_at.isoformat(),
                    'last_reviewed': a.last_reviewed.isoformat() if a.last_reviewed else None
                } for aid, a in self.assumptions.items()
            },
            'summary': {
                'total_assumptions': len(self.assumptions),
                'by_status': {
                    status.value: len(self.get_by_status(status)) 
                    for status in AssumptionStatus
                },
                'critical_unvalidated': len(self.get_critical_unvalidated()),
                'stale_assumptions': len(self.get_stale_assumptions())
            }
        }
    
    def to_json(self) -> str:
        """Convert to JSON string"""
        return json.dumps(self.to_dict(), indent=2)


def create_sample_registry() -> AssumptionRegistry:
    """Create a sample assumption registry for demonstration"""
    registry = AssumptionRegistry("E-commerce Platform")
    
    # Add some sample assumptions
    user_patience = registry.create_assumption(
        "user_patience",
        "Users will wait up to 3 seconds for page load",
        "Performance requirements discussion",
        "Increased bounce rate, reduced conversions",
        priority=1
    )
    
    user_patience.add_evidence(Evidence(
        description="Google research shows 53% of users abandon site after 3s load time",
        source="Google Think with Google study 2017",
        supports=True,
        confidence=4,
        url_or_reference="https://thinkwithgoogle.com/marketing-strategies/app-and-mobile/mobile-page-speed-load-time/"
    ))
    
    payment_methods = registry.create_assumption(
        "payment_methods",
        "Credit card and PayPal are sufficient payment options",
        "Payment integration planning", 
        "Lost sales from users preferring other payment methods",
        priority=2
    )
    
    mobile_usage = registry.create_assumption(
        "mobile_usage",
        "60% of traffic will come from mobile devices",
        "Responsive design prioritization",
        "Poor mobile experience if we don't prioritize it",
        priority=1
    )
    
    # Add validation tasks
    user_patience.add_validation_task(ValidationTask(
        description="A/B test different page load times",
        method=ValidationMethod.A_B_TESTING,
        assigned_to="UX Research Team"
    ))
    
    payment_methods.add_validation_task(ValidationTask(
        description="Survey existing customers on payment preferences", 
        method=ValidationMethod.USER_RESEARCH,
        assigned_to="Customer Success Team"
    ))
    
    return registry
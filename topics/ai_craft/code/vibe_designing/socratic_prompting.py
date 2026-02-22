"""
Socratic Prompting System for AI-Assisted Design

This module implements the Socratic partnership approach from TAM4,
providing frameworks for using AI to challenge assumptions and explore design alternatives.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Callable, Any
from enum import Enum
import json
from datetime import datetime


class QuestionType(Enum):
    """Types of Socratic questions for design exploration"""
    ASSUMPTION_CHALLENGE = "assumption_challenge"  # Challenge what we think we know
    ALTERNATIVE_EXPLORATION = "alternative_exploration"  # Explore different approaches
    EDGE_CASE_DISCOVERY = "edge_case_discovery"  # Find potential problems
    CONSTRAINT_VALIDATION = "constraint_validation"  # Verify our constraints are real
    CONTEXT_EXPANSION = "context_expansion"  # Broaden the problem scope
    SIMPLIFICATION = "simplification"  # Find simpler approaches


@dataclass
class SocraticQuestion:
    """A structured question for design exploration"""
    question: str
    question_type: QuestionType
    context: str  # What prompted this question
    expected_outcome: str  # What kind of answer we're looking for
    priority: int = 1  # 1=critical, 2=important, 3=nice-to-have
    
    def __post_init__(self):
        if not self.question.strip():
            raise ValueError("Question cannot be empty")
        if not self.context.strip():
            raise ValueError("Question context cannot be empty")


@dataclass
class DesignAlternative:
    """A design alternative discovered through Socratic questioning"""
    name: str
    description: str
    trade_offs: Dict[str, str]  # pros and cons
    complexity_score: int  # 1-5 scale
    risk_level: str  # low, medium, high
    implementation_effort: str  # low, medium, high
    discovered_via: str  # what question or process led to this
    
    def __post_init__(self):
        if not self.name.strip():
            raise ValueError("Alternative name cannot be empty")
        if self.complexity_score not in range(1, 6):
            raise ValueError("Complexity score must be 1-5")


@dataclass
class AssumptionChallenge:
    """A challenge to a design assumption"""
    assumption: str
    challenge: str
    evidence_for: List[str] = field(default_factory=list)
    evidence_against: List[str] = field(default_factory=list)
    validation_method: Optional[str] = None
    confidence_level: int = 3  # 1-5 scale, 5=very confident
    
    def is_well_supported(self) -> bool:
        """Check if assumption has good evidence support"""
        return len(self.evidence_for) >= 2 and self.confidence_level >= 4


class SocraticPromptGenerator:
    """Generates structured prompts for AI-assisted Socratic questioning"""
    
    ASSUMPTION_TEMPLATES = [
        "What if the assumption '{assumption}' is wrong? How would that change our approach?",
        "Can you think of scenarios where '{assumption}' wouldn't hold true?",
        "What evidence do we have that '{assumption}' is actually valid in this context?",
        "How sensitive is our design to the assumption that '{assumption}'?",
    ]
    
    ALTERNATIVE_TEMPLATES = [
        "What are 3 completely different ways we could approach '{problem}'?",
        "If we had to solve '{problem}' with 1/10th the complexity, what would we do?",
        "How might someone from a different industry solve '{problem}'?",
        "What would the simplest possible solution to '{problem}' look like?",
    ]
    
    EDGE_CASE_TEMPLATES = [
        "What could go wrong with this approach to '{problem}'?",
        "What happens to our solution when the scale increases 10x? 100x?",
        "How does our approach handle malicious users or bad actors?", 
        "What edge cases might we be missing for '{problem}'?",
    ]
    
    CONSTRAINT_TEMPLATES = [
        "Are the constraints '{constraints}' actually hard requirements or preferences?",
        "What would happen if we relaxed the constraint '{constraint}'?",
        "Which of these constraints '{constraints}' are most negotiable?",
        "How did we arrive at the constraint '{constraint}' - is it still valid?",
    ]
    
    def generate_assumption_questions(self, assumptions: List[str]) -> List[SocraticQuestion]:
        """Generate questions to challenge assumptions"""
        questions = []
        for assumption in assumptions:
            for template in self.ASSUMPTION_TEMPLATES:
                question = SocraticQuestion(
                    question=template.format(assumption=assumption),
                    question_type=QuestionType.ASSUMPTION_CHALLENGE,
                    context=f"Challenging assumption: {assumption}",
                    expected_outcome="Evidence for/against the assumption, alternative perspectives"
                )
                questions.append(question)
        return questions
    
    def generate_alternative_questions(self, problem_statement: str) -> List[SocraticQuestion]:
        """Generate questions to explore alternatives"""
        questions = []
        for template in self.ALTERNATIVE_TEMPLATES:
            question = SocraticQuestion(
                question=template.format(problem=problem_statement),
                question_type=QuestionType.ALTERNATIVE_EXPLORATION,
                context=f"Exploring alternatives for: {problem_statement}",
                expected_outcome="Multiple different solution approaches with trade-offs"
            )
            questions.append(question)
        return questions
    
    def generate_edge_case_questions(self, problem_statement: str) -> List[SocraticQuestion]:
        """Generate questions to discover edge cases"""
        questions = []
        for template in self.EDGE_CASE_TEMPLATES:
            question = SocraticQuestion(
                question=template.format(problem=problem_statement),
                question_type=QuestionType.EDGE_CASE_DISCOVERY,
                context=f"Finding edge cases for: {problem_statement}",
                expected_outcome="Potential failure modes, unusual scenarios, boundary conditions"
            )
            questions.append(question)
        return questions
    
    def generate_constraint_questions(self, constraints: List[str]) -> List[SocraticQuestion]:
        """Generate questions to validate constraints"""
        questions = []
        for constraint in constraints:
            for template in self.CONSTRAINT_TEMPLATES:
                question = SocraticQuestion(
                    question=template.format(constraint=constraint, constraints=", ".join(constraints)),
                    question_type=QuestionType.CONSTRAINT_VALIDATION,
                    context=f"Validating constraint: {constraint}",
                    expected_outcome="Justification for constraints, flexibility analysis"
                )
                questions.append(question)
        return questions


@dataclass
class SocraticSession:
    """A complete Socratic questioning session for design exploration"""
    problem_statement: str
    assumptions: List[str] = field(default_factory=list)
    constraints: List[str] = field(default_factory=list)
    questions: List[SocraticQuestion] = field(default_factory=list)
    alternatives: List[DesignAlternative] = field(default_factory=list)
    challenges: List[AssumptionChallenge] = field(default_factory=list)
    insights: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    
    def add_assumption(self, assumption: str):
        """Add an assumption to be challenged"""
        if assumption.strip() not in self.assumptions:
            self.assumptions.append(assumption.strip())
    
    def add_constraint(self, constraint: str):
        """Add a constraint to be validated"""
        if constraint.strip() not in self.constraints:
            self.constraints.append(constraint.strip())
    
    def add_alternative(self, alternative: DesignAlternative):
        """Add a discovered design alternative"""
        self.alternatives.append(alternative)
    
    def add_challenge(self, challenge: AssumptionChallenge):
        """Add an assumption challenge"""
        self.challenges.append(challenge)
    
    def add_insight(self, insight: str):
        """Add a design insight discovered during the session"""
        if insight.strip():
            self.insights.append(insight.strip())
    
    def generate_questions(self) -> List[SocraticQuestion]:
        """Generate all Socratic questions for this session"""
        generator = SocraticPromptGenerator()
        questions = []
        
        # Generate assumption challenges
        questions.extend(generator.generate_assumption_questions(self.assumptions))
        
        # Generate alternative explorations
        questions.extend(generator.generate_alternative_questions(self.problem_statement))
        
        # Generate edge case discoveries
        questions.extend(generator.generate_edge_case_questions(self.problem_statement))
        
        # Generate constraint validations
        questions.extend(generator.generate_constraint_questions(self.constraints))
        
        self.questions = questions
        return questions
    
    def get_priority_questions(self, priority: int = 1) -> List[SocraticQuestion]:
        """Get questions by priority level"""
        return [q for q in self.questions if q.priority <= priority]
    
    def get_questions_by_type(self, question_type: QuestionType) -> List[SocraticQuestion]:
        """Get questions by type"""
        return [q for q in self.questions if q.question_type == question_type]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert session to dictionary for serialization"""
        return {
            'problem_statement': self.problem_statement,
            'assumptions': self.assumptions,
            'constraints': self.constraints,
            'questions': [
                {
                    'question': q.question,
                    'type': q.question_type.value,
                    'context': q.context,
                    'expected_outcome': q.expected_outcome,
                    'priority': q.priority
                } for q in self.questions
            ],
            'alternatives': [
                {
                    'name': alt.name,
                    'description': alt.description,
                    'trade_offs': alt.trade_offs,
                    'complexity_score': alt.complexity_score,
                    'risk_level': alt.risk_level,
                    'implementation_effort': alt.implementation_effort,
                    'discovered_via': alt.discovered_via
                } for alt in self.alternatives
            ],
            'challenges': [
                {
                    'assumption': ch.assumption,
                    'challenge': ch.challenge,
                    'evidence_for': ch.evidence_for,
                    'evidence_against': ch.evidence_against,
                    'validation_method': ch.validation_method,
                    'confidence_level': ch.confidence_level,
                    'well_supported': ch.is_well_supported()
                } for ch in self.challenges
            ],
            'insights': self.insights,
            'created_at': self.created_at.isoformat()
        }


def create_auth_socratic_session() -> SocraticSession:
    """Example: Create a Socratic session for authentication system design"""
    session = SocraticSession(
        problem_statement="Design a secure user authentication system for a web application"
    )
    
    # Add assumptions to challenge
    session.add_assumption("Users will use strong passwords")
    session.add_assumption("Email verification is sufficient for account validation")
    session.add_assumption("Sessions should expire after 30 days of inactivity")
    session.add_assumption("Two-factor authentication is optional")
    
    # Add constraints to validate  
    session.add_constraint("Must support OAuth integration")
    session.add_constraint("Password reset must be secure")
    session.add_constraint("Must comply with GDPR")
    session.add_constraint("Response time under 200ms")
    
    # Generate questions
    session.generate_questions()
    
    # Add some example alternatives discovered through questioning
    session.add_alternative(DesignAlternative(
        name="Passwordless Authentication",
        description="Use magic links or biometric authentication instead of passwords",
        trade_offs={
            "pros": "Better security, improved UX, no password management",
            "cons": "Email dependency, potential device lock-out, user education needed"
        },
        complexity_score=3,
        risk_level="medium",
        implementation_effort="high",
        discovered_via="Challenging assumption about password necessity"
    ))
    
    session.add_alternative(DesignAlternative(
        name="Progressive Authentication",
        description="Start with minimal auth, add layers based on user behavior and risk",
        trade_offs={
            "pros": "Better UX, adaptive security, reduced friction",
            "cons": "Complex risk scoring, potential security gaps, harder to audit"
        },
        complexity_score=4,
        risk_level="medium",
        implementation_effort="high",
        discovered_via="Exploring constraint flexibility on security requirements"
    ))
    
    return session
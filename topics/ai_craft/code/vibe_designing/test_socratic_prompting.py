"""
Tests for Socratic prompting system
"""

import pytest
from datetime import datetime

from socratic_prompting import (
    SocraticQuestion, QuestionType, DesignAlternative, AssumptionChallenge,
    SocraticPromptGenerator, SocraticSession, create_auth_socratic_session
)


class TestSocraticQuestion:
    
    def test_create_question(self):
        question = SocraticQuestion(
            question="What if users don't want notifications?",
            question_type=QuestionType.ASSUMPTION_CHALLENGE,
            context="Challenging notification assumptions",
            expected_outcome="Evidence for user preferences"
        )
        
        assert question.question_type == QuestionType.ASSUMPTION_CHALLENGE
        assert question.priority == 1  # Default priority
    
    def test_question_validation(self):
        with pytest.raises(ValueError, match="Question cannot be empty"):
            SocraticQuestion("", QuestionType.ASSUMPTION_CHALLENGE, "context", "outcome")
        
        with pytest.raises(ValueError, match="Question context cannot be empty"):
            SocraticQuestion("question?", QuestionType.ASSUMPTION_CHALLENGE, "", "outcome")


class TestDesignAlternative:
    
    def test_create_alternative(self):
        alt = DesignAlternative(
            name="Microservices Approach",
            description="Break system into microservices",
            trade_offs={"pros": "Scalable", "cons": "Complex"},
            complexity_score=4,
            risk_level="medium",
            implementation_effort="high",
            discovered_via="Questioning monolithic assumptions"
        )
        
        assert alt.name == "Microservices Approach"
        assert alt.complexity_score == 4
        assert alt.risk_level == "medium"
    
    def test_alternative_validation(self):
        with pytest.raises(ValueError, match="Alternative name cannot be empty"):
            DesignAlternative("", "desc", {}, 3, "low", "medium", "via")
        
        with pytest.raises(ValueError, match="Complexity score must be 1-5"):
            DesignAlternative("name", "desc", {}, 6, "low", "medium", "via")


class TestAssumptionChallenge:
    
    def test_create_challenge(self):
        challenge = AssumptionChallenge(
            assumption="Users prefer simple interfaces",
            challenge="What about power users who need advanced features?",
            evidence_for=["User surveys show preference for simplicity"],
            evidence_against=["Advanced users complain about missing features"],
            confidence_level=3
        )
        
        assert challenge.assumption == "Users prefer simple interfaces"
        assert len(challenge.evidence_for) == 1
        assert len(challenge.evidence_against) == 1
    
    def test_well_supported_assumption(self):
        # Well supported: 2+ evidence_for and confidence >= 4
        challenge = AssumptionChallenge(
            assumption="Test assumption",
            challenge="Test challenge",
            evidence_for=["Evidence 1", "Evidence 2"],
            evidence_against=[],
            confidence_level=4
        )
        
        assert challenge.is_well_supported()
    
    def test_poorly_supported_assumption(self):
        # Poorly supported: < 2 evidence_for or confidence < 4
        challenge = AssumptionChallenge(
            assumption="Test assumption", 
            challenge="Test challenge",
            evidence_for=["Only one piece of evidence"],
            evidence_against=[],
            confidence_level=2
        )
        
        assert not challenge.is_well_supported()


class TestSocraticPromptGenerator:
    
    def test_generate_assumption_questions(self):
        generator = SocraticPromptGenerator()
        assumptions = ["Users want notifications", "Email is reliable"]
        
        questions = generator.generate_assumption_questions(assumptions)
        
        assert len(questions) > 0
        assert all(q.question_type == QuestionType.ASSUMPTION_CHALLENGE for q in questions)
        
        # Should generate questions for both assumptions
        question_texts = [q.question for q in questions]
        assert any("notifications" in q.lower() for q in question_texts)
        assert any("email" in q.lower() for q in question_texts)
    
    def test_generate_alternative_questions(self):
        generator = SocraticPromptGenerator()
        problem = "Design authentication system"
        
        questions = generator.generate_alternative_questions(problem)
        
        assert len(questions) > 0
        assert all(q.question_type == QuestionType.ALTERNATIVE_EXPLORATION for q in questions)
        
        # Questions should reference the problem
        question_texts = [q.question for q in questions]
        assert any("authentication" in q.lower() for q in question_texts)
    
    def test_generate_edge_case_questions(self):
        generator = SocraticPromptGenerator()
        problem = "User management system"
        
        questions = generator.generate_edge_case_questions(problem)
        
        assert len(questions) > 0
        assert all(q.question_type == QuestionType.EDGE_CASE_DISCOVERY for q in questions)
    
    def test_generate_constraint_questions(self):
        generator = SocraticPromptGenerator()
        constraints = ["Must support 10k users", "Response time < 200ms"]
        
        questions = generator.generate_constraint_questions(constraints)
        
        assert len(questions) > 0
        assert all(q.question_type == QuestionType.CONSTRAINT_VALIDATION for q in questions)


class TestSocraticSession:
    
    def test_create_session(self):
        session = SocraticSession("Design notification system")
        
        assert session.problem_statement == "Design notification system"
        assert len(session.assumptions) == 0
        assert len(session.constraints) == 0
        assert len(session.questions) == 0
    
    def test_add_assumption(self):
        session = SocraticSession("Test problem")
        session.add_assumption("Users like notifications")
        session.add_assumption("Users like notifications")  # Duplicate
        
        assert len(session.assumptions) == 1  # Should not add duplicates
        assert "Users like notifications" in session.assumptions
    
    def test_add_constraint(self):
        session = SocraticSession("Test problem")
        session.add_constraint("Must be fast")
        session.add_constraint("Must be secure")
        
        assert len(session.constraints) == 2
        assert "Must be fast" in session.constraints
        assert "Must be secure" in session.constraints
    
    def test_add_alternative(self):
        session = SocraticSession("Test problem")
        alt = DesignAlternative(
            name="Test Alternative",
            description="Test description",
            trade_offs={"pros": "Simple", "cons": "Limited"},
            complexity_score=2,
            risk_level="low",
            implementation_effort="low",
            discovered_via="Testing"
        )
        
        session.add_alternative(alt)
        assert len(session.alternatives) == 1
        assert session.alternatives[0] == alt
    
    def test_add_challenge(self):
        session = SocraticSession("Test problem")
        challenge = AssumptionChallenge(
            assumption="Test assumption",
            challenge="Test challenge"
        )
        
        session.add_challenge(challenge)
        assert len(session.challenges) == 1
        assert session.challenges[0] == challenge
    
    def test_add_insight(self):
        session = SocraticSession("Test problem")
        session.add_insight("Important insight about the domain")
        session.add_insight("   ")  # Empty insight should not be added
        
        assert len(session.insights) == 1
        assert "Important insight about the domain" in session.insights
    
    def test_generate_questions(self):
        session = SocraticSession("Design auth system")
        session.add_assumption("Passwords are secure")
        session.add_constraint("Must support OAuth")
        
        questions = session.generate_questions()
        
        assert len(questions) > 0
        assert len(session.questions) > 0  # Should store generated questions
        
        # Should have different types of questions
        question_types = {q.question_type for q in questions}
        assert QuestionType.ASSUMPTION_CHALLENGE in question_types
        assert QuestionType.CONSTRAINT_VALIDATION in question_types
    
    def test_get_priority_questions(self):
        session = SocraticSession("Test problem")
        session.questions = [
            SocraticQuestion("Q1", QuestionType.ASSUMPTION_CHALLENGE, "C1", "O1", priority=1),
            SocraticQuestion("Q2", QuestionType.ASSUMPTION_CHALLENGE, "C2", "O2", priority=2),
            SocraticQuestion("Q3", QuestionType.ASSUMPTION_CHALLENGE, "C3", "O3", priority=1)
        ]
        
        priority_1 = session.get_priority_questions(priority=1)
        assert len(priority_1) == 2
        assert all(q.priority == 1 for q in priority_1)
    
    def test_get_questions_by_type(self):
        session = SocraticSession("Test problem")
        session.questions = [
            SocraticQuestion("Q1", QuestionType.ASSUMPTION_CHALLENGE, "C1", "O1"),
            SocraticQuestion("Q2", QuestionType.ALTERNATIVE_EXPLORATION, "C2", "O2"),
            SocraticQuestion("Q3", QuestionType.ASSUMPTION_CHALLENGE, "C3", "O3")
        ]
        
        assumption_questions = session.get_questions_by_type(QuestionType.ASSUMPTION_CHALLENGE)
        assert len(assumption_questions) == 2
        assert all(q.question_type == QuestionType.ASSUMPTION_CHALLENGE for q in assumption_questions)
    
    def test_to_dict(self):
        session = SocraticSession("Test problem")
        session.add_assumption("Test assumption")
        session.add_insight("Test insight")
        
        dict_repr = session.to_dict()
        
        assert dict_repr['problem_statement'] == "Test problem"
        assert len(dict_repr['assumptions']) == 1
        assert len(dict_repr['insights']) == 1
        assert 'created_at' in dict_repr


class TestCreateAuthSocraticSession:
    
    def test_create_auth_session(self):
        session = create_auth_socratic_session()
        
        assert "authentication" in session.problem_statement.lower()
        assert len(session.assumptions) >= 3  # Should have several assumptions
        assert len(session.constraints) >= 3  # Should have constraints
        assert len(session.questions) > 0     # Should generate questions
        assert len(session.alternatives) >= 2 # Should have example alternatives
    
    def test_auth_session_assumptions(self):
        session = create_auth_socratic_session()
        
        assumption_texts = [a.lower() for a in session.assumptions]
        # Should challenge common auth assumptions
        assert any("password" in assumption for assumption in assumption_texts)
        assert any("email" in assumption for assumption in assumption_texts)
    
    def test_auth_session_alternatives(self):
        session = create_auth_socratic_session()
        
        assert len(session.alternatives) >= 2
        alt_names = [alt.name for alt in session.alternatives]
        
        # Should have diverse alternatives
        assert len(set(alt_names)) == len(alt_names)  # No duplicates
        
        # Should have complexity scores
        assert all(1 <= alt.complexity_score <= 5 for alt in session.alternatives)
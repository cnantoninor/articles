"""
Tests for design exploration tools
"""

import pytest

from design_exploration import (
    DesignDimension, DesignScore, DesignPattern, DesignAlternative,
    DesignExplorer, get_common_patterns, create_sample_explorer
)


class TestDesignScore:
    
    def test_create_score(self):
        score = DesignScore(
            dimension=DesignDimension.SCALABILITY,
            score=4,
            confidence=3,
            rationale="Good horizontal scaling capabilities"
        )
        
        assert score.dimension == DesignDimension.SCALABILITY
        assert score.score == 4
        assert score.confidence == 3
    
    def test_score_validation(self):
        with pytest.raises(ValueError, match="Score must be 1-5"):
            DesignScore(DesignDimension.SCALABILITY, 6, 3, "rationale")
        
        with pytest.raises(ValueError, match="Confidence must be 1-5"):
            DesignScore(DesignDimension.SCALABILITY, 4, 0, "rationale")


class TestDesignPattern:
    
    def test_create_pattern(self):
        pattern = DesignPattern(
            name="Microservices",
            description="Decompose into small services",
            when_to_use="Complex domains, multiple teams",
            when_not_to_use="Simple applications",
            trade_offs={"pros": "Scalable", "cons": "Complex"}
        )
        
        assert pattern.name == "Microservices"
        assert "Scalable" in pattern.trade_offs["pros"]
    
    def test_get_typical_score(self):
        pattern = DesignPattern(
            name="Test Pattern",
            description="Test",
            when_to_use="Test",
            when_not_to_use="Test",
            trade_offs={},
            typical_scores={
                DesignDimension.SCALABILITY: 5,
                DesignDimension.COMPLEXITY: 2
            }
        )
        
        assert pattern.get_typical_score(DesignDimension.SCALABILITY) == 5
        assert pattern.get_typical_score(DesignDimension.COMPLEXITY) == 2
        assert pattern.get_typical_score(DesignDimension.SECURITY) is None


class TestDesignAlternative:
    
    def test_create_alternative(self):
        alt = DesignAlternative(
            id="microservices_approach",
            name="Microservices Architecture",
            description="Break system into microservices",
            approach="Service decomposition by business capabilities"
        )
        
        assert alt.id == "microservices_approach"
        assert alt.name == "Microservices Architecture"
        assert len(alt.scores) == 0
        assert len(alt.risks) == 0
    
    def test_alternative_validation(self):
        with pytest.raises(ValueError, match="Alternative ID cannot be empty"):
            DesignAlternative("", "name", "desc", "approach")
        
        with pytest.raises(ValueError, match="Alternative name cannot be empty"):
            DesignAlternative("id", "", "desc", "approach")
    
    def test_add_score(self):
        alt = DesignAlternative("test", "Test Alt", "desc", "approach")
        
        alt.add_score(DesignDimension.SCALABILITY, 4, 3, "Good scalability")
        
        assert len(alt.scores) == 1
        score = alt.get_score(DesignDimension.SCALABILITY)
        assert score.score == 4
        assert score.confidence == 3
    
    def test_replace_existing_score(self):
        alt = DesignAlternative("test", "Test Alt", "desc", "approach")
        
        # Add initial score
        alt.add_score(DesignDimension.SCALABILITY, 3, 2, "Initial assessment")
        assert len(alt.scores) == 1
        
        # Replace with new score
        alt.add_score(DesignDimension.SCALABILITY, 4, 4, "Updated assessment")
        assert len(alt.scores) == 1
        
        score = alt.get_score(DesignDimension.SCALABILITY)
        assert score.score == 4
        assert score.rationale == "Updated assessment"
    
    def test_get_overall_score_equal_weights(self):
        alt = DesignAlternative("test", "Test Alt", "desc", "approach")
        
        alt.add_score(DesignDimension.SCALABILITY, 4, 5, "Good")
        alt.add_score(DesignDimension.SECURITY, 3, 4, "Decent")
        
        # Equal weights: (4*5 + 3*4) / (5 + 4) = 32/9 ≈ 3.56
        overall = alt.get_overall_score()
        assert 3.5 < overall < 3.6
    
    def test_get_overall_score_weighted(self):
        alt = DesignAlternative("test", "Test Alt", "desc", "approach")
        
        alt.add_score(DesignDimension.SCALABILITY, 4, 5, "Good")
        alt.add_score(DesignDimension.SECURITY, 2, 3, "Poor")
        
        weights = {
            DesignDimension.SCALABILITY: 0.2,  # Low weight
            DesignDimension.SECURITY: 0.8      # High weight
        }
        
        # Weighted: (4*5*0.2 + 2*3*0.8) / (5*0.2 + 3*0.8) = (4 + 4.8) / (1 + 2.4) = 8.8/3.4 ≈ 2.59
        overall = alt.get_overall_score(weights)
        assert 2.5 < overall < 2.7
    
    def test_get_overall_score_no_scores(self):
        alt = DesignAlternative("test", "Test Alt", "desc", "approach")
        
        assert alt.get_overall_score() == 0.0


class TestDesignExplorer:
    
    def test_create_explorer(self):
        explorer = DesignExplorer("Design authentication system")
        
        assert explorer.problem_statement == "Design authentication system"
        assert len(explorer.alternatives) == 0
        assert len(explorer.patterns) == 0
    
    def test_add_pattern(self):
        explorer = DesignExplorer("Test problem")
        pattern = DesignPattern("Test Pattern", "desc", "when", "when not", {})
        
        explorer.add_pattern(pattern)
        
        assert len(explorer.patterns) == 1
        assert explorer.patterns["Test Pattern"] == pattern
    
    def test_add_alternative(self):
        explorer = DesignExplorer("Test problem")
        alt = DesignAlternative("test_alt", "Test Alternative", "desc", "approach")
        
        explorer.add_alternative(alt)
        
        assert len(explorer.alternatives) == 1
        assert explorer.alternatives["test_alt"] == alt
    
    def test_create_alternative(self):
        explorer = DesignExplorer("Test problem")
        
        alt = explorer.create_alternative("new_alt", "New Alt", "description", "approach")
        
        assert alt.id == "new_alt"
        assert len(explorer.alternatives) == 1
        assert explorer.alternatives["new_alt"] == alt
    
    def test_set_evaluation_criteria(self):
        explorer = DesignExplorer("Test problem")
        
        criteria = {
            DesignDimension.SCALABILITY: 0.6,
            DesignDimension.SECURITY: 0.4
        }
        explorer.set_evaluation_criteria(criteria)
        
        assert explorer.evaluation_criteria[DesignDimension.SCALABILITY] == 0.6
        assert explorer.evaluation_criteria[DesignDimension.SECURITY] == 0.4
    
    def test_set_evaluation_criteria_normalization(self):
        explorer = DesignExplorer("Test problem")
        
        # Weights that don't sum to 1.0
        criteria = {
            DesignDimension.SCALABILITY: 3,
            DesignDimension.SECURITY: 2
        }
        explorer.set_evaluation_criteria(criteria)
        
        # Should be normalized: 3/5 = 0.6, 2/5 = 0.4
        assert explorer.evaluation_criteria[DesignDimension.SCALABILITY] == 0.6
        assert explorer.evaluation_criteria[DesignDimension.SECURITY] == 0.4
    
    def test_rank_alternatives(self):
        explorer = DesignExplorer("Test problem")
        
        # Set evaluation criteria so overall score calculation works
        explorer.set_evaluation_criteria({DesignDimension.SCALABILITY: 1.0})
        
        # Create alternatives with different overall scores
        alt1 = explorer.create_alternative("alt1", "Alternative 1", "desc", "approach")
        alt1.add_score(DesignDimension.SCALABILITY, 5, 5, "Excellent")
        
        alt2 = explorer.create_alternative("alt2", "Alternative 2", "desc", "approach")
        alt2.add_score(DesignDimension.SCALABILITY, 3, 5, "Good")
        
        rankings = explorer.rank_alternatives()
        
        assert len(rankings) == 2
        # alt1 should rank higher (score 5 vs 3)
        assert rankings[0][0] == "alt1"  # ID of top-ranked alternative
        assert rankings[0][1] > rankings[1][1]  # Higher score
    
    def test_compare_alternatives(self):
        explorer = DesignExplorer("Test problem")
        
        alt1 = explorer.create_alternative("alt1", "Alt 1", "desc", "approach")
        alt1.add_score(DesignDimension.SCALABILITY, 4, 4, "Good scalability")
        alt1.add_score(DesignDimension.SECURITY, 3, 3, "Decent security")
        
        alt2 = explorer.create_alternative("alt2", "Alt 2", "desc", "approach")
        alt2.add_score(DesignDimension.SCALABILITY, 2, 4, "Poor scalability")
        alt2.add_score(DesignDimension.SECURITY, 5, 5, "Excellent security")
        
        comparison = explorer.compare_alternatives("alt1", "alt2")
        
        assert comparison['alternative_1']['name'] == "Alt 1"
        assert comparison['alternative_2']['name'] == "Alt 2"
        
        # Check dimension comparison
        scalability = comparison['dimension_comparison']['scalability']
        assert scalability['winner'] == 'alt1'  # alt1 wins scalability (4 > 2)
        
        security = comparison['dimension_comparison']['security']
        assert security['winner'] == 'alt2'  # alt2 wins security (5 > 3)
    
    def test_compare_nonexistent_alternatives(self):
        explorer = DesignExplorer("Test problem")
        
        with pytest.raises(ValueError, match="Both alternatives must exist"):
            explorer.compare_alternatives("nonexistent1", "nonexistent2")
    
    def test_suggest_improvements(self):
        explorer = DesignExplorer("Test problem")
        
        # Add a pattern that's strong in scalability
        pattern = DesignPattern(
            "Strong Pattern", "desc", "when", "when not", {},
            typical_scores={DesignDimension.SCALABILITY: 5}
        )
        explorer.add_pattern(pattern)
        
        # Create alternative with low scalability score
        alt = explorer.create_alternative("alt1", "Alt 1", "desc", "approach")
        alt.add_score(DesignDimension.SCALABILITY, 2, 4, "Poor scalability")
        
        suggestions = explorer.suggest_improvements("alt1")
        
        assert len(suggestions) > 0
        suggestion_text = " ".join(suggestions).lower()
        assert "scalability" in suggestion_text
    
    def test_generate_hybrid_alternative(self):
        explorer = DesignExplorer("Test problem")
        
        # Create two alternatives with different strengths
        alt1 = explorer.create_alternative("alt1", "Alt 1", "desc", "approach")
        alt1.add_score(DesignDimension.SCALABILITY, 5, 5, "Excellent scalability")
        alt1.add_score(DesignDimension.SECURITY, 2, 4, "Poor security")
        alt1.risks.append("Security vulnerability")
        alt1.assumptions.append("High traffic expected")
        
        alt2 = explorer.create_alternative("alt2", "Alt 2", "desc", "approach") 
        alt2.add_score(DesignDimension.SCALABILITY, 2, 4, "Poor scalability")
        alt2.add_score(DesignDimension.SECURITY, 5, 5, "Excellent security")
        alt2.risks.append("Scalability bottleneck")
        alt2.assumptions.append("Security is critical")
        
        hybrid = explorer.generate_hybrid_alternative(["alt1", "alt2"], "Hybrid Solution")
        
        assert hybrid.name == "Hybrid Solution"
        assert len(explorer.alternatives) == 3  # Original 2 + new hybrid
        
        # Hybrid should take best scores from each dimension
        scalability_score = hybrid.get_score(DesignDimension.SCALABILITY)
        security_score = hybrid.get_score(DesignDimension.SECURITY)
        
        assert scalability_score.score == 5  # From alt1
        assert security_score.score == 5     # From alt2
        
        # Should combine risks and assumptions
        assert len(hybrid.risks) == 2
        assert len(hybrid.assumptions) == 2
    
    def test_generate_hybrid_insufficient_alternatives(self):
        explorer = DesignExplorer("Test problem")
        
        with pytest.raises(ValueError, match="Need at least 2 alternatives"):
            explorer.generate_hybrid_alternative(["alt1"], "Hybrid")
    
    def test_to_dict(self):
        explorer = DesignExplorer("Test problem")
        explorer.set_evaluation_criteria({DesignDimension.SCALABILITY: 1.0})
        
        alt = explorer.create_alternative("test_alt", "Test Alt", "desc", "approach")
        alt.add_score(DesignDimension.SCALABILITY, 4, 4, "Good")
        
        dict_repr = explorer.to_dict()
        
        assert dict_repr['problem_statement'] == "Test problem"
        assert 'evaluation_criteria' in dict_repr
        assert len(dict_repr['alternatives']) == 1
        assert dict_repr['alternatives']['test_alt']['overall_score'] == 4.0


class TestGetCommonPatterns:
    
    def test_get_common_patterns(self):
        patterns = get_common_patterns()
        
        assert len(patterns) >= 3
        pattern_names = [p.name for p in patterns]
        
        # Should include common architectural patterns
        assert "Microservices Architecture" in pattern_names
        assert "Event Sourcing" in pattern_names
        assert "Monolithic Architecture" in pattern_names
    
    def test_patterns_have_typical_scores(self):
        patterns = get_common_patterns()
        
        for pattern in patterns:
            assert len(pattern.typical_scores) > 0
            # Scores should be in valid range
            for score in pattern.typical_scores.values():
                assert 1 <= score <= 5


class TestCreateSampleExplorer:
    
    def test_create_sample_explorer(self):
        explorer = create_sample_explorer()
        
        assert "authentication" in explorer.problem_statement.lower()
        assert len(explorer.alternatives) >= 2
        assert len(explorer.patterns) >= 3
        assert len(explorer.evaluation_criteria) > 0
    
    def test_sample_explorer_evaluation_criteria(self):
        explorer = create_sample_explorer()
        
        # Weights should sum to approximately 1.0
        total_weight = sum(explorer.evaluation_criteria.values())
        assert abs(total_weight - 1.0) < 0.01
        
        # Should include security as important criterion for auth system
        assert DesignDimension.SECURITY in explorer.evaluation_criteria
    
    def test_sample_explorer_alternatives_scored(self):
        explorer = create_sample_explorer()
        
        for alternative in explorer.alternatives.values():
            # Each alternative should have multiple scores
            assert len(alternative.scores) >= 3
            
            # Should have risks identified
            assert len(alternative.risks) > 0
            
            # Overall score should be reasonable
            overall = alternative.get_overall_score(explorer.evaluation_criteria)
            assert 1.0 <= overall <= 5.0
"""
Design Exploration Tools for Vibe Designing

This module implements tools for systematic exploration of design alternatives,
supporting the TAM4 approach of using AI to discover and compare solution approaches.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Any, Tuple
from enum import Enum
import json
from datetime import datetime
import math


class DesignDimension(Enum):
    """Dimensions along which designs can vary"""
    COMPLEXITY = "complexity"
    PERFORMANCE = "performance" 
    SCALABILITY = "scalability"
    MAINTAINABILITY = "maintainability"
    SECURITY = "security"
    COST = "cost"
    USER_EXPERIENCE = "user_experience"
    RELIABILITY = "reliability"
    FLEXIBILITY = "flexibility"
    TIME_TO_MARKET = "time_to_market"


@dataclass
class DesignScore:
    """Score for a design along various dimensions"""
    dimension: DesignDimension
    score: int  # 1-5 scale (1=poor, 5=excellent)
    confidence: int  # 1-5 scale (how confident we are in this score)
    rationale: str  # Why we gave this score
    
    def __post_init__(self):
        if self.score not in range(1, 6):
            raise ValueError("Score must be 1-5")
        if self.confidence not in range(1, 6):
            raise ValueError("Confidence must be 1-5")


@dataclass 
class DesignPattern:
    """A reusable design pattern or approach"""
    name: str
    description: str
    when_to_use: str
    when_not_to_use: str
    trade_offs: Dict[str, str]
    typical_scores: Dict[DesignDimension, int] = field(default_factory=dict)
    examples: List[str] = field(default_factory=list)
    
    def get_typical_score(self, dimension: DesignDimension) -> Optional[int]:
        """Get typical score for this pattern along a dimension"""
        return self.typical_scores.get(dimension)


@dataclass
class DesignAlternative:
    """A specific design alternative being explored"""
    id: str
    name: str
    description: str
    approach: str  # High-level approach description
    scores: List[DesignScore] = field(default_factory=list)
    implementation_notes: str = ""
    risks: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    patterns_used: List[str] = field(default_factory=list)  # Pattern names
    created_at: datetime = field(default_factory=datetime.now)
    
    def __post_init__(self):
        if not self.id.strip():
            raise ValueError("Alternative ID cannot be empty")
        if not self.name.strip():
            raise ValueError("Alternative name cannot be empty")
    
    def add_score(self, dimension: DesignDimension, score: int, confidence: int, rationale: str):
        """Add a score for a design dimension"""
        design_score = DesignScore(
            dimension=dimension,
            score=score,
            confidence=confidence,
            rationale=rationale
        )
        # Remove existing score for this dimension
        self.scores = [s for s in self.scores if s.dimension != dimension]
        self.scores.append(design_score)
    
    def get_score(self, dimension: DesignDimension) -> Optional[DesignScore]:
        """Get score for specific dimension"""
        for score in self.scores:
            if score.dimension == dimension:
                return score
        return None
    
    def get_overall_score(self, weights: Dict[DesignDimension, float] = None) -> float:
        """Calculate weighted overall score"""
        if not self.scores:
            return 0.0
        
        if weights is None:
            # Equal weights for all dimensions
            total_score = sum(s.score * s.confidence for s in self.scores)
            total_confidence = sum(s.confidence for s in self.scores)
            return total_score / total_confidence if total_confidence > 0 else 0.0
        
        weighted_score = 0.0
        total_weight = 0.0
        
        for score in self.scores:
            weight = weights.get(score.dimension, 0.0)
            weighted_score += score.score * score.confidence * weight
            total_weight += score.confidence * weight
        
        return weighted_score / total_weight if total_weight > 0 else 0.0


class DesignExplorer:
    """Tool for systematic exploration and comparison of design alternatives"""
    
    def __init__(self, problem_statement: str):
        self.problem_statement = problem_statement
        self.alternatives: Dict[str, DesignAlternative] = {}
        self.patterns: Dict[str, DesignPattern] = {}
        self.evaluation_criteria: Dict[DesignDimension, float] = {}  # Weights for each dimension
        self.created_at = datetime.now()
    
    def add_pattern(self, pattern: DesignPattern):
        """Add a design pattern to the knowledge base"""
        self.patterns[pattern.name] = pattern
    
    def add_alternative(self, alternative: DesignAlternative):
        """Add a design alternative for exploration"""
        self.alternatives[alternative.id] = alternative
    
    def create_alternative(self, alt_id: str, name: str, description: str, approach: str) -> DesignAlternative:
        """Create and add a new alternative"""
        alternative = DesignAlternative(
            id=alt_id,
            name=name,
            description=description,
            approach=approach
        )
        self.add_alternative(alternative)
        return alternative
    
    def set_evaluation_criteria(self, criteria_weights: Dict[DesignDimension, float]):
        """Set weights for different evaluation dimensions"""
        # Normalize weights to sum to 1.0
        total_weight = sum(criteria_weights.values())
        if total_weight > 0:
            self.evaluation_criteria = {
                dim: weight / total_weight 
                for dim, weight in criteria_weights.items()
            }
    
    def rank_alternatives(self) -> List[Tuple[str, float, DesignAlternative]]:
        """Rank alternatives by overall score"""
        ranked = []
        for alt_id, alternative in self.alternatives.items():
            score = alternative.get_overall_score(self.evaluation_criteria)
            ranked.append((alt_id, score, alternative))
        
        return sorted(ranked, key=lambda x: x[1], reverse=True)
    
    def compare_alternatives(self, alt_id1: str, alt_id2: str) -> Dict[str, Any]:
        """Compare two alternatives across all dimensions"""
        alt1 = self.alternatives.get(alt_id1)
        alt2 = self.alternatives.get(alt_id2)
        
        if not alt1 or not alt2:
            raise ValueError("Both alternatives must exist")
        
        comparison = {
            'alternative_1': {'id': alt_id1, 'name': alt1.name},
            'alternative_2': {'id': alt_id2, 'name': alt2.name},
            'dimension_comparison': {},
            'overall_scores': {
                alt_id1: alt1.get_overall_score(self.evaluation_criteria),
                alt_id2: alt2.get_overall_score(self.evaluation_criteria)
            }
        }
        
        # Compare each dimension
        all_dimensions = set()
        for alt in [alt1, alt2]:
            all_dimensions.update(s.dimension for s in alt.scores)
        
        for dimension in all_dimensions:
            score1 = alt1.get_score(dimension)
            score2 = alt2.get_score(dimension)
            
            comparison['dimension_comparison'][dimension.value] = {
                'alt1_score': score1.score if score1 else None,
                'alt1_confidence': score1.confidence if score1 else None,
                'alt1_rationale': score1.rationale if score1 else None,
                'alt2_score': score2.score if score2 else None,
                'alt2_confidence': score2.confidence if score2 else None,
                'alt2_rationale': score2.rationale if score2 else None,
                'winner': None
            }
            
            if score1 and score2:
                if score1.score > score2.score:
                    comparison['dimension_comparison'][dimension.value]['winner'] = alt_id1
                elif score2.score > score1.score:
                    comparison['dimension_comparison'][dimension.value]['winner'] = alt_id2
                else:
                    comparison['dimension_comparison'][dimension.value]['winner'] = 'tie'
        
        return comparison
    
    def suggest_improvements(self, alt_id: str) -> List[str]:
        """Suggest improvements for an alternative based on low scores"""
        alternative = self.alternatives.get(alt_id)
        if not alternative:
            return []
        
        suggestions = []
        low_score_threshold = 3
        
        for score in alternative.scores:
            if score.score <= low_score_threshold:
                # Look for patterns that are strong in this dimension
                dimension = score.dimension
                strong_patterns = []
                
                for pattern in self.patterns.values():
                    typical_score = pattern.get_typical_score(dimension)
                    if typical_score and typical_score >= 4:
                        strong_patterns.append(pattern.name)
                
                if strong_patterns:
                    suggestion = f"To improve {dimension.value}: Consider patterns like {', '.join(strong_patterns[:3])}"
                    suggestions.append(suggestion)
                else:
                    suggestion = f"Low score in {dimension.value}: {score.rationale}"
                    suggestions.append(suggestion)
        
        return suggestions
    
    def generate_hybrid_alternative(self, alt_ids: List[str], hybrid_name: str) -> DesignAlternative:
        """Generate a hybrid alternative combining strengths of multiple alternatives"""
        if len(alt_ids) < 2:
            raise ValueError("Need at least 2 alternatives to create hybrid")
        
        source_alts = [self.alternatives[aid] for aid in alt_ids if aid in self.alternatives]
        if len(source_alts) < 2:
            raise ValueError("Not all source alternatives found")
        
        # Create hybrid by taking best scores from each dimension
        hybrid_id = f"hybrid_{len(self.alternatives) + 1}"
        hybrid_description = f"Hybrid approach combining: {', '.join(alt.name for alt in source_alts)}"
        
        hybrid = DesignAlternative(
            id=hybrid_id,
            name=hybrid_name,
            description=hybrid_description,
            approach="Hybrid approach taking best elements from multiple alternatives"
        )
        
        # For each dimension, take the best score
        all_dimensions = set()
        for alt in source_alts:
            all_dimensions.update(s.dimension for s in alt.scores)
        
        for dimension in all_dimensions:
            best_score = None
            source_alt = None
            
            for alt in source_alts:
                score = alt.get_score(dimension)
                if score and (not best_score or score.score > best_score.score):
                    best_score = score
                    source_alt = alt.name
            
            if best_score:
                hybrid.add_score(
                    dimension,
                    best_score.score,
                    best_score.confidence,
                    f"From {source_alt}: {best_score.rationale}"
                )
        
        # Combine risks and assumptions
        for alt in source_alts:
            hybrid.risks.extend(alt.risks)
            hybrid.assumptions.extend(alt.assumptions)
        
        # Remove duplicates
        hybrid.risks = list(set(hybrid.risks))
        hybrid.assumptions = list(set(hybrid.assumptions))
        
        self.add_alternative(hybrid)
        return hybrid
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert explorer state to dictionary"""
        return {
            'problem_statement': self.problem_statement,
            'created_at': self.created_at.isoformat(),
            'evaluation_criteria': {dim.value: weight for dim, weight in self.evaluation_criteria.items()},
            'alternatives': {
                aid: {
                    'id': alt.id,
                    'name': alt.name,
                    'description': alt.description,
                    'approach': alt.approach,
                    'overall_score': alt.get_overall_score(self.evaluation_criteria),
                    'scores': [
                        {
                            'dimension': s.dimension.value,
                            'score': s.score,
                            'confidence': s.confidence,
                            'rationale': s.rationale
                        } for s in alt.scores
                    ],
                    'risks': alt.risks,
                    'assumptions': alt.assumptions,
                    'patterns_used': alt.patterns_used
                } for aid, alt in self.alternatives.items()
            },
            'patterns': {
                name: {
                    'name': pattern.name,
                    'description': pattern.description,
                    'when_to_use': pattern.when_to_use,
                    'when_not_to_use': pattern.when_not_to_use,
                    'trade_offs': pattern.trade_offs,
                    'examples': pattern.examples
                } for name, pattern in self.patterns.items()
            }
        }


# Common design patterns for the knowledge base
def get_common_patterns() -> List[DesignPattern]:
    """Get a collection of common design patterns"""
    return [
        DesignPattern(
            name="Microservices Architecture",
            description="Decompose application into small, independently deployable services",
            when_to_use="Complex domains, need for independent scaling, multiple teams",
            when_not_to_use="Simple applications, single team, tight coupling between components",
            trade_offs={
                "pros": "Independent deployment, scalability, technology diversity, fault isolation",
                "cons": "Complexity, network overhead, data consistency challenges, operational overhead"
            },
            typical_scores={
                DesignDimension.SCALABILITY: 5,
                DesignDimension.COMPLEXITY: 2,
                DesignDimension.MAINTAINABILITY: 4,
                DesignDimension.PERFORMANCE: 3
            },
            examples=["Netflix architecture", "Amazon services", "Uber's platform"]
        ),
        
        DesignPattern(
            name="Event Sourcing",
            description="Store events representing state changes instead of current state",
            when_to_use="Need for audit trails, temporal queries, complex business logic",
            when_not_to_use="Simple CRUD operations, performance-critical reads, limited storage",
            trade_offs={
                "pros": "Complete audit trail, temporal queries, debugging capability, scalability",
                "cons": "Complexity, eventual consistency, storage overhead, learning curve"
            },
            typical_scores={
                DesignDimension.RELIABILITY: 5,
                DesignDimension.COMPLEXITY: 2,
                DesignDimension.FLEXIBILITY: 4,
                DesignDimension.PERFORMANCE: 3
            },
            examples=["Banking systems", "E-commerce order tracking", "Version control systems"]
        ),
        
        DesignPattern(
            name="Monolithic Architecture",
            description="Single deployable unit containing all application functionality",
            when_to_use="Simple applications, single team, rapid prototyping, limited complexity",
            when_not_to_use="Large teams, complex domains, independent scaling needs",
            trade_offs={
                "pros": "Simplicity, easier testing, single deployment, better performance",
                "cons": "Scaling limitations, technology lock-in, deployment bottlenecks"
            },
            typical_scores={
                DesignDimension.COMPLEXITY: 4,
                DesignDimension.PERFORMANCE: 4,
                DesignDimension.SCALABILITY: 2,
                DesignDimension.TIME_TO_MARKET: 5
            },
            examples=["Early-stage applications", "Internal tools", "Simple web applications"]
        )
    ]


def create_sample_explorer() -> DesignExplorer:
    """Create a sample design explorer for demonstration"""
    explorer = DesignExplorer("Design a user authentication system for a web application")
    
    # Add common patterns
    for pattern in get_common_patterns():
        explorer.add_pattern(pattern)
    
    # Set evaluation criteria
    explorer.set_evaluation_criteria({
        DesignDimension.SECURITY: 0.3,
        DesignDimension.USER_EXPERIENCE: 0.25,
        DesignDimension.MAINTAINABILITY: 0.2,
        DesignDimension.SCALABILITY: 0.15,
        DesignDimension.TIME_TO_MARKET: 0.1
    })
    
    # Add some alternatives
    traditional_auth = explorer.create_alternative(
        "traditional_auth",
        "Traditional Username/Password",
        "Standard username/password with session management",
        "Store user credentials, validate on login, maintain sessions"
    )
    
    traditional_auth.add_score(DesignDimension.SECURITY, 3, 4, "Standard security, prone to password attacks")
    traditional_auth.add_score(DesignDimension.USER_EXPERIENCE, 3, 5, "Familiar but requires password management")
    traditional_auth.add_score(DesignDimension.MAINTAINABILITY, 4, 4, "Simple to implement and maintain")
    traditional_auth.add_score(DesignDimension.SCALABILITY, 4, 4, "Scales well with proper session handling")
    traditional_auth.add_score(DesignDimension.TIME_TO_MARKET, 5, 5, "Quick to implement")
    traditional_auth.risks.extend([
        "Password breaches", "Credential stuffing attacks", "Password reset vulnerabilities"
    ])
    
    oauth_sso = explorer.create_alternative(
        "oauth_sso",
        "OAuth/SSO Integration",
        "Use OAuth providers like Google, GitHub, Microsoft for authentication",
        "Redirect to OAuth provider, handle callback, store user info"
    )
    
    oauth_sso.add_score(DesignDimension.SECURITY, 4, 4, "Offloads security to proven providers")
    oauth_sso.add_score(DesignDimension.USER_EXPERIENCE, 4, 4, "Convenient, no new passwords")
    oauth_sso.add_score(DesignDimension.MAINTAINABILITY, 4, 3, "Less auth code but OAuth complexity")
    oauth_sso.add_score(DesignDimension.SCALABILITY, 5, 4, "Providers handle scale")
    oauth_sso.add_score(DesignDimension.TIME_TO_MARKET, 4, 4, "Quick integration but OAuth setup needed")
    oauth_sso.risks.extend([
        "Provider downtime", "OAuth token vulnerabilities", "User locked to specific providers"
    ])
    
    return explorer
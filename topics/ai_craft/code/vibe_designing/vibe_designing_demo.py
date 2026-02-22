#!/usr/bin/env python3
"""
Vibe Designing Demo - Interactive demonstration of the TAM4 concepts

This demo walks through the complete vibe designing process:
1. Domain modeling before prompting
2. Socratic questioning for assumption challenges  
3. Design exploration and comparison
4. Assumption tracking and validation

Usage: python vibe_designing_demo.py
"""

import json
from typing import Dict, Any

from domain_modeling import (
    DomainModelBuilder, EntityLifecycleState, DomainModel
)
from socratic_prompting import (
    SocraticSession, QuestionType, DesignAlternative as SocraticAlternative
)
from assumption_tracking import (
    AssumptionRegistry, Evidence, ValidationMethod, ValidationTask
)
from design_exploration import (
    DesignExplorer, DesignDimension, get_common_patterns
)


def print_header(title: str):
    """Print a formatted section header"""
    print("\n" + "="*60)
    print(f" {title}")
    print("="*60)


def print_subheader(title: str):
    """Print a formatted subsection header"""
    print(f"\n--- {title} ---")


def demo_domain_modeling():
    """Demonstrate domain modeling before coding"""
    print_header("STEP 1: DOMAIN MODELING (Before Prompting)")
    
    print("Problem: Design a user notification system for a mobile app")
    print("\nBefore jumping into code generation, let's model the domain...")
    
    # Build a comprehensive domain model
    model = (DomainModelBuilder("User Notification System", 
                               "System for managing and delivering notifications to mobile app users")
        # Domain invariants
        .with_invariant(
            "user_consent",
            "Users must explicitly consent to receive notifications",
            "No notifications sent without user opt-in per category",
            priority=1
        )
        .with_invariant(
            "rate_limiting",
            "System must respect notification frequency limits",
            "Maximum 5 notifications per user per day unless urgent",
            priority=1
        )
        .with_invariant(
            "delivery_tracking",
            "All notification attempts must be logged",
            "Track sent, delivered, opened, and failed notifications",
            priority=2
        )
        # Edge cases
        .with_edge_case(
            "User disables notifications after consent",
            "high",
            4,
            "Respect system-level notification settings dynamically"
        )
        .with_edge_case(
            "Network failure during notification delivery",
            "medium",
            3,
            "Implement retry logic with exponential backoff"
        )
        .with_edge_case(
            "User receives duplicate notifications",
            "medium",
            2,
            "Implement deduplication based on content and timing"
        )
        # Assumptions
        .with_assumption("Users want timely notifications for important events")
        .with_assumption("Push notification services (FCM, APNS) are reliable")
        .with_assumption("Users will engage with notifications if relevant")
        .with_assumption("Notification preferences are relatively stable")
        # Entity lifecycle
        .with_entity("Notification")
            .with_states(
                EntityLifecycleState.CREATED,
                EntityLifecycleState.ACTIVE,
                EntityLifecycleState.ARCHIVED
            )
            .with_transition(EntityLifecycleState.CREATED, EntityLifecycleState.ACTIVE)
            .with_transition(EntityLifecycleState.ACTIVE, EntityLifecycleState.ARCHIVED)
            .with_business_event("NotificationScheduled")
            .with_business_event("NotificationSent")
            .with_business_event("NotificationDelivered")
            .with_business_event("NotificationOpened")
            .with_business_event("NotificationFailed")
            .and_model()
        .build()
    )
    
    print("\n📋 DOMAIN MODEL SUMMARY:")
    print(f"• {len(model.invariants)} domain invariants identified")
    print(f"• {len(model.edge_cases)} edge cases discovered") 
    print(f"• {len(model.assumptions)} assumptions to validate")
    print(f"• {len(model.entities)} entities with lifecycles")
    
    print("\n🔴 CRITICAL INVARIANTS:")
    for inv in model.get_critical_invariants():
        print(f"  • {inv.name}: {inv.rule}")
    
    print("\n⚠️  HIGH RISK EDGE CASES:")
    for case in model.get_high_risk_cases():
        print(f"  • {case.scenario} (Risk: {case.risk_score()})")
        if case.mitigation:
            print(f"    → Mitigation: {case.mitigation}")
    
    input("\nPress Enter to continue to Socratic questioning...")
    return model


def demo_socratic_questioning(domain_model: DomainModel):
    """Demonstrate Socratic questioning process"""
    print_header("STEP 2: SOCRATIC QUESTIONING (While Prompting)")
    
    print("Now let's challenge our assumptions and explore alternatives...")
    print("This is where you'd engage with AI to question everything!")
    
    # Create Socratic session
    session = SocraticSession(
        problem_statement="Design a user notification system for a mobile app"
    )
    
    # Add assumptions from domain model
    for assumption in domain_model.assumptions:
        session.add_assumption(assumption)
    
    # Add some constraints
    session.add_constraint("Must support both iOS and Android")
    session.add_constraint("Notifications must be delivered within 30 seconds")
    session.add_constraint("System must handle 100k users initially")
    session.add_constraint("Must comply with privacy regulations")
    
    # Generate questions
    questions = session.generate_questions()
    
    print(f"\n🤔 GENERATED {len(questions)} SOCRATIC QUESTIONS:")
    
    # Show sample questions by type
    for qtype in QuestionType:
        type_questions = session.get_questions_by_type(qtype)
        if type_questions:
            print(f"\n{qtype.value.title().replace('_', ' ')} Questions:")
            for i, q in enumerate(type_questions[:2], 1):  # Show first 2
                print(f"  {i}. {q.question}")
    
    # Simulate discovering alternatives through questioning
    print("\n💡 ALTERNATIVES DISCOVERED THROUGH QUESTIONING:")
    
    # Add alternatives discovered via Socratic process
    session.add_alternative(SocraticAlternative(
        name="Event-Driven Architecture",
        description="Use event streaming for real-time notification triggers",
        trade_offs={
            "pros": "Real-time processing, scalable, decoupled components",
            "cons": "Added complexity, eventual consistency, operational overhead"
        },
        complexity_score=4,
        risk_level="medium", 
        implementation_effort="high",
        discovered_via="Questioning constraint about 30-second delivery requirement"
    ))
    
    session.add_alternative(SocraticAlternative(
        name="Progressive Enhancement",
        description="Start with simple notifications, add features based on user behavior",
        trade_offs={
            "pros": "Lower initial complexity, user-driven features, faster time to market",
            "cons": "May miss important use cases, requires analytics, ongoing development"
        },
        complexity_score=2,
        risk_level="low",
        implementation_effort="medium",
        discovered_via="Challenging assumption about notification feature completeness"
    ))
    
    for alt in session.alternatives:
        print(f"\n  📎 {alt.name}")
        print(f"     {alt.description}")
        print(f"     Complexity: {alt.complexity_score}/5, Risk: {alt.risk_level}")
        print(f"     Discovered via: {alt.discovered_via}")
    
    input("\nPress Enter to continue to design exploration...")
    return session


def demo_design_exploration(session: SocraticSession):
    """Demonstrate systematic design exploration"""
    print_header("STEP 3: DESIGN EXPLORATION (After Prompting)")
    
    print("Let's systematically explore and compare design alternatives...")
    
    # Create design explorer
    explorer = DesignExplorer("User notification system for mobile app")
    
    # Add common patterns
    for pattern in get_common_patterns():
        explorer.add_pattern(pattern)
    
    # Set evaluation criteria based on domain requirements
    explorer.set_evaluation_criteria({
        DesignDimension.SCALABILITY: 0.25,
        DesignDimension.RELIABILITY: 0.25,
        DesignDimension.MAINTAINABILITY: 0.2,
        DesignDimension.USER_EXPERIENCE: 0.15,
        DesignDimension.TIME_TO_MARKET: 0.15
    })
    
    print("\n📊 EVALUATION CRITERIA (weighted):")
    for dim, weight in explorer.evaluation_criteria.items():
        print(f"  • {dim.value}: {weight*100:.0f}%")
    
    # Create detailed alternatives based on Socratic discoveries
    simple_queue = explorer.create_alternative(
        "simple_queue",
        "Simple Queue-Based System",
        "Traditional queue-based notification system with background workers",
        "Queue notifications → Background workers → Push to devices"
    )
    
    simple_queue.add_score(DesignDimension.SCALABILITY, 3, 4, "Queues scale well but workers may bottleneck")
    simple_queue.add_score(DesignDimension.RELIABILITY, 4, 4, "Well-understood pattern, proven reliability")
    simple_queue.add_score(DesignDimension.MAINTAINABILITY, 4, 5, "Simple architecture, easy to debug")
    simple_queue.add_score(DesignDimension.USER_EXPERIENCE, 3, 3, "Reliable but not real-time")
    simple_queue.add_score(DesignDimension.TIME_TO_MARKET, 5, 5, "Quick to implement with existing tools")
    simple_queue.risks.extend([
        "Queue backlog during high traffic",
        "Worker failure handling complexity",
        "Not real-time for urgent notifications"
    ])
    
    event_streaming = explorer.create_alternative(
        "event_streaming", 
        "Event Streaming Architecture",
        "Real-time event streaming with stream processing for notifications",
        "Event stream → Stream processors → Real-time notification delivery"
    )
    
    event_streaming.add_score(DesignDimension.SCALABILITY, 5, 4, "Horizontally scalable stream processing")
    event_streaming.add_score(DesignDimension.RELIABILITY, 3, 3, "Complex failure modes, eventual consistency")
    event_streaming.add_score(DesignDimension.MAINTAINABILITY, 2, 4, "Complex debugging, distributed system challenges")
    event_streaming.add_score(DesignDimension.USER_EXPERIENCE, 5, 4, "Real-time notifications, immediate delivery")
    event_streaming.add_score(DesignDimension.TIME_TO_MARKET, 2, 4, "Complex setup, requires streaming infrastructure")
    event_streaming.risks.extend([
        "Stream processing complexity",
        "Event ordering challenges",
        "Infrastructure operational overhead"
    ])
    
    # Compare alternatives
    print("\n🏆 ALTERNATIVE RANKINGS:")
    rankings = explorer.rank_alternatives()
    for i, (alt_id, score, alt) in enumerate(rankings, 1):
        print(f"  {i}. {alt.name}: {score:.2f}/5.0")
        print(f"     {alt.description}")
    
    # Detailed comparison
    print("\n🔍 DETAILED COMPARISON:")
    comparison = explorer.compare_alternatives("simple_queue", "event_streaming")
    
    print(f"\n{comparison['alternative_1']['name']} vs {comparison['alternative_2']['name']}")
    print(f"Overall Scores: {comparison['overall_scores']['simple_queue']:.2f} vs {comparison['overall_scores']['event_streaming']:.2f}")
    
    print("\nDimension-by-dimension:")
    for dim, comp in comparison['dimension_comparison'].items():
        winner = comp['winner']
        if winner != 'tie':
            winner_name = comparison['alternative_1']['name'] if winner == 'simple_queue' else comparison['alternative_2']['name']
            print(f"  {dim}: {winner_name} wins ({comp[f'{winner}_score']}/5)")
    
    # Generate hybrid
    print("\n🔄 GENERATING HYBRID ALTERNATIVE:")
    hybrid = explorer.generate_hybrid_alternative(
        ["simple_queue", "event_streaming"],
        "Progressive Streaming System"
    )
    
    print(f"Created: {hybrid.name}")
    print(f"Description: {hybrid.description}")
    print(f"Overall Score: {hybrid.get_overall_score(explorer.evaluation_criteria):.2f}")
    
    # Suggestions
    print("\n💡 IMPROVEMENT SUGGESTIONS:")
    for alt_id in explorer.alternatives.keys():
        suggestions = explorer.suggest_improvements(alt_id)
        if suggestions:
            alt_name = explorer.alternatives[alt_id].name
            print(f"\n  For {alt_name}:")
            for suggestion in suggestions:
                print(f"    • {suggestion}")
    
    input("\nPress Enter to continue to assumption tracking...")
    return explorer


def demo_assumption_tracking(domain_model: DomainModel, session: SocraticSession):
    """Demonstrate assumption tracking and validation"""
    print_header("STEP 4: ASSUMPTION TRACKING & VALIDATION")
    
    print("Finally, let's track and validate our assumptions systematically...")
    
    # Create assumption registry
    registry = AssumptionRegistry("User Notification System")
    
    # Add assumptions from domain model and session
    all_assumptions = set(domain_model.assumptions + session.assumptions)
    
    assumption_map = {
        "user_engagement": "Users will engage with notifications if relevant",
        "service_reliability": "Push notification services (FCM, APNS) are reliable",
        "preference_stability": "Notification preferences are relatively stable",
        "timely_delivery": "Users want timely notifications for important events"
    }
    
    for key, description in assumption_map.items():
        if any(description in assumption for assumption in all_assumptions):
            registry.create_assumption(
                key,
                description,
                "Domain modeling and Socratic questioning",
                "Feature adoption and user satisfaction at risk",
                priority=1 if "reliable" in description or "timely" in description else 2
            )
    
    print(f"\n📝 TRACKING {len(registry.assumptions)} ASSUMPTIONS:")
    for assumption in registry.assumptions.values():
        print(f"  • {assumption.description}")
        print(f"    Priority: {assumption.priority}, Status: {assumption.status.value}")
    
    # Add evidence for some assumptions
    print("\n🔍 ADDING VALIDATION EVIDENCE:")
    
    # Evidence for user engagement
    user_engagement = registry.get_assumption("user_engagement")
    if user_engagement:
        user_engagement.add_evidence(Evidence(
            description="Industry study shows 15% avg notification open rate",
            source="Mobile Marketing Statistics 2023",
            supports=True,
            confidence=3,
            url_or_reference="https://example.com/mobile-stats"
        ))
        
        user_engagement.add_evidence(Evidence(
            description="Our competitor has 23% open rate reported",
            source="Competitor analysis",
            supports=True,
            confidence=4
        ))
        print(f"  ✅ {user_engagement.description}")
        print(f"     Status: {user_engagement.status.value}")
        print(f"     Evidence count: {len(user_engagement.evidence)}")
    
    # Add validation tasks
    print("\n📋 VALIDATION TASKS CREATED:")
    
    service_reliability = registry.get_assumption("service_reliability")
    if service_reliability:
        task = ValidationTask(
            description="Monitor FCM/APNS uptime and delivery rates for 1 month",
            method=ValidationMethod.DATA_ANALYSIS,
            assigned_to="DevOps Team"
        )
        service_reliability.add_validation_task(task)
        print(f"  • Task: {task.description}")
        print(f"    Method: {task.method.value}, Assigned: {task.assigned_to}")
    
    preference_stability = registry.get_assumption("preference_stability")  
    if preference_stability:
        task = ValidationTask(
            description="Survey users about notification preference changes",
            method=ValidationMethod.USER_RESEARCH,
            assigned_to="UX Research Team"
        )
        preference_stability.add_validation_task(task)
        print(f"  • Task: {task.description}")
        print(f"    Method: {task.method.value}, Assigned: {task.assigned_to}")
    
    # Summary report
    print("\n📊 ASSUMPTION REGISTRY SUMMARY:")
    summary = registry.to_dict()['summary']
    print(f"  Total assumptions: {summary['total_assumptions']}")
    print(f"  Critical unvalidated: {summary['critical_unvalidated']}")
    print("  Status breakdown:")
    for status, count in summary['by_status'].items():
        if count > 0:
            print(f"    • {status}: {count}")
    
    # Critical assumptions needing attention
    critical_unvalidated = registry.get_critical_unvalidated()
    if critical_unvalidated:
        print(f"\n🚨 CRITICAL ASSUMPTIONS NEEDING VALIDATION:")
        for assumption in critical_unvalidated:
            print(f"  • {assumption.description}")
            print(f"    Impact if wrong: {assumption.impact_if_wrong}")
    
    input("\nPress Enter to see the complete workflow summary...")
    return registry


def demo_complete_workflow():
    """Run the complete vibe designing workflow"""
    print_header("VIBE DESIGNING: FROM PROBLEM TO VALIDATION")
    
    print("""
This demo illustrates the complete Vibe Designing process from TAM4:

🎯 THE PROBLEM: Design a user notification system for a mobile app

Instead of immediately prompting an AI to generate code, we follow the
structured approach of deepening our understanding first.

The workflow demonstrates:
1. Domain Modeling BEFORE prompting (3 minutes)
2. Socratic Questioning WHILE prompting (2 minutes) 
3. Design Exploration AFTER prompting (1 minute)
4. Assumption Tracking throughout the process

This approach transforms AI from a "code vending machine" into a
"Socratic partner" for better design thinking.
    """)
    
    input("Press Enter to start the demo...")
    
    # Step 1: Domain modeling
    domain_model = demo_domain_modeling()
    
    # Step 2: Socratic questioning 
    socratic_session = demo_socratic_questioning(domain_model)
    
    # Step 3: Design exploration
    design_explorer = demo_design_exploration(socratic_session)
    
    # Step 4: Assumption tracking
    assumption_registry = demo_assumption_tracking(domain_model, socratic_session)
    
    # Final summary
    print_header("COMPLETE WORKFLOW SUMMARY")
    
    print("🎉 VIBE DESIGNING PROCESS COMPLETE!")
    print(f"""
📋 DOMAIN MODEL: {len(domain_model.invariants)} invariants, {len(domain_model.edge_cases)} edge cases
🤔 SOCRATIC SESSION: {len(socratic_session.questions)} questions, {len(socratic_session.alternatives)} alternatives discovered  
🔍 DESIGN EXPLORATION: {len(design_explorer.alternatives)} alternatives compared
📝 ASSUMPTION TRACKING: {len(assumption_registry.assumptions)} assumptions being validated

KEY INSIGHT: Instead of rushing to code generation, we spent time understanding
the problem domain, challenging assumptions, and systematically exploring 
alternatives. This leads to better prompting and ultimately better solutions.

The result? We're now ready to generate code with:
- Clear domain understanding
- Validated assumptions  
- Compared alternatives
- Identified risks and constraints

THIS is vibe designing: using AI to think better, not just code faster.
    """)
    
    print("\n" + "="*60)
    print(" Thank you for trying Vibe Designing!")
    print("="*60)


if __name__ == "__main__":
    try:
        demo_complete_workflow()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted. Thanks for trying Vibe Designing!")
    except Exception as e:
        print(f"\nDemo error: {e}")
        print("This is a demonstration - in real usage, you'd handle errors gracefully.")
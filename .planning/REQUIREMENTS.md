# Requirements: IRIS-2 Learnings Presentation

**Defined:** 2026-01-27
**Core Value:** Show practitioners how to consciously position on Speed/Understanding/Reliability triangle

## Milestone 2: IRIS-2 Learnings Presentation

Requirements for 8-10 slide internal Bloomberg presentation.

### Structure

- [x] **STRUCT-01**: Opening slide with hook — "Same confidence, different warrant"
- [x] **STRUCT-02**: Trade-off Triangle visual as central framework
- [ ] **STRUCT-03**: Closing slide with actionable takeaways for colleagues

### Understanding Vertex (DDD Pull)

- [x] **UNDR-01**: Bounded contexts with glob-activated rules example (`.cursor/rules/*.mdc`)
- [x] **UNDR-02**: Ubiquitous language via `constants.py` example
- [x] **UNDR-03**: Business rules loaded in context files example (`experiments.mdc`)

### Reliability Vertex (TDD Pull)

- [x] **RELY-01**: Human-authored E2E test as circular validation breaker (`test_user_journey_e2e.py`)
- [x] **RELY-02**: Mock boundaries defined in testing rules
- [x] **RELY-03**: "Do NOT Over-Generate Tests" rule

### Speed Vertex (Workflow Pull)

- [x] **SPEED-01**: Workflow commands for structured LLM interactions (`.cursor/commands/`)
- [x] **SPEED-02**: LOC metrics in PR descriptions ("Pure Code Added" column)
- [x] **SPEED-03**: Verification-before-fix workflow (`verifyeventuallyfix.md`)

### Meta/Workflow

- [x] **META-01**: GSD as successor to custom commands
- [x] **META-02**: Multi-AI context sync script (`sync-ai-instructions.sh`)

## Out of Scope

| Feature | Reason |
|---------|--------|
| Full epistemic debt theory | Presentation is practical, not theoretical |
| Article content | Paused milestone |
| External conference version | Internal team first |
| Measurement section | Too speculative for concrete presentation |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| STRUCT-01 | Phase 9 | Complete |
| STRUCT-02 | Phase 9 | Complete |
| STRUCT-03 | Phase 11 | Pending |
| UNDR-01 | Phase 10 | Complete |
| UNDR-02 | Phase 10 | Complete |
| UNDR-03 | Phase 10 | Complete |
| RELY-01 | Phase 10 | Complete |
| RELY-02 | Phase 10 | Complete |
| RELY-03 | Phase 10 | Complete |
| SPEED-01 | Phase 10 | Complete |
| SPEED-02 | Phase 10 | Complete |
| SPEED-03 | Phase 10 | Complete |
| META-01 | Phase 10 | Complete |
| META-02 | Phase 10 | Complete |

**Coverage:**
- Total requirements: 14
- Mapped to phases: 14
- Unmapped: 0

---
*Requirements defined: 2026-01-27*
*Last updated: 2026-01-27 after initial definition*

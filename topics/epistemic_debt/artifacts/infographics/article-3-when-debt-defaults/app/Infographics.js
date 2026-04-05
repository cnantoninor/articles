'use client';

import { useState, useRef, useEffect, useCallback } from 'react';

const T = {
  bg: '#0c0e13',
  surface: '#14171e',
  surfaceHover: '#1a1e28',
  border: '#252a36',
  text: '#e2e4e9',
  textMuted: '#8a8f9e',
  accent: '#f97316',
  accentAlt: '#3b82f6',
  danger: '#ef4444',
  success: '#22c55e',
  purple: '#a855f7',
  cream: '#fef3c7',
  font: "'JetBrains Mono', 'SF Mono', 'Fira Code', monospace",
  fontDisplay: "'Space Grotesk', 'Inter', sans-serif",
};

function useAnimatedValue(target, duration = 1200) {
  const [value, setValue] = useState(0);
  const rafRef = useRef(null);
  const startRef = useRef(null);
  const startValRef = useRef(0);

  useEffect(() => {
    if (rafRef.current) cancelAnimationFrame(rafRef.current);
    startRef.current = null;
    startValRef.current = value;
    const from = startValRef.current;
    const to = target;

    const step = (ts) => {
      if (!startRef.current) startRef.current = ts;
      const elapsed = ts - startRef.current;
      const t = Math.min(elapsed / duration, 1);
      const ease = 1 - Math.pow(1 - t, 3);
      setValue(from + (to - from) * ease);
      if (t < 1) rafRef.current = requestAnimationFrame(step);
    };
    rafRef.current = requestAnimationFrame(step);
    return () => { if (rafRef.current) cancelAnimationFrame(rafRef.current); };
  }, [target, duration]);

  return value;
}

// Tooltip for formula terms
function FormulaTooltip({ term, definition, children }) {
  const [show, setShow] = useState(false);
  return (
    <span
      style={{ position: 'relative', display: 'inline-block', cursor: 'help' }}
      onMouseEnter={() => setShow(true)}
      onMouseLeave={() => setShow(false)}
    >
      <span style={{
        color: T.accent,
        fontFamily: T.font,
        fontSize: 12,
        borderBottom: `1px dashed ${T.accent}80`,
      }}>{children}</span>
      {show && (
        <span style={{
          position: 'absolute',
          bottom: '100%',
          left: '50%',
          transform: 'translateX(-50%)',
          marginBottom: 6,
          background: T.surfaceHover,
          border: `1px solid ${T.border}`,
          borderRadius: 6,
          padding: '6px 10px',
          width: 200,
          fontSize: 11,
          fontFamily: T.font,
          color: T.text,
          zIndex: 100,
          whiteSpace: 'normal',
          lineHeight: 1.5,
          boxShadow: `0 4px 12px ${T.bg}cc`,
          pointerEvents: 'none',
        }}>
          <span style={{ color: T.accent, fontWeight: 700 }}>{term}</span>
          {' — '}
          {definition}
        </span>
      )}
    </span>
  );
}

// ─── Component 1: FrictionRemoval ────────────────────────────────────────────

function FrictionRemoval() {
  const [postLLM, setPostLLM] = useState(false);

  const steps = [
    { id: 'search', label: 'Search', icon: '🔍', frictionLabel: 'Filter noise' },
    { id: 'adapt', label: 'Adapt', icon: '✂️', frictionLabel: 'Remove irrelevant parts' },
    { id: 'integrate', label: 'Integrate', icon: '🔗', frictionLabel: 'Fit to your context' },
    { id: 'reconcile', label: 'Reconcile', icon: '⚖️', frictionLabel: 'Resolve conflicts' },
    { id: 'commit', label: 'Commit', icon: '✅', frictionLabel: null },
  ];

  return (
    <div>
      <div style={{ display: 'flex', gap: 8, marginBottom: 20 }}>
        {['Pre-LLM', 'Post-LLM'].map((label, i) => (
          <button
            key={label}
            onClick={() => setPostLLM(i === 1)}
            style={{
              padding: '6px 16px',
              borderRadius: 20,
              border: `1px solid ${(postLLM ? i === 1 : i === 0) ? T.accent : T.border}`,
              background: (postLLM ? i === 1 : i === 0) ? `${T.accent}20` : 'transparent',
              color: (postLLM ? i === 1 : i === 0) ? T.accent : T.textMuted,
              fontFamily: T.font,
              fontSize: 11,
              cursor: 'pointer',
            }}
          >
            {label}
          </button>
        ))}
      </div>

      <div style={{ display: 'flex', alignItems: 'center', gap: 0, marginBottom: 24, flexWrap: 'wrap', gap: 8 }}>
        {steps.map((step, i) => {
          const hasFriction = step.frictionLabel !== null;
          const frictionRemoved = postLLM && hasFriction;

          return (
            <div key={step.id} style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
              <div style={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                gap: 4,
              }}>
                <div style={{
                  padding: '8px 14px',
                  borderRadius: 8,
                  background: step.id === 'commit'
                    ? `${T.success}20`
                    : frictionRemoved
                    ? `${T.border}40`
                    : postLLM && !hasFriction
                    ? `${T.success}20`
                    : `${T.accentAlt}20`,
                  border: `1px solid ${step.id === 'commit'
                    ? T.success
                    : frictionRemoved
                    ? T.border
                    : T.accentAlt}`,
                  color: frictionRemoved ? T.border : step.id === 'commit' ? T.success : T.accentAlt,
                  fontFamily: T.font,
                  fontSize: 11,
                  fontWeight: 700,
                  transition: 'all 0.4s',
                  opacity: frictionRemoved ? 0.3 : 1,
                  textDecoration: frictionRemoved ? 'line-through' : 'none',
                  minWidth: 80,
                  textAlign: 'center',
                }}>
                  {step.icon} {step.label}
                </div>
                {hasFriction && (
                  <div style={{
                    fontSize: 9,
                    fontFamily: T.font,
                    color: frictionRemoved ? T.border : T.textMuted,
                    opacity: frictionRemoved ? 0.3 : 0.8,
                    transition: 'all 0.4s',
                    textAlign: 'center',
                    maxWidth: 90,
                    lineHeight: 1.3,
                    textDecoration: frictionRemoved ? 'line-through' : 'none',
                  }}>
                    {step.frictionLabel}
                  </div>
                )}
              </div>
              {i < steps.length - 1 && (
                <div style={{
                  color: T.textMuted,
                  fontSize: 16,
                  opacity: 0.5,
                }}>→</div>
              )}
            </div>
          );
        })}
      </div>

      {postLLM && (
        <div style={{
          padding: '12px 16px',
          background: `${T.danger}10`,
          border: `1px dashed ${T.danger}60`,
          borderRadius: 8,
          marginBottom: 12,
          animation: 'fadeIn 0.4s ease',
        }}>
          <div style={{ fontFamily: T.font, fontSize: 11, color: T.danger, fontWeight: 700, marginBottom: 4 }}>
            COMPREHENSION GAP
          </div>
          <div style={{ fontFamily: T.font, fontSize: 11, color: T.textMuted, lineHeight: 1.6 }}>
            Code arrives whole: interfaces, error handling, architecture — all at once. The friction that forced
            integration work is gone. So is the understanding that friction produced.
          </div>
        </div>
      )}

      {!postLLM && (
        <div style={{
          padding: '12px 16px',
          background: `${T.accentAlt}10`,
          border: `1px dashed ${T.accentAlt}60`,
          borderRadius: 8,
          marginBottom: 12,
        }}>
          <div style={{ fontFamily: T.font, fontSize: 11, color: T.accentAlt, fontWeight: 700, marginBottom: 4 }}>
            FRICTION AS PEDAGOGY
          </div>
          <div style={{ fontFamily: T.font, fontSize: 11, color: T.textMuted, lineHeight: 1.6 }}>
            Each step forced cognitive engagement: moving generic code to your specific context, resolving conflicts,
            understanding why it fits. Annoying. Also pedagogical.
          </div>
        </div>
      )}

      <div style={{
        padding: '10px 14px',
        background: `${T.accent}10`,
        borderLeft: `3px solid ${T.accent}`,
        borderRadius: '0 6px 6px 0',
        fontFamily: T.font,
        fontSize: 11,
        color: T.textMuted,
        fontStyle: 'italic',
        lineHeight: 1.6,
      }}>
        "Speed removes the throttle. Plausibility disarms the instinct to question."
      </div>
    </div>
  );
}

// ─── Component 2: ExperimentResults ──────────────────────────────────────────

function ExperimentResults() {
  const [viewMode, setViewMode] = useState('success'); // 'success' | 'failure'
  const [activeGroup, setActiveGroup] = useState(null);

  const groups = [
    {
      id: 'A',
      label: 'Manual Coding',
      sublabel: 'Group A — No AI',
      success: 69.2,
      failure: 30.8,
      n: '18/26',
      nFail: '8/26',
      paperLabel: 'High Cognitive Ownership',
      paperColor: T.success,
      detail: 'Participants wrote code without AI assistance. Lower velocity during development, but high understanding of their own code. When the logic bomb was injected, 18 of 26 found and fixed it within 30 minutes.',
    },
    {
      id: 'C',
      label: 'Scaffolded AI',
      sublabel: 'Group C — Explanation Gate',
      success: 61.5,
      failure: 38.5,
      n: '16/26',
      nFail: '10/26',
      paperLabel: 'Mitigated Epistemic Debt',
      paperColor: T.accentAlt,
      detail: 'AI assistance gated by an "Explanation Gate" — participants had to demonstrate understanding before integrating AI-generated code. Nearly matched manual performance (61.5% vs 69.2%), and matched unrestricted AI\'s development velocity (Tukey HSD p=.64).',
    },
    {
      id: 'B',
      label: 'Unrestricted AI',
      sublabel: 'Group B — No Gate',
      success: 23.1,
      failure: 76.9,
      n: '6/26',
      nFail: '20/26',
      paperLabel: 'Collapse of Competence',
      paperColor: T.danger,
      detail: 'AI assistance with no scaffolding. Fast velocity during development, but when AI was removed for the maintenance task, only 6 of 26 succeeded. The code was there. The understanding wasn\'t.',
    },
  ];

  const maxVal = 100;

  return (
    <div>
      <div style={{ display: 'flex', gap: 8, marginBottom: 20, alignItems: 'center' }}>
        <span style={{ fontFamily: T.font, fontSize: 11, color: T.textMuted }}>View:</span>
        {[
          { key: 'success', label: 'Success rate (paper)' },
          { key: 'failure', label: 'Failure rate (article)' },
        ].map(({ key, label }) => (
          <button
            key={key}
            onClick={() => setViewMode(key)}
            style={{
              padding: '5px 14px',
              borderRadius: 20,
              border: `1px solid ${viewMode === key ? T.accent : T.border}`,
              background: viewMode === key ? `${T.accent}20` : 'transparent',
              color: viewMode === key ? T.accent : T.textMuted,
              fontFamily: T.font,
              fontSize: 11,
              cursor: 'pointer',
            }}
          >
            {label}
          </button>
        ))}
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
        {groups.map((g) => {
          const val = viewMode === 'success' ? g.success : g.failure;
          const frac = viewMode === 'success' ? g.n : g.nFail;
          const isActive = activeGroup === g.id;

          return (
            <div key={g.id}>
              <div
                onClick={() => setActiveGroup(isActive ? null : g.id)}
                style={{
                  cursor: 'pointer',
                  padding: '12px 14px',
                  borderRadius: 8,
                  border: `1px solid ${isActive ? g.paperColor : T.border}`,
                  background: isActive ? `${g.paperColor}08` : T.surface,
                  transition: 'all 0.2s',
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 }}>
                  <div>
                    <span style={{ fontFamily: T.fontDisplay, fontSize: 13, fontWeight: 700, color: T.text }}>
                      {g.label}
                    </span>
                    <span style={{ fontFamily: T.font, fontSize: 10, color: T.textMuted, marginLeft: 8 }}>
                      {g.sublabel}
                    </span>
                  </div>
                  <div style={{ textAlign: 'right' }}>
                    <span style={{ fontFamily: T.font, fontSize: 18, fontWeight: 800, color: g.paperColor }}>
                      {val.toFixed(1)}%
                    </span>
                    <span style={{ fontFamily: T.font, fontSize: 10, color: T.textMuted, marginLeft: 6 }}>
                      ({frac})
                    </span>
                  </div>
                </div>

                <div style={{
                  height: 8,
                  borderRadius: 4,
                  background: T.border,
                  overflow: 'hidden',
                }}>
                  <div style={{
                    height: '100%',
                    width: `${(val / maxVal) * 100}%`,
                    background: g.paperColor,
                    borderRadius: 4,
                    transition: 'width 0.6s cubic-bezier(0.34, 1.56, 0.64, 1)',
                    boxShadow: `0 0 8px ${g.paperColor}60`,
                  }} />
                </div>

                <div style={{
                  marginTop: 8,
                  display: 'inline-block',
                  padding: '2px 8px',
                  borderRadius: 12,
                  background: `${g.paperColor}20`,
                  border: `1px solid ${g.paperColor}40`,
                  fontFamily: T.font,
                  fontSize: 10,
                  color: g.paperColor,
                  fontWeight: 600,
                }}>
                  {g.paperLabel}
                </div>
              </div>

              {isActive && (
                <div style={{
                  padding: '12px 14px',
                  background: `${g.paperColor}08`,
                  border: `1px solid ${g.paperColor}30`,
                  borderTop: 'none',
                  borderRadius: '0 0 8px 8px',
                  fontFamily: T.font,
                  fontSize: 11,
                  color: T.textMuted,
                  lineHeight: 1.7,
                }}>
                  {g.detail}
                </div>
              )}
            </div>
          );
        })}
      </div>

      <div style={{
        marginTop: 16,
        padding: '10px 14px',
        background: `${T.accent}10`,
        borderLeft: `3px solid ${T.accent}`,
        borderRadius: '0 6px 6px 0',
        fontFamily: T.font,
        fontSize: 11,
        color: T.textMuted,
        lineHeight: 1.6,
      }}>
        <span style={{ color: T.accent, fontWeight: 700 }}>Key finding:</span>
        {' '}Scaffolded AI (61.5%) nearly matches Manual (69.2%) on maintenance — while matching Unrestricted AI's development velocity.
        The gate costs almost nothing in productivity. It buys back most of the understanding.
      </div>

      <div style={{
        marginTop: 8,
        fontFamily: T.font,
        fontSize: 10,
        color: T.textMuted,
        opacity: 0.7,
      }}>
        Source: Sankaranarayanan (2026), arXiv:2602.20206. Preprint, not yet peer-reviewed. n=78 novice programmers. Task: binary repair success on injected logic bomb, 30 min, no AI.
      </div>
    </div>
  );
}

// ─── Component 3: BehaviorGap ─────────────────────────────────────────────────

function BehaviorGap() {
  const [showExplainer, setShowExplainer] = useState(false);

  const stats = [
    {
      pct: 96,
      label: "don't fully trust AI output",
      sublabel: 'Stated belief',
      color: T.accentAlt,
      desc: "96% of developers know, in principle, that AI-generated code is unreliable. This is the stated position.",
    },
    {
      pct: 48,
      label: 'verify before committing',
      sublabel: 'Actual behavior',
      color: T.accent,
      desc: "Only 48% verify AI-generated code before committing. Half act on the belief. Half don't.",
    },
    {
      pct: 42,
      label: 'of committed code is AI-generated',
      sublabel: 'System state',
      color: T.danger,
      desc: "42% of all committed code comes from AI. Combined with 52% unverified, this means roughly 1 in 5 committed lines is AI-generated and unverified.",
    },
  ];

  return (
    <div>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 20, marginBottom: 20 }}>
        {stats.map((s, i) => (
          <div key={i}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginBottom: 6 }}>
              <div>
                <span style={{ fontFamily: T.fontDisplay, fontSize: 13, fontWeight: 700, color: T.text }}>
                  {s.sublabel}
                </span>
              </div>
              <div style={{ display: 'flex', alignItems: 'baseline', gap: 6 }}>
                <span style={{ fontFamily: T.font, fontSize: 24, fontWeight: 800, color: s.color }}>
                  {s.pct}%
                </span>
                <span style={{ fontFamily: T.font, fontSize: 11, color: T.textMuted }}>{s.label}</span>
              </div>
            </div>
            <div style={{ height: 6, borderRadius: 3, background: T.border, overflow: 'hidden' }}>
              <div style={{
                height: '100%',
                width: `${s.pct}%`,
                background: s.color,
                borderRadius: 3,
                boxShadow: `0 0 8px ${s.color}60`,
                transition: 'width 0.8s cubic-bezier(0.34, 1.2, 0.64, 1)',
              }} />
            </div>
            <div style={{
              marginTop: 6,
              fontFamily: T.font,
              fontSize: 10,
              color: T.textMuted,
              lineHeight: 1.5,
            }}>
              {s.desc}
            </div>
          </div>
        ))}
      </div>

      <div style={{
        padding: '12px 14px',
        background: T.surface,
        border: `1px solid ${T.border}`,
        borderRadius: 8,
        marginBottom: 12,
      }}>
        <div style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          fontFamily: T.font,
          fontSize: 11,
          color: T.textMuted,
        }}>
          <span>Gap: stated belief → actual behavior</span>
          <span style={{ color: T.danger, fontWeight: 700 }}>96% → 48%</span>
        </div>
        <div style={{
          marginTop: 10,
          height: 24,
          borderRadius: 4,
          background: T.border,
          position: 'relative',
          overflow: 'hidden',
        }}>
          <div style={{
            position: 'absolute',
            left: 0,
            top: 0,
            height: '100%',
            width: '48%',
            background: T.accentAlt,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: 9,
            fontFamily: T.font,
            fontWeight: 700,
            color: T.bg,
          }}>VERIFY</div>
          <div style={{
            position: 'absolute',
            left: '48%',
            top: 0,
            height: '100%',
            width: '52%',
            background: `${T.danger}80`,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: 9,
            fontFamily: T.font,
            fontWeight: 700,
            color: T.text,
          }}>SKIP (52%)</div>
        </div>
      </div>

      <button
        onClick={() => setShowExplainer(!showExplainer)}
        style={{
          padding: '6px 14px',
          borderRadius: 6,
          border: `1px solid ${T.border}`,
          background: 'transparent',
          color: T.textMuted,
          fontFamily: T.font,
          fontSize: 11,
          cursor: 'pointer',
          marginBottom: showExplainer ? 10 : 0,
        }}
      >
        {showExplainer ? '▲ Hide' : '▼ Why the gap?'} — Automation bias
      </button>

      {showExplainer && (
        <div style={{
          padding: '12px 14px',
          background: `${T.purple}10`,
          border: `1px solid ${T.purple}30`,
          borderRadius: 8,
          fontFamily: T.font,
          fontSize: 11,
          color: T.textMuted,
          lineHeight: 1.7,
        }}>
          <div style={{ color: T.purple, fontWeight: 700, marginBottom: 6 }}>AUTOMATION BIAS</div>
          The mere presence of a decision support system suppresses monitoring behaviors that would otherwise
          surface errors. This is attentional, not motivational — experts and novices alike are affected
          (Parasuraman & Manzey, 2010). The gap between what developers say they believe and what they do
          is itself a form of epistemic debt: a gap between stated confidence and actual behavior.
        </div>
      )}

      <div style={{ marginTop: 12, fontFamily: T.font, fontSize: 10, color: T.textMuted, opacity: 0.7 }}>
        Source: Sonar (January 2026), survey of 1,100+ developers.
      </div>
    </div>
  );
}

// ─── Component 4: IndustrySignals ─────────────────────────────────────────────

function IndustrySignals() {
  const [activeMetric, setActiveMetric] = useState(null);

  const metrics = [
    {
      id: 'incidents',
      label: 'Incidents per PR',
      before: null,
      after: null,
      change: '+23.5%',
      direction: 'up',
      color: T.danger,
      note: 'PR volume rose 20% YoY. Incident rate rose faster — velocity outpaced quality assurance.',
      source: 'Cortex, 2026 Benchmark Report',
    },
    {
      id: 'duplication',
      label: 'Code duplication',
      before: '8.3%',
      after: '12.3%',
      change: '+48%',
      direction: 'up',
      color: T.danger,
      note: 'Copy-paste duplication of changed lines, 2020–2024. Code reused without refactoring.',
      source: 'GitClear 2025',
    },
    {
      id: 'refactoring',
      label: 'Refactoring activity',
      before: '25%',
      after: '<10%',
      change: '−60%+',
      direction: 'down',
      color: T.danger,
      note: 'Refactoring as share of code changes, 2021–2024. Teams generating fast, not cleaning up.',
      source: 'GitClear 2025',
    },
    {
      id: 'churn',
      label: 'Short-term churn',
      before: '3.1%',
      after: '5.7%',
      change: '+84%',
      direction: 'up',
      color: T.danger,
      note: 'New code revised shortly after authoring, 2020–2024. A signal of generating without fully understanding.',
      source: 'GitClear 2025',
    },
  ];

  const coderabbit = [
    { label: 'Logic errors', mult: 1.75, color: T.danger },
    { label: 'Maintainability', mult: 1.64, color: T.accent },
    { label: 'Security findings', mult: 1.57, color: T.purple },
    { label: 'Performance issues', mult: 1.42, color: T.accentAlt },
  ];

  return (
    <div>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 10, marginBottom: 20 }}>
        {metrics.map((m) => {
          const isActive = activeMetric === m.id;
          return (
            <div key={m.id}>
              <div
                onClick={() => setActiveMetric(isActive ? null : m.id)}
                style={{
                  padding: '10px 14px',
                  borderRadius: 8,
                  border: `1px solid ${isActive ? m.color : T.border}`,
                  background: isActive ? `${m.color}08` : T.surface,
                  cursor: 'pointer',
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  transition: 'all 0.2s',
                }}
              >
                <div style={{ fontFamily: T.fontDisplay, fontSize: 12, fontWeight: 600, color: T.text }}>
                  {m.label}
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                  {m.before && (
                    <span style={{ fontFamily: T.font, fontSize: 11, color: T.textMuted }}>
                      {m.before} → {m.after}
                    </span>
                  )}
                  <span style={{
                    fontFamily: T.font,
                    fontSize: 14,
                    fontWeight: 800,
                    color: m.color,
                  }}>
                    {m.direction === 'up' ? '↑' : '↓'} {m.change}
                  </span>
                </div>
              </div>
              {isActive && (
                <div style={{
                  padding: '10px 14px',
                  background: `${m.color}08`,
                  border: `1px solid ${m.color}30`,
                  borderTop: 'none',
                  borderRadius: '0 0 8px 8px',
                  fontFamily: T.font,
                  fontSize: 11,
                  color: T.textMuted,
                  lineHeight: 1.6,
                }}>
                  <div>{m.note}</div>
                  <div style={{ marginTop: 4, color: T.textMuted, opacity: 0.6 }}>Source: {m.source}</div>
                </div>
              )}
            </div>
          );
        })}
      </div>

      <div style={{
        padding: '14px',
        background: T.surface,
        border: `1px solid ${T.border}`,
        borderRadius: 8,
        marginBottom: 12,
      }}>
        <div style={{
          fontFamily: T.font,
          fontSize: 10,
          color: T.textMuted,
          fontWeight: 700,
          marginBottom: 12,
          textTransform: 'uppercase',
          letterSpacing: 1,
        }}>
          AI-co-authored code vs human-only code (CodeRabbit, Dec 2025 — 470 open-source PRs)
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
          {coderabbit.map((c) => (
            <div key={c.label}>
              <div style={{
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                marginBottom: 4,
              }}>
                <span style={{ fontFamily: T.font, fontSize: 11, color: T.textMuted }}>{c.label}</span>
                <span style={{ fontFamily: T.font, fontSize: 13, fontWeight: 700, color: c.color }}>
                  {c.mult}×
                </span>
              </div>
              <div style={{ height: 4, borderRadius: 2, background: T.border, overflow: 'hidden' }}>
                <div style={{
                  height: '100%',
                  width: `${((c.mult - 1) / 1.0) * 70}%`,
                  background: c.color,
                  borderRadius: 2,
                  boxShadow: `0 0 6px ${c.color}60`,
                }} />
              </div>
            </div>
          ))}
        </div>
        <div style={{ marginTop: 8, fontFamily: T.font, fontSize: 10, color: T.textMuted, opacity: 0.6 }}>
          Multipliers relative to human-only code. Small sample — directional signal, not settled evidence.
        </div>
      </div>

      <div style={{
        padding: '10px 14px',
        background: `${T.accent}10`,
        borderLeft: `3px solid ${T.accent}`,
        borderRadius: '0 6px 6px 0',
        fontFamily: T.font,
        fontSize: 11,
        color: T.textMuted,
        lineHeight: 1.6,
      }}>
        Velocity is up. Quality metrics are down. The breaking happens differently — not obvious crashes,
        but subtle failures of code that looks correct and encodes assumptions nobody examined.
      </div>
    </div>
  );
}

// ─── Component 5: CaseStudyExplorer ───────────────────────────────────────────

function CaseStudyExplorer() {
  const [activeCase, setActiveCase] = useState(0);

  const cases = [
    {
      id: 'saas',
      label: 'Case 1',
      title: 'The Database Deletion',
      org: 'SaaStr / Replit (July 2025)',
      summary: 'A SaaS founder gave an AI coding assistant production database credentials and natural-language constraints. The assistant deleted executive records and company entries, then generated replacement records and misleading status updates.',
      color: T.danger,
      terms: [
        {
          term: 'Layer (k)',
          ft: 'k',
          value: 'L3 — Architecture',
          ftDef: 'The abstraction level where the debt lives: L1=function, L2=module, L3=architecture, L4=intent',
          explanation: 'The intent was clear ("no production changes"). Missing was architectural enforcement: no dev/prod separation, no capability-level access controls.',
        },
        {
          term: 't₀',
          ft: 't₀',
          value: '~Day 6–7',
          ftDef: 'The moment when the epistemic gap is first detected and must be paid down',
          explanation: 'Early detection. The failure was loud — deletions were immediately visible. Rollback paths existed.',
        },
        {
          term: 'c₃',
          ft: 'c_k',
          value: 'Below 10× (effective)',
          ftDef: 'The cascade cost multiplier at layer k. L3 structural prediction: ~10×',
          explanation: 'Part 2 predicts c₃ ≈ 10×. Effective cost fell below this because t₀ was early, failure was loud, and rollback existed. The t₀ lever worked as intended.',
        },
        {
          term: 'Counterfactual',
          ft: null,
          value: '—',
          ftDef: null,
          explanation: 'The same L3 gap in a mature system with a later t₀ would have incurred the full structural multiplier.',
        },
      ],
      lesson: 'Underspecified linguistic constraints were treated as operational controls. Conceptual boundaries are not sufficient without hard capability boundaries.',
    },
    {
      id: 'alter',
      label: 'Case 2',
      title: 'The 10:1 Cost Ratio',
      org: 'AlterSquare (December 2025)',
      summary: 'A software development firm saved 200 hours during an MVP sprint using GitHub Copilot. Missing error handling, absent input validation, and insecure authentication patterns were buried in generated code. The team spent 2,000 hours on remediation.',
      color: T.accent,
      terms: [
        {
          term: 'Layer (k)',
          ft: 'k',
          value: 'L3 — Architecture',
          ftDef: 'The abstraction level where the debt lives: L1=function, L2=module, L3=architecture, L4=intent',
          explanation: 'Missing error handling strategy, absent input validation across critical paths, insecure authentication — cross-cutting architectural concerns, not isolated bugs.',
        },
        {
          term: 't₀',
          ft: 't₀',
          value: 'Post-MVP, in production',
          ftDef: 'The moment when the epistemic gap is first detected and must be paid down',
          explanation: 'Late detection. By the time the gap was recognized, every generated module needed re-understanding before it could be safely fixed.',
        },
        {
          term: 'c_k (effective)',
          ft: 'c_k',
          value: '≈ 10×',
          ftDef: 'The cascade cost multiplier at layer k. L3 structural prediction: ~10×',
          explanation: 'The observed 10:1 ratio (self-reported; not independently verified) aligns with the L3 structural prediction. Late t₀ compounded the cost.',
        },
        {
          term: 'Counterfactual',
          ft: null,
          value: '—',
          ftDef: null,
          explanation: 'Had t₀ arrived during the sprint (architectural review, integration testing), the gap would have been narrower and c_k far smaller than 10×.',
        },
      ],
      lesson: "The team didn't know what they didn't know. The absence of error handling wasn't immediately visible. It was a gap in what was generated, not a flaw in what was present.",
    },
  ];

  const c = cases[activeCase];

  return (
    <div>
      <div style={{ display: 'flex', gap: 8, marginBottom: 20 }}>
        {cases.map((cs, i) => (
          <button
            key={cs.id}
            onClick={() => setActiveCase(i)}
            style={{
              padding: '6px 16px',
              borderRadius: 20,
              border: `1px solid ${activeCase === i ? cs.color : T.border}`,
              background: activeCase === i ? `${cs.color}20` : 'transparent',
              color: activeCase === i ? cs.color : T.textMuted,
              fontFamily: T.font,
              fontSize: 11,
              cursor: 'pointer',
            }}
          >
            {cs.label}: {cs.title}
          </button>
        ))}
      </div>

      <div style={{
        padding: '12px 14px',
        background: T.surface,
        border: `1px solid ${c.color}40`,
        borderRadius: 8,
        marginBottom: 16,
      }}>
        <div style={{ fontFamily: T.font, fontSize: 10, color: T.textMuted, marginBottom: 4 }}>{c.org}</div>
        <div style={{ fontFamily: T.font, fontSize: 11, color: T.text, lineHeight: 1.7 }}>{c.summary}</div>
      </div>

      <div style={{ marginBottom: 14 }}>
        <div style={{
          fontFamily: T.font,
          fontSize: 10,
          color: T.textMuted,
          fontWeight: 700,
          textTransform: 'uppercase',
          letterSpacing: 1,
          marginBottom: 8,
        }}>
          Formula Mapping
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
          {c.terms.map((t, i) => (
            <div key={i} style={{
              padding: '10px 14px',
              background: T.surface,
              border: `1px solid ${T.border}`,
              borderRadius: 6,
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 4 }}>
                <div style={{ fontFamily: T.font, fontSize: 11, color: T.textMuted }}>
                  {t.ft ? (
                    <FormulaTooltip term={t.ft} definition={t.ftDef}>{t.term}</FormulaTooltip>
                  ) : (
                    <span style={{ color: T.textMuted }}>{t.term}</span>
                  )}
                </div>
                <div style={{
                  fontFamily: T.font,
                  fontSize: 12,
                  fontWeight: 700,
                  color: c.color,
                }}>
                  {t.value}
                </div>
              </div>
              <div style={{ fontFamily: T.font, fontSize: 11, color: T.textMuted, lineHeight: 1.6 }}>
                {t.explanation}
              </div>
            </div>
          ))}
        </div>
      </div>

      <div style={{
        padding: '10px 14px',
        background: `${c.color}10`,
        borderLeft: `3px solid ${c.color}`,
        borderRadius: '0 6px 6px 0',
        fontFamily: T.font,
        fontSize: 11,
        color: T.textMuted,
        fontStyle: 'italic',
        lineHeight: 1.6,
      }}>
        {c.lesson}
      </div>
    </div>
  );
}

// ─── Component 6: CostRatioSimulator ──────────────────────────────────────────

function CostRatioSimulator() {
  const [t0Position, setT0Position] = useState(85); // 0-100, where 100 = post-MVP

  // At position 85+ (post-MVP), cost = 2000h, savings = 200h
  // At position 0 (sprint start), cost ≈ 0
  // Break-even is around position 18 (40h / 200h sprint)
  const sprintHours = 200;
  const maxRemediation = 2000;

  const savings = Math.round(sprintHours * Math.min(t0Position / 100, 1));
  const costMultiplier = t0Position < 20
    ? 0.8 + (t0Position / 20) * 1.5
    : t0Position < 60
    ? 2.3 + ((t0Position - 20) / 40) * 4
    : 6.3 + ((t0Position - 60) / 40) * 13.7;
  const remediationCost = Math.round(savings * costMultiplier);
  const netGain = savings - remediationCost;
  const ratio = savings > 0 ? (remediationCost / savings).toFixed(1) : '—';

  const breakEven = t0Position <= 18;
  const isArticleScenario = t0Position >= 80;

  const getLabel = () => {
    if (t0Position <= 5) return 'Sprint day 1 — gap caught immediately';
    if (t0Position <= 18) return 'Sprint day ~36 — early review catches gaps';
    if (t0Position <= 40) return 'Mid-sprint — some modules already entangled';
    if (t0Position <= 70) return 'Near completion — most code committed';
    if (t0Position <= 85) return 'End of sprint — MVP delivered';
    return 'Post-MVP in production — AlterSquare scenario';
  };

  return (
    <div>
      <div style={{ marginBottom: 20 }}>
        <div style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          marginBottom: 8,
        }}>
          <span style={{ fontFamily: T.font, fontSize: 11, color: T.textMuted }}>
            Position of{' '}
            <FormulaTooltip term="t₀" definition="The moment when the epistemic gap is first detected and must be paid down">
              t₀
            </FormulaTooltip>
          </span>
          <span style={{
            fontFamily: T.font,
            fontSize: 11,
            color: isArticleScenario ? T.danger : breakEven ? T.success : T.accent,
            fontWeight: 700,
          }}>
            {getLabel()}
          </span>
        </div>
        <input
          type="range"
          min={0}
          max={100}
          value={t0Position}
          onChange={(e) => setT0Position(Number(e.target.value))}
          style={{
            width: '100%',
            accentColor: T.accent,
            cursor: 'pointer',
          }}
        />
        <div style={{
          display: 'flex',
          justifyContent: 'space-between',
          fontFamily: T.font,
          fontSize: 9,
          color: T.textMuted,
          marginTop: 4,
        }}>
          <span>Sprint start</span>
          <span>Mid-sprint</span>
          <span>Post-MVP</span>
        </div>
      </div>

      <div style={{ display: 'flex', gap: 10, marginBottom: 20, flexWrap: 'wrap' }}>
        {[
          { label: 'Hours saved', value: `${savings}h`, color: T.success },
          { label: 'Remediation cost', value: `${remediationCost.toLocaleString()}h`, color: T.danger },
          { label: 'Cost ratio', value: `${ratio}:1`, color: netGain < 0 ? T.danger : T.success },
          { label: 'Net', value: netGain >= 0 ? `+${netGain}h` : `${netGain}h`, color: netGain >= 0 ? T.success : T.danger },
        ].map((s) => (
          <div key={s.label} style={{
            flex: 1,
            minWidth: 100,
            padding: '10px 12px',
            background: T.surface,
            border: `1px solid ${T.border}`,
            borderRadius: 8,
            textAlign: 'center',
          }}>
            <div style={{ fontFamily: T.font, fontSize: 9, color: T.textMuted, marginBottom: 4 }}>{s.label}</div>
            <div style={{ fontFamily: T.font, fontSize: 16, fontWeight: 800, color: s.color }}>{s.value}</div>
          </div>
        ))}
      </div>

      {/* Visual bar comparison */}
      <div style={{ marginBottom: 16 }}>
        <div style={{ marginBottom: 8 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 4 }}>
            <span style={{ fontFamily: T.font, fontSize: 10, color: T.success }}>Savings</span>
            <span style={{ fontFamily: T.font, fontSize: 10, color: T.success }}>{savings}h</span>
          </div>
          <div style={{ height: 14, borderRadius: 3, background: T.border, overflow: 'hidden' }}>
            <div style={{
              height: '100%',
              width: `${(savings / maxRemediation) * 100}%`,
              background: T.success,
              borderRadius: 3,
              transition: 'width 0.3s',
            }} />
          </div>
        </div>
        <div>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 4 }}>
            <span style={{ fontFamily: T.font, fontSize: 10, color: T.danger }}>Remediation</span>
            <span style={{ fontFamily: T.font, fontSize: 10, color: T.danger }}>{remediationCost.toLocaleString()}h</span>
          </div>
          <div style={{ height: 14, borderRadius: 3, background: T.border, overflow: 'hidden' }}>
            <div style={{
              height: '100%',
              width: `${Math.min((remediationCost / maxRemediation) * 100, 100)}%`,
              background: T.danger,
              borderRadius: 3,
              transition: 'width 0.3s',
            }} />
          </div>
        </div>
      </div>

      {breakEven && (
        <div style={{
          padding: '10px 14px',
          background: `${T.success}10`,
          border: `1px solid ${T.success}40`,
          borderRadius: 8,
          fontFamily: T.font,
          fontSize: 11,
          color: T.success,
          lineHeight: 1.6,
        }}>
          Break-even zone: early detection keeps recovery cost manageable. The t₀ lever works.
        </div>
      )}

      {isArticleScenario && (
        <div style={{
          padding: '10px 14px',
          background: `${T.danger}10`,
          border: `1px solid ${T.danger}40`,
          borderRadius: 8,
          fontFamily: T.font,
          fontSize: 11,
          color: T.textMuted,
          lineHeight: 1.6,
        }}>
          <span style={{ color: T.danger, fontWeight: 700 }}>AlterSquare scenario:</span>
          {' '}200h saved → 2,000h remediation. Every generated module had to be re-understood before it could be safely fixed. Self-reported figures; not independently verified.
        </div>
      )}

      <div style={{ marginTop: 12, fontFamily: T.font, fontSize: 10, color: T.textMuted, opacity: 0.7 }}>
        Model is illustrative — demonstrates the t₀ lever from Part 2's break-even analysis applied to the AlterSquare numbers. Not a precise cost formula.
      </div>
    </div>
  );
}

// ─── Component 7: ScaleSpectrum ───────────────────────────────────────────────

function ScaleSpectrum() {
  const [activeNode, setActiveNode] = useState(null);

  const nodes = [
    {
      id: 'saas',
      label: 'SaaStr / Replit',
      scale: 'Startup',
      date: 'July 2025',
      t0: 'Early (Day 6–7)',
      visibility: 'Loud — immediate',
      blastRadius: 'One project',
      layer: 'L3',
      color: T.accent,
      scaleIcon: '●',
      outcome: 'Production DB deleted and replaced with fabricated data. Platform CEO acknowledged within 48h. Incident #1152 in AI Incident Database.',
      pattern: 'Linguistic constraints treated as operational controls. No hard capability boundaries.',
    },
    {
      id: 'alter',
      label: 'AlterSquare',
      scale: 'Small firm',
      date: 'December 2025',
      t0: 'Late — post-MVP',
      visibility: 'Silent — gradual',
      blastRadius: 'Entire codebase',
      layer: 'L3',
      color: T.danger,
      scaleIcon: '●●',
      outcome: '200h saved → 2,000h remediation. Missing error handling, absent validation, insecure auth patterns across MVP. Self-reported figures.',
      pattern: 'Architectural debt accumulated across entire sprint. Late t₀ meant every module needed re-understanding.',
    },
    {
      id: 'aws',
      label: 'AWS / Kiro',
      scale: 'Enterprise',
      date: 'December 2025',
      t0: 'Not reported',
      visibility: 'Loud — outage',
      blastRadius: 'AWS Cost Explorer',
      layer: 'L3 (reported)',
      color: T.purple,
      scaleIcon: '●●●',
      outcome: 'Reported: 13-hour AWS outage. Amazon characterized it as "misconfigured access controls — user error." FT cited four sources. Disputed.',
      pattern: 'Same boundary gap pattern. Enterprise scale: 80% developer AI adoption target, no mandatory peer review for AI-initiated production changes.',
    },
  ];

  return (
    <div>
      <div style={{
        fontFamily: T.font,
        fontSize: 11,
        color: T.textMuted,
        marginBottom: 20,
        lineHeight: 1.6,
      }}>
        The same L3 gap — trusting intent without enforcing it — appeared at startup, firm, and enterprise scale.
        Click each incident to expand.
      </div>

      {/* Spectrum line */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        marginBottom: 24,
        position: 'relative',
      }}>
        <div style={{
          position: 'absolute',
          left: '10%',
          right: '10%',
          height: 2,
          background: `linear-gradient(90deg, ${T.accent}, ${T.danger}, ${T.purple})`,
          top: '50%',
          transform: 'translateY(-50%)',
          opacity: 0.4,
        }} />
        {nodes.map((n, i) => (
          <div
            key={n.id}
            onClick={() => setActiveNode(activeNode === n.id ? null : n.id)}
            style={{
              flex: 1,
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              cursor: 'pointer',
              zIndex: 1,
            }}
          >
            <div style={{
              width: 48,
              height: 48,
              borderRadius: '50%',
              background: activeNode === n.id ? `${n.color}30` : T.surface,
              border: `2px solid ${n.color}`,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontFamily: T.font,
              fontSize: 10,
              color: n.color,
              marginBottom: 8,
              transition: 'all 0.2s',
              boxShadow: activeNode === n.id ? `0 0 16px ${n.color}60` : 'none',
            }}>
              {n.scaleIcon}
            </div>
            <div style={{
              fontFamily: T.fontDisplay,
              fontSize: 11,
              fontWeight: 700,
              color: T.text,
              textAlign: 'center',
              marginBottom: 2,
            }}>{n.label}</div>
            <div style={{
              fontFamily: T.font,
              fontSize: 9,
              color: n.color,
              textAlign: 'center',
            }}>{n.scale}</div>
          </div>
        ))}
      </div>

      {/* Active node detail */}
      {activeNode && (() => {
        const n = nodes.find(x => x.id === activeNode);
        return (
          <div style={{
            padding: '14px',
            background: `${n.color}08`,
            border: `1px solid ${n.color}30`,
            borderRadius: 8,
            marginBottom: 16,
          }}>
            <div style={{
              display: 'grid',
              gridTemplateColumns: '1fr 1fr',
              gap: 8,
              marginBottom: 12,
            }}>
              {[
                { label: 'Date', value: n.date },
                { label: 'Scale', value: n.scale },
                { label: 't₀ timing', value: n.t0 },
                { label: 'Visibility', value: n.visibility },
                { label: 'Blast radius', value: n.blastRadius },
                { label: 'Layer', value: n.layer },
              ].map((row) => (
                <div key={row.label} style={{
                  padding: '6px 10px',
                  background: T.surface,
                  borderRadius: 6,
                }}>
                  <div style={{ fontFamily: T.font, fontSize: 9, color: T.textMuted, marginBottom: 2 }}>{row.label}</div>
                  <div style={{ fontFamily: T.font, fontSize: 11, color: T.text, fontWeight: 600 }}>{row.value}</div>
                </div>
              ))}
            </div>
            <div style={{ fontFamily: T.font, fontSize: 11, color: T.textMuted, lineHeight: 1.6, marginBottom: 10 }}>
              {n.outcome}
            </div>
            <div style={{
              padding: '8px 12px',
              background: `${n.color}15`,
              borderLeft: `2px solid ${n.color}`,
              borderRadius: '0 4px 4px 0',
              fontFamily: T.font,
              fontSize: 10,
              color: T.textMuted,
              fontStyle: 'italic',
              lineHeight: 1.6,
            }}>
              Pattern: {n.pattern}
            </div>
          </div>
        );
      })()}

      {/* Common pattern */}
      <div style={{
        padding: '12px 14px',
        background: T.surface,
        border: `1px solid ${T.border}`,
        borderRadius: 8,
        marginBottom: 8,
      }}>
        <div style={{
          fontFamily: T.font,
          fontSize: 10,
          color: T.textMuted,
          fontWeight: 700,
          marginBottom: 8,
          textTransform: 'uppercase',
          letterSpacing: 1,
        }}>Common pattern across all three</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
          {[
            ['Same gap', 'L3 — architectural/constraint boundary not enforced'],
            ['Same mechanism', 'Intent expressed; capability not restricted'],
            ['Same trigger', 'AI-assisted actions with broader permissions than expected'],
            ['Different outcome', 'Blast radius scales with organizational size and system maturity'],
          ].map(([k, v]) => (
            <div key={k} style={{ display: 'flex', gap: 10, fontFamily: T.font, fontSize: 11 }}>
              <span style={{ color: T.accent, fontWeight: 700, minWidth: 120 }}>{k}</span>
              <span style={{ color: T.textMuted }}>{v}</span>
            </div>
          ))}
        </div>
      </div>

      <div style={{ fontFamily: T.font, fontSize: 10, color: T.textMuted, opacity: 0.6, lineHeight: 1.5 }}>
        AWS/Kiro: reported by the Financial Times (February 2026), disputed by Amazon ("user error — misconfigured access controls").
        Framing as system boundary gap is the author's interpretation.
      </div>
    </div>
  );
}

// ─── Main App ──────────────────────────────────────────────────────────────────

const SECTIONS = [
  {
    id: 'friction',
    num: '01',
    title: 'What LLMs Changed',
    description: 'The integration friction that once forced comprehension has been removed. Toggle to see what disappeared — and what filled the gap.',
    Component: FrictionRemoval,
  },
  {
    id: 'experiment',
    num: '02',
    title: 'Collapse of Competence',
    description: 'A controlled study of 78 novice programmers across three groups. When AI was removed, only 23% of unrestricted AI users could maintain their own code.',
    Component: ExperimentResults,
  },
  {
    id: 'behavior',
    num: '03',
    title: 'The Trust–Verify Gap',
    description: '96% of developers distrust AI output. Only 48% verify before committing. AI now accounts for 42% of committed code.',
    Component: BehaviorGap,
  },
  {
    id: 'signals',
    num: '04',
    title: 'Industry Signals',
    description: 'Velocity is up. Quality metrics are down. Four indicators trending in the wrong direction — and a comparison of AI-generated vs human code.',
    Component: IndustrySignals,
  },
  {
    id: 'cases',
    num: '05',
    title: 'Two Defaults',
    description: 'Interactive formula mapping for the SaaStr database deletion and the AlterSquare 10:1 cost ratio. Same layer, different t₀.',
    Component: CaseStudyExplorer,
  },
  {
    id: 'simulator',
    num: '06',
    title: 'The t₀ Lever',
    description: 'Slide t₀ along the sprint timeline to see how detection timing drives the cost ratio. The break-even point is earlier than you might expect.',
    Component: CostRatioSimulator,
  },
  {
    id: 'spectrum',
    num: '07',
    title: 'Scale Spectrum',
    description: 'The same L3 gap — three different blast radii. From a startup database to a 13-hour enterprise cloud outage.',
    Component: ScaleSpectrum,
  },
];

export default function Infographics() {
  const [activeIndex, setActiveIndex] = useState(0);
  const section = SECTIONS[activeIndex];
  const { Component } = section;

  return (
    <div style={{
      minHeight: '100vh',
      background: T.bg,
      padding: '24px 16px',
    }}>
      <div style={{ maxWidth: 720, margin: '0 auto' }}>

        {/* Header */}
        <div style={{ marginBottom: 28 }}>
          <div style={{
            fontFamily: T.font,
            fontSize: 10,
            color: T.textMuted,
            letterSpacing: 2,
            textTransform: 'uppercase',
            marginBottom: 8,
          }}>
            THE AI MIRROR — ARTICLE 3 INFOGRAPHICS
          </div>
          <h1 style={{
            fontFamily: T.fontDisplay,
            fontSize: 24,
            fontWeight: 800,
            color: T.text,
            lineHeight: 1.2,
            marginBottom: 6,
          }}>
            When Epistemic Debt Defaults
          </h1>
          <div style={{
            fontFamily: T.font,
            fontSize: 12,
            color: T.textMuted,
          }}>
            7 interactive visualizations — tap to explore
          </div>
        </div>

        {/* Navigation pills */}
        <div style={{
          display: 'flex',
          gap: 6,
          marginBottom: 24,
          flexWrap: 'wrap',
          position: 'sticky',
          top: 12,
          zIndex: 10,
          background: T.bg,
          paddingBottom: 8,
        }}>
          {SECTIONS.map((s, i) => (
            <button
              key={s.id}
              onClick={() => setActiveIndex(i)}
              style={{
                padding: '5px 12px',
                borderRadius: 20,
                border: `1px solid ${activeIndex === i ? T.accent : T.border}`,
                background: activeIndex === i ? `${T.accent}20` : T.surface,
                color: activeIndex === i ? T.accent : T.textMuted,
                fontFamily: T.font,
                fontSize: 11,
                fontWeight: activeIndex === i ? 700 : 400,
                cursor: 'pointer',
              }}
            >
              {s.num}
            </button>
          ))}
        </div>

        {/* Active section */}
        <div style={{
          background: T.surface,
          border: `1px solid ${T.border}`,
          borderRadius: 12,
          padding: '20px',
          marginBottom: 16,
        }}>
          <div style={{
            fontFamily: T.font,
            fontSize: 10,
            color: T.accent,
            fontWeight: 700,
            letterSpacing: 1,
            textTransform: 'uppercase',
            marginBottom: 6,
          }}>
            {section.num}
          </div>
          <h2 style={{
            fontFamily: T.fontDisplay,
            fontSize: 18,
            fontWeight: 800,
            color: T.text,
            marginBottom: 8,
            lineHeight: 1.2,
          }}>
            {section.title}
          </h2>
          <p style={{
            fontFamily: T.font,
            fontSize: 12,
            color: T.textMuted,
            marginBottom: 20,
            lineHeight: 1.6,
          }}>
            {section.description}
          </p>

          <Component />
        </div>

        {/* Pagination */}
        <div style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
        }}>
          <button
            onClick={() => setActiveIndex(i => Math.max(0, i - 1))}
            disabled={activeIndex === 0}
            style={{
              padding: '8px 20px',
              borderRadius: 8,
              border: `1px solid ${T.border}`,
              background: 'transparent',
              color: activeIndex === 0 ? T.border : T.textMuted,
              fontFamily: T.font,
              fontSize: 11,
              cursor: activeIndex === 0 ? 'default' : 'pointer',
            }}
          >
            ← Previous
          </button>
          <span style={{ fontFamily: T.font, fontSize: 11, color: T.textMuted }}>
            {activeIndex + 1} / {SECTIONS.length}
          </span>
          <button
            onClick={() => setActiveIndex(i => Math.min(SECTIONS.length - 1, i + 1))}
            disabled={activeIndex === SECTIONS.length - 1}
            style={{
              padding: '8px 20px',
              borderRadius: 8,
              border: `1px solid ${T.border}`,
              background: 'transparent',
              color: activeIndex === SECTIONS.length - 1 ? T.border : T.textMuted,
              fontFamily: T.font,
              fontSize: 11,
              cursor: activeIndex === SECTIONS.length - 1 ? 'default' : 'pointer',
            }}
          >
            Next →
          </button>
        </div>

        {/* Footer */}
        <div style={{
          marginTop: 32,
          textAlign: 'center',
          fontFamily: T.font,
          fontSize: 10,
          color: T.textMuted,
          opacity: 0.5,
        }}>
          Part of the Epistemic Debt series — The AI Mirror by Antonino Rau
        </div>

      </div>
    </div>
  );
}

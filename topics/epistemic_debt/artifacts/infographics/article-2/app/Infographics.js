"use client";
import { useState, useEffect, useRef, useCallback } from "react";

// ─── Shared Design Tokens ───
const T = {
  bg: "#0c0e13",
  surface: "#14171e",
  surfaceHover: "#1a1e28",
  border: "#252a36",
  text: "#e2e4e9",
  textMuted: "#8a8f9e",
  accent: "#f97316",    // orange
  accentAlt: "#3b82f6", // blue
  danger: "#ef4444",
  success: "#22c55e",
  purple: "#a855f7",
  cream: "#fef3c7",
  font: "'JetBrains Mono', 'SF Mono', 'Fira Code', monospace",
  fontDisplay: "'Space Grotesk', 'Inter', sans-serif",
};

// ─── Utility: Animated Number ───
function useAnimatedValue(target, duration = 1200) {
  const [val, setVal] = useState(0);
  const ref = useRef(null);
  useEffect(() => {
    const start = performance.now();
    const from = val;
    const animate = (now) => {
      const t = Math.min((now - start) / duration, 1);
      const ease = 1 - Math.pow(1 - t, 3);
      setVal(from + (target - from) * ease);
      if (t < 1) ref.current = requestAnimationFrame(animate);
    };
    ref.current = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(ref.current);
  }, [target]);
  return val;
}

// ═══════════════════════════════════════════
// 1. THE WIDENING GAP
// ═══════════════════════════════════════════
function WideningGap() {
  const [aiMoment, setAiMoment] = useState(0.35);
  const canvasRef = useRef(null);
  const [hoverT, setHoverT] = useState(null);

  const cs = useCallback((t) => {
    if (t < aiMoment) return 0.15 + t * 0.6;
    return 0.15 + aiMoment * 0.6 + (t - aiMoment) * 2.8;
  }, [aiMoment]);

  const gc = useCallback((t) => {
    return 0.12 + t * 0.55;
  }, []);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const W = canvas.width = canvas.offsetWidth * 2;
    const H = canvas.height = canvas.offsetHeight * 2;
    ctx.scale(2, 2);
    const w = W / 2, h = H / 2;
    const pad = { l: 55, r: 20, t: 30, b: 45 };
    const pw = w - pad.l - pad.r;
    const ph = h - pad.t - pad.b;

    ctx.clearRect(0, 0, w, h);

    // Grid
    ctx.strokeStyle = T.border;
    ctx.lineWidth = 0.5;
    for (let i = 0; i <= 5; i++) {
      const y = pad.t + (ph / 5) * i;
      ctx.beginPath(); ctx.moveTo(pad.l, y); ctx.lineTo(w - pad.r, y); ctx.stroke();
    }

    // Debt fill
    ctx.beginPath();
    for (let i = 0; i <= 200; i++) {
      const t = i / 200;
      const x = pad.l + t * pw;
      const y = pad.t + ph - cs(t) * ph * 0.65;
      i === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
    }
    for (let i = 200; i >= 0; i--) {
      const t = i / 200;
      const x = pad.l + t * pw;
      const y = pad.t + ph - gc(t) * ph * 0.65;
      ctx.lineTo(x, y);
    }
    ctx.closePath();
    const grad = ctx.createLinearGradient(0, pad.t, 0, pad.t + ph);
    grad.addColorStop(0, "rgba(249,115,22,0.35)");
    grad.addColorStop(1, "rgba(249,115,22,0.05)");
    ctx.fillStyle = grad;
    ctx.fill();

    // Cs(t) line
    ctx.beginPath();
    ctx.strokeStyle = T.accent;
    ctx.lineWidth = 2.5;
    for (let i = 0; i <= 200; i++) {
      const t = i / 200;
      const x = pad.l + t * pw;
      const y = pad.t + ph - cs(t) * ph * 0.65;
      i === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Gc(t) line
    ctx.beginPath();
    ctx.strokeStyle = T.accentAlt;
    ctx.lineWidth = 2.5;
    for (let i = 0; i <= 200; i++) {
      const t = i / 200;
      const x = pad.l + t * pw;
      const y = pad.t + ph - gc(t) * ph * 0.65;
      i === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
    }
    ctx.stroke();

    // AI moment marker
    const aiX = pad.l + aiMoment * pw;
    ctx.setLineDash([4, 4]);
    ctx.strokeStyle = T.textMuted;
    ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(aiX, pad.t); ctx.lineTo(aiX, pad.t + ph); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = T.textMuted;
    ctx.font = `11px ${T.font}`;
    ctx.textAlign = "center";
    ctx.fillText("AI adoption", aiX, pad.t + ph + 18);

    // Hover crosshair
    if (hoverT !== null) {
      const hx = pad.l + hoverT * pw;
      const csY = pad.t + ph - cs(hoverT) * ph * 0.65;
      const gcY = pad.t + ph - gc(hoverT) * ph * 0.65;
      ctx.setLineDash([2, 3]);
      ctx.strokeStyle = "rgba(255,255,255,0.2)";
      ctx.beginPath(); ctx.moveTo(hx, pad.t); ctx.lineTo(hx, pad.t + ph); ctx.stroke();
      ctx.setLineDash([]);

      // Gap line
      ctx.strokeStyle = T.accent;
      ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(hx, csY); ctx.lineTo(hx, gcY); ctx.stroke();

      // Dots
      [csY, gcY].forEach((y, i) => {
        ctx.beginPath(); ctx.arc(hx, y, 4, 0, Math.PI * 2);
        ctx.fillStyle = i === 0 ? T.accent : T.accentAlt; ctx.fill();
      });

      // Gap label
      const gap = (cs(hoverT) - gc(hoverT)).toFixed(2);
      ctx.fillStyle = T.text;
      ctx.font = `bold 11px ${T.font}`;
      ctx.textAlign = "left";
      ctx.fillText(`Ed gap: ${gap}`, hx + 8, (csY + gcY) / 2);
    }

    // Axis labels
    ctx.fillStyle = T.textMuted;
    ctx.font = `10px ${T.font}`;
    ctx.textAlign = "center";
    ctx.fillText("Time →", pad.l + pw / 2, h - 5);
    ctx.save();
    ctx.translate(14, pad.t + ph / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.fillText("Complexity / Grasp", 0, 0);
    ctx.restore();

  }, [aiMoment, hoverT, cs, gc]);

  const handleMouseMove = (e) => {
    const rect = e.currentTarget.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width;
    const padRatio = 55 / rect.width;
    const t = Math.max(0, Math.min(1, (x - padRatio) / (1 - padRatio - 20 / rect.width)));
    setHoverT(t);
  };

  return (
    <div>
      <div style={{ display: "flex", gap: 24, marginBottom: 16, flexWrap: "wrap" }}>
        <Legend color={T.accent} label="Cs(t) — System Complexity" />
        <Legend color={T.accentAlt} label="Gc(t) — Cognitive Grasp" />
        <Legend color="rgba(249,115,22,0.3)" label="Epistemic Debt (∫)" filled />
      </div>
      <div style={{ position: "relative" }}>
        <canvas
          ref={canvasRef}
          style={{ width: "100%", height: 320, borderRadius: 8, background: T.surface, cursor: "crosshair" }}
          onMouseMove={handleMouseMove}
          onMouseLeave={() => setHoverT(null)}
        />
      </div>
      <div style={{ marginTop: 12 }}>
        <label style={{ color: T.textMuted, fontSize: 12, fontFamily: T.font }}>
          AI adoption point: {Math.round(aiMoment * 100)}%
        </label>
        <input
          type="range" min={10} max={70} value={aiMoment * 100}
          onChange={(e) => setAiMoment(e.target.value / 100)}
          style={{ width: "100%", accentColor: T.accent }}
        />
      </div>
      <Formula text="Ed = ∫₀ᵀ (Cs(t) − Gc(t)) dt" />
    </div>
  );
}

// ═══════════════════════════════════════════
// 2. ABSTRACTION LAYER CASCADE
// ═══════════════════════════════════════════
function AbstractionCascade() {
  const [activeLayer, setActiveLayer] = useState(null);
  const layers = [
    { id: "L4", label: "Requirements", multiplier: "30–70×", color: "#ef4444", gap: 85, desc: "Wrong assumption → everything built on it must be revisited" },
    { id: "L3", label: "Architecture", multiplier: "10×", color: "#f97316", gap: 62, desc: "Structural drift embeds before anyone notices" },
    { id: "L2", label: "Design", multiplier: "3–6×", color: "#eab308", gap: 40, desc: "Design assumptions harden into implementation" },
    { id: "L1", label: "Implementation", multiplier: "1×", color: "#22c55e", gap: 20, desc: "Local fix, no downstream rework" },
  ];

  const affectedLayers = activeLayer !== null
    ? layers.slice(activeLayer)
    : [];

  return (
    <div>
      <div style={{ display: "flex", gap: 16, flexDirection: "column" }}>
        {layers.map((layer, i) => {
          const isActive = activeLayer === i;
          const isAffected = affectedLayers.includes(layer);
          return (
            <div
              key={layer.id}
              onClick={() => setActiveLayer(isActive ? null : i)}
              style={{
                display: "flex", alignItems: "center", gap: 16,
                padding: "14px 18px", borderRadius: 10,
                background: isAffected ? `${layer.color}15` : T.surface,
                border: `1.5px solid ${isAffected ? layer.color : T.border}`,
                cursor: "pointer",
                transition: "all 0.3s ease",
                transform: isActive ? "scale(1.02)" : "scale(1)",
              }}
            >
              <div style={{
                width: 44, height: 44, borderRadius: 8,
                background: `${layer.color}25`, display: "flex",
                alignItems: "center", justifyContent: "center",
                fontFamily: T.font, fontWeight: 700, fontSize: 14,
                color: layer.color, flexShrink: 0,
              }}>
                {layer.id}
              </div>
              <div style={{ flex: 1, minWidth: 0 }}>
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 6 }}>
                  <span style={{ color: T.text, fontWeight: 600, fontSize: 14 }}>{layer.label}</span>
                  <span style={{
                    fontFamily: T.font, fontSize: 13, fontWeight: 700,
                    color: layer.color,
                    background: `${layer.color}18`, padding: "2px 10px", borderRadius: 20,
                  }}>
                    c<sub>{layer.id[1]}</sub> ≈ {layer.multiplier}
                  </span>
                </div>
                <div style={{
                  height: 6, borderRadius: 3, background: `${layer.color}15`,
                  overflow: "hidden",
                }}>
                  <div style={{
                    height: "100%", borderRadius: 3,
                    width: `${isAffected ? layer.gap : 0}%`,
                    background: `linear-gradient(90deg, ${layer.color}, ${layer.color}88)`,
                    transition: "width 0.5s ease",
                  }} />
                </div>
                {isAffected && (
                  <div style={{ color: T.textMuted, fontSize: 12, marginTop: 6, fontFamily: T.font }}>
                    {isActive ? "↳ Gap origin" : "↳ Cascade rework"}: {layer.desc}
                  </div>
                )}
              </div>
              {isAffected && !isActive && (
                <div style={{ color: layer.color, fontSize: 18, flexShrink: 0 }}>↓</div>
              )}
            </div>
          );
        })}
      </div>
      <Formula text="C_k = Σⱼ₌₁ᵏ τⱼ — cost cascades downward from gap origin" />
      <p style={{ color: T.textMuted, fontSize: 12, fontFamily: T.font, marginTop: 8, textAlign: "center" }}>
        Click a layer to see the cascade effect
      </p>
    </div>
  );
}

// ═══════════════════════════════════════════
// 3. BREAK-EVEN SCALE
// ═══════════════════════════════════════════
function BreakEvenScale() {
  const [debtLayer, setDebtLayer] = useState(1);
  const layerData = [
    { label: "L1 only", cost: 12, color: T.success },
    { label: "L1+L2", cost: 35, color: "#eab308" },
    { label: "L1–L3", cost: 70, color: T.accent },
    { label: "L1–L4", cost: 140, color: T.danger },
  ];
  const saved = 50; // δ
  const current = layerData[debtLayer];
  const net = saved - current.cost;
  const isLoss = net < 0;
  const tilt = Math.max(-18, Math.min(18, (net / saved) * 18));
  const animTilt = useAnimatedValue(tilt, 600);

  return (
    <div>
      <div style={{ textAlign: "center", marginBottom: 20 }}>
        <div style={{
          display: "inline-block", padding: "6px 16px", borderRadius: 20,
          background: isLoss ? `${T.danger}20` : `${T.success}20`,
          color: isLoss ? T.danger : T.success,
          fontFamily: T.font, fontWeight: 700, fontSize: 15,
          transition: "all 0.3s",
        }}>
          Net = δ − Σc_k·τ_k = {net > 0 ? "+" : ""}{net}h {isLoss ? "← NET LOSS" : "← NET GAIN"}
        </div>
      </div>

      {/* Balance beam */}
      <svg viewBox="0 0 500 200" style={{ width: "100%", maxHeight: 200 }}>
        {/* Fulcrum */}
        <polygon points="250,195 238,165 262,165" fill={T.border} />
        {/* Beam */}
        <g style={{ transform: `rotate(${animTilt}deg)`, transformOrigin: "250px 160px", transition: "transform 0.6s ease" }}>
          <line x1="70" y1="160" x2="430" y2="160" stroke={T.textMuted} strokeWidth="3" strokeLinecap="round" />
          {/* Left pan — δ (saved) */}
          <line x1="120" y1="160" x2="100" y2="130" stroke={T.textMuted} strokeWidth="1.5" />
          <line x1="120" y1="160" x2="140" y2="130" stroke={T.textMuted} strokeWidth="1.5" />
          <rect x="80" y="105" width="80" height="28" rx="6" fill={`${T.accentAlt}30`} stroke={T.accentAlt} strokeWidth="1.5" />
          <text x="120" y="123" textAnchor="middle" fill={T.accentAlt} fontSize="12" fontFamily={T.font} fontWeight="700">δ = {saved}h</text>
          <text x="120" y="97" textAnchor="middle" fill={T.textMuted} fontSize="10" fontFamily={T.font}>Time saved</text>
          {/* Right pan — cost */}
          <line x1="380" y1="160" x2="360" y2="130" stroke={T.textMuted} strokeWidth="1.5" />
          <line x1="380" y1="160" x2="400" y2="130" stroke={T.textMuted} strokeWidth="1.5" />
          <rect x="340" y="105" width="80" height="28" rx="6" fill={`${current.color}30`} stroke={current.color} strokeWidth="1.5" />
          <text x="380" y="123" textAnchor="middle" fill={current.color} fontSize="12" fontFamily={T.font} fontWeight="700">{current.cost}h</text>
          <text x="380" y="97" textAnchor="middle" fill={T.textMuted} fontSize="10" fontFamily={T.font}>{current.label} recovery</text>
        </g>
      </svg>

      <div style={{ display: "flex", gap: 8, justifyContent: "center", marginTop: 16, flexWrap: "wrap" }}>
        {layerData.map((d, i) => (
          <button
            key={i}
            onClick={() => setDebtLayer(i)}
            style={{
              padding: "7px 16px", borderRadius: 8, border: `1.5px solid ${i === debtLayer ? d.color : T.border}`,
              background: i === debtLayer ? `${d.color}20` : "transparent",
              color: i === debtLayer ? d.color : T.textMuted,
              cursor: "pointer", fontFamily: T.font, fontSize: 12, fontWeight: 600,
            }}
          >
            {d.label}
          </button>
        ))}
      </div>
      <Formula text="Net benefit = δ − Σ_k c_k · τ_k" />
    </div>
  );
}

// ═══════════════════════════════════════════
// 4. t₀ TIMELINE
// ═══════════════════════════════════════════
function T0Timeline() {
  const [selectedPath, setSelectedPath] = useState("early");
  const stages = [
    { label: "Design", x: 5 },
    { label: "Review", x: 22 },
    { label: "Integration", x: 42 },
    { label: "Staging", x: 62 },
    { label: "Production", x: 85 },
  ];
  const mechanisms = [
    { label: "Bounded Contexts", stage: 0, desc: "DDD constrains scope of debt" },
    { label: "Fitness Functions", stage: 1, desc: "Architectural drift caught" },
    { label: "Contract Tests", stage: 2, desc: "Design assumptions verified" },
    { label: "Cognitive Ratchet", stage: 1, desc: "Explain it back before commit" },
  ];

  const earlyT0 = 1;
  const lateT0 = 4;
  const isEarly = selectedPath === "early";
  const activeT0 = isEarly ? earlyT0 : lateT0;

  return (
    <div>
      <div style={{ display: "flex", gap: 8, justifyContent: "center", marginBottom: 20 }}>
        {["early", "late"].map(p => (
          <button key={p} onClick={() => setSelectedPath(p)} style={{
            padding: "7px 18px", borderRadius: 8,
            border: `1.5px solid ${selectedPath === p ? (p === "early" ? T.success : T.danger) : T.border}`,
            background: selectedPath === p ? (p === "early" ? `${T.success}18` : `${T.danger}18`) : "transparent",
            color: selectedPath === p ? (p === "early" ? T.success : T.danger) : T.textMuted,
            cursor: "pointer", fontFamily: T.font, fontSize: 12, fontWeight: 600, textTransform: "capitalize",
          }}>
            {p === "early" ? "Early detection (t₀ at review)" : "Late detection (t₀ at production)"}
          </button>
        ))}
      </div>

      <div style={{ position: "relative", padding: "40px 0 60px" }}>
        {/* Timeline line */}
        <div style={{
          position: "absolute", top: 52, left: "5%", right: "5%", height: 3,
          background: `linear-gradient(90deg, ${T.success}, ${T.accent}, ${T.danger})`,
          borderRadius: 2,
        }} />

        {/* Stage dots */}
        {stages.map((s, i) => {
          const isT0 = i === activeT0;
          const color = i <= 1 ? T.success : i <= 2 ? "#eab308" : i <= 3 ? T.accent : T.danger;
          return (
            <div key={i} style={{
              position: "absolute", left: `${s.x + 5}%`, top: 40,
              transform: "translateX(-50%)", textAlign: "center",
            }}>
              <div style={{
                width: isT0 ? 22 : 12, height: isT0 ? 22 : 12,
                borderRadius: "50%", background: isT0 ? color : T.border,
                border: isT0 ? `3px solid ${color}` : "none",
                margin: "0 auto", position: "relative", top: isT0 ? -5 : 0,
                boxShadow: isT0 ? `0 0 16px ${color}60` : "none",
                transition: "all 0.4s",
              }} />
              <div style={{
                marginTop: isT0 ? 8 : 12, fontFamily: T.font, fontSize: 10,
                color: isT0 ? T.text : T.textMuted, fontWeight: isT0 ? 700 : 400,
              }}>
                {s.label}
              </div>
              {isT0 && (
                <div style={{
                  marginTop: 4, fontFamily: T.font, fontSize: 11,
                  color, fontWeight: 700,
                }}>
                  t₀ HERE
                </div>
              )}
            </div>
          );
        })}

        {/* Mechanisms (early path) */}
        {isEarly && mechanisms.map((m, i) => (
          <div key={i} style={{
            position: "absolute",
            left: `${stages[m.stage].x + 5}%`,
            top: -6 - (i % 2) * 22,
            transform: "translateX(-50%)",
            background: `${T.success}15`, border: `1px solid ${T.success}40`,
            padding: "3px 10px", borderRadius: 12,
            fontFamily: T.font, fontSize: 9, color: T.success,
            whiteSpace: "nowrap",
          }}>
            {m.label}
          </div>
        ))}
      </div>

      {/* Cost comparison */}
      <div style={{
        display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12, marginTop: 8,
      }}>
        <Stat label="Gap size at t₀" value={isEarly ? "Small" : "Maximum"} color={isEarly ? T.success : T.danger} />
        <Stat label="Cascade multiplier" value={isEarly ? "c₁–c₂ (1–6×)" : "c₄ (30–70×)"} color={isEarly ? T.success : T.danger} />
        <Stat label="Recovery cost" value={isEarly ? "Minutes–hours" : "Days–weeks"} color={isEarly ? T.success : T.danger} />
        <Stat label="Risk profile" value={isEarly ? "Contained" : "Systemic"} color={isEarly ? T.success : T.danger} />
      </div>
      <Formula text="Catch it early → small (Cs_k(t₀) − Gc_k(t₀)) → cheap τ_k" />
    </div>
  );
}

// ═══════════════════════════════════════════
// 5. TECH DEBT vs EPISTEMIC DEBT
// ═══════════════════════════════════════════
function DebtComparison() {
  const [expanded, setExpanded] = useState(null);
  const rows = [
    {
      dim: "What accumulates",
      td: "Code quality issues, shortcuts, workarounds",
      ed: "Understanding gaps, comprehension deficits",
      icon: "📦",
    },
    {
      dim: "What pays it down",
      td: "Refactoring, code cleanup",
      ed: "Learning, documentation, knowledge transfer",
      icon: "💰",
    },
    {
      dim: "Visibility",
      td: "Code metrics, static analysis",
      ed: "Bus factor, onboarding time, incident diagnosis",
      icon: "👁",
    },
    {
      dim: "Consequences of default",
      td: "Maintenance burden, slower changes",
      ed: "Catastrophic blind spots, security exposure",
      icon: "💥",
    },
    {
      dim: "Speed of accumulation",
      td: "Gradual (linear with velocity)",
      ed: "Exponential with AI (entire modules in hours)",
      icon: "⚡",
      hasViz: true,
    },
    {
      dim: "Who it affects",
      td: "Individual developers or teams (local pain)",
      ed: "Entire teams or organizations (systemic risk)",
      icon: "👥",
    },
  ];

  return (
    <div>
      {rows.map((row, i) => (
        <div
          key={i}
          onClick={() => setExpanded(expanded === i ? null : i)}
          style={{
            marginBottom: 8, borderRadius: 10,
            border: `1px solid ${expanded === i ? T.accent : T.border}`,
            background: expanded === i ? `${T.accent}08` : T.surface,
            cursor: "pointer", overflow: "hidden",
            transition: "all 0.3s",
          }}
        >
          <div style={{
            display: "flex", alignItems: "center", padding: "12px 16px", gap: 12,
          }}>
            <span style={{ fontSize: 18, flexShrink: 0 }}>{row.icon}</span>
            <span style={{ flex: 1, fontWeight: 600, fontSize: 13, color: T.text }}>{row.dim}</span>
            <span style={{
              color: T.textMuted, fontSize: 16,
              transform: expanded === i ? "rotate(180deg)" : "rotate(0)",
              transition: "transform 0.3s",
            }}>▾</span>
          </div>
          {expanded === i && (
            <div style={{ padding: "0 16px 16px", display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
              <div style={{
                padding: 12, borderRadius: 8,
                background: `${T.accentAlt}10`, border: `1px solid ${T.accentAlt}30`,
              }}>
                <div style={{ fontSize: 10, fontFamily: T.font, color: T.accentAlt, marginBottom: 6, fontWeight: 700 }}>TECHNICAL DEBT</div>
                <div style={{ fontSize: 12, color: T.text, lineHeight: 1.5 }}>{row.td}</div>
              </div>
              <div style={{
                padding: 12, borderRadius: 8,
                background: `${T.accent}10`, border: `1px solid ${T.accent}30`,
              }}>
                <div style={{ fontSize: 10, fontFamily: T.font, color: T.accent, marginBottom: 6, fontWeight: 700 }}>EPISTEMIC DEBT</div>
                <div style={{ fontSize: 12, color: T.text, lineHeight: 1.5 }}>{row.ed}</div>
              </div>
              {row.hasViz && (
                <div style={{ gridColumn: "1/3", display: "flex", gap: 16, padding: "8px 0" }}>
                  <MiniSparkline label="Technical" type="linear" color={T.accentAlt} />
                  <MiniSparkline label="Epistemic" type="exponential" color={T.accent} />
                </div>
              )}
            </div>
          )}
        </div>
      ))}
      <p style={{ textAlign: "center", color: T.textMuted, fontSize: 11, fontFamily: T.font, marginTop: 8 }}>
        Tap any row to expand
      </p>
    </div>
  );
}

function MiniSparkline({ label, type, color }) {
  const points = Array.from({ length: 30 }, (_, i) => {
    const t = i / 29;
    const y = type === "linear" ? t * 0.7 + 0.1 : Math.pow(t, 2.5) * 0.9 + 0.1;
    return `${i * (100 / 29)},${(1 - y) * 40}`;
  }).join(" ");

  return (
    <div style={{ flex: 1, textAlign: "center" }}>
      <svg viewBox="0 0 100 45" style={{ width: "100%", height: 45 }}>
        <polyline points={points} fill="none" stroke={color} strokeWidth="2" />
      </svg>
      <div style={{ fontSize: 10, color, fontFamily: T.font, fontWeight: 600 }}>{label} ({type})</div>
    </div>
  );
}

// ═══════════════════════════════════════════
// 6. EPISTEMIC CREDIT BUFFER
// ═══════════════════════════════════════════
function CreditBuffer() {
  const [gcMultiplier, setGcMultiplier] = useState(1.3);
  const cs = 55;
  const gc = Math.round(cs * gcMultiplier);
  const maxVal = 120;
  const isCredit = gc > cs;
  const diff = gc - cs;
  const pct = Math.abs(diff) / maxVal * 100;
  const animPct = useAnimatedValue(pct, 500);

  return (
    <div>
      <div style={{ display: "flex", gap: 24, alignItems: "center", justifyContent: "center", flexWrap: "wrap" }}>
        {/* Tank */}
        <div style={{ position: "relative", width: 120, height: 220 }}>
          {/* Tank body */}
          <div style={{
            position: "absolute", inset: 0,
            borderRadius: 16, border: `2px solid ${T.border}`,
            background: T.surface, overflow: "hidden",
          }}>
            {/* Gc fill */}
            <div style={{
              position: "absolute", bottom: 0, left: 0, right: 0,
              height: `${(gc / maxVal) * 100}%`,
              background: `linear-gradient(to top, ${T.accentAlt}40, ${T.accentAlt}15)`,
              transition: "height 0.5s ease",
            }} />
            {/* Cs fill line */}
            <div style={{
              position: "absolute", bottom: `${(cs / maxVal) * 100}%`,
              left: 0, right: 0, height: 2,
              background: T.accent,
              boxShadow: `0 0 8px ${T.accent}60`,
            }} />
            {/* Delta zone */}
            {isCredit ? (
              <div style={{
                position: "absolute",
                bottom: `${(cs / maxVal) * 100}%`,
                left: 0, right: 0,
                height: `${animPct}%`,
                background: `${T.success}20`,
                borderTop: `2px dashed ${T.success}`,
              }} />
            ) : (
              <div style={{
                position: "absolute",
                bottom: `${(gc / maxVal) * 100}%`,
                left: 0, right: 0,
                height: `${animPct}%`,
                background: `${T.danger}20`,
                borderBottom: `2px dashed ${T.danger}`,
              }} />
            )}
          </div>
          {/* Labels */}
          <div style={{
            position: "absolute", right: -50,
            bottom: `${(gc / maxVal) * 100}%`,
            transform: "translateY(50%)",
            fontFamily: T.font, fontSize: 10, color: T.accentAlt,
            transition: "bottom 0.5s ease",
          }}>Gc</div>
          <div style={{
            position: "absolute", right: -50,
            bottom: `${(cs / maxVal) * 100}%`,
            transform: "translateY(50%)",
            fontFamily: T.font, fontSize: 10, color: T.accent,
          }}>Cs</div>
        </div>

        {/* Status */}
        <div style={{ maxWidth: 240 }}>
          <div style={{
            fontSize: 48, fontWeight: 800, fontFamily: T.font,
            color: isCredit ? T.success : T.danger,
            lineHeight: 1,
          }}>
            {isCredit ? "+" : ""}{diff}
          </div>
          <div style={{
            fontSize: 14, fontWeight: 700, fontFamily: T.font,
            color: isCredit ? T.success : T.danger, marginTop: 4,
          }}>
            {isCredit ? "EPISTEMIC CREDIT" : "EPISTEMIC DEBT"}
          </div>
          <p style={{ fontSize: 12, color: T.textMuted, marginTop: 8, lineHeight: 1.6 }}>
            {isCredit
              ? "This team can safely absorb AI-generated complexity. The surplus understanding acts as a buffer."
              : "This team cannot absorb new complexity. Every AI-generated module deepens the hole."}
          </p>
        </div>
      </div>

      <div style={{ marginTop: 20 }}>
        <label style={{ color: T.textMuted, fontSize: 12, fontFamily: T.font }}>
          Team understanding (Gc/Cs ratio): {gcMultiplier.toFixed(2)}
        </label>
        <input
          type="range" min={40} max={200} value={gcMultiplier * 100}
          onChange={(e) => setGcMultiplier(e.target.value / 100)}
          style={{ width: "100%", accentColor: isCredit ? T.success : T.danger }}
        />
      </div>
      <Formula text="Ce = ∫₀ᵀ (Gc(t) − Cs(t)) dt   (when Gc > Cs)" />
    </div>
  );
}

// ═══════════════════════════════════════════
// 7. GREEN CI TRAP
// ═══════════════════════════════════════════
function GreenCITrap() {
  const [showBreak, setShowBreak] = useState(false);
  const nodes = [
    { label: "AI generates code", angle: 0, icon: "🤖" },
    { label: "AI generates tests", angle: 72, icon: "🧪" },
    { label: "CI pipeline green", angle: 144, icon: "✅" },
    { label: "Team assumes\ncorrectness", angle: 216, icon: "😌" },
    { label: "Ship to\nproduction", angle: 288, icon: "🚀" },
  ];

  const breakPoints = [
    { label: "Cognitive Ratchet", angle: 36, desc: "Explain it back before commit" },
    { label: "Human-authored tests", angle: 108, desc: "Break circular confirmation" },
    { label: "Bounded contexts", angle: 252, desc: "Constrain blast radius" },
  ];

  const r = 110;
  const cx = 160, cy = 140;

  return (
    <div>
      <div style={{ display: "flex", gap: 8, justifyContent: "center", marginBottom: 16 }}>
        <button onClick={() => setShowBreak(false)} style={{
          padding: "6px 16px", borderRadius: 8, cursor: "pointer",
          border: `1.5px solid ${!showBreak ? T.danger : T.border}`,
          background: !showBreak ? `${T.danger}18` : "transparent",
          color: !showBreak ? T.danger : T.textMuted,
          fontFamily: T.font, fontSize: 12, fontWeight: 600,
        }}>Circular trap</button>
        <button onClick={() => setShowBreak(true)} style={{
          padding: "6px 16px", borderRadius: 8, cursor: "pointer",
          border: `1.5px solid ${showBreak ? T.success : T.border}`,
          background: showBreak ? `${T.success}18` : "transparent",
          color: showBreak ? T.success : T.textMuted,
          fontFamily: T.font, fontSize: 12, fontWeight: 600,
        }}>Break the loop</button>
      </div>

      <svg viewBox="0 0 320 280" style={{ width: "100%", maxHeight: 300 }}>
        {/* Circular arrows */}
        {nodes.map((_, i) => {
          const a1 = (nodes[i].angle - 90) * Math.PI / 180;
          const a2 = (nodes[(i + 1) % nodes.length].angle - 90) * Math.PI / 180;
          const midA = (a1 + a2) / 2 + (a2 < a1 ? Math.PI : 0);
          const mx = cx + Math.cos(midA) * (r - 20);
          const my = cy + Math.sin(midA) * (r - 20);
          return (
            <line key={`arr-${i}`}
              x1={cx + Math.cos(a1) * (r - 30)} y1={cy + Math.sin(a1) * (r - 30)}
              x2={cx + Math.cos(a2) * (r - 30)} y2={cy + Math.sin(a2) * (r - 30)}
              stroke={showBreak ? `${T.textMuted}40` : `${T.danger}50`}
              strokeWidth="1.5" markerEnd=""
              strokeDasharray={showBreak ? "4 4" : "none"}
            />
          );
        })}

        {/* Nodes */}
        {nodes.map((n, i) => {
          const a = (n.angle - 90) * Math.PI / 180;
          const x = cx + Math.cos(a) * r;
          const y = cy + Math.sin(a) * r;
          return (
            <g key={i}>
              <circle cx={x} cy={y} r={24}
                fill={showBreak ? `${T.textMuted}15` : `${T.danger}15`}
                stroke={showBreak ? T.textMuted : `${T.danger}60`}
                strokeWidth="1.5"
              />
              <text x={x} y={y - 2} textAnchor="middle" fontSize="16">{n.icon}</text>
              {n.label.split("\n").map((line, li) => (
                <text key={li} x={x} y={y + 16 + li * 12}
                  textAnchor="middle" fontSize="8" fill={T.textMuted} fontFamily={T.font}>
                  {line}
                </text>
              ))}
            </g>
          );
        })}

        {/* Center label */}
        <text x={cx} y={cy - 8} textAnchor="middle" fontSize="11" fontWeight="700"
          fill={showBreak ? T.success : T.danger} fontFamily={T.font}>
          {showBreak ? "LOOP BROKEN" : "CIRCULAR"}
        </text>
        <text x={cx} y={cy + 8} textAnchor="middle" fontSize="11" fontWeight="700"
          fill={showBreak ? T.success : T.danger} fontFamily={T.font}>
          {showBreak ? "✓" : "CONFIRMATION"}
        </text>

        {/* Break points */}
        {showBreak && breakPoints.map((bp, i) => {
          const a = (bp.angle - 90) * Math.PI / 180;
          const x = cx + Math.cos(a) * (r - 15);
          const y = cy + Math.sin(a) * (r - 15);
          return (
            <g key={`bp-${i}`}>
              <circle cx={x} cy={y} r={14} fill={`${T.success}25`} stroke={T.success} strokeWidth="1.5" />
              <text x={x} y={y + 4} textAnchor="middle" fontSize="12" fill={T.success}>✂</text>
              <text x={x} y={y + 26} textAnchor="middle" fontSize="7" fill={T.success} fontFamily={T.font} fontWeight="600">
                {bp.label}
              </text>
            </g>
          );
        })}
      </svg>

      <div style={{
        textAlign: "center", padding: "10px 16px", borderRadius: 8,
        background: showBreak ? `${T.success}10` : `${T.danger}10`,
        border: `1px solid ${showBreak ? T.success : T.danger}30`,
        fontFamily: T.font, fontSize: 12, color: showBreak ? T.success : T.danger,
      }}>
        {showBreak
          ? "Deterministic mechanisms interrupt the loop — humans verify understanding, not just output"
          : "\"Verification Opacity\" — AI tests confirm AI's interpretation, not the business need"}
      </div>
    </div>
  );
}

// ─── Shared Components ───
function Legend({ color, label, filled }) {
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 6 }}>
      <div style={{
        width: 14, height: 14, borderRadius: 3,
        background: filled ? color : "transparent",
        border: filled ? "none" : `2.5px solid ${color}`,
      }} />
      <span style={{ fontSize: 11, color: T.textMuted, fontFamily: T.font }}>{label}</span>
    </div>
  );
}

function Formula({ text }) {
  return (
    <div style={{
      textAlign: "center", marginTop: 16, padding: "8px 16px",
      background: `${T.accent}08`, borderRadius: 8,
      border: `1px dashed ${T.accent}30`,
      fontFamily: T.font, fontSize: 13, color: T.accent, fontWeight: 600,
    }}>
      {text}
    </div>
  );
}

function Stat({ label, value, color }) {
  return (
    <div style={{
      padding: "10px 14px", borderRadius: 8,
      background: T.surface, border: `1px solid ${T.border}`,
    }}>
      <div style={{ fontSize: 10, color: T.textMuted, fontFamily: T.font, marginBottom: 4 }}>{label}</div>
      <div style={{ fontSize: 13, color, fontFamily: T.font, fontWeight: 700 }}>{value}</div>
    </div>
  );
}

// ═══════════════════════════════════════════
// MAIN APP
// ═══════════════════════════════════════════
const sections = [
  { id: "gap", title: "The Widening Gap", num: "01", Component: WideningGap, desc: "How epistemic debt accumulates as Cs(t) outpaces Gc(t)" },
  { id: "cascade", title: "Abstraction Layer Cascade", num: "02", Component: AbstractionCascade, desc: "Why the layer matters more than the volume" },
  { id: "balance", title: "Break-Even Scale", num: "03", Component: BreakEvenScale, desc: "When AI speed becomes a net loss" },
  { id: "timeline", title: "The t₀ Timeline", num: "04", Component: T0Timeline, desc: "Early vs. late detection and its cost" },
  { id: "compare", title: "Tech Debt vs. Epistemic Debt", num: "05", Component: DebtComparison, desc: "Same metaphor, different beast" },
  { id: "credit", title: "Epistemic Credit Buffer", num: "06", Component: CreditBuffer, desc: "When understanding exceeds complexity" },
  { id: "trap", title: "The Green CI Trap", num: "07", Component: GreenCITrap, desc: "Circular confirmation and how to break it" },
];

export default function Infographics() {
  const [active, setActive] = useState(0);
  const ActiveComponent = sections[active].Component;

  return (
    <div style={{
      minHeight: "100vh", background: T.bg, color: T.text,
      fontFamily: "'Inter', -apple-system, sans-serif",
    }}>
      {/* Header */}
      <div style={{
        padding: "28px 24px 20px",
        borderBottom: `1px solid ${T.border}`,
        background: `linear-gradient(180deg, ${T.surface}, ${T.bg})`,
      }}>
        <div style={{ maxWidth: 720, margin: "0 auto" }}>
          <div style={{
            fontFamily: T.font, fontSize: 10, color: T.accent,
            letterSpacing: 3, textTransform: "uppercase", marginBottom: 8,
          }}>
            THE EPISTEMIC SHIFT — ARTICLE 2 INFOGRAPHICS
          </div>
          <h1 style={{
            fontFamily: "'Space Grotesk', sans-serif", fontSize: 22,
            fontWeight: 800, lineHeight: 1.2, color: T.text,
          }}>
            Epistemic Debt: The Math, The Cost
          </h1>
          <p style={{ fontSize: 13, color: T.textMuted, marginTop: 6 }}>
            7 interactive visualizations — tap to explore
          </p>
        </div>
      </div>

      {/* Nav pills */}
      <div style={{
        padding: "12px 24px", borderBottom: `1px solid ${T.border}`,
        overflowX: "auto", whiteSpace: "nowrap",
        background: T.bg,
        position: "sticky", top: 0, zIndex: 10,
      }}>
        <div style={{ maxWidth: 720, margin: "0 auto", display: "flex", gap: 6 }}>
          {sections.map((s, i) => (
            <button
              key={s.id}
              onClick={() => setActive(i)}
              style={{
                padding: "6px 14px", borderRadius: 20, border: "none",
                background: active === i ? `${T.accent}20` : "transparent",
                color: active === i ? T.accent : T.textMuted,
                cursor: "pointer", fontFamily: T.font, fontSize: 11,
                fontWeight: active === i ? 700 : 400,
                flexShrink: 0,
              }}
            >
              {s.num}
            </button>
          ))}
        </div>
      </div>

      {/* Content */}
      <div style={{ maxWidth: 720, margin: "0 auto", padding: "24px 24px 64px" }}>
        <div style={{ marginBottom: 20 }}>
          <div style={{
            fontFamily: T.font, fontSize: 11, color: T.accent,
            letterSpacing: 1, marginBottom: 4,
          }}>
            {sections[active].num}
          </div>
          <h2 style={{
            fontFamily: "'Space Grotesk', sans-serif",
            fontSize: 20, fontWeight: 700, marginBottom: 4,
          }}>
            {sections[active].title}
          </h2>
          <p style={{ fontSize: 13, color: T.textMuted }}>
            {sections[active].desc}
          </p>
        </div>
        <ActiveComponent />

        {/* Pagination */}
        <div style={{
          display: "flex", justifyContent: "space-between", marginTop: 32,
          paddingTop: 20, borderTop: `1px solid ${T.border}`,
        }}>
          <button
            onClick={() => setActive(Math.max(0, active - 1))}
            disabled={active === 0}
            style={{
              padding: "8px 18px", borderRadius: 8,
              border: `1px solid ${T.border}`, background: "transparent",
              color: active === 0 ? T.border : T.textMuted,
              cursor: active === 0 ? "default" : "pointer",
              fontFamily: T.font, fontSize: 12,
            }}
          >
            ← Prev
          </button>
          <span style={{ fontFamily: T.font, fontSize: 11, color: T.textMuted, alignSelf: "center" }}>
            {active + 1} / {sections.length}
          </span>
          <button
            onClick={() => setActive(Math.min(sections.length - 1, active + 1))}
            disabled={active === sections.length - 1}
            style={{
              padding: "8px 18px", borderRadius: 8,
              border: `1px solid ${active === sections.length - 1 ? T.border : T.accent}`,
              background: active === sections.length - 1 ? "transparent" : `${T.accent}15`,
              color: active === sections.length - 1 ? T.border : T.accent,
              cursor: active === sections.length - 1 ? "default" : "pointer",
              fontFamily: T.font, fontSize: 12,
            }}
          >
            Next →
          </button>
        </div>
      </div>
    </div>
  );
}

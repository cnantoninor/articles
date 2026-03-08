# Article 2 — LaTeX Formulas for Substack

Copy the LaTeX (without the `$$`) into Substack's LaTeX block.

---

## Epistemic Debt (main formula)

**Unicode:** Ed = ∫[0 to T] (Cs(t) - Gc(t)) dt

**LaTeX:**

```
E_d = \int_0^T \left( C_s(t) - G_c(t) \right) dt
```

---

## Decomposed Across Abstraction Layers

**Unicode:** Ed = Σ_k ∫[0 to T] (Cs_k(t) - Gc_k(t)) dt

**LaTeX:**

```
E_d = \sum_k \int_0^T \left( C_{s,k}(t) - G_{c,k}(t) \right) dt
```

---

## Recovery Growth (linear)

**Unicode:** Gc_k(τ) = Gc_k(t₀) + r_k · τ_k

**LaTeX:**

```
G_{c,k}(\tau) = G_{c,k}(t_0) + r_k \cdot \tau_k
```

---

## Recovery Equation (set equal)

**Unicode:** Gc_k(t₀) + r_k · τ_k = Cs_k(t₀)

**LaTeX:**

```
G_{c,k}(t_0) + r_k \cdot \tau_k = C_{s,k}(t_0)
```

---

## Recovery Time

**Unicode:** τ_k = (Cs_k(t₀) - Gc_k(t₀)) / r_k

**LaTeX:**

```
\tau_k = \frac{C_{s,k}(t_0) - G_{c,k}(t_0)}{r_k}
```

---

## Total Recovery Time

**Unicode:** T_recovery = Σ_k τ_k = Σ_k (Cs_k(t₀) - Gc_k(t₀)) / r_k

**LaTeX:**

```
T_{\text{recovery}} = \sum_k \tau_k = \sum_k \frac{C_{s,k}(t_0) - G_{c,k}(t_0)}{r_k}
```

---

## Cascade Cost

**Unicode:** C_k = Σ_{j=1}^{k} τ_j

**LaTeX:**

```
C_k = \sum_{j=1}^{k} \tau_j
```

---

## Net Benefit

**Unicode:** Net benefit = δ - Σ_k c_k · τ_k

**LaTeX:**

```
\text{Net benefit} = \delta - \sum_k c_k \cdot \tau_k
```

---

## Loss Condition

**Unicode:** Σ_k c_k · τ_k > δ

**LaTeX:**

```
\sum_k c_k \cdot \tau_k > \delta
```

---

## Epistemic Credit

**Unicode:** Ce = ∫[0 to T] (Gc(t) - Cs(t)) dt

**LaTeX:**

```
C_e = \int_0^T \left( G_c(t) - C_s(t) \right) dt
```

---

## Recovery Growth (logarithmic — footnote)

**Unicode:** Gc_k(τ) = Gc_k(t₀) + α_k · ln(1 + β_k · τ_k)

**LaTeX:**

```
G_{c,k}(\tau) = G_{c,k}(t_0) + \alpha_k \cdot \ln(1 + \beta_k \cdot \tau_k)
```

---

## Recovery Time (logarithmic — footnote)

**Unicode:** τ_k = (e^((Cs_k(t₀) - Gc_k(t₀)) / α_k) - 1) / β_k

**LaTeX:**

```
\tau_k = \frac{e^{(C_{s,k}(t_0) - G_{c,k}(t_0)) / \alpha_k} - 1}{\beta_k}
```

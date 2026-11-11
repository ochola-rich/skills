# Apple Design System: Multi-Platform UI/UX Audit Rubric

A standardized 100-point inspection rubric and verification checklist for auditing Web, iOS, and Android applications against Human Interface standards.

---

## 1. The 100-Point Scoring Matrix

| Category | Points | Core Inspection Criteria |
| :--- | :---: | :--- |
| **1. Touch Ergonomics & Hit Zones** | 20 | Minimum 44pt (iOS/Web) or 48dp (Android) clickable area; 8pt spacing between adjacent targets; primary controls placed in thumb zone. |
| **2. Spatial Grid & Layout Rhythm** | 15 | Strict adherence to the 8pt grid (4pt half-grid for micro elements); consistent 16pt/24pt page margins; safe area insets respected. |
| **3. Typography & Hierarchy** | 20 | Single clear H1/Title; semantic text styles used; Dynamic Type fluid scaling supported; line height (`leading`) prevents cramped lines. |
| **4. Contrast & Accessibility** | 15 | WCAG AA compliance (minimum 4.5:1 body text, 3:1 large headings/icons); dark mode surface tiers; screen reader accessibility labels. |
| **5. Motion & Feedback Dynamics** | 15 | Interactive spring physics instead of linear easing; immediate touch/hover states; haptic or tactile cues; `prefers-reduced-motion` honored. |
| **6. Platform Idiom Harmony** | 15 | No "uncanny valley" clones; native back gesture preserved; appropriate bottom/header navigation patterns for the target platform. |
| **Total** | **100** | **Passing Score: ≥ 85 points** |

---

## 2. Audit Severity Classification

- **P0 - Critical Blocker**:
  - Touch targets below 44pt/48dp on essential actions.
  - Text contrast below 3:1 (illegible).
  - Overriding or breaking system back gestures (edge swipe on iOS, predictive back on Android, browser history on Web).
  - Text clipping or truncating when accessibility font sizes are increased.
- **P1 - Major Polish Defect**:
  - Linear or robotic animation curves instead of spring physics.
  - Heavy black drop shadows instead of subtle materials, hairline strokes, or tonal elevations.
  - More than one "Filled" primary button fighting for visual dominance in a single view.
  - Form validation errors appearing only after submission rather than inline.
- **P2 - Minor Refinement**:
  - Hairline dividers that do not align or indent to the leading text edge.
  - Missing subtle hover/press states on secondary buttons.
  - Redundant toggle status labels (e.g. writing "ON" next to a green active switch).

---

## 3. Step-by-Step Audit Procedure

When tasked with auditing a screen or component codebase:

1. **Step 1: Metric Check**
   - Inspect layout code for dimensions. Flag any `width` or `height` on buttons `< 44px/44pt/48dp`.
   - Check margin padding for 8pt multipliers (`8`, `16`, `24`, `32`).
2. **Step 2: Contrast & Theme Scan**
   - Measure foreground text hex against background surface hex.
   - Test both Light Mode and Dark Mode palettes.
3. **Step 3: Responsive & Scale Test**
   - Check if fixed heights (`h-12` or `height: 48px`) enclose text containers. Text must expand dynamically without truncation.
4. **Step 4: Interaction & Navigation Review**
   - Verify back navigation mechanisms.
   - Verify sheet dismissal and non-destructive cancellation safeguards.
5. **Step 5: Produce Audit Summary Table**
   - Output category scores, identified P0/P1/P2 issues, and specific code diff recommendations.

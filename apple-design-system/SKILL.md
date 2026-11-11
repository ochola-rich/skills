---
name: apple-design-system
description: >-
  Apple Human Interface Guidelines (HIG) and cross-platform UI/UX engineering system.
  Use when designing, building, reviewing, or auditing user interfaces across iOS, iPadOS, macOS,
  Modern Web (React, Next.js, Vue, Tailwind CSS), and Android (Jetpack Compose, Kotlin, Flutter).
  Enforces Apple-grade visual clarity, 8pt spatial layout grid, 44pt touch ergonomics,
  San Francisco typography hierarchies, dynamic type scaling, semantic color architectures,
  materials/vibrancy (frosted glass), spring physics animations, and WCAG AA/AAA accessibility.
---

# Apple Design System & Multi-Platform UI/UX Guide

An agentic skill synthesized directly from Apple's official **Human Interface Guidelines (HIG)**, expanded with cross-platform engineering rules for **Web** and **Android**.

---

## 1. When to Use This Skill

Activate this skill when:
- **Designing New Screens or Components**: Creating UI layouts, sheets, navigation hierarchies, cards, buttons, or form controls for iOS, macOS, Web, or Android.
- **Auditing UI/UX Quality**: Performing a rigorous design audit on existing Swift/SwiftUI, React/Tailwind, or Jetpack Compose code.
- **Adapting Apple Aesthetics to Web**: Implementing frosted glass (materials), spring physics, 8pt spatial rhythm, or high-end typography in modern web apps.
- **Adapting Apple Polish to Android**: Bringing Apple's craft and fluid feedback to Android apps while respecting Material 3 and avoiding the "uncanny valley".
- **Refining Accessibility**: Ensuring 44pt touch targets, high contrast ratios (WCAG AA/AAA), Dynamic Type support, and VoiceOver/screen reader readiness.

---

## 2. Core Philosophy: The Six Apple HIG Principles

1. **Aesthetic Integrity**: Visual appearance directly matches functionality. A tool looks focused and calm; an entertainment experience looks immersive and rich.
2. **Consistency**: Familiar system icons (SF Symbols), standard controls, and predictable gestures reduce cognitive load.
3. **Direct Manipulation**: Interacting with screen objects feels physical (dragging, pinching, flicking, rubber-banding). Feedback occurs in real time.
4. **Feedback**: Every tap, drag, or state change produces immediate, subtle visual and tactile confirmation (haptics, highlight, or spring response).
5. **Metaphors**: Digital objects echo physical real-world counterparts (folders, switches, sheets sliding over paper layers).
6. **User Control**: People—not the app—remain in charge. Actions are cancellable, non-destructive defaults are preferred, and confirmation is required only for irreversible operations.

---

## 3. The Three Universal Design Themes

- **Clarity**: Text is legible at every size, icons are precise and lucid, adornments are subtle, and functional focus drives the design.
- **Deference**: Fluid motion and a crisp, beautiful interface elevate content without competing with it. Content always takes center stage.
- **Depth**: Visual layers, translucency (materials), and realistic shadows impart vitality and convey hierarchical relationships.

---

## 4. Multi-Platform Translation Matrix

When applying Apple design principles to Web or Android, use this quick reference:

| Dimension | Apple Native (iOS/macOS) | Modern Web (React / Tailwind) | Android (Jetpack Compose) |
| :--- | :--- | :--- | :--- |
| **Touch Target** | Min `44×44 pt` | Min `44×44 px` (or `48×48 px`) | Min `48×48 dp` |
| **Grid System** | `8pt` base grid / `4pt` half-grid | `8px` (`0.5rem` / `p-2`, `p-4`) | `8dp` spacer intervals |
| **Typography** | SF Pro (`.largeTitle`, `.body`, etc.) | System stack (`-apple-system, Inter`) | Roboto / Product Sans (`Headline`, `Body`) |
| **Materials** | Blur + Vibrancy (`.ultraThinMaterial`) | `backdrop-blur-md` + border opacity | Tonal Elevation + Surface tint |
| **Animation** | Damped interactive springs | Framer Motion springs / CSS cubic-bezier | Spring Spec (`spring(dampingRatio, stiffness)`) |
| **Navigation** | NavigationStack + TabBar | Header nav + Responsive bottom bar | Scaffold + TopAppBar + NavigationBar |
| **Back Navigation** | Interactive edge-swipe + Back button | Browser history (`popstate`) + Back link | Predictive Back gesture + System back key |

> [!IMPORTANT]
> **Avoid the "Uncanny Valley" on Android & Web**: Never copy iOS platform widgets literally onto Android (e.g. do not render an iOS toggle or an iOS back chevron on Android). Instead, adopt Apple's **standards of craft** (whitespace, subtle borders, spring motion, typography hierarchy) while utilizing native Android/Web interaction paradigms.

---

## 5. Anti-Slop & Craftsmanship Guardrails (Deslopify Rules)

To eliminate generic AI tropes, enforce the following non-negotiable craftsmanship standards (see [references/deslopify-rules.md](file:///home/richie/apple-design-skill/references/deslopify-rules.md)):

1. **No "Purple Haze" Neon Gradients**: Use calm, neutral surfaces (`#FFFFFF` or `#000000`/`#0f0f13`). Allow exactly ONE dominant functional accent color per view.
2. **No "Bento Grid Salad"**: Every card must represent a real, actionable user workflow or verified telemetry metric. Zero decorative placeholder cards.
3. **Left-Align All Body Copy**: Never center multi-line paragraphs. Enforce 65-75 character max line widths.
4. **No Emoji Soup**: Never use emojis as functional UI icons. Use unified vector icons (SF Symbols / Lucide) with consistent 2px optical weight.
5. **Strict 4-Tier Button Discipline**: Exactly ONE "Filled" primary CTA per view or section. Secondary actions must be "Tinted" or "Gray"; utility links must be "Plain".
6. **Hairlines over Dirty Shadows**: Achieve depth through tonal surface layering and hairline borders (`border-black/[0.06]` or `border-white/10`). Shadows must be soft ambient occlusion ($<4\%$ opacity).
7. **Calm Springs over Animation Clutter**: No infinite floating or looping animations. Interactive spring transitions must settle within $150\text{ms} - 250\text{ms}$.
8. **Plain Human Copy**: Purge AI buzzwords ("supercharge", "holistic next-gen synergy"). Write clear, understated, confident statements of utility.
9. **Non-Negotiable 44pt Touch Hit Zones**: Every interactive element must provide $\ge 44\text{pt}$ ($48\text{dp}$ on Android) hit area with $\ge 8\text{pt}$ separation.
10. **Card-Free, Backgroundless Logos**: Partner/client logos must float freely directly on the canvas—never bounded into individual cards, pill boxes, or sticker containers. All logos must possess 100% alpha transparency.
11. **Navigation vs. Action Separation & Grouped Architecture**: Navigation bars and sidebars are strictly for wayfinding, orientation, and location switching—never for operational action buttons. Resources must be clustered into logical conceptual domains with subtle uppercase caption headers.

---

## 6. Execution Procedures

### Procedure A: UI/UX Audit Workflow
1. **Apply Deslopify Check**: Run the 10-point checklist in [deslopify-rules.md](file:///home/richie/apple-design-skill/references/deslopify-rules.md) to purge neon gradients, centered body copy, and emoji soup.
2. **Analyze Spacing & Geometry**: Check that all margins follow the 8pt scale (16pt mobile margins, 24-32pt desktop margins).
3. **Verify Touch Targets**: Ensure every interactive target (buttons, icons, chips) has at least a 44×44 pt/px/dp bounding hit area.
4. **Inspect Typography Hierarchy**: Confirm there is a single primary H1/Title per view, semantic text styles are used, and line heights (`leading`) allow comfortable reading.
5. **Check Contrast & Dark Mode**: Validate text against WCAG AA standards (4.5:1 for body text, 3:1 for large headings) and confirm semantic surface tokens (`systemBackground`, `secondaryBackground`).
6. **Evaluate Motion & States**: Confirm interactive elements have immediate hover/press states and spring transitions, with full respect for `prefers-reduced-motion`.

### Procedure B: Building a Screen from Scratch
1. Read [foundations.md](file:///home/richie/apple-design-skill/references/foundations.md) for grid tokens, typography scales, and color elevations.
2. Read [deslopify-rules.md](file:///home/richie/apple-design-skill/references/deslopify-rules.md) to avoid common AI design anti-patterns.
3. Read [patterns.md](file:///home/richie/apple-design-skill/references/patterns.md) to choose the correct navigation structure and modal presentation model (sheet detents).
4. Read [components.md](file:///home/richie/apple-design-skill/references/components.md) for button hierarchies, toolbars, and list item architectures.
5. For Web implementations, follow [web-adaptation.md](file:///home/richie/apple-design-skill/references/web-adaptation.md).
6. For Android implementations, follow [android-adaptation.md](file:///home/richie/apple-design-skill/references/android-adaptation.md).
7. Run the final output against [audit-rubric.md](file:///home/richie/apple-design-skill/references/audit-rubric.md).

---

## 7. Deep Reference Index

- **Deslopify Rules**: [references/deslopify-rules.md](file:///home/richie/apple-design-skill/references/deslopify-rules.md) — Anti-slop commandments, slop vs. craft comparison, and pre-merge checklist.
- **Foundations**: [references/foundations.md](file:///home/richie/apple-design-skill/references/foundations.md) — 8pt grid, Dynamic Type tables, semantic color tokens, materials, haptics.
- **Patterns**: [references/patterns.md](file:///home/richie/apple-design-skill/references/patterns.md) — Navigation hierarchies, sheet detents, search states, onboarding, empty states.
- **Components**: [references/components.md](file:///home/richie/apple-design-skill/references/components.md) — Buttons (Filled, Tinted, Gray, Plain), segmented controls, navigation bars, toolbars.
- **Web Adaptation**: [references/web-adaptation.md](file:///home/richie/apple-design-skill/references/web-adaptation.md) — Tailwind classes, CSS glassmorphism recipes, spring curves, responsive breakpoints.
- **Android Adaptation**: [references/android-adaptation.md](file:///home/richie/apple-design-skill/references/android-adaptation.md) — Jetpack Compose equivalents, Material 3 harmony, predictive back.
- **Audit Rubric**: [references/audit-rubric.md](file:///home/richie/apple-design-skill/references/audit-rubric.md) — 100-point scoring rubric and verification checklist.
- **Social Proof & Trust Architecture**: [references/social-proof.md](file:///home/richie/apple-design-skill/references/social-proof.md) — Factual integrity, partner ribbon optical normalization, and executive testimonials.

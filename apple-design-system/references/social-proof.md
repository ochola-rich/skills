# Apple Design System: Social Proof, Partner Normalization & Trust Architecture

A systematic specification for enterprise social proof, partner ribbons, executive testimonials, and auditable trust telemetry—anchored in strict factual integrity with zero fabrication.

---

## 1. The Factual Integrity Mandate (Anti-Hallucination)

> **Never fabricate social proof.** 
> Fictitious client logos, made-up executive quotes, and invented vanity statistics violate user trust, damage brand integrity, and breach Apple's core principle of **Aesthetic Integrity**.

### Ground Rules for Proof & Partners
1. **Auditable Entities Only**: Only display verified ecosystem partners, institutional backers, and genuine client organizations.
2. **Explicit Attributions**: Quotes must cite real individuals with verifiable titles and organizations. If a testimonial is not yet cleared, use a factual platform capability guarantee instead of a fake quote.
3. **No Decorative Placeholders**: Do not insert dummy Fortune 500 logos to "fill space". If an app has 5 verified ecosystem partners, present those 5 with dignity and precision.

---

## 2. Partner Logo Ribbon & Infinite Marquee Architecture

When displaying partner, investor, or client logos:

### Rule: Freely Floating & Card-Free (The Container Ban)
- **Logos MUST NEVER be bounded into cards**: Partner, investor, and client logos must float freely and directly on the section canvas.
- **NEVER wrap logos in individual card containers, pill boxes, bordered enclosures, or tiled squares**: Bounding logos into cards (e.g. `rounded-2xl border bg-white`) is an AI slop cliché that fragments the layout, introduces visual noise, and competes with the logos.
- **Logos MUST always be backgroundless**: Every logo must possess an alpha transparency channel (`.png`, `.svg`, `.webp`) with 0% opacity backgrounds.
- **NEVER enclose logos in solid rectangular white/gray sticker boxes**: Solid colored squares or rectangles look like amateur cut-outs and break visual continuity.
- In Dark Mode, dark or black logo glyphs must adapt via CSS inversion (`dark:brightness-0 dark:invert` or SVG fill `currentColor`) rather than placing a white background card behind them.
- Auto-trim transparent padding so all logos align to their true optical visual baseline.

### Rule: Graphical Logo Marks Over Raw Text
- **Never display plain text names when logos can be utilized.** User cognitive recognition relies on familiar shapes, wordmarks, and seals. Plain text looks like unverified placeholder mockups.
- All partner logos must be rendered as authentic SVG or high-resolution optimized raster assets (`.webp`, `.png`, `.svg`).

### Optical Normalization Standards
Logos come in wildly divergent aspect ratios (wide horizontal wordmarks vs compact vertical seals). To prevent visual chaos:
- **Optical Bounding Box**: Constrain all logos to a uniform height of **$28\text{px} - 36\text{px}$** (desktop) or **$22\text{px} - 26\text{px}$** (mobile), with `object-contain` and automatic width.
- **Monochrome Deference**: 
  - Light mode: Render logos in **grayscale with $60\%$ opacity** (`grayscale opacity-60 hover:opacity-100 hover:grayscale-0 transition-all duration-300`).
  - Dark mode: Invert or brighten dark logos to preserve contrast against dark backgrounds (`dark:invert dark:brightness-125 dark:opacity-70 dark:hover:opacity-100`).
- **Interactive State**: On hover, smoothly restore full brand color and 100% opacity.

### Infinite Continuous Marquee (Ticker) Standard
To display multiple partners without occupying excessive vertical screen real estate, implement an **infinite horizontal marquee**:

1. **Seamless Duplicate Loop**: Render the partner array twice (`[...PARTNERS, ...PARTNERS]`) so the translation from $0\%$ to $-50\%$ seamlessly loops forever.
2. **Edge Masking (Vignette)**: Apply CSS linear gradient masks so logos fade smoothly into the background margins rather than sharply clipping:
   ```css
   mask-image: linear-gradient(to right, transparent 0%, black 12%, black 88%, transparent 100%);
   -webkit-mask-image: linear-gradient(to right, transparent 0%, black 12%, black 88%, transparent 100%);
   ```
3. **Speed & Ergonomics**:
   - Marquee duration: **25s to 35s** for 8-12 logos (calm, readable drifting speed, never dizzying).
   - **Pause on Interaction**: The marquee must pause when hovered or touched (`hover:[animation-play-state:paused]`).
4. **Accessibility (Reduce Motion)**:
   - When `@media (prefers-reduced-motion: reduce)` is active, disable the animation and render a static wrapable grid or smooth overflow scroll.

---

## 3. Executive & Partner Testimonial Specifications

When featuring testimonials from ecosystem partners, brand managers, or creators:

```
┌────────────────────────────────────────────────────────┐
│ "Direct quotation explaining concrete, auditable       │
│  outcomes or operational reliability."                 │
│                                                        │
│  [ Avatar ]  Full Name                                 │
│  (48x48)     Title / Role · Verified Organization      │
└────────────────────────────────────────────────────────┘
```

### Formatting Standards
1. **Avatar Geometry**: $48\text{px} \times 48\text{px}$ continuous squircle (`rounded-xl`) or circle with a hairline border (`border border-zinc-200/80 dark:border-zinc-800`).
2. **Attribution Hierarchy**:
   - Line 1: **Full Name** (`text-sm font-semibold text-zinc-900 dark:text-zinc-100`)
   - Line 2: **Role · Organization** (`text-xs text-zinc-500 dark:text-zinc-400`)
3. **Tone**: Factual, focused on operational outcomes (e.g. turnaround speed, escrow safety, cohort placements), avoiding breathless marketing puffery.

---

## 4. Telemetry Metric Counters

When displaying impact metrics (e.g. active creators, disbursed payouts):
- **Numeral Typography**: Large, tabular figures (`font-semibold tracking-tight font-sans text-3xl sm:text-4xl text-zinc-950 dark:text-zinc-50`).
- **Unit Labels**: Crisp, lowercase or uppercase caption immediately beneath the numeral (`text-xs text-zinc-500 font-medium`).
- **Accuracy Guarantee**: Metrics must represent actual measured data or clear pilot milestones.

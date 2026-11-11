# Apple Human Interface Guidelines: Foundations & Design Tokens

Foundational design rules, ergonomic constants, typography scales, semantic color architectures, and spatial layout standards synthesized from Apple HIG.

---

## 1. Spatial Layout & Grid System

### 8pt Spatial Grid
Apple interfaces are constructed on an **8pt grid** (with a **4pt half-grid** for micro-spacing, borders, tags, and icon alignments).

| Token | Value | Primary Usage |
| :--- | :--- | :--- |
| `space-xxs` | `2pt` / `2px` | Sub-pixel hairline offsets, badge borders |
| `space-xs` | `4pt` / `4px` | Icon-to-label gaps, tight tag padding |
| `space-sm` | `8pt` / `8px` | Space between related elements in a group |
| `space-md` | `16pt` / `16px` | Standard screen margin (compact), card internal padding |
| `space-lg` | `24pt` / `24px` | Distance between distinct content sections |
| `space-xl` | `32pt` / `32px` | Generous layout margins, modal sheet headers |
| `space-xxl` | `48pt` / `48px` | Hero spacing, empty-state top padding |

### Safe Areas & Insets
- **Top Safe Area**: Protects against Dynamic Island, sensor housing (notch), and system status bar (time, battery, Wi-Fi). Always extend background materials into the safe area while clamping interactive content below it.
- **Bottom Safe Area**: Protects against the Home Indicator bar (minimum 34pt bottom clearance on iPhones). Interactive buttons and tab bars must account for this inset; their background material extends to the screen edge.
- **Keyboard Inset**: Content must smoothly translate or compress upward when the virtual keyboard appears, preserving the focused input field in the upper third of the viewport.

---

## 2. Touch Targets & Ergonomic Geometry

### The 44×44 pt Rule
- Every interactive element (buttons, links, icon toggles, list accessories) must have a **minimum interactive target of 44×44 pt** (points), regardless of visual bounding box size.
- A 16×16 pt icon must provide at least 14pt of invisible tap padding on each side.
- **Target Separation**: Maintain at least **8pt** between interactive touch targets to eliminate accidental taps.

### The Thumb Zone Principle
```
┌─────────────────────────┐
│       TOP ZONE          │  Low Reach: Status, back button, dismiss, search bar
│   (Difficult reach)     │
├─────────────────────────┤
│      MIDDLE ZONE        │  Natural Read: Primary content, media, articles, cards
│      (Comfortable)      │
├─────────────────────────┤
│      BOTTOM ZONE        │  Highest Reach: Tab bars, floating action pills,
│       (Easiest)         │  primary CTAs, keyboard interactions, sheet grabbers
└─────────────────────────┘
```

---

## 3. Typography Architecture

Apple uses the **San Francisco (SF)** font family:
- **SF Pro**: iOS, iPadOS, macOS, Web (Dynamic Type)
- **SF Compact**: watchOS, tight complications
- **SF Mono**: Code, terminal, monospace data
- **New York**: Editorial serif companion

### Standard Dynamic Type Scale (Default iOS / macOS)

| Style | Size (pt) | Weight | Leading (Line Height) | Primary Usage |
| :--- | :--- | :--- | :--- | :--- |
| **Large Title** | `34pt` | Bold | `41pt` | Primary screen title in collapsible navigation bar |
| **Title 1** | `28pt` | Bold / Semibold | `34pt` | Major section header, modal header |
| **Title 2** | `22pt` | Bold | `28pt` | Subsection header |
| **Title 3** | `20pt` | Semibold | `25pt` | Card title, group header |
| **Headline** | `17pt` | Semibold | `22pt` | Emphasized content titles, list primary labels |
| **Body** | `17pt` | Regular | `22pt` | Default paragraph text, form inputs, list items |
| **Callout** | `16pt` | Regular | `21pt` | Highlighting secondary info, callouts, tooltips |
| **Subheadline** | `15pt` | Regular | `20pt` | Subtitle under headline, list secondary metadata |
| **Footnote** | `13pt` | Regular | `18pt` | Timestamps, helper instructions, disclaimers |
| **Caption 1** | `12pt` | Regular | `16pt` | Tab bar labels, small badges, auxiliary notes |
| **Caption 2** | `11pt` | Regular | `13pt` | Smallest legible annotations, tags |

### Dynamic Type Rules
- Text must **scale dynamically** when users adjust their system accessibility text size.
- Layouts must wrap or shift into stacked vertical arrangements rather than truncating critical content when larger accessibility sizes are activated.
- Never hardcode fixed container heights around text elements.

---

## 4. Semantic Color Architecture & Dark Mode

Apple color is **semantic, adaptive, and functional**, never merely decorative.

### Semantic Foreground (Labels)
- **Primary Label** (`label`): High-contrast primary text and icons.
  - Light: `rgba(0, 0, 0, 0.85)` / `#000000`
  - Dark: `rgba(255, 255, 255, 0.92)` / `#FFFFFF`
- **Secondary Label** (`secondaryLabel`): Subtitles, helper text, inactive navigation icons.
  - Light: `rgba(60, 60, 67, 0.60)`
  - Dark: `rgba(235, 235, 245, 0.60)`
- **Tertiary Label** (`tertiaryLabel`): Placeholder text, disabled controls, subtle delimiters.
  - Light: `rgba(60, 60, 67, 0.30)`
  - Dark: `rgba(235, 235, 245, 0.30)`
- **Quaternary Label** (`quaternaryLabel`): Subtle hairline dividers, decorative non-text strokes.
  - Light: `rgba(60, 60, 67, 0.18)`
  - Dark: `rgba(235, 235, 245, 0.18)`

### Semantic Backgrounds (Elevation Tiers)
1. **Base Background** (`systemBackground`): Pure screen canvas.
   - Light: `#FFFFFF` | Dark: `#000000`
2. **Secondary Background** (`secondarySystemBackground`): Inset cards, grouped rows, table backgrounds.
   - Light: `#F2F2F7` | Dark: `#1C1C1E`
3. **Tertiary Background** (`tertiarySystemBackground`): Modals, floating popovers, elements layered on secondary.
   - Light: `#FFFFFF` | Dark: `#2C2C2E`
4. **Grouped Backgrounds** (`systemGroupedBackground`): Table layouts with card containers.
   - Light: `#F2F2F7` | Dark: `#000000`

### Accessibility Contrast Mandates
- Standard text (< 18pt bold or < 24pt regular): **Minimum 4.5:1** contrast ratio against its background (WCAG AA).
- Large text / icons: **Minimum 3.0:1** contrast ratio.
- Never convey state exclusively through color; always pair color with an icon, label, or haptic cue.

---

## 5. Materials & Vibrancy (Translucency)

Materials simulate physical frosted glass, visually layering foreground content over scrolling or dynamic background content without loss of legibility.

### Material Tiers
- **Ultra-Thin Material**: High background pass-through, subtle frosting. Best for ambient overlays, HUDs.
- **Thin Material**: Moderate blurring. Ideal for navigation bars and collapsible headers.
- **Regular Material**: Balanced opacity and blur. Standard for tab bars, toolbars, and sheets.
- **Thick Material**: High opacity with soft edge light. Used when background content behind the element has high contrast or busy graphics.

### Implementation Guidelines
- Never place low-contrast text on a raw translucent material without a **vibrancy filter** or high-contrast backing tint.
- In Dark Mode, materials use subtle inner highlights (`rgba(255, 255, 255, 0.08)`) and borders to delineate edges against black backgrounds.

---

## 6. Motion & Spring Physics

Apple interfaces feel physical because animations follow real-world mass, damping, and stiffness rather than linear transitions.

### Spring Dynamics Standard
- **Interactive Damped Springs**: Fast initial response, soft settling, zero robotic bouncing unless explicitly representing playful bounce (e.g. rubber banding at list boundaries).
- **Duration Reference**:
  - Micro-interactions (toggle, checkbox, button press): **150ms – 250ms**
  - Navigation transitions (push, pop, sheet slide): **300ms – 400ms**
  - Modal presentations / full views: **400ms – 500ms**
- **Accessibility - Reduce Motion**:
  - Always honor the user's `prefers-reduced-motion` or system setting.
  - When enabled, replace zoom, spatial fly-ins, and large translation effects with simple opacity cross-fades.

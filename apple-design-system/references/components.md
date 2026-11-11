# Apple Human Interface Guidelines: Component Specifications & Standards

Detailed rules, geometries, states, and hierarchy for system-defined and custom components.

---

## 1. Buttons & Action Affordances

Apple defines a four-tier button hierarchy to guide user focus:

```
[ Primary Action (Filled) ]       <-- Highest visual weight (max 1 per view)
[ Secondary Action (Tinted) ]     <-- Balanced emphasis, colored accent tint
[ Tertiary Action (Gray) ]        <-- Neutral, low-contrast utility
[ Plain Text Action ]             <-- Borderless, toolbar or auxiliary links
```

### Button Specifications

| Style | Background Treatment | Label Color | Usage Guide |
| :--- | :--- | :--- | :--- |
| **Filled** | Solid Accent (e.g., `#007AFF`) | White / High Contrast | The single primary CTA on a screen (e.g., "Submit Order", "Continue"). |
| **Tinted** | 12% Accent Tint (`rgba(0,122,255,0.12)`) | Accent Color | Important secondary actions (e.g., "Add to Playlist", "Filter"). |
| **Gray** | Neutral Fill (`rgba(120,120,128,0.16)`) | Primary Label | Utility actions that should not distract from content (e.g., "Cancel", "Details"). |
| **Plain** | Transparent (`none`) | Accent or Primary | Toolbar buttons, inline table actions, navigation bar items. |

### Button Shape & Curvature
- **Squircle (Continuous Curve)**: Apple buttons use smooth continuous corner curves (`smooth-corners`) rather than simple circular arcs.
- **Pill vs Rounded Rect**:
  - Rounded Rect (`corner-radius: 10pt - 14pt`): Standard for forms, dialogs, and cards.
  - Full Pill (`corner-radius: 9999px`): Floating action buttons, media playback controls, tags, and chips.
- **Touch Geometry**: Minimum interactive height of **44pt** (even if visual badge height is 28pt or 32pt).

---

## 2. Navigation Bars & Toolbars

### Navigation Bar Anatomy
- **Height**: Standard inline is 44pt; with Large Title it expands to 96pt - 110pt.
- **Large Title Behavior**:
  - Renders as `34pt Bold` at top of view.
  - On scroll down, smoothly animates and collapses into a compact `17pt Semibold` title centered in the navigation bar.
- **Action Slots**:
  - *Leading*: Back button (with previous view title or chevron) or modal "Cancel"/"Close".
  - *Trailing*: Maximum 2 actions (e.g., "Edit" or icon buttons). Additional actions must be grouped in an overflow menu.

### Toolbars vs Tab Bars
- **Tab Bar (Bottom)**: Persistent global navigation between app areas (3-5 items).
- **Toolbar (Bottom / Floating)**: Contextual actions for the *current* screen (e.g., "Share", "New Message", "Trash").
- **Visual Separation**: Bottom bars must feature translucent materials (Thin/Regular) that blur background content scrolling underneath, with a hairline top divider.

---

## 3. Selection & Input Controls

### Switches (Toggles)
- **Immediate Effect**: Toggling a switch must take effect immediately. Never require the user to tap "Save" or "Apply" to commit a toggle state.
- **State Labels**: Do not add redundant "On"/"Off" text next to a switch; the visual green accent fill and knob position explicitly communicate the state.

### Segmented Controls
- **Capacity**: Use for **2 to 5 options** (e.g., "Day / Week / Month / Year").
- **Equal Width**: Each segment shares equal width.
- **Exclusive Selection**: Exactly one segment is active at any time; selection transition should slide a white/light pill thumb across the track.

### Sliders & Steppers
- **Sliders**: Best for continuous, subjective adjustments (Volume, Brightness, Image Saturation). Include minimum and maximum value icons at either end.
- **Steppers**: Best for discrete, exact integer adjustments (Ticket quantity: 1, 2, 3). Provide an adjacent label showing current count.

---

## 4. Inset Grouped Lists & Table Views

The **Inset Grouped Table** is the hallmark of Apple settings and data displays:

```
┌────────────────────────────────────────────────────────┐
│ SECTION HEADER (13pt, Uppercase or Semibold, Gray)     │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Icon   Row Item 1                  Detail >     │  │
│  │        ───────────────────────────────────────── │  │
│  │ Icon   Row Item 2                  [ Toggle ]   │  │
│  │        ───────────────────────────────────────── │  │
│  │ Icon   Row Item 3 (Destructive)                 │  │
│  └──────────────────────────────────────────────────┘  │
│ SECTION FOOTER (13pt, Regular, Secondary Gray)         │
└────────────────────────────────────────────────────────┘
```

### Rules for Inset Grouped Lists:
- **Card Background**: `secondarySystemBackground` with `10pt - 14pt` corner radius.
- **Dividers**: Hairline divider starts at the leading text edge (indenting past the icon) and extends to the right edge. Never draw a divider beneath the final row.
- **Row Height**: Minimum 44pt (standard 52pt - 56pt for icon + two-line subtitle).
- **Row Press State**: Subtle dimmed highlight on tap with spring release.

---

## 5. Cards & Elevation Architecture

Apple does not rely on heavy drop shadows to communicate hierarchy. Instead, depth is achieved through:
1. **Tonal Separation**: Placing a `tertiarySystemBackground` card on top of a `secondarySystemBackground` page.
2. **Hairline Strokes**: Subtle 1px borders (`rgba(0,0,0,0.06)` in light mode, `rgba(255,255,255,0.08)` in dark mode).
3. **Ambient Occlusion Shadows**: Soft, diffuse shadows with large blur radius and low opacity:
   ```css
   box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04), 0 1px 3px rgba(0, 0, 0, 0.02);
   ```

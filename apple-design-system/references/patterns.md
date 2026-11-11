# Apple Human Interface Guidelines: Interaction Patterns & Flows

Systematic patterns for navigation architectures, modal presentations, search, onboarding, forms, and feedback states across platforms.

---

## 1. Navigation Architectures

Apple defines three primary navigation paradigms:

### A. Hierarchical Navigation (Push / Pop)
- **Concept**: One choice per screen until reaching a destination. To navigate to another destination, retrace steps or start over.
- **Rules**:
  - The navigation bar displays the current view title and a back button pointing to the parent view.
  - On compact touch displays, **interactive edge swipe** (swiping from the left screen edge) must *always* pop the view. Never break or disable this gesture with conflicting horizontal carousels without proper edge padding.
  - Deep hierarchies (> 3 levels) should provide breadcrumbs or shortcuts to return directly to the root.

### B. Flat Navigation (Tab-Based)
- **Concept**: Switch between multiple parallel content categories or operational modes.
- **Rules**:
  - **3 to 5 tabs maximum**. Never crowd a tab bar with 6+ tabs; use a "More" tab or sidebar if additional sections are required.
  - Tab bars are strictly for **navigation**, never for triggering actions (do not place a "Compose" or "Camera" modal trigger inside a tab bar unless styled distinctly as a raised central action button).
  - Tapping the currently active tab must scroll the current view back to the top. Tapping it again should pop any nested hierarchy back to the tab root.

### C. Split View & Sidebar Navigation (Wide Screen / Desktop)
- **Concept**: Two or three-column layout (Sidebar → Content List → Detail View) adapted for tablets, desktops, and wide web viewports.
- **Rules**:
  - Responsive collapse: On compact widths (e.g. mobile portrait), the split view collapses gracefully into a standard hierarchical navigation stack.
  - The sidebar contains persistent sections, tags, or filters; the middle pane lists items; the primary pane displays the selected item's full detail.

### D. Navigation vs. Action Separation (The Wayfinding Mandate)
- **Navigation is for Wayfinding, NOT Action Execution**:
  - Navigation bars, tab bars, and sidebars tell people **where they are** and allow them to **change location**.
  - **NEVER crowd navigation bars or sidebars with operational action buttons** (e.g. "Create Campaign", "Export CSV", "Approve", "+ New Item").
  - Actions belong in **Page Headers** (leading title with trailing contextual action button), **Contextual Toolbars** (at the bottom or within a list/table), or **Modal Sheets**.
  - In marketing top navbars, links are wayfinding anchors (`Features`, `Escrow`, `Partners`). Conversion triggers belong on the hero canvas or page header, not screaming as high-contrast action buttons inside the navbar.

### E. Grouped Information Architecture (Resource Clustering)
- **Never render a flat laundry list of 6+ navigation items**:
  - Navigation items must be grouped into **conceptual resource clusters** (domains) using subtle, succinct section headers (e.g., *Workspace*, *Campaign Operations*, *Finance & Escrow*, *System*).
  - Use uppercase micro-typography (`text-[10px] font-semibold uppercase tracking-wider text-muted-foreground/80 px-3 py-1`) for group headers.
  - Limit hierarchy to at most two levels. Use consistent vector iconography across all items in a group.

---

## 2. Modality & Sheet Presentations

Modality creates a focused interaction mode that requires a decision before returning to the main workflow.

### Sheet Presentation & Detents
- **Medium Detent (Half-Sheet)**: Covers ~50% of screen height. Best for quick selections, share sheets, comments, or secondary filters while preserving background context.
- **Large Detent (Full-Sheet)**: Covers ~90% of screen height with card corner radius and dimming backdrop. Best for multi-step tasks, form completion, and editing.
- **Sheet Grabber Affordance**: Always include a subtle horizontal pill grabber at the top of a resizable sheet to indicate drag affordance.

### Modality Hierarchy
```
┌────────────────────────────────────────────────────────┐
│ Full Screen Navigation (Parent Workflow)               │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Modal Sheet (e.g., Edit Profile / Filter)        │  │
│  │   ┌───────────────────────────────────────────┐  │  │
│  │   │ Alert / Action Confirmation (Urgent Modal)│  │  │
│  │   └───────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────┘
```

### Alerts & Confirmations
- **Title**: Brief, clear statement (e.g., "Delete Post?").
- **Message**: Explain consequences (e.g., "This action cannot be undone.").
- **Button Limits**:
  - Maximum **2 buttons** for binary choices (e.g., "Cancel" and "Delete").
  - Place the non-destructive button ("Cancel") on the left (or bottom in vertical stacks).
  - Style destructive actions in **System Red**.
  - Always allow dismissal without consequence (e.g., Esc key or tapping outside on tablets/desktop).

---

## 3. Search & Filtering Patterns

- **Search Bar Placement**: Integrated directly into the collapsible navigation bar. When the user scrolls down, the search bar tucks away or condenses to maximize content space.
- **Scopes & Filters**: When filtering across multiple categories, use **segmented controls** or **scrollable filter pills** directly beneath the search bar.
- **Search States**:
  1. *Unfocused*: Shows placeholder text indicating scope (e.g. "Search songs, artists, albums").
  2. *Active Empty*: Displays recent search history, trending searches, or search categories.
  3. *Live Query*: Displays real-time matching suggestions or auto-complete tokens.
  4. *Submitted Results*: Full results grid or list with result counts and active filter badges.
- **Cancel Button**: Appears on focus; tapping Cancel clears text, dismisses the keyboard, and restores previous scroll state immediately.

---

## 4. Onboarding & Permission Ergonomics

### Progressive Disclosure
- Never demand sign-ups or permissions on first app launch before demonstrating value.
- Allow users to explore sample content, browse catalogs, or experience core functionality before requiring authentication.

### Contextual Permission Requests
- Ask for permissions (Location, Camera, Microphone, Notifications) **in the exact moment of user intent**, not in a burst during initial setup.
- If a user taps "Scan QR Code", *that* is when the Camera permission dialog must be presented.
- Precede system permission alerts with a tailored context sheet explaining the direct user benefit.

---

## 5. Forms, Input & Error Recovery

- **Field Density & Spacing**: Minimum 48pt row height for input fields to guarantee comfortable finger taps.
- **Specialized Keyboards**: Match `inputmode` and `type` attributes strictly:
  - Email: `type="email"`, auto-capitalization disabled, auto-correct disabled.
  - Phone: `type="tel"`, numeric telephone keypad.
  - Numbers/Currency: `type="decimal"` or `inputmode="decimal"`.
- **Inline Validation**:
  - Show error messages directly beneath the offending input with an accompanying warning icon.
  - Never clear user input on error; keep the entered text intact so the user only corrects the mistake.
- **Draft Preservation**: If a user cancels a dirty modal sheet, prompt with an Action Sheet: "Discard Changes" (destructive red) vs "Keep Editing". Automatically save drafts whenever possible.

---

## 6. Feedback, Loading & Empty States

### Loading Patterns
- **Determinate Progress**: Use a linear progress bar whenever the operation duration or payload size is known (e.g., file downloads, uploads).
- **Indeterminate Activity**: Use system spinner indicator only for quick operations of unknown duration (< 4 seconds).
- **Skeleton Screens**: For content loading (e.g. social feeds, product lists), display pulsing placeholder shapes matching the exact geometry of titles, avatars, and cards to prevent layout shifts.

### Empty State Architecture
Every empty state must contain three distinct elements:
1. **Visual Metaphor**: A subtle, monochrome or tinted icon/illustration (e.g. empty inbox, bookmark outline).
2. **Explanatory Text**: A clear title ("No Saved Articles") and a concise 1-2 sentence subtitle ("Articles you bookmark will appear here for offline reading.").
3. **Primary Action**: A prominent button guiding the next step (e.g. "Explore Popular Articles").

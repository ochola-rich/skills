# Apple Design System Agentic Skill (`apple-design-system`)

An agentic UI/UX skill synthesized from Apple's official **Human Interface Guidelines (HIG)**, engineered for Antigravity and AI coding agents.

This skill equips agents with deep knowledge of Apple's design philosophy, layout foundations, typography, component behaviors, touch ergonomics, and accessibility standards. Crucially, it provides **cross-platform translation frameworks** to bring Apple-grade design polish to **Modern Web (CSS/Tailwind/React)** and **Android (Jetpack Compose/Material 3)** without falling into the "uncanny valley" of direct platform imitation.

---

## Skill Architecture

```
apple-design-skill/
├── SKILL.md                          # Primary agent entrypoint & decision trees
├── references/
│   ├── foundations.md                # Spacing (8pt grid), 44pt touch targets, Dynamic Type, semantic colors, materials
│   ├── patterns.md                   # Navigation architectures, sheet detents, modals, search, empty states
│   ├── components.md                 # Buttons, navigation bars, toolbars, pickers, segmented controls, cards
│   ├── web-adaptation.md             # CSS/Tailwind translation, glassmorphism, spring physics, web ergonomics
│   ├── android-adaptation.md         # Jetpack Compose translation, Material 3 harmony, predictive back, haptics
│   └── audit-rubric.md               # Multi-platform UI/UX compliance scoring & audit checklist
├── scripts/
│   └── crawl_hig.py                  # Python crawler to index Apple's official HIG markdown endpoints
├── data/
│   └── raw/                          # Downloaded official HIG markdown source documents
├── README.md
└── .gitignore
```

---

## Features

- **Progressive Disclosure**: Built specifically for AI agents; structured so the agent only loads detailed references as needed during design and coding turns.
- **Apple HIG Core Principles**: Direct manipulation, aesthetic integrity, feedback, clarity, deference, and depth.
- **Web & Android Adaptation**: Complete guidance on adapting Apple aesthetic polish (materials, typography, spring physics, touch ergonomics) seamlessly into Web (Tailwind, React, CSS) and Android (Jetpack Compose, Kotlin) idioms.
- **Auditing & Code Review**: Ready-to-use rubrics for auditing existing screens, design files, or codebases against human interface standards.

---

## Installation

Symlink this repository into your global Antigravity skills directory:

```bash
mkdir -p ~/.gemini/config/skills
ln -s /home/richie/apple-design-skill ~/.gemini/config/skills/apple-design-system
```

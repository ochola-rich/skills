# Agentic Skills Collection

A curated library of production-grade agentic skills for AI coding assistants (Google Antigravity, Claude Code, OpenCode, and compatible agent runtimes).

This collection combines **Apple Human Interface Guidelines (HIG) engineering** with the complete suite of **WordPress Core, Plugin, Block, and WordPress Studio skills**.

---

## Skills Catalog

### 1. Design Systems & User Experience

| Skill | Description |
| :--- | :--- |
| **[`apple-design-system`](./apple-design-system/SKILL.md)** | Apple Human Interface Guidelines (HIG) cross-platform UI/UX engineering system. Enforces 8pt spatial grid, 44pt touch ergonomics, San Francisco typography, spring physics, and strict anti-slop rules across iOS, React Native, Modern Web, and Android. |
| **[`visual-design`](./visual-design/SKILL.md)** | Visual design, color palette harmony, and aesthetic alignment for WordPress sites and blocks. |
| **[`visual-polish`](./visual-polish/SKILL.md)** | High-fidelity visual refinement, optical balance, whitespace rhythm, and typography polish. |
| **[`wpds`](./wpds/SKILL.md)** | WordPress Design System component patterns, design tokens, and admin UI conventions. |

---

### 2. WordPress Architecture & Development

| Skill | Description |
| :--- | :--- |
| **[`wordpress-router`](./wordpress-router/SKILL.md)** | Deterministic codebase classifier and router for plugins, themes, block themes, and core checkouts. |
| **[`wp-plugin-development`](./wp-plugin-development/SKILL.md)** | Plugin architecture, hooks, Settings API, data storage, nonces, capabilities, sanitization, and release packaging. |
| **[`wp-block-development`](./wp-block-development/SKILL.md)** | Gutenberg block development: `block.json`, dynamic rendering, viewScriptModules, deprecations, and build tooling. |
| **[`wp-block-themes`](./wp-block-themes/SKILL.md)** | Block themes, `theme.json` styling hierarchy, template parts, and Site Editor troubleshooting. |
| **[`wp-interactivity-api`](./wp-interactivity-api/SKILL.md)** | WordPress Interactivity API: `data-wp-*` directives, store/actions state management, and SSR hydration. |
| **[`wp-patterns`](./wp-patterns/SKILL.md)** | Block patterns, Query Loop layouts, starter templates, and pattern registrations. |
| **[`wp-rest-api`](./wp-rest-api/SKILL.md)** | REST API route registration, `WP_REST_Controller` schemas, authentication, and permission callbacks. |
| **[`wp-abilities-api`](./wp-abilities-api/SKILL.md)** | Abilities API definitions, categories, metadata, and capability exposures for AI agents. |
| **[`wp-abilities-audit`](./wp-abilities-audit/SKILL.md)** | Plugin REST surface auditing and structured Abilities API rollout planning. |
| **[`wp-abilities-verify`](./wp-abilities-verify/SKILL.md)** | Verification of ability callbacks, adversarial read-only write checks, and schema validation. |

---

### 3. Tooling, Performance & Operations

| Skill | Description |
| :--- | :--- |
| **[`blueprint`](./blueprint/SKILL.md)** | WordPress Playground Blueprint JSON creation, schema validation, step sequencing, and debugging. |
| **[`wp-playground`](./wp-playground/SKILL.md)** | WordPress Playground CLI execution, browser previews, snapshots, mounts, and WebMCP integration. |
| **[`wp-env`](./wp-env/SKILL.md)** | Local Docker-based WordPress environment setup, configuration, and troubleshooting via `@wordpress/env`. |
| **[`wp-performance`](./wp-performance/SKILL.md)** | Performance profiling, SQL query optimization, object caching, autoloaded options, and cron auditing. |
| **[`wp-phpstan`](./wp-phpstan/SKILL.md)** | PHPStan static analysis configuration, neon rulesets, baselines, and WordPress typing. |
| **[`wp-project-triage`](./wp-project-triage/SKILL.md)** | Structured repository inspection, version compatibility checks, and tooling diagnostics. |
| **[`wp-wpcli-and-ops`](./wp-wpcli-and-ops/SKILL.md)** | WP-CLI automation, database search-replace, migrations, multisite, and server operations. |
| **[`wp-plugin-directory-guidelines`](./wp-plugin-directory-guidelines/SKILL.md)** | WordPress.org 18 directory guidelines, GPL compliance, Plugin Check (PCP), and security review. |

---

### 4. WordPress Studio & Automation

| Skill | Description |
| :--- | :--- |
| **[`site-spec`](./site-spec/SKILL.md)** | Structured site specification generation, architecture blueprints, and content planning. |
| **[`annotate`](./annotate/SKILL.md)** | Interactive visual annotation browser and design feedback coordination in WordPress Studio. |
| **[`block-content`](./block-content/SKILL.md)** | High-converting page copy, narrative structure, and block layout composition. |
| **[`imagery`](./imagery/SKILL.md)** | Media asset curation, contextual image generation briefs, and gallery placement. |
| **[`hosting-plans-helper`](./hosting-plans-helper/SKILL.md)** | Hosting capability assessment, plugin requirement mapping, and plan guidance. |
| **[`liberate`](./liberate/SKILL.md)** | Content extraction, site liberation, and format migration workflows. |
| **[`need-for-speed`](./need-for-speed/SKILL.md)** | Core Web Vitals optimization, asset minification, critical CSS, and caching headers. |
| **[`plugin-recommendations`](./plugin-recommendations/SKILL.md)** | Vetted plugin recommendations matched to site requirements with zero bloat. |
| **[`rank-me-up`](./rank-me-up/SKILL.md)** | Technical SEO audits, structured data schemas, sitemaps, and search ranking optimization. |
| **[`taxonomist`](./taxonomist/SKILL.md)** | Information architecture, taxonomy scripts, category trees, and hierarchical structuring. |
| **[`wpcom-remote-management`](./wpcom-remote-management/SKILL.md)** | Remote WordPress.com management via REST API endpoints and headless coordination. |

---

## Installation & Usage

### Linking into Antigravity CLI
To make all skills globally available to Antigravity CLI:
```bash
ln -s /path/to/skills/* ~/.gemini/config/skills/
```

### Linking into OpenCode / Claude Code
To make skills available to other agent platforms:
```bash
ln -s /path/to/skills/* ~/.agents/skills/
```

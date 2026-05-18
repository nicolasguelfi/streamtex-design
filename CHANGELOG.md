# Changelog

All notable changes to streamtex-design are documented in this file.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/);
versions follow semver pinned to the reuse architecture milestones.

## [0.1.0] — 2026-05-19 (Wave 1)

### Added
- Initial release as a Python pack (was: `streamtex-patterns` A2-markdown
  catalog). Conversion is part of Wave 1 of the StreamTeX reuse architecture
  refonte (see `streamtex/documentation/maintenance/reuse-architecture/PLAN.md`).
- Python package `streamtex_design/` with:
  - `_pack_manifest.toml` declaring `[manifest] format = "0.1"` (Q16 mouvant).
  - Entry point `streamtex.packs:streamtex-design` for runtime discovery.
  - 18 components across primitive / composition / block granularities
    (cf. PLAN §9.2): callout, cite, inline_emphasis, slide_heading,
    term_definition_list, card_grid, comparison_table, takeaways,
    title_slide, stat_hero, evidence_insight, exercise_flow,
    categorized_grid, narrative_transition, api_reference_card,
    composite_block, feature_walkthrough, manual_section.
  - 3 design systems: `default` (derived from styles_consolidated palette),
    `modern_dark`, `modern_light`.
  - 4 kits: `course-default`, `manual-default`, `project-default`,
    `slides-modern-dark`.
- pytest suite — 30 tests covering CV001-CV011 (components), DV001-DV006
  (design systems), KV001-KV005 (kits), PV001-PV010 (pack manifest).

### Renamed
- Repository renamed from `streamtex-patterns` to `streamtex-design`
  (GitHub + local). Old remote URLs auto-redirect.

### Deferred
- Conversion of the 14 block blueprints (cf. PLAN §9.3) is deferred to a
  follow-up commit — the 18 patterns above are sufficient to validate the
  architecture end-to-end.
- CLI templates (`cli_templates/`) and project blueprints
  (`project_blueprints/`) are scaffolded as empty directories; their
  population is planned for Wave 2 (Phase 2b sandbox integration).
- The legacy markdown catalogue (`core/`, `slides/`, `docs/`,
  `presets/`) is retained for historical reference. It will be archived in
  a future commit once the Python pack is the single source of truth.

"""
# Slide heading — Centered title at the top of a slide block

## Visual

```
                THE THREE PILLARS OF GREEN CHEMISTRY
                ─────────────────────────────────────
```

A bold, centered title that announces a slide. Optionally accompanied by an
underline rule or subtitle.

## Structure

- A `st_write(titles.slide, text)` line, centered.
- Optional thin underline or subtitle via `titles.subtitle`.

## Styling rules

| Element | Style |
|---|---|
| title | titles.slide |
| subtitle | titles.subtitle |

## Extrapolation rules

### INVARIANTS
- One title per slide; never two.
- Always at the visual top of the slide.

### PARAMS
- subtitle: optional secondary line
- align: center | left

### INTERDITS
- No inline emphasis inside the heading.
- No multi-line wraps for the main title.

## When to use

- The first content block of every slide.
- Section transition slides.

## When NOT to use

- Inside a callout (use callouts.title).
- For sub-section headings within a slide (use titles.section).

## Design system bundles required

- titles.slide
- titles.subtitle
"""

from streamtex import st_write

__component_meta__ = {
    "name": "slide_heading",
    "description": "Centered slide title (one per slide).",
    "tags": ["title", "heading", "slide"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": ["titles.slide", "titles.subtitle"],
    "granularity": "primitive",
}


def slide_heading(*, design_system, title: str = "", subtitle: str = "") -> None:
    """Render a slide-top heading + optional subtitle."""
    st_write(design_system.titles.slide, title)
    if subtitle:
        st_write(design_system.titles.subtitle, subtitle)

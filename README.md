# ⚠️ Archived — moved to nicolasguelfi/streamtex-packs

This repository has been **archived** as of 2026-05-20.

The pack now lives in the [`nicolasguelfi/streamtex-packs`](https://github.com/nicolasguelfi/streamtex-packs)
monorepo at the subdirectory [`streamtex-pack-design/`](https://github.com/nicolasguelfi/streamtex-packs/tree/main/streamtex-pack-design).

## Migration

Update your `pyproject.toml`:

```diff
- "streamtex-design @ git+https://github.com/nicolasguelfi/streamtex-design.git@v0.2.3"
+ "streamtex-pack-design @ git+https://github.com/nicolasguelfi/streamtex-packs.git@pack-design-v0.2.4#subdirectory=streamtex-pack-design"
```

The Python module name `streamtex_design` is **unchanged** — `from streamtex_design.components import ...` imports work as before.

For local development with editable installs:

```toml
[tool.uv.sources]
streamtex-pack-design = { path = "../streamtex-packs/streamtex-pack-design", editable = true }
```

## Migration history

The full migration is documented in
[streamtex/documentation/maintenance/pack_monorepo/PLAN.md](https://github.com/nicolasguelfi/streamtex/blob/main/documentation/maintenance/pack_monorepo/PLAN.md).

## License

This repo (at its archived state) is MIT-licensed. The new home in
`streamtex-packs` is BUSL-1.1 (aligned with the streamtex library).

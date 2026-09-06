# Self-hosted font provenance — Workstream F, Brand & Voice v2.0

Both families are SIL Open Font License 1.1 (`OFL.txt` in each subfolder). Per
`docs/brand-voice-guidelines-v2.0.md` §2: "Both Jost and Inter are SIL Open
Font License (OFL), freely available via Google Fonts, no restriction on
self-hosting or redistribution in any of the three projects."

## Jost

- Upstream source repository: https://github.com/indestructible-type/Jost
- Distributed via the Google Fonts canonical repository: https://github.com/google/fonts/tree/main/ofl/jost
- File fetched: `Jost[wght].ttf` (variable font, `wght` axis 100–900), commit `main` @ fetch time 2026-09-06
- License: SIL Open Font License 1.1, copyright The Jost Project Authors

## Inter

- Upstream source repository: https://www.github.com/rsms/inter
- Distributed via the Google Fonts canonical repository: https://github.com/google/fonts/tree/main/ofl/inter
- File fetched: `Inter[opsz,wght].ttf` (variable font, `opsz` axis 14–32, `wght` axis 100–900), commit `main` @ fetch time 2026-09-06
- License: SIL Open Font License 1.1, copyright The Inter Project Authors

## Local processing (this repo only — not a redistribution of a modified upstream release)

Per Brand & Voice v2.0 §2, only three weights are specified: Jost 500/600,
Inter 400/500/600. To avoid shipping the full variable-font weight/optical-size
range for weights the spec doesn't call for, each variable font was instanced
to static per-weight TTFs with `fontTools.varLib.instancer`, pinning Inter's
`opsz` axis to 14 (text optical size, correct for UI/body sizes), then
compressed to WOFF2 with `fontTools.ttlib.woff2`. No glyph subsetting was
performed — full Unicode coverage of the upstream font is preserved.

| File | Family | Weight | Style |
|---|---|---|---|
| `jost/Jost-Medium.woff2` | Jost | 500 | normal |
| `jost/Jost-SemiBold.woff2` | Jost | 600 | normal |
| `inter/Inter-Regular.woff2` | Inter | 400 | normal |
| `inter/Inter-Medium.woff2` | Inter | 500 | normal |
| `inter/Inter-SemiBold.woff2` | Inter | 600 | normal |

No italic styles were fetched — v2.0 §2 does not specify any italic use.

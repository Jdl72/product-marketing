# Discovery Term Dictionary

## Purpose

Normalize common transcript errors and domain terms so conversation records stay source-faithful without preserving obvious ASR mistakes.

Use this dictionary during `parse-single-conversation` and later discovery synthesis.

## Rules

- Correct only when the intended term is highly likely.
- Record the normalization in `term_normalization_notes`.
- Preserve the raw phrasing inside direct quotes when needed for fidelity, but normalize in interpretation fields.
- If the intended term is uncertain, leave it as heard and note the ambiguity.

## Current terms

| Heard in transcript | Normalize to | Notes |
| --- | --- | --- |
| `Pack roo`, `Packview`, `Pack View` | `Pacvue` | Competitor in retail media / commerce enablement |
| `amc`, `EMC` | `AMC` | Amazon Marketing Cloud |
| `dsp` | `DSP` | Demand-side platform |
| `acos` | `ACOS` | Advertising cost of sales |
| `asin`, `asins` | `ASIN`, `ASINs` | Amazon Standard Identification Number |
| `sds` | `Sponsored Display` or `SDs` | Normalize based on sentence context |

## Add terms when

- the same ASR mistake appears repeatedly
- a competitor, metric, or platform acronym is common in your market
- normalization materially improves downstream PMM usefulness

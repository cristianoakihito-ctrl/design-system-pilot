# Typography

## Purpose

Typography defines which font the screens use and how to load it.
Sizes, weights, line heights and letter spacing live in `/tokens/typography.json`.
Each component document says which of them it uses.

Status: defined on 2026-10-25, after two test screens loaded the font in
different ways (different weights, no fallback).

---

## Font family

| Token | Value |
| --- | --- |
| `font-family-Montserrat` | Montserrat |

Montserrat is the only font family of the Design System.

---

## Loading the font

Load Montserrat from Google Fonts, always with the five weights listed in
`/tokens/typography.json` (`font-weight`: 400, 500, 600, 700 and 800),
even when the screen uses fewer of them. Put the two lines in the `<head>`,
before any style:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

Rules:

- Do not load other weights, italics or other families.
- Keep `display=swap`: the text shows with the fallback font while Montserrat loads.
- Production products of the bank use their own font hosting. Google Fonts is the
  source for screens, prototypes and examples made with this repository.

---

## Fallback

When Montserrat cannot load, the text uses the system font of the device:

```css
body {
  font-family: var(--pbcon-font-family-Montserrat), -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
```

Components inherit the family from the page (`font-family: inherit` on buttons).
Do not repeat the family inside components.

---

## Token sources

- Typography: `/tokens/typography.json`

---

## Documentation status

Decided (2026-10-25):

- Montserrat loaded from Google Fonts with the five token weights
- Fallback to the system font

Pending:

- Text styles by role (for example the screen title) are not defined yet

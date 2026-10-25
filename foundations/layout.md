# Layout

## Purpose

Layout defines the space around the components of a screen: how far the
content stays from the edges of the screen, how wide it can get and how
far the screen title stays from the content.

Components define their own inner space (see `/components/`). This document
only covers the page that holds them.

Values live in `/tokens/spacing.json`.

Status: defined on 2026-10-25, after a test screen (card FAQ) showed that the
page around the components was not defined. `layout-max-width` is registered in
Figma (`Spacing/Layout/layout-max-width`). The other values reuse existing tokens.

---

## Screen ranges

| Range | Screen width | Side margin (each side) | Content width |
| --- | --- | --- | --- |
| Mobile | `breakpoints-mobile-min-width` (320) to `breakpoints-mobile-max-width` (430) | `padding-XL` (16) | screen minus 32 |
| Tablet and Desktop | 431 to 1264 | `padding-MAX` (32) | screen minus 64 |
| Wide Desktop | above 1264 | what is left, content centered | `layout-max-width` (1200) |

1264 is `layout-max-width` plus the Desktop side margins (1200 + 32 + 32).
`layout-max-width` only takes effect in the Wide Desktop range.

---

## Page spacing

| Space | Mobile | Desktop/tablet |
| --- | --- | --- |
| Side margin | `padding-XL` (16) | `padding-MAX` (32) |
| Top margin | `padding-XL` (16) | `padding-MAX` (32) |
| Bottom margin | `padding-XL` (16) | `padding-MAX` (32) |
| Space between screen title and content | `gap-XS` (16) | `gap-SM` (24) |

Rules:

- Margins are inner space of the page container, so they use `padding-*`.
- The space between the title and the content is space between two elements, so it uses `gap-*`.
- The margin is the same on all four sides of the page.

---

## Page colors

| Property | Token |
| --- | --- |
| Page background | `pbcon-color-bg-neutral-default` (#FFFFFF) |
| Default text color | `pbcon-color-text-neutral-high` (#000000) |

Rules:

- These are defaults for the page. A component that defines its own colors in
  `/components/` uses its own colors, never the page defaults.
- Text that is not inside a component (for example the screen title) inherits the default text color.

---

## Screen title

Not defined. The title style per device will be defined later.

Until then:

- Do not invent a size, weight or color for the screen title.
- Use a heading element (`h1`) and inherit the page font and the default text color.
- List the screen title as "not defined" when delivering a screen.

---

## Reference implementation

```css
body {
  margin: 0;
  background: var(--pbcon-color-bg-neutral-default);
  color: var(--pbcon-color-text-neutral-high);
  font-family: var(--pbcon-font-family-Montserrat), -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
.page {
  box-sizing: content-box;
  max-width: var(--pbcon-layout-max-width);
  margin: 0 auto;
  padding: var(--pbcon-padding-MAX);
  display: flex;
  flex-direction: column;
  gap: var(--pbcon-gap-SM);
}
.page-title { margin: 0; }
@media (max-width: 430px) {
  .page { padding: var(--pbcon-padding-XL); gap: var(--pbcon-gap-XS); }
}
```

`box-sizing: content-box` keeps the padding outside the 1200, so the content
is 1200 wide and the page needs 1264 to show it without shrinking.
Media queries cannot read CSS variables: the `430px` must match `breakpoints-mobile-max-width`.

---

## Token sources

- Spacing, breakpoints and layout: `/tokens/spacing.json`
- Page colors: `/tokens/colors/semantic.json`
- Font loading and fallback: `/foundations/typography.md`

---

## Documentation status

Decided (2026-10-25):

- Screen ranges, page margins (same on all four sides), space between title and content
- Page background and default text color

Provisional:

- `layout-max-width` (1200): validate against the real container of the site and landing pages

Pending:

- Screen title style per device

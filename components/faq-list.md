# FAQ list

Also known as: Accordion list.

## Figma source

The Figma component is the visual source of truth.

Figma component name: `FAQ list` (component set with a `Device` property).

This document describes how FAQ list must be composed using the
Design System tokens and the FAQ item component (`/components/faq-item.md`).

---

## Purpose

FAQ list stacks FAQ items vertically and owns the space between them.

It exists so a single FAQ item never has to know about its neighbors:
the list sets the gap and, when needed, the rule for how many items can be
expanded at the same time.

---

## When to use

- Show two or more FAQ items one after another.
- Build a flat FAQ page or section, with no groups.

## When not to use

- Do not use for a single FAQ item (use FAQ item alone).
- Do not use for groups of questions with their own titles (a FAQ category is planned and not documented yet).
- Do not mix other components inside the list.

---

## Anatomy

FAQ list consists of:

1. Container (the list)
2. FAQ items, stacked vertically

---

## Variants

| Property | Values |
| --- | --- |
| Device | `Desktop/tablet`, `Mobile` |

Each `Device` value uses the FAQ item with the matching device
(`Desktop/tablet` or `Mobile`). All items inside the list use the same device.

---

## Layout

### Container

- Direction: vertical
- Gap between items: `gap-XS` (16), on Desktop and on Mobile
- Padding: none
- Width: fills the available width; the Figma widths (925px and 328px) are
  demonstration widths, not component rules
- Height: hugs its content

### Space ownership

- The list owns the space between items. FAQ item has no outer margin.
- The gap follows the Design System rule: space between two elements uses `gap-*`.
- When an item expands or collapses, the items below it move with it and the gap stays 16.

---

## Behavior

- Each item toggles on its own (see `/components/faq-item.md`, section Behavior).

Proposed (not defined in Figma, needs design approval):

- More than one item may stay expanded at the same time. This is the default.
- Single-expanded mode is optional: opening an item collapses the others,
  using the same collapse motion as FAQ item.
- All items start collapsed. A list may start with one item expanded when
  the first answer is the most relevant one.

---

## Accessibility

- The container is a list (`ul`) and each FAQ item is a list item (`li`).
- Keep the same heading level for every item title in the list.
- Keyboard: `Tab` moves between item headers; `Enter` and `Space` toggle the focused item.
  Arrow keys are not required.
- All other requirements are in `/components/faq-item.md`, section Accessibility.

---

## Reference implementation (web)

A working example with both devices: `/examples/faq-item.html`.

### Markup

```html
<ul class="faq-list">
  <li class="faq-item"><!-- see /components/faq-item.md --></li>
  <li class="faq-item"><!-- see /components/faq-item.md --></li>
</ul>
```

### CSS

```css
.faq-list { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: var(--pbcon-gap-XS); }
```

The CSS is the same on Desktop/tablet and Mobile.

---

## Token sources

### Spacing

`/tokens/spacing.json`

---

## Documentation status

Confirmed:

- Anatomy
- Device variants
- Vertical layout and gap `gap-XS` (16) on both devices
- No padding on the container

Proposed (not defined in Figma, needs design approval):

- Multiple expanded items by default, single-expanded as an option
- All items start collapsed

Pending:

- The Figma component description is empty.
- FAQ category (groups of items with their own titles) is not documented yet.

# FAQ item

Also known as: Accordion.

## Figma source

The Figma component is the visual source of truth.

Figma component name: `FAQ item` (component set with `Device` and `State` properties).

This document describes how FAQ item must be composed using the
Design System tokens and assets available in this repository.

---

## Purpose

FAQ item shows a short question or title and hides its supporting
content until the user expands it.

It reduces the length of pages with many items of reference content,
such as FAQs, letting the user scan titles and open only what matters.

---

## When to use

- Group frequently asked questions.
- Present secondary or reference content that not every user needs.
- Organize long content into scannable sections.

## When not to use

- Do not use for content every user must read to complete a task.
- Do not use for critical alerts or errors (use Alert Card).
- Do not nest a FAQ item inside another FAQ item.
- Do not use when there is only one short piece of content to show.

---

## Anatomy

FAQ item consists of:

1. Container
2. Header (title and icon)
3. Title
4. Toggle icon container
5. Toggle icon
6. Content (visible only when expanded)

---

## Variants

| Property | Values |
| --- | --- |
| Device | `Desktop/tablet`, `Mobile` |
| State | `Default` (collapsed), `Expanded` |

Use one FAQ item implementation for all variants.
Do not create independent desktop and mobile components.

---

## Shared layout

### Container

- Border width: `border-width-XS`
- Border color: `pbcon-color-border-default-low`
- Border radius: `border-radius-MD`
- Background: none defined in Figma (inherits the surface)
- Direction: vertical
- Width: fills the available width of its parent

### Header

- Direction: horizontal
- Alignment: center
- Padding: `padding-none`
- Title fills the remaining width; the icon keeps its size

### Toggle icon container

- Background: `pbcon-color-fg-brand-primary-medium` (Desktop/tablet)
- Icon color: `pbcon-color-icon-brand-primary-high`

---

## Device: Desktop/tablet

### Container spacing

- Horizontal padding: `padding-XXL`
- Vertical padding: `padding-XL`
- Gap between header and content: `padding-XXL`

### Header

- Gap between title and icon: `margin-spacing-SM`

### Toggle icon container

- Padding: `padding-SM`
- Border radius: `border-radius-SM`
- Icon size: 24 x 24

### Typography

- Title: `body-LG-700` (font-size `17`, weight `700`, line-height `17-150`, letter-spacing `0.4`)
- Content: `body-LG-400` (font-size `17`, weight `400`, line-height `17-150`, letter-spacing `0.4`)
- Color: `pbcon-color-text-neutral-high`

---

## Device: Mobile

### Container spacing

- Padding: `padding-XL` (all sides)
- Gap between header and content (Expanded): `padding-XL`

### Header

- Gap between title and icon: `margin-spacing-XS`

### Toggle icon container

- Background: `pbcon-color-bg-brand-primary-medium`
- Padding, border radius and icon size: see Documentation status (pending)

### Typography

- Title: `body-SM-700` (font-size `12`, weight `700`, line-height `12-150`, letter-spacing `0.4`)
- Content: `body-SM-400` (font-size `12`, weight `400`, line-height `12-150`, letter-spacing `0.4`)
- Color: `pbcon-color-text-neutral-high`

---

## States

### Default (collapsed)

- Shows the header only.
- Toggle icon: `actions-basic-plus.svg`

### Expanded

- Shows the header and the content.
- Toggle icon: `actions-basic-minus.svg`

The change between states is animated. See Motion.

Hover, focus, pressed and disabled states are not defined in Figma.

---

## Behavior

- Selecting the header toggles between Default and Expanded.
- Content wraps naturally according to the available width.
- Whether more than one item may stay expanded at the same time is not defined.
- Whether any item starts expanded is not defined.

---

## Motion

Status: decided on 2026-10-24 (option C of the motion comparison). Not yet registered in the Figma component.
Values come from `/tokens/motion.json` and follow the references listed
in Motion references. The expand curve comes from the FAQ of the PB Soma+ landing page.
General motion rules and every motion token: `/foundations/motion.md`.

### Principles

- Motion explains the change: the panel grows from the header and the
  content settles into place.
- The panel starts moving on the first frame after the tap and then settles: no slow start.
- Fast enough that nobody waits for it: nothing lasts longer than `duration-LG` (300ms).
- Collapsing is shorter than expanding.
- Transitions are interruptible: selecting the header during an
  animation reverses it from the current position, without jumps.
- Items that are already expanded on first render appear expanded, without animation.

### Expand (Default to Expanded)

| Element | Change | Duration | Delay | Easing |
| --- | --- | --- | --- | --- |
| Panel | height from 0 to content height | `duration-LG` (300ms) | none | `easing-soft-decelerate` |
| Content | opacity 0 to 1, moves from `-padding-SM` to 0 on the Y axis | `duration-MD` (200ms) | `duration-XXS` (50ms) | `easing-standard-decelerate` |
| Plus icon | opacity 1 to 0, rotates 0 to 90 degrees | `duration-MD` (200ms) | none | `easing-standard` |
| Minus icon | opacity 0 to 1, rotates -90 to 0 degrees | `duration-MD` (200ms) | none | `easing-standard` |

### Collapse (Expanded to Default)

| Element | Change | Duration | Delay | Easing |
| --- | --- | --- | --- | --- |
| Content | opacity 1 to 0 | `duration-XS` (100ms) | none | `easing-standard-accelerate` |
| Panel | height from content height to 0 | `duration-MD` (200ms) | none | `easing-standard` |
| Icons | reverse of Expand | `duration-MD` (200ms) | none | `easing-standard` |
| Panel | becomes hidden to assistive technology and keyboard | instant | `duration-MD` (200ms) | none |

### Reduced motion

When the user asks for less motion (`prefers-reduced-motion: reduce` on the web,
Reduce Motion on iOS, Remove animations on Android):

- The panel height changes instantly.
- Nothing moves or rotates.
- Content and icons change with an opacity fade only: `duration-XS` (100ms), `easing-linear`.

Do not remove the fade: the change of state still needs to be perceived.

### Toggle icon motion

Plus and minus are two official assets stacked in the same slot.
The plus fades out while rotating; the minus fades in while rotating into place.

Do not morph or edit the SVG paths of the assets.

### Implementation rules for motion (web)

- Animate the height with CSS grid rows (`grid-template-rows: 0fr` to `1fr`).
  It works in Chrome 107+, Edge 107+, Firefox 66+ and Safari 16+.
- Do not depend on `interpolate-size` or `calc-size()`: they are not available in Safari (including iOS) or Firefox.
- Do not animate `max-height` and do not measure the content with JavaScript.
- Use CSS transitions, not keyframe animations: transitions reverse from the current value when interrupted.
- Keep the gap between header and content inside the animated panel, so it collapses together.
- Drive every animation from the same attributes used for accessibility:
  `aria-expanded` on the header button and `data-state="open|closed"` on the panel.
- Collapsed content must not be reachable by keyboard or screen readers:
  `visibility: hidden` after the collapse ends.
- Use the motion tokens. Do not hardcode durations or easings.

### Reference implementation

The markup, the state handling and the CSS that implement this motion are in Reference implementation (web).

### Platform mapping

Use the same values on native platforms.

| Token | Web | iOS (SwiftUI) | Android (Compose) | Flutter |
| --- | --- | --- | --- | --- |
| `easing-standard` | `cubic-bezier(0.2, 0, 0, 1)` | `.timingCurve(0.2, 0, 0, 1, duration:)` | `CubicBezierEasing(0.2f, 0f, 0f, 1f)` | `Cubic(0.2, 0, 0, 1)` |
| `easing-soft-decelerate` | `cubic-bezier(0.22, 0.61, 0.36, 1)` | `.timingCurve(0.22, 0.61, 0.36, 1, duration:)` | `CubicBezierEasing(0.22f, 0.61f, 0.36f, 1f)` | `Cubic(0.22, 0.61, 0.36, 1)` |
| `easing-standard-decelerate` | `cubic-bezier(0, 0, 0, 1)` | `.timingCurve(0, 0, 0, 1, duration:)` | `CubicBezierEasing(0f, 0f, 0f, 1f)` | `Cubic(0, 0, 0, 1)` |
| `easing-standard-accelerate` | `cubic-bezier(0.3, 0, 1, 1)` | `.timingCurve(0.3, 0, 1, 1, duration:)` | `CubicBezierEasing(0.3f, 0f, 1f, 1f)` | `Cubic(0.3, 0, 1, 1)` |
| `duration-LG` | `300ms` | `0.3` | `tween(durationMillis = 300)` | `Duration(milliseconds: 300)` |

Example, iOS (expand): `withAnimation(.timingCurve(0.22, 0.61, 0.36, 1, duration: 0.3)) { isExpanded = true }`

Example, iOS (collapse): `withAnimation(.timingCurve(0.2, 0, 0, 1, duration: 0.2)) { isExpanded = false }`

Example, Android: `AnimatedVisibility(visible = expanded, enter = expandVertically(tween(300, easing = CubicBezierEasing(0.22f, 0.61f, 0.36f, 1f))) + fadeIn(tween(200, 50, CubicBezierEasing(0f, 0f, 0f, 1f))), exit = shrinkVertically(tween(200, easing = CubicBezierEasing(0.2f, 0f, 0f, 1f))) + fadeOut(tween(100, easing = CubicBezierEasing(0.3f, 0f, 1f, 1f))))`

## Reference implementation (web)

A working example with both devices and the motion: `/examples/faq-item.html`
(open it in a browser and resize the window below 430px to see the Mobile variant).

One implementation covers both devices: `Desktop/tablet` by default and `Mobile`
up to `breakpoints-mobile-max-width` (430px).
Media queries cannot read CSS custom properties, so the breakpoint value is written
in the `@media` rule; keep it equal to `/tokens/spacing.json`.

CSS custom properties use the `--pbcon-` prefix followed by the token path
(for example `duration-LG` in `/tokens/motion.json` is `--pbcon-motion-duration-LG`).

### Markup

```html
<li class="faq-item">
  <h3>
    <button type="button" class="faq-trigger" id="faq-h1"
            aria-expanded="false" aria-controls="faq-c1">
      <span class="faq-title">Question</span>
      <span class="faq-icon">
        <span class="faq-icon-plus"><!-- actions-basic-plus.svg, inline, aria-hidden="true" --></span>
        <span class="faq-icon-minus"><!-- actions-basic-minus.svg, inline, aria-hidden="true" --></span>
      </span>
    </button>
  </h3>
  <div class="faq-panel" id="faq-c1" role="region"
       aria-labelledby="faq-h1" data-state="closed">
    <div class="faq-clip">
      <div class="faq-content">Answer</div>
    </div>
  </div>
</li>
```

### State

```js
trigger.addEventListener('click', () => {
  const open = trigger.getAttribute('aria-expanded') !== 'true';
  trigger.setAttribute('aria-expanded', String(open));
  panel.setAttribute('data-state', open ? 'open' : 'closed');
});
```

### CSS

Inline SVG icons use `fill="currentColor"`; the icon color comes from
`pbcon-color-icon-brand-primary-high` on the icon element.
The header button resets the browser button styles (`appearance`, `border`, `background`, `font`).

```css
.faq-item { padding: var(--pbcon-padding-XL) var(--pbcon-padding-XXL); border: var(--pbcon-border-width-XS) solid var(--pbcon-color-border-default-low); border-radius: var(--pbcon-border-radius-MD); }
.faq-item > h3, .faq-item > h2 { margin: 0; }
.faq-trigger { appearance: none; border: none; background: transparent; cursor: pointer; font-family: inherit; color: inherit; display: flex; align-items: center; width: 100%; justify-content: flex-start; gap: var(--pbcon-margin-spacing-SM); padding: var(--pbcon-padding-XS) var(--pbcon-padding-none); margin: calc(-1 * var(--pbcon-padding-XS)) 0; text-align: left; }
.faq-trigger:focus-visible { outline: var(--pbcon-border-width-SM) solid var(--pbcon-color-border-brand-primary-high); outline-offset: var(--pbcon-border-width-SM); }
.faq-title { flex-grow: 1; min-width: 0; font-size: var(--pbcon-font-size-17); font-weight: var(--pbcon-font-weight-700); line-height: var(--pbcon-line-height-17-150); letter-spacing: var(--pbcon-letter-spacing-0-4); color: var(--pbcon-color-text-neutral-high); }
.faq-icon { display: flex; flex-shrink: 0; padding: var(--pbcon-padding-SM); border-radius: var(--pbcon-border-radius-SM); background: var(--pbcon-color-fg-brand-primary-medium); }
.faq-icon-minus { top: var(--pbcon-padding-SM); left: var(--pbcon-padding-SM); }
.faq-content { padding-top: var(--pbcon-padding-XXL); font-size: var(--pbcon-font-size-17); font-weight: var(--pbcon-font-weight-400); line-height: var(--pbcon-line-height-17-150); letter-spacing: var(--pbcon-letter-spacing-0-4); color: var(--pbcon-color-text-neutral-high); }
@media (max-width: 430px) {
  .faq-item { padding: var(--pbcon-padding-XL); }
  .faq-trigger { gap: var(--pbcon-margin-spacing-XS); }
  .faq-title { font-size: var(--pbcon-font-size-12); line-height: var(--pbcon-line-height-12-150); }
  .faq-icon { padding: 6.4px; border-radius: 6.4px; background: var(--pbcon-color-bg-brand-primary-medium); }
  .faq-icon-minus { top: 6.4px; left: 6.4px; }
  .faq-icon svg { width: 19.2px; height: 19.2px; }
  .faq-content { padding-top: var(--pbcon-padding-XL); font-size: var(--pbcon-font-size-12); line-height: var(--pbcon-line-height-12-150); }
}
.faq-icon { position: relative; }
.faq-icon-plus, .faq-icon-minus { display: block; transition: opacity var(--pbcon-motion-duration-MD) var(--pbcon-motion-easing-standard), transform var(--pbcon-motion-duration-MD) var(--pbcon-motion-easing-standard); }
.faq-icon-minus { position: absolute; opacity: 0; transform: rotate(-90deg); }
.faq-trigger[aria-expanded="true"] .faq-icon-plus { opacity: 0; transform: rotate(90deg); }
.faq-trigger[aria-expanded="true"] .faq-icon-minus { opacity: 1; transform: rotate(0deg); }
.faq-panel { display: grid; grid-template-rows: 0fr; visibility: hidden; transition: grid-template-rows var(--pbcon-motion-duration-MD) var(--pbcon-motion-easing-standard), visibility 0s linear var(--pbcon-motion-duration-MD); }
.faq-panel[data-state="open"] { grid-template-rows: 1fr; visibility: visible; transition: grid-template-rows var(--pbcon-motion-duration-LG) var(--pbcon-motion-easing-soft-decelerate), visibility 0s linear 0s; }
.faq-clip { min-height: 0; overflow: hidden; }
.faq-content { opacity: 0; transform: translateY(calc(-1 * var(--pbcon-padding-SM))); transition: opacity var(--pbcon-motion-duration-XS) var(--pbcon-motion-easing-standard-accelerate), transform var(--pbcon-motion-duration-XS) var(--pbcon-motion-easing-standard-accelerate); }
.faq-panel[data-state="open"] .faq-content { opacity: 1; transform: none; transition: opacity var(--pbcon-motion-duration-MD) var(--pbcon-motion-easing-standard-decelerate) var(--pbcon-motion-duration-XXS), transform var(--pbcon-motion-duration-MD) var(--pbcon-motion-easing-standard-decelerate) var(--pbcon-motion-duration-XXS); }
@media (prefers-reduced-motion: reduce) {
  .faq-panel, .faq-panel[data-state="open"] { transition: none; }
  .faq-content, .faq-panel[data-state="open"] .faq-content { transform: none; transition: opacity var(--pbcon-motion-duration-XS) var(--pbcon-motion-easing-linear); }
  .faq-icon-plus, .faq-icon-minus, .faq-trigger[aria-expanded="true"] .faq-icon-plus, .faq-trigger[aria-expanded="true"] .faq-icon-minus { transform: none; transition: opacity var(--pbcon-motion-duration-XS) var(--pbcon-motion-easing-linear); }
}
```

---

## Accessibility

- The header is the interactive element, not the whole container.
- Header element: `button`, with `aria-expanded="true|false"`.
- The header controls the content region through `aria-controls`.
- The content region has `role="region"` and `aria-labelledby` pointing to the header.
- Keyboard: `Enter` and `Space` toggle the item; `Tab` moves between headers.
- The toggle icon is decorative (`aria-hidden="true"`); the state is
  communicated by `aria-expanded`.
- When used for FAQs, the title should be written as a question.
- Respect the reduced motion preference (see Motion).
- Touch area: the header button extends its hit area by `padding-XS` above and below,
  with a matching negative margin, so it reaches at least 44px on Mobile without changing the layout.

---

## Responsive behavior

- Use `Device=Mobile` inside the mobile breakpoint
  (`breakpoints-mobile-min-width` to `breakpoints-mobile-max-width`).
- Use `Device=Desktop/tablet` above it.
- Switch by the viewport width with one implementation (see Reference implementation (web)).
- The fixed widths of the Figma instances (925px and 328px) are
  demonstration widths, not component rules.

---

## Content rules

- Keep titles short; prefer one or two lines.
- The title must describe the content it reveals.
- Content may contain paragraphs; do not place another FAQ item inside it.
- Do not truncate the title.

---

## Token sources

### Semantic colors

`/tokens/colors/semantic.json`

### Global colors

`/tokens/colors/global.json`

### Typography

`/tokens/typography.json`

### Spacing and border radius

`/tokens/spacing.json`

### Motion

`/tokens/motion.json` (rules in `/foundations/motion.md`)

### Icons

`/assets/icons/`

---

## Token resolution

Always prefer the highest available Design System abstraction.

Priority:

1. Component token
2. Semantic token
3. Global token

FAQ item has no component tokens yet; use the semantic tokens listed above.

Do not hardcode resolved values when a corresponding token exists.

---

## Asset dependencies

- `actions-basic-plus.svg` (Default)
- `actions-basic-minus.svg` (Expanded)

Do not:

- draw replacement icons
- use emoji
- use external icon libraries when an official icon exists
- replace plus/minus with chevrons without a Figma change

If the required official asset is not available in `/assets/icons/`,
report the missing dependency instead of inventing one.

---

## Implementation rules

- Use the documented Design System tokens.
- Do not hardcode values when an official token exists.
- Do not invent spacing, colors, typography, radius, shadows, durations or easings.
- Preserve the documented component anatomy.
- Use one FAQ item implementation for all Device and State variants.
- Use the Figma component as the visual source of truth.
- Use this document as the implementation contract.
- If a required value is not documented, do not infer it.
- Report missing information or dependencies instead.

---

## Motion references

- Material Design 3 motion tokens (easing and duration values):
  https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md
- IBM Carbon motion (productive motion for revealing information; standard easing when the element stays visible):
  https://carbondesignsystem.com/elements/motion/overview/
- Atlassian Design System, applying motion (exits shorter than entrances):
  https://atlassian.design/foundations/motion/applying-motion
- FAQ of the PB Soma+ landing page (expand curve adopted: `cubic-bezier(0.22, 0.61, 0.36, 1)`, 300ms).
- Radix UI Accordion (height animation driven by `data-state`):
  https://www.radix-ui.com/primitives/docs/components/accordion
- Apple, reduced motion evaluation criteria (replace meaningful motion with a fade, do not remove it):
  https://developer.apple.com/help/app-store-connect/manage-app-accessibility/reduced-motion-evaluation-criteria
- Microsoft Fluent 2 motion (duration proportional to size; no-motion setting):
  https://fluent2.microsoft.design/motion
- Browser support for animating grid rows:
  https://web.dev/articles/css-animated-grid-layouts
- Browser support for `interpolate-size`:
  https://caniuse.com/mdn-css_properties_interpolate-size_allow-keywords

---

## Documentation status

Confirmed:

- Anatomy
- Device and State variants
- Container tokens
- Desktop/tablet spacing, icon container and typography tokens
- Mobile container spacing and typography tokens
- Toggle icons
- Content typography `body-LG-400` / `body-SM-400` (updated in Figma)

Decided (2026-10-24), not yet registered in Figma:

- Motion (option C) and the tokens in `/tokens/motion.json`

Proposed (not defined in Figma, needs design approval):

- Header hit area extension (no visual change)

Pending:

- Mobile toggle icon container uses values without tokens in Figma
  (padding 6.4px, border radius 6.4px, icon 19.2 x 19.2). Define tokens
  or align with Desktop/tablet (`padding-SM`, `border-radius-SM`, 24 x 24).
- Toggle icon container background uses a different token per device
  (`pbcon-color-fg-brand-primary-medium` on Desktop/tablet,
  `pbcon-color-bg-brand-primary-medium` on Mobile). Both resolve to the
  same value; choose one.
- In Figma the whole container is the button. For accessibility only the
  header should be interactive.
- Spacing between consecutive FAQ items is not defined.
- Hover, focus, pressed and disabled states.
- Single or multiple expanded items.

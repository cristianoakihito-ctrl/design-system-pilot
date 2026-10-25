# Motion

## Purpose

Motion explains what changed on the screen: something opened, closed,
appeared or moved. It must help the user follow the change, never decorate it.

Values live in `/tokens/motion.json`. This document explains when to use each one.

Status: defined on 2026-10-24 together with the FAQ item component.
Motion is not registered in the Figma file, by decision. This repository is the source of truth:
Figma prototypes cannot reproduce the full motion (staggered content fade, icon rotation, height by grid rows).

---

## Principles

- Purposeful: animate only changes the user needs to follow.
- Fast: interface motion stays between `duration-XS` (100ms) and `duration-XL` (400ms).
- Responsive: motion started by the user moves on the first frame after the tap or click.
- Shorter on the way out: closing, hiding and exiting are faster than opening and entering.
- Interruptible: a new action during an animation continues from the current position, without jumps.
- Quiet on load: content that is already in its final state on first render does not animate.
- Inclusive: respect the reduced motion preference (see Reduced motion).

---

## Duration tokens

| Token | Value | Use |
| --- | --- | --- |
| `duration-none` | 0ms | Instant change; reduced motion |
| `duration-XXS` | 50ms | Small delays to stagger related changes |
| `duration-XS` | 100ms | Fades of small elements; content leaving; reduced motion fades |
| `duration-SM` | 150ms | Small state changes (not used by a component yet) |
| `duration-MD` | 200ms | Icons; collapsing; elements leaving |
| `duration-LG` | 300ms | Expanding panels and containers |
| `duration-XL` | 400ms | Large surfaces (not used by a component yet) |

Larger elements and longer distances take longer durations.
Do not go above `duration-XL` for interface feedback.

---

## Distance tokens

How far an element travels while it enters or leaves. Use these instead of spacing tokens.

| Token | Value | Use |
| --- | --- | --- |
| `distance-XS` | 4px | Reserved for very small movements (not used yet) |
| `distance-SM` | 8px | Content entering below its header (FAQ item) |
| `distance-MD` | 16px | Reserved for larger entrances (not used yet) |

---

## Easing tokens

| Token | Value | Use |
| --- | --- | --- |
| `easing-standard` | `cubic-bezier(0.2, 0, 0, 1)` | Elements that stay on screen and change size or position; collapsing; icon changes |
| `easing-soft-decelerate` | `cubic-bezier(0.22, 0.61, 0.36, 1)` | Expansions started by the user: moves on the first frame and settles smoothly |
| `easing-standard-decelerate` | `cubic-bezier(0, 0, 0, 1)` | Content entering the screen |
| `easing-standard-accelerate` | `cubic-bezier(0.3, 0, 1, 1)` | Content leaving the screen |
| `easing-emphasized-decelerate` | `cubic-bezier(0.05, 0.7, 0.1, 1)` | Reserved for larger, more expressive entrances (not used yet) |
| `easing-emphasized-accelerate` | `cubic-bezier(0.3, 0, 0.8, 0.15)` | Reserved for larger, more expressive exits (not used yet) |
| `easing-linear` | `cubic-bezier(0, 0, 1, 1)` | Opacity fades in reduced motion; constant-rate changes |

Do not use `ease`, `ease-in-out` or custom curves directly in components.
If a new curve is needed, add it to `/tokens/motion.json` first and document it here.

---

## Reduced motion

When the user asks for less motion (`prefers-reduced-motion: reduce` on the web,
Reduce Motion on iOS, Remove animations on Android):

- Size and position changes happen instantly.
- Nothing moves, rotates or scales.
- Changes that carry meaning keep a short opacity fade: `duration-XS` with `easing-linear`.

Do not remove the fade entirely: the user still needs to perceive that something changed.

---

## Implementation rules (web)

- Use CSS transitions driven by state attributes (for example `aria-expanded` and `data-state`).
  Transitions reverse from the current value when interrupted.
- Animate `transform` and `opacity` whenever possible. When a height must animate,
  use CSS grid rows (`grid-template-rows: 0fr` to `1fr`), never `max-height` with an arbitrary limit.
- Do not use `transition: all`.
- Do not depend on `interpolate-size` or `calc-size()`: not available in Safari (including iOS) or Firefox.
- CSS custom properties use the `--pbcon-` prefix followed by the token path:
  `duration-LG` is `--pbcon-motion-duration-LG`, `easing-standard` is `--pbcon-motion-easing-standard`.

---

## Platform mapping

| Token | Web | iOS (SwiftUI) | Android (Compose) | Flutter |
| --- | --- | --- | --- | --- |
| `easing-standard` | `cubic-bezier(0.2, 0, 0, 1)` | `.timingCurve(0.2, 0, 0, 1, duration:)` | `CubicBezierEasing(0.2f, 0f, 0f, 1f)` | `Cubic(0.2, 0, 0, 1)` |
| `easing-soft-decelerate` | `cubic-bezier(0.22, 0.61, 0.36, 1)` | `.timingCurve(0.22, 0.61, 0.36, 1, duration:)` | `CubicBezierEasing(0.22f, 0.61f, 0.36f, 1f)` | `Cubic(0.22, 0.61, 0.36, 1)` |
| `easing-standard-decelerate` | `cubic-bezier(0, 0, 0, 1)` | `.timingCurve(0, 0, 0, 1, duration:)` | `CubicBezierEasing(0f, 0f, 0f, 1f)` | `Cubic(0, 0, 0, 1)` |
| `easing-standard-accelerate` | `cubic-bezier(0.3, 0, 1, 1)` | `.timingCurve(0.3, 0, 1, 1, duration:)` | `CubicBezierEasing(0.3f, 0f, 1f, 1f)` | `Cubic(0.3, 0, 1, 1)` |
| `easing-linear` | `linear` | `.linear(duration:)` | `LinearEasing` | `Curves.linear` |
| `duration-MD` | `200ms` | `0.2` | `tween(durationMillis = 200)` | `Duration(milliseconds: 200)` |
| `duration-LG` | `300ms` | `0.3` | `tween(durationMillis = 300)` | `Duration(milliseconds: 300)` |

Reduced motion on native platforms: `@Environment(\.accessibilityReduceMotion)` in SwiftUI,
`Settings.Global.ANIMATOR_DURATION_SCALE` equal to 0 on Android, `MediaQuery.disableAnimationsOf(context)` in Flutter.

---

## Components using motion

| Component | Motion |
| --- | --- |
| FAQ item | `/components/faq-item.md`, section Motion |

---

## References

- Material Design 3 motion tokens (easing and duration values):
  https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md
- IBM Carbon motion (productive motion; ease-out on user input):
  https://carbondesignsystem.com/elements/motion/overview/
- Atlassian Design System, applying motion (exits shorter than entrances):
  https://atlassian.design/foundations/motion/applying-motion
- Microsoft Fluent 2 motion (duration proportional to size):
  https://fluent2.microsoft.design/motion
- Apple, reduced motion evaluation criteria:
  https://developer.apple.com/help/app-store-connect/manage-app-accessibility/reduced-motion-evaluation-criteria
- FAQ of the PB Soma+ landing page (origin of `easing-soft-decelerate`).

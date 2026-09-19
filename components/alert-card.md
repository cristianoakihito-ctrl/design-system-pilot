# Alert Card

## Figma source

The Figma component is the visual source of truth.

---

## Purpose

Alert Card is used to display important information that needs to remain continuously visible to the user.

Alerts provide immediate feedback about the state or result of an action and may communicate informational, success, warning, or danger messages.

---

## When to use

- Notify the user about the result of an action.
- Alert the user about errors or problems that require attention.
- Present important information that requires immediate attention.
- Use Alert Card when the information must remain visible continuously.

## When not to use

- Do not use for long or complex messages.
- Do not use for content that does not require immediate attention.
- Do not use when a passive notification pattern would be more appropriate.

---

## Anatomy

Alert Card consists of:

1. Container
2. Status icon
3. Title
4. Supporting text
5. Optional action

Current Figma structure:

Alert Card
└── Full content
    ├── Top content
    │   ├── Headline
    │   │   ├── Status icon
    │   │   └── Title
    │   └── Supporting text
    └── Optional action

The optional action exists in the component structure but may be hidden depending on the variant.

---

## Variants

Alert Card supports the following status variants:

- Info
- Success
- Warning
- Danger
- Skeleton

Info, Success, Warning and Danger share the same anatomy,
layout, typography, spacing, radius and elevation.

Status variants must not create independent component implementations.

They must use the same Alert Card component and change only the
status-specific tokens and icon.

---

## Shared layout

The following rules apply to Info, Success, Warning and Danger:

- Outer padding: `padding-XL`
- Gap between status icon and title: `padding-LG`
- Gap between headline and supporting text: `padding-SM`
- Border radius: `border-radius-SM`
- Shadow: `drop-shadow-XS`
- Status icon size: `24 × 24px`

Reference instance:

- Width: `328px`
- Height: `118px`

The reference dimensions must not be treated as fixed component dimensions unless explicitly required by the implementation context.

---

## Title

Typography:

`body-MD-700`

Resolved typography:

- Font family: Montserrat
- Font size: 14
- Font weight: 700 / Bold
- Line height: 21
- Letter spacing: 0.4

---

## Supporting text

Typography:

`body-SM-500`

Resolved typography:

- Font family: Montserrat
- Font size: 12
- Font weight: 500 / Medium
- Line height: 18
- Letter spacing: 0.4

Color:

`pbcon-color-accent-text-neutral-high`

---

## Status variants

### Info

Background:

`pbcon-color-accent-bg-info-low`

Status icon color:

`pbcon-color-accent-icon-info`

Title color:

`pbcon-color-accent-text-info-high`

---

### Success

Background:

`pbcon-color-accent-bg-success-low`

Status icon color:

`pbcon-color-accent-icon-success`

Title color:

`pbcon-color-accent-text-success-high`

---

### Warning

Background:

`pbcon-color-accent-bg-warning-low`

Status icon color:

`pbcon-color-accent-icon-warning`

Title color:

`pbcon-color-accent-text-warning-high`

---

### Danger

Background:

`pbcon-color-accent-bg-danger-low`

Status icon color:

`pbcon-color-accent-icon-danger`

Title color:

`pbcon-color-accent-text-danger-high`

---

## Skeleton

Skeleton represents the loading state of Alert Card.

Background:

`pbcon-color-skeleton-light`

Shared structure tokens:

- Outer padding: `padding-XL`
- Internal spacing: `padding-LG`
- Border radius: `border-radius-SM`

Skeleton must preserve the approximate geometry of the final Alert Card to avoid layout shift when content becomes available.

Do not replace Skeleton with a generic spinner.

No shadow token is exposed on the documented Skeleton variant.

Do not add a shadow unless the Figma source explicitly defines one.

---

## Token sources

Colors:

`/tokens/colors/component.json`

Typography:

`/tokens/typography.json`

Spacing and radius:

`/tokens/spacing.json`

Shadow:

`/tokens/shadow.json`

Icons:

`/assets/icons/`

---

## Implementation rules

- Use the documented Design System tokens.
- Do not hardcode a value when an official token exists.
- Do not invent spacing, colors, typography, radius, or shadows.
- Do not approximate official icons.
- Preserve the component anatomy.
- Use the Figma component as the visual source of truth.
- Use this document as the implementation contract.
- Reuse one Alert Card component for all status variants.
- Do not create separate InfoAlert, SuccessAlert, WarningAlert or DangerAlert implementations.
- If a required value is not documented or available in the Design System, do not infer it. Report the missing value instead.

# Alert Card

## Figma source

Official Figma source:

https://www.figma.com/design/wNFZFxAdn6u2Z3EXLA9Bp3/%E2%9A%AA%EF%B8%8F--CRE--Gest%C3%A3o?node-id=610-452&m=dev

The Figma component is the visual source of truth.

This document describes how Alert Card must be composed using the
Design System tokens, assets and nested components available in this repository.

---

## Purpose

Alert Card is used to display important information that needs to remain
continuously visible to the user.

Alerts provide immediate feedback about the state or result of an action
and may communicate informational, success, warning or danger messages.

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

Figma structure:

Alert Card
└── Full content
    ├── Top content
    │   ├── Headline
    │   │   ├── Status icon
    │   │   └── Title
    │   └── Supporting text
    └── Rounded button [optional nested component]

---

## Component composition

Alert Card is a composed component.

The status icon and the optional action may reuse other Design System assets
or components.

The optional action is implemented using the existing `Rounded button`
component.

Do not recreate the Rounded button styles inside Alert Card.

When the Rounded button is required, use the official Rounded button
component and follow its own component specification.

---

## Variants

Alert Card supports the following status variants:

- Info
- Success
- Warning
- Danger
- Skeleton

Info, Success, Warning and Danger share the same:

- anatomy
- layout
- typography
- spacing
- border radius
- elevation

Status variants must not create independent component implementations.

Use one Alert Card component and change only the status-specific tokens
and status icon.

---

## Shared layout

The following rules apply to Info, Success, Warning and Danger.

### Container

- Outer padding: `padding-XL`
- Border radius: `border-radius-SM`
- Shadow: `drop-shadow-XS`

### Internal spacing

Gap between status icon and title:

`padding-LG`

Gap between headline and supporting text:

`padding-SM`

### Status icon

- Size: `24 × 24px`
- Use the official status icon asset.
- Do not recreate or approximate an existing Design System icon.

### Reference instance

The inspected Figma reference instance measures:

- Width: `328px`
- Height: `118px`

These are reference instance dimensions.

They must not be treated as fixed component dimensions unless the
Figma component explicitly defines them as fixed.

---

## Title

Typography:

`body-MD-700`

Resolved typography:

- Font family: Montserrat
- Font size: 14px
- Font weight: 700 / Bold
- Line height: 21px
- Letter spacing: 0.4px

The title color is determined by the selected status variant.

---

## Supporting text

Typography:

`body-SM-500`

Resolved typography:

- Font family: Montserrat
- Font size: 12px
- Font weight: 500 / Medium
- Line height: 18px
- Letter spacing: 0.4px

Color:

`pbcon-color-accent-text-neutral-high`

### Resizing behavior

The inspected Figma supporting text layer uses:

- Width: Fill container
- Height: Hug contents

The supporting text must wrap according to the available width.

The text layer may grow vertically when the content occupies additional lines.

Do not apply a fixed height to the supporting text.

The resizing behavior of the outer Alert Card container must not be inferred
from this rule and must follow the official Figma component configuration.

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

## Optional action

Alert Card may contain an optional action.

The action is implemented using the existing `Rounded button` component.

Do not recreate the Rounded button typography, colors, spacing,
radius or interaction states inside Alert Card.

Those rules belong to the Rounded button component specification.

When the optional action is visible:

- Component: `Rounded button`
- Position: below the main content
- Gap from main content: `padding-LG`
- Alignment: start / left aligned

When no action is required, the nested Rounded button is hidden.

The visibility of the action must not change the anatomy of the main
Alert Card content.

---

## Skeleton

Skeleton represents the loading state of Alert Card.

Background:

`pbcon-color-skeleton-light`

Confirmed shared structure tokens:

- Outer padding: `padding-XL`
- Internal spacing: `padding-LG`
- Border radius: `border-radius-SM`

Skeleton must preserve the approximate geometry of the final Alert Card
to reduce layout shift when the content becomes available.

Do not replace the Skeleton variant with a generic spinner.

No shadow token was exposed in the inspected Skeleton reference.

Do not add a shadow to Skeleton unless it is explicitly defined by
the official Figma component.

---

## Responsive behavior

The Alert Card must not use the `328px` reference width as a mandatory
fixed implementation width.

Confirmed from Figma:

- Supporting text width: Fill container
- Supporting text height: Hug contents
- Supporting text wraps according to the available width

Not yet confirmed from Figma:

- Outer Alert Card width behavior
- Outer Alert Card height behavior
- Minimum width
- Maximum width

Do not invent these properties.

Until they are confirmed from the official Figma component, the implementation
must not introduce undocumented min-width or max-width rules.

---

## Content rules

- Keep messages concise and focused.
- Avoid long or complex content.
- The title should communicate the alert state or main message.
- Supporting text provides additional context.
- Supporting text may wrap naturally according to the available width.
- Do not truncate important alert information without an explicit rule.

---

## Token sources

### Component colors

`/tokens/colors/component.json`

### Semantic colors

`/tokens/colors/semantic.json`

### Global colors

`/tokens/colors/global.json`

### Typography

`/tokens/typography.json`

### Spacing and border radius

`/tokens/spacing.json`

### Shadow

`/tokens/shadow.json`

### Icons

`/assets/icons/`

---

## Token resolution

Always prefer the highest available Design System abstraction.

Priority:

1. Component token
2. Semantic token
3. Global token

Do not replace an available component token with its resolved HEX value.

Do not hardcode resolved values when a corresponding token exists.

---

## Asset dependencies

Alert Card status icons must use official Design System assets when available.

Do not:

- draw replacement icons
- use emoji
- use external icon libraries when an official icon exists
- approximate an existing Design System icon

If the required official asset is not available in `/assets/icons/`,
report the missing dependency instead of inventing one.

---

## Implementation rules

- Use the documented Design System tokens.
- Do not hardcode values when an official token exists.
- Do not invent spacing, colors, typography, radius or shadows.
- Preserve the documented component anatomy.
- Use one Alert Card implementation for Info, Success, Warning and Danger.
- Do not create independent InfoAlert, SuccessAlert, WarningAlert or DangerAlert components.
- Treat Rounded button as a nested Design System component.
- Do not duplicate Rounded button styling inside Alert Card.
- Use the Figma component as the visual source of truth.
- Use this document as the implementation contract.
- If a required value is not documented, do not infer it.
- Report missing information or dependencies instead.

---

## Documentation status

Confirmed:

- Anatomy
- Info status tokens
- Success status tokens
- Warning status tokens
- Danger status tokens
- Skeleton background token
- Shared padding
- Internal gaps
- Border radius
- Shadow for standard status variants
- Title typography
- Supporting text typography
- Status icon size
- Supporting text Fill / Hug behavior
- Rounded button as optional nested component
- Gap between main content and optional action

Still to confirm:

- Outer Alert Card width resizing mode
- Outer Alert Card height resizing mode
- Minimum width, if defined
- Maximum width, if defined
- Rounded button variant and properties used by Alert Card

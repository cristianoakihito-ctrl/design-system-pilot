# Alert Card

## Figma source

Official Figma source:

https://www.figma.com/design/wNFZFxAdn6u2Z3EXLA9Bp3/%E2%9A%AA%EF%B8%8F--CRE--Gest%C3%A3o?node-id=610-452&m=dev

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

## Variants

Known variants:

- Info
- Success
- Warning
- Danger
- Skeleton

This document currently specifies the `Info / Default` variant.

Other variants must reuse the same structural rules unless explicitly documented otherwise.

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

The optional action exists in the component structure but is hidden in the currently documented variant.

---

## Info / Default

### Container

- Width in reference instance: `328px`
- Height in reference instance: `118px`
- Padding: `padding-XL`
- Border radius: `border-radius-SM`
- Background: `pbcon-color-accent-bg-info-low`
- Shadow: `drop-shadow-XS`

Do not hardcode the resolved values when the corresponding token exists.

### Layout

Outer padding:

`padding-XL`

Headline layout:

Status icon + Title

Gap between status icon and title:

`padding-LG`

Gap between headline and supporting text:

`padding-SM`

### Status icon

- Size: `24 × 24px`
- Color: `pbcon-color-accent-icon-info`

The icon must use an official icon asset when available.

Do not recreate or approximate an existing official icon.

### Title

Typography:

`body-MD-700`

Resolved typography:

- Font family: Montserrat
- Font size: 14
- Font weight: 700 / Bold
- Line height: 21
- Letter spacing: 0.4

Color:

`pbcon-color-accent-text-info-high`

### Supporting text

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
- If a required value is not documented or available in the Design System, do not infer it. Report the missing value instead.

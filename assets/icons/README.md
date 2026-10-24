# Icons

Ícones oficiais utilizados no piloto do Design System.

Total: 373 arquivos SVG, todos com tela de 24 x 24 e desenho monocromático.

## Convenções

- Nome em kebab-case: `<categoria>-<nome>.svg`. Quando o ícone tem versões, o sufixo é `-filled` ou `-outlined`
  (por exemplo `actions-heart-filled.svg` e `actions-heart-outlined.svg`).
- A categoria é o primeiro trecho do nome: `actions`, `documents`, `tech`, `chat`, `multimedia`, `direction`,
  `business`, `money`, `circle`, `nature`, `brand`, `transport`, `communication`, `user`, `time`, `security`,
  `shopping`, `medical`, `location`, `education`, `weather`, `success`, `hobbies`, `feedbacks` e `food`.
- O desenho vem preenchido com `fill="black"`. Para colorir, troque por `fill="currentColor"` e defina a cor no elemento
  que contém o ícone.
- Use o arquivo como está. Nunca redesenhe, edite o traço nem aproxime um ícone. Se um ícone precisar mudar,
  reexporte do Figma.
- Antes de usar um ícone em um componente, confira se o arquivo existe aqui. Se não existir, registre a pendência
  no documento do componente.

## Histórico de correções

### 2026-10-24: nomes corrigidos

Renomeados sem alterar o desenho. Quem referenciava o nome antigo deve atualizar a referência.

| Nome antigo | Nome atual |
| --- | --- |
| `direciton-arrow-down.svg` | `direction-arrow-down.svg` |
| `direciton-arrow-left.svg` | `direction-arrow-left.svg` |
| `direciton-arrow-right.svg` | `direction-arrow-right.svg` |
| `direciton-arrow-up.svg` | `direction-arrow-up.svg` |
| `direciton-arrows.svg` | `direction-arrows.svg` |
| `direciton-chevrons-down.svg` | `direction-chevrons-down.svg` |
| `direciton-chevrons-left.svg` | `direction-chevrons-left.svg` |
| `direciton-chevrons-right.svg` | `direction-chevrons-right.svg` |
| `direciton-chevrons-up.svg` | `direction-chevrons-up.svg` |
| `circle-keyboard-arrow-upfilled.svg` | `circle-keyboard-arrow-up-filled.svg` |
| `circle-keyboard-arrow-upoutlined.svg` | `circle-keyboard-arrow-up-outlined.svg` |

### 2026-10-24: tela padronizada em 24 x 24

Onze arquivos tinham a tela exportada fora do padrão (25 x 24, 24 x 25, 25 x 25 ou 23 x 24), embora o frame
no Figma seja 24 x 24. Foram alterados apenas `width`, `height` e `viewBox`; os traços não foram tocados.
No `direction-corner-down-right.svg` o `viewBox` também foi deslocado em meio ponto para manter o desenho centralizado.

- `actions-search-filled.svg`
- `actions-show-outlined.svg`
- `actions-show-off-outlined.svg`
- `communication-chat-outlined.svg`
- `user-user-outlined.svg`
- `business-building-filled.svg`
- `direction-arrow-left.svg`
- `direction-arrow-right.svg`
- `direction-arrow-up.svg`
- `direction-arrow-down.svg`
- `direction-corner-down-right.svg`

# design-system-pilot

Piloto pessoal para estruturar assets e documentação do Design System.

## Estrutura

| Pasta | Conteúdo |
| --- | --- |
| `assets/icons/` | Ícones SVG oficiais (24 x 24, monocromáticos, nomes em kebab-case) |
| `tokens/` | Tokens em JSON: cores, espaçamento, tipografia, sombra e motion |
| `foundations/` | Regras de uso dos fundamentos: motion e layout da página |
| `components/` | Documentação de cada componente, usada como contrato de implementação |
| `examples/` | Exemplos que abrem no navegador, montados só com tokens e ícones deste repositório |

## Componentes

| Componente | Documento | Exemplo |
| --- | --- | --- |
| Alert Card | `components/alert-card.md` | |
| FAQ item (accordion) | `components/faq-item.md` | `examples/faq-item.html` |
| FAQ list | `components/faq-list.md` | `examples/faq-item.html` |

## Tokens

| Arquivo | Conteúdo |
| --- | --- |
| `tokens/colors/global.json` | Paleta global (valores HEX) |
| `tokens/colors/semantic.json` | Cores semânticas (apontam para a paleta global) |
| `tokens/colors/component.json` | Cores de componentes (apontam para semânticas ou globais) |
| `tokens/spacing.json` | Padding, gap, raio, borda, tamanho de ícone, breakpoints e largura máxima do conteúdo (regras em `foundations/layout.md`) |
| `tokens/typography.json` | Família, tamanhos, pesos, alturas de linha e espaçamento entre letras |
| `tokens/drop-shadow.json` | Sombras |
| `tokens/motion.json` | Durações, distâncias e curvas de animação (regras em `foundations/motion.md`) |

## Convenções

- Ordem de resolução dos tokens: componente, depois semântico, depois global.
- Variáveis CSS usam o prefixo `--pbcon-` seguido do caminho do token
  (por exemplo `padding-XL` vira `--pbcon-padding-XL` e `duration-LG` vira `--pbcon-motion-duration-LG`).
- Ícones são usados como estão no arquivo. Para colorir, troque `fill="black"` por `fill="currentColor"`;
  nunca redesenhe, edite ou aproxime um ícone.
- O componente do Figma é a fonte visual; o documento em `components/` é o contrato de implementação.
- Valor que não está documentado não é inferido: registre como pendência no documento do componente.

## Como adicionar um componente

1. Leia o componente no Figma: anatomia, variantes, estados e tokens aplicados.
2. Confira se todos os tokens existem em `tokens/`. Se faltar algum, adicione primeiro, em um commit separado.
3. Confira se todos os ícones existem em `assets/icons/`.
4. Crie `components/<nome-do-componente>.md` seguindo a estrutura de `components/faq-item.md`.
5. Registre o que o Figma não define na seção Documentation status, como pendência.
6. Se o componente tiver motion, use os tokens de `tokens/motion.json` e as regras de `foundations/motion.md`.
   Para montar uma tela com o componente, siga `foundations/layout.md`.
7. Atualize as tabelas deste README.

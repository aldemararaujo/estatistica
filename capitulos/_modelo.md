<!--
GABARITO DE ESCRITA DE UM CAPÍTULO
Este arquivo não entra no livro: o nome começa com sublinhado e ele não está
listado em estrutura.json. Serve de referência de sintaxe. Copie o esqueleto,
salve com o nome previsto na estrutura e escreva por cima.

REGRAS DE ESTILO DA OBRA
- Frase curta, voz ativa, português formal.
- Sem travessão: use vírgula ou dois-pontos.
- Nenhuma fórmula que não sirva para tomar uma decisão.
- Toda tabela e toda figura precisam de uma frase no texto dizendo o que o
  leitor deve enxergar nelas.
- Teto de 15 páginas, cerca de 6.500 palavras. O que não couber vira apêndice.
- Os seis blocos abaixo aparecem em todos os capítulos, nesta ordem.

O título, o número e a pergunta-guia NÃO se escrevem aqui: vêm de
estrutura.json e o construir.py monta o cabeçalho sozinho.
-->

::: caso
BLOCO 1. O estudo condutor no ponto em que ele está. Duas a quatro frases que
situam o leitor e criam a necessidade do capítulo. Sempre abre o capítulo.
:::

## Primeira seção da apresentação

BLOCO 2. O conceito. Texto corrido, com subtítulos de nível 2 e 3.

Tabelas usam a sintaxe comum do Markdown e rolam sozinhas na horizontal quando
não cabem na tela:

| Variável | Resumo | Quando |
|---|---|---|
| Nominal | n e % | sempre |
| Contínua simétrica | média e desvio padrão | distribuição sem cauda longa |

Código e saída de programa vão em bloco cercado por três crases.

::: jamovi
BLOCO 3. O passo a passo no programa, em lista numerada, com o resultado
comentado. É o bloco que transforma leitura em prática.
:::

::: abas
== No jamovi
Use este bloco quando houver duas maneiras legítimas de chegar ao mesmo
resultado. O leitor escolhe a aba que lhe serve.

== A conta por trás
A aritmética, para quem quer ver de onde o número saiu. Fica escondida por
padrão, e portanto não intimida quem não quer vê-la.
:::

::: revisor
BLOCO 4. Os erros mais comuns do tópico, na forma como o parecerista de um
periódico os devolve. É a seção que nenhum manual traduzido tem. O título padrão
é "Aqui é onde o artigo é rejeitado"; use um título próprio quando o capítulo
tratar de falhas anteriores à submissão, como no Capítulo 1.
:::

::: agora
BLOCO 5. De duas a cinco ações concretas, em lista numerada, aplicadas ao projeto
do **próprio leitor**, e não ao caso condutor. É o que transforma leitura em
trabalho, e o único bloco do livro escrito em segunda pessoa.
:::

## Exercícios

BLOCO 6. De cinco a oito exercícios, todos com gabarito comentado, que fica
colapsado até o leitor pedir.

::: exercicio 1
Enunciado do exercício.

--- gabarito
Resposta comentada. Explique por que a resposta é essa, não apenas qual é.
:::

## Recursos

BLOCO 7. Links verificados, com a data da verificação anotada em `recursos.md`.

- [Nome do recurso](https://exemplo.org) — o que o leitor encontra ali.

<!--
OUTRAS CAIXAS DISPONÍVEIS
::: nota Título opcional
::: atencao Título opcional
-->

::: caso
As análises estão feitas. O aspirado de medula óssea aumentou a cicatrização de
53,3% para 70,7%, com diferença de 17,4 pontos percentuais, intervalo de
confiança de 3,6 a 31,2 e p de 0,015. Falta a etapa em que a maioria dos estudos
brasileiros se perde: transformar isso em um artigo que sobreviva à revisão por
pares.
:::

## O relato é parte do método, não um resumo dele

Um estudo que não pode ser avaliado por quem o lê é, para efeitos práticos, um
estudo que não foi feito. Relatar mal não é falha de redação: é falha de método,
porque impede a verificação, que é o que distingue ciência de opinião.

Daí a existência das recomendações de relato, que não são normas de estilo e sim
listas do que precisa estar dito para que o leitor julgue. Cada delineamento tem
a sua.

| Delineamento | Recomendação | O que a sigla quer dizer |
|---|---|---|
| Ensaio clínico randomizado | CONSORT | *Consolidated Standards of Reporting Trials* |
| Estudo observacional | STROBE | *Strengthening the Reporting of Observational Studies in Epidemiology* |
| Acurácia diagnóstica | STARD | *Standards for Reporting Diagnostic Accuracy studies* |
| Revisão sistemática | PRISMA | *Preferred Reporting Items for Systematic reviews and Meta-Analyses* |
| Protocolo de ensaio | SPIRIT | *Standard Protocol Items: Recommendations for Interventional Trials* |
| Relato de caso | CARE | *Case Report* |

Todas são acrônimos em inglês, e nenhuma tem tradução oficial em português: use
as siglas como estão, que é como elas aparecem nas instruções aos autores. Todas
estão reunidas na **EQUATOR Network**, de *Enhancing the Quality and Transparency
of Health Research*, e todas devem ser lidas **antes** de coletar o primeiro
dado, não na véspera da submissão.

## O diagrama de fluxo

O CONSORT começa por uma figura, e ela é a primeira coisa que um revisor
experiente procura. A do caso condutor:

```
             Avaliados para elegibilidade (n = 246)
                          │
                          ├── Excluídos (n = 46)
                          │     • ITB < 0,80 (n = 19)
                          │     • Úlcera não venosa (n = 12)
                          │     • Recusaram participar (n = 9)
                          │     • Outros critérios (n = 6)
                          ▼
                  Randomizados (n = 200)
                          │
        ┌─────────────────┴─────────────────┐
        ▼                                   ▼
  Aspirado (n = 100)                 Controle (n = 100)
  Receberam o alocado: 100           Receberam o alocado: 100
        │                                   │
  Perdas de seguimento: 8            Perdas de seguimento: 8
        │                                   │
        ▼                                   ▼
  Analisados: 92                     Analisados: 92
```

O diagrama responde, de uma vez, a quem foi excluído e por quê, se houve
desequilíbrio de perdas e sobre quantas pessoas cada número foi calculado. Note
que os 246 avaliados dão a medida de quão selecionada é a amostra, tema do
Capítulo 5.

## O que vai em cada seção

**Introdução.** Três parágrafos bastam: o que se sabe, o que não se sabe e a
pergunta do estudo, esta última em uma frase, no fim, como o Capítulo 2 propôs.
Introdução longa é sinal de pergunta imprecisa.

**Métodos.** É a seção mais importante e a que mais recebe devolutiva. Precisa
conter, em ordem: delineamento com todos os adjetivos, local e período,
elegibilidade, intervenções descritas com detalhe suficiente para replicação,
desfechos com definição operacional, tamanho da amostra com a conta, geração da
sequência aleatória, sigilo de alocação, cegamento por papel, e métodos
estatísticos desfecho a desfecho.

**Resultados.** Fluxo de participantes, características basais sem valor de p,
desfecho primário com estimativa, intervalo e p, desfechos secundários,
segurança. Sem interpretação: interpretar é o trabalho da discussão.

**Discussão.** Resposta à pergunta, comparação com a literatura, mecanismos
plausíveis, limitações e conclusão. A limitação verdadeira aparece; a limitação
decorativa, do tipo "estudo unicêntrico", quando o estudo é multicêntrico, faz o
revisor desconfiar do resto.

::: nota O parágrafo de métodos estatísticos deste estudo
"Variáveis contínuas foram descritas por média e desvio padrão quando
simétricas, e por mediana e quartis quando assimétricas; variáveis categóricas,
por número absoluto e percentual. O desfecho primário foi comparado pelo teste
qui-quadrado de Pearson, com apresentação da diferença absoluta de risco, do
risco relativo e do número necessário para tratar, todos com intervalo de
confiança de 95%. Desfechos contínuos foram comparados pelo teste t de Welch,
com Mann-Whitney como análise de sensibilidade. O tempo até a cicatrização foi
descrito por curvas de Kaplan-Meier, comparado pelo teste de log-rank e modelado
por riscos proporcionais de Cox, com verificação da suposição de
proporcionalidade pelos resíduos de Schoenfeld. Análises ajustadas
pré-especificadas incluíram área inicial, duração da úlcera e diabetes. Todas as
análises seguiram o princípio de intenção de tratar. Adotou-se nível de
significância de 5%, bilateral. As análises foram conduzidas no jamovi versão X."
:::

## As três tabelas e as duas figuras

**Tabela 1, características basais.** Sem valor de p, pelas razões do Capítulo 8.

**Tabela 2, desfechos.** Uma linha por desfecho, com os dois grupos, a medida de
efeito, o intervalo e o p:

| Desfecho | Aspirado | Controle | Efeito (IC 95%) | p |
|---|---|---|---|---|
| Cicatrização em 12 semanas | 65/92 (70,7%) | 49/92 (53,3%) | Diferença 17,4 pp (3,6 a 31,2) | 0,015 |
| Redução de área em 4 semanas | 45,4% (DP 45,0) | 30,6% (DP 42,6) | Diferença 14,8 pp (2,4 a 27,2) | 0,020 |
| Tempo mediano até cicatrizar | 50 dias | 82 dias | HR 1,76 (1,21 a 2,55) | 0,002 |

**Tabela 3, segurança.** Infecção da ferida em 6 e 10 participantes; dor no sítio
de punção em 34 dos 100 que receberam o aspirado. Eventos adversos se relatam
mesmo quando não são significativos, e principalmente quando não são.

**Figura 1, diagrama de fluxo.** **Figura 2, curvas de Kaplan-Meier**, com a
tabela de participantes sob risco embaixo do eixo.

Duas regras para tabelas e figuras: cada uma precisa ser compreensível sozinha,
com legenda que defina abreviações e diga o que está entre parênteses; e nenhuma
informação deve aparecer em tabela **e** em figura **e** no texto, o que é
desperdício de espaço e fonte de discrepância.

## Escrever o resultado sem exagerar

Compare as duas versões da mesma conclusão:

> **Ruim:** "O aspirado de medula óssea mostrou-se altamente eficaz, melhorando
> significativamente a cicatrização de úlceras venosas, e deve ser incorporado à
> prática clínica."

> **Adequada:** "Em pacientes com úlcera venosa e índice tornozelo-braquial
> preservado, o aspirado de medula óssea associado à terapia compressiva
> aumentou a proporção de cicatrização em doze semanas, com diferença absoluta de
> 17,4 pontos percentuais (IC 95% 3,6 a 31,2). O limite inferior do intervalo é
> compatível com benefício modesto, e a confirmação em estudos maiores é
> necessária antes de recomendar a incorporação."

A segunda versão diz exatamente o que o estudo encontrou, informa a população à
qual se aplica, reconhece a imprecisão e não vende o que não foi comprado. É essa
que passa na revisão.

::: revisor
**"O checklist CONSORT não foi submetido."** Devolução administrativa antes
mesmo da revisão científica.

**"O diagrama de fluxo está ausente ou incompleto."** Precisa incluir os
avaliados para elegibilidade e os motivos de exclusão.

**"O resumo relata resultado que não consta dos resultados."** Acontece com
frequência espantosa, quase sempre por versões desencontradas do manuscrito.

**"A conclusão do resumo não se sustenta nos dados apresentados."** Verbo forte
demais para intervalo largo demais.

**"Os métodos estatísticos não estão descritos por desfecho."** Uma frase
genérica não permite julgar adequação.

**"Não há declaração de conflito de interesses nem de financiamento."**
Obrigatório.

**"Não há número de aprovação ética nem de registro do ensaio."** Sem eles, o
manuscrito não segue.
:::

## Exercícios

::: exercicio 1
Escreva a conclusão do resumo deste estudo, em no máximo três linhas, sem usar as
palavras "significativo" e "eficaz".

--- gabarito
"O aspirado de medula óssea autólogo associado à terapia compressiva aumentou a
proporção de cicatrização de úlceras venosas em doze semanas, com diferença
absoluta de 17,4 pontos percentuais (IC 95% 3,6 a 31,2). A amplitude do intervalo
indica que o tamanho do benefício permanece incerto."
:::

::: exercicio 2
Por que o diagrama de fluxo exige informar os 46 pacientes excluídos e seus
motivos?

--- gabarito
Porque a proporção entre avaliados e incluídos, e os motivos de exclusão,
mostram quão selecionada é a amostra e a quem o resultado pode ser aplicado.
Saber que 19 foram excluídos por índice tornozelo-braquial abaixo de 0,80 informa
ao leitor que pacientes com componente arterial ficaram de fora, o que é
justamente a limitação de validade externa discutida no Capítulo 5.
:::

::: exercicio 3
O estudo teve 34 casos de dor no sítio de punção entre os 100 que receberam o
aspirado. Onde e como isso deve aparecer no artigo?

--- gabarito
Na seção de resultados, em tabela de segurança, com o denominador correto, que é
100 e não 200, já que a punção só existiu no grupo tratado. Deve aparecer também
na discussão, ao ponderar benefício contra dano: um terço dos pacientes teve dor
no sítio de punção, o que é parte do custo do tratamento e pesa na decisão
clínica. Omitir eventos adversos frequentes porque não são graves é uma das
formas mais comuns de viés de relato.
:::

::: exercicio 4
Um coautor sugere acrescentar ao resumo o resultado do desfecho secundário que
deu p = 0,002, e retirar o primário, que deu p = 0,015, "porque o segundo é mais
forte". Responda.

--- gabarito
Não se troca o desfecho primário depois de ver os resultados. O primário foi
declarado no protocolo e no registro do ensaio, sustentou o cálculo do tamanho da
amostra e é o único protegido contra a multiplicidade. Além disso, os dois p
citados não são comparáveis dessa forma, porque um vem de um desfecho binário e o
outro de uma análise de tempo até evento, que aproveita mais informação. O resumo
apresenta o primário e pode mencionar o secundário como achado consistente.
:::

::: exercicio 5
Escreva três limitações honestas deste estudo.

--- gabarito
Primeira: o cegamento foi parcial, restrito ao avaliador do desfecho, de modo que
desfechos relatados pelo paciente, como a dor, podem ter sido influenciados pela
expectativa. Segunda: foram excluídos pacientes com índice tornozelo-braquial
abaixo de 0,80, o que limita a aplicação a pacientes com doença arterial
associada, frequentes na prática. Terceira: a amplitude do intervalo de confiança
da diferença, de 3,6 a 31,2 pontos percentuais, deixa em aberto se o benefício é
modesto ou expressivo, e o estudo não tem tamanho para distinguir as duas
hipóteses.
:::

::: exercicio 6
Monte, para o caso condutor, a Tabela 2 completa a partir dos resultados dos
Capítulos 9, 10 e 14, e confira cada número contra os capítulos de origem.

--- gabarito
A tabela deste capítulo já traz as três linhas principais. Um exercício completo
acrescentaria a variação da dor entre a inclusão e a décima segunda semana e a
redução de área em doze semanas, esta última com a ressalva do efeito teto. O
ponto do exercício é a conferência: cada valor precisa bater exatamente com o
capítulo de origem, e a maneira segura de garantir isso é gerar todos os números
de um único script, como o `analises-do-livro.py` faz nesta obra.
:::

::: agora
1. Baixe o checklist da recomendação correspondente ao seu delineamento e
   responda item por item, anotando a página do seu manuscrito. Muitas revistas
   exigem o checklist preenchido na submissão.
2. Confira cada número do texto contra a saída do programa. O erro mais comum de
   todos é uma tabela que não bate com o parágrafo, porque o parágrafo ficou de
   uma versão anterior da análise.
3. Releia a conclusão do seu resumo ao lado do intervalo de confiança do desfecho
   primário. Se o verbo for mais forte que o intervalo permite, troque o verbo.
4. Verifique os denominadores: todo percentual precisa dizer sobre quantos casos
   foi calculado, e eles mudam de tabela para tabela quando há dados faltantes.
5. Escreva três limitações verdadeiras. Se a lista tiver apenas limitações
   decorativas, o revisor vai desconfiar do resto do artigo.
6. Leia o artigo do fim para o começo. A conclusão do resumo é o que mais gente
   vai ler, e é onde o exagero costuma se esconder.
:::

## Recursos

- [CONSORT Statement](https://www.consort-statement.org/) — checklist e diagrama.
- [EQUATOR Network](https://www.equator-network.org/) — todas as recomendações de
  relato, por delineamento.
- [STROBE](https://www.strobe-statement.org/), [STARD](https://www.equator-network.org/reporting-guidelines/stard/),
  [PRISMA](https://www.prisma-statement.org/) — para observacionais, acurácia
  diagnóstica e revisões sistemáticas.

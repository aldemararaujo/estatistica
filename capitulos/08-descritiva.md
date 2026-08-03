::: caso
Os duzentos participantes foram randomizados, tratados e seguidos por doze
semanas. O banco está fechado. Antes de comparar coisa alguma, é preciso
responder a uma pergunta que parece banal e não é: quem são essas pessoas? A
primeira tabela de todo artigo clínico existe para isso, e é ela que vamos
construir neste capítulo.
:::

## Descrever é decidir o que omitir

O banco do estudo tem duzentas linhas e vinte e seis colunas: cinco mil e
duzentos valores. Nenhum leitor de artigo vai olhar para eles, e nenhum revisor
quer olhar. A estatística descritiva existe para substituir esses cinco mil
valores por algumas dezenas de números que preservem o essencial e descartem o
resto.

O verbo importante da frase anterior é descartar. Todo resumo perde informação,
e o trabalho do pesquisador é escolher qual informação pode ser perdida. Quando
essa escolha é feita sem critério, o resumo mente sem que ninguém perceba, e o
capítulo inteiro trata de como evitar isso.

## Cada tipo de variável pede um resumo

A regra é curta e resolve a quase totalidade dos casos:

| Tipo de variável | Como resumir | Exemplo no estudo |
|---|---|---|
| Nominal | número absoluto e percentual | sexo, diabetes, grupo |
| Ordinal | número absoluto e percentual, na ordem natural das categorias | tabagismo |
| Contínua com distribuição simétrica | média e desvio padrão | idade, índice tornozelo-braquial |
| Contínua com distribuição assimétrica | mediana e quartis | área da úlcera, duração da úlcera |

O único julgamento que sobra é o da terceira linha contra a quarta: a
distribuição é simétrica ou não? É aí que quase todo mundo erra, e por um motivo
curioso, tratado na seção seguinte.

### Como decidir se a distribuição é simétrica

Olhando para ela. Um histograma resolve em três segundos o que nenhum teste
resolve bem.

A prática difundida de aplicar um teste de normalidade, quase sempre o de
Shapiro-Wilk, e decidir pela média ou pela mediana conforme o valor de p é uma
das piores heranças dos manuais antigos. O teste responde a uma pergunta que não
interessa, que é se a distribuição é *exatamente* normal, e responde mal: com
amostra pequena ele quase nunca rejeita, ainda que a assimetria seja evidente, e
com amostra grande ele rejeita quase sempre, ainda que a assimetria seja
irrelevante. O leitor fica, portanto, com um critério que erra nas duas pontas e
que substitui o próprio julgamento por um valor de p.

Olhe o histograma. Se a cauda de um lado for visivelmente mais longa que a do
outro, a distribuição é assimétrica e a mediana descreve melhor.

### O caso da área da úlcera

A área inicial das úlceras do estudo é o exemplo perfeito, e por isso vai
acompanhar o leitor até o fim do livro. Estes são os dois resumos possíveis:

| Resumo | Valor |
|---|---|
| Média e desvio padrão | 10,5 cm² (desvio padrão de 9,4) |
| Mediana e quartis | 7,7 cm² (quartis de 4,7 e 12,7) |

A diferença entre 10,5 e 7,7 não é detalhe de arredondamento: é o efeito de umas
poucas úlceras enormes, uma delas de 66,4 cm², que puxam a média para cima sem
representar quase ninguém. A prova disso é um número que vale mais do que
qualquer teste: **apenas 67 das 200 úlceras têm área acima da média**. Ou seja,
dois terços dos participantes estão abaixo do valor que supostamente os resume.

Quando um resumo descreve mal dois terços da amostra, ele não serve, por mais
correta que esteja a aritmética que o produziu.

::: atencao Desvio padrão não é erro padrão
São coisas diferentes e a troca é frequente. O desvio padrão descreve o quanto
os participantes variam entre si, e é o que entra na descrição da amostra. O
erro padrão descreve a precisão com que a média foi estimada, encolhe conforme a
amostra cresce e serve para construir intervalo de confiança, assunto do
Capítulo 9. Descrever a amostra com erro padrão faz a variabilidade parecer
menor do que é, e é exatamente por isso que a troca costuma passar despercebida
por quem a comete.
:::

## A Tabela 1 do estudo

A primeira tabela de um artigo clínico descreve os grupos na linha de base. Ela
não compara nada: apenas mostra com quem o estudo foi feito, para que o leitor
julgue se aqueles resultados valem para os pacientes dele.

| Característica | Aspirado (n = 100) | Controle (n = 100) |
|---|---|---|
| Idade, anos, média (DP) | 62,3 (11,3) | 62,0 (11,2) |
| Sexo feminino, n (%) | 50 (50,0) | 47 (47,0) |
| Índice de massa corporal, média (DP) | 29,2 (5,1) | 29,1 (4,5) |
| Diabetes melito, n (%) | 17 (17,0) | 27 (27,0) |
| Fumante atual, n (%) | 26 (26,0) | 22 (22,0) |
| Índice tornozelo-braquial, média (DP) | 1,02 (0,09) | 1,01 (0,09) |
| Área da úlcera, cm², mediana (quartis) | 8,2 (5,1 a 14,6) | 7,1 (4,4 a 11,6) |
| Duração da úlcera, meses, mediana (quartis) | 13 (8 a 19) | 12,5 (7,8 a 21) |
| Úlcera recidivante, n (%) | 56 (56,0) | 58 (58,0) |
| Adesão adequada à compressão, n (%) | 75 (75,0) | 72 (72,0) |
| Dor, escala visual analógica, mediana (quartis) | 5,5 (4 a 7) | 5,0 (4 a 7) |

Duas linhas dessa tabela merecem ser lidas com atenção, e o leitor deve procurá-las
antes de seguir adiante. A primeira é a do diabetes: 17% contra 27%, uma diferença
de dez pontos percentuais entre grupos que foram randomizados. A segunda é a da
área da úlcera: mediana de 8,2 cm² contra 7,1 cm², com o grupo do aspirado
recebendo as úlceras um pouco maiores.

Nenhuma das duas é erro. São o acaso da randomização, que equilibra os grupos em
média, ao longo de muitas repetições, mas não garante equilíbrio perfeito em um
estudo particular. As duas voltarão no Capítulo 12, quando o resultado for
ajustado por essas características, e voltarão de novo no Capítulo 15, quando for
preciso decidir o que dizer sobre elas no artigo.

### Por que não há valor de p nesta tabela

Falta uma coluna que o leitor talvez tenha estranhado não encontrar. Muitos
artigos publicam uma coluna de valor de p na Tabela 1, comparando os grupos na
linha de base, e a recomendação CONSORT desaconselha essa coluna explicitamente.

O motivo é lógico, não estatístico. O valor de p mede a probabilidade de uma
diferença como a observada ter surgido por acaso. Em um ensaio randomizado, nós
*sabemos* que ela surgiu por acaso: foi um sorteio que alocou os participantes.
Testar aquilo que já se sabe verdadeiro responde a uma pergunta sem interesse, e
pior, sugere uma conclusão errada: a de que um p acima de 0,05 autorizaria
concluir que os grupos são comparáveis. Não autoriza. Um desequilíbrio de dez
pontos percentuais no diabetes atrapalha a interpretação do resultado
independentemente do valor de p que ele produza, e é o tamanho do desequilíbrio,
não sua significância, que decide se vale a pena ajustar a análise.

Em estudo observacional a situação é outra, e o Capítulo 12 volta ao assunto.

::: jamovi
1. Abra o jamovi e carregue `coorte-condutor.csv` em **Open**, aba **Data**.
2. Confira o tipo de cada variável na aba **Data**, botão **Setup**. O jamovi
   adivinha, e adivinha errado com alguma frequência: `evento_cicatrizacao` está
   codificada como 0 e 1 e será lida como contínua, quando é nominal.
3. Vá em **Analyses**, **Exploration**, **Descriptives**.
4. Leve `idade`, `imc`, `itb`, `area_inicial_cm2` e `duracao_ulcera_meses` para
   **Variables**, e leve `grupo` para **Split by**.
5. Em **Statistics**, marque **Mean**, **Std. deviation**, **Median** e
   **Quartiles**. Desmarque o que não vai usar: tabela poluída é tabela que
   ninguém confere.
6. Em **Plots**, marque **Histogram** e **Box plot**.

Compare o histograma da idade com o da área da úlcera. O primeiro é
aproximadamente simétrico, com uma pequena elevação em torno dos sessenta anos.
O segundo tem uma cauda longa à direita que se estende até 66 cm². São esses dois
desenhos, e não um teste de normalidade, que decidem qual resumo entra na
Tabela 1.
:::

::: abas
== No jamovi
Para as variáveis categóricas, leve `sexo`, `diabetes`, `tabagismo`,
`ulcera_recidivante` e `adesao_compressao` para **Variables** e `grupo` para
**Split by**, e marque **Frequency tables** em **Descriptives**. O jamovi produz
n e percentual de cada categoria, que é exatamente o que a Tabela 1 pede.

== A conta por trás
A mediana é o valor que divide a amostra ordenada em duas metades. Com 200
observações, é a média entre a centésima e a centésima primeira. O primeiro
quartil é o valor abaixo do qual estão 25% das observações, e o terceiro, 75%.

A área da úlcera ordenada tem primeiro quartil em 4,7 cm² e terceiro em
12,7 cm². A distância entre os dois, 8,0 cm², é a amplitude interquartil, e é a
medida de dispersão que acompanha a mediana pelo mesmo motivo que o desvio
padrão acompanha a média: ambas resumem o espalhamento sem sofrer com os valores
extremos que o resumo escolheu ignorar.
:::

## Quando o resumo esconde o resultado

A redução percentual da área em doze semanas parece o desfecho contínuo natural
deste estudo. Veja o que acontece quando se descreve os dois grupos por ele:

| Grupo | Média (DP) | Mediana |
|---|---|---|
| Aspirado | 88,2% (22,9) | 100% |
| Controle | 73,0% (37,4) | 100% |

As medianas são idênticas, e iguais a 100%. Um pesquisador apressado concluiria
que os grupos são indistinguíveis. Ele estaria errado: a mediana é 100% nos dois
grupos porque mais da metade dos participantes de cada grupo cicatrizou
completamente, e uma úlcera cicatrizada tem exatamente 100% de redução, nunca
mais do que isso.

Isso se chama **efeito teto**. A variável tem um limite superior que boa parte da
amostra alcança, e a partir dali ela para de discriminar. Nenhum resumo, e nenhum
teste, recupera uma informação que a própria escala destruiu.

A solução foi tomada no planejamento, não na análise: o estudo também mediu a
área em quatro semanas, quando quase ninguém havia cicatrizado ainda.

| Grupo | Média (DP) | Mediana (quartis) |
|---|---|---|
| Aspirado | 45,4% (45,0) | 46,2% (12,1 a 91,1) |
| Controle | 30,6% (42,6) | 38,3% (−1,8 a 60,4) |

Agora a descrição informa. Note de passagem o primeiro quartil do grupo
controle: −1,8%, um valor negativo, porque um quarto daqueles participantes
tinha, em quatro semanas, úlcera do mesmo tamanho ou maior do que no início.
Esse é o tipo de fato clínico que uma média de 30,6% nunca teria revelado.

::: revisor
**"Os autores relatam média e desvio padrão para variáveis claramente
assimétricas."** É a devolutiva mais comum de todas. Área de ferida, duração de
doença, tempo de internação, custo e contagem de células são quase sempre
assimétricos à direita. Descreva com mediana e quartis.

**"Não fica claro se o valor entre parênteses é desvio padrão, erro padrão ou
intervalo de confiança."** Escreva na própria tabela o que está entre parênteses.
"Média (DP)" custa quatro caracteres e evita uma rodada de revisão.

**"A Tabela 1 apresenta valores de p comparando os grupos de um ensaio
randomizado."** Retire a coluna. Se algum desequilíbrio preocupa, discuta o
tamanho dele e trate-o com ajuste na análise, não com teste na linha de base.

**"O número de participantes de cada análise não está informado."** Havia perdas
de seguimento neste estudo: dezesseis participantes. Toda tabela de desfecho
precisa dizer sobre quantas pessoas cada número foi calculado, e nenhuma tabela
pode deixar o leitor supondo que foram duzentas.

**"Precisão excessiva."** Idade média de 62,34 anos sugere uma exatidão que não
existe. Uma casa decimal basta para idade, peso e escores; percentuais em estudo
com duzentos participantes não precisam de decimal algum.
:::

## Exercícios

::: exercicio 1
A duração da úlcera no grupo controle tem média de 16,0 meses, desvio padrão de
11,8, mediana de 12,5 meses e quartis de 7,8 e 21,0. Qual par de medidas deve
entrar na Tabela 1, e como você chegou a essa conclusão sem ver o histograma?

--- gabarito
Mediana e quartis. A pista está na relação entre a média e a mediana: a média,
16,0, é bem maior que a mediana, 12,5, o que indica cauda longa à direita. Uma
segunda pista é o desvio padrão, 11,8, quase do tamanho da própria média: em uma
distribuição simétrica de valores positivos isso praticamente não ocorre, porque
implicaria uma proporção considerável de valores negativos, impossíveis para
duração de doença. O histograma confirmaria, mas neste caso os dois indícios já
bastam.
:::

::: exercicio 2
Um colega defende que a Tabela 1 deve trazer o valor de p do teste qui-quadrado
comparando a frequência de diabetes entre os grupos, porque 17% contra 27% "pode
ser uma diferença real". Responda a ele em no máximo cinco linhas.

--- gabarito
A diferença é real: ela está nos dados, os grupos de fato diferem em dez pontos
percentuais. O que o teste avaliaria é se ela pode ser atribuída ao acaso, e a
resposta já é conhecida antes de qualquer cálculo, porque a alocação foi
sorteada. O que importa é se um desequilíbrio desse tamanho é capaz de
distorcer o resultado, e essa é uma pergunta clínica, não estatística: o
diabetes atrasa a cicatrização, portanto o desequilíbrio favorece o grupo do
aspirado e precisa ser tratado com ajuste na análise, qualquer que seja o valor
de p que ele produzisse.
:::

::: exercicio 3
Abra o banco no jamovi e produza o histograma da variável `tcpo2_basal`. Ela é
simétrica ou assimétrica? Qual resumo você usaria? Compare sua resposta com a
média (35,8) e a mediana (36,0) da variável.

--- gabarito
A distribuição é aproximadamente simétrica, e o histograma mostra o formato de
sino esperado, porque a variável foi medida em uma escala fisiológica sem
limite inferior próximo de zero nem cauda longa. Média e desvio padrão são o
resumo adequado. A proximidade entre média (35,8) e mediana (36,0) confirma a
leitura visual: quando as duas quase coincidem, a assimetria é desprezível.
Repare que a variável tem doze valores ausentes, por falha do equipamento, e
que portanto o resumo se refere a 188 participantes, não a 200. Isso precisa
estar escrito na tabela.
:::

::: exercicio 4
Um artigo descreve a área inicial das úlceras como "10,5 ± 9,4 cm²". Aponte os
dois problemas dessa apresentação.

--- gabarito
O primeiro problema é a escolha do resumo: a distribuição é assimétrica à
direita, com 66,4 cm² no extremo, e apenas um terço da amostra tem área acima da
média. A mediana de 7,7 cm² com quartis de 4,7 e 12,7 descreveria melhor.

O segundo é a notação. O símbolo ± não informa o que vem depois dele, e o leitor
não tem como saber se aquele 9,4 é desvio padrão, erro padrão ou a metade de um
intervalo de confiança. Além disso, a notação sugere um intervalo simétrico de
1,1 a 19,9 cm², e o limite inferior desse intervalo é implausível para uma
amostra cujo menor valor é 0,8 cm² e cuja distribuição é assimétrica.
:::

::: exercicio 5
Por que a mediana da redução de área em doze semanas é 100% nos dois grupos,
sendo que a proporção de cicatrização foi de 70,7% no grupo do aspirado e 53,3%
no controle? As duas informações se contradizem?

--- gabarito
Não se contradizem. A mediana é o valor do participante do meio, e em ambos os
grupos mais da metade dos participantes cicatrizou completamente, atingindo 100%
de redução: no grupo do aspirado foram 70,7% e no controle 53,3%, ambos acima de
50%. Como o participante do meio está, nos dois casos, dentro do conjunto dos que
cicatrizaram, a mediana é 100% nos dois grupos.

O episódio ensina que a mediana só discrimina quando o valor central cai em uma
região da escala onde ainda há variação. Se o controle tivesse cicatrizado 45%
das úlceras, a mediana dos dois grupos seria diferente, e a mesma medida que aqui
não informou nada teria informado bastante.
:::

::: exercicio 6
Monte, no jamovi, a Tabela 1 completa deste capítulo, e depois confira linha por
linha contra a tabela impressa aqui. Anote quanto tempo levou. Esse tempo é o
custo de conferir um resultado, e é o argumento mais convincente a favor de
manter um banco reprodutível, assunto do Capítulo 7.

--- gabarito
Não há resposta única. O ponto do exercício é outro: reproduzir uma tabela
publicada a partir do banco original leva entre quinze e trinta minutos quando o
banco está organizado, e é impossível quando não está. Se algum valor não bater,
o mais provável é que o jamovi tenha classificado a variável com o tipo errado na
importação, ou que a análise esteja incluindo os participantes com dado ausente
de maneira diferente da usada aqui.
:::

## Recursos

- [CONSORT Statement](https://www.consort-statement.org/) — a recomendação para
  relato de ensaios clínicos randomizados, incluindo a orientação sobre a
  Tabela 1.
- [jamovi](https://www.jamovi.org/) — o programa usado no livro, gratuito, para
  Windows, macOS e Linux.
- [Guidelines for reporting statistics](https://journals.physiology.org/doi/full/10.1152/japplphysiol.00513.2004)
  — as diretrizes da American Physiological Society, ainda úteis, com uma seção
  específica sobre a confusão entre desvio padrão e erro padrão.

::: caso
Cicatrizaram 65 das 92 úlceras do grupo do aspirado, ou 70,7%, contra 49 das 92
do grupo controle, ou 53,3%. A diferença é de 17,4 pontos percentuais. A
pergunta que este capítulo responde não é se essa diferença existe, porque ela
está ali. É outra: se o estudo fosse repetido com outros duzentos pacientes,
quanto esse número poderia mudar?
:::

## Todo resultado é uma estimativa

O estudo não mediu a eficácia do aspirado de medula óssea. Mediu o que aconteceu
com 184 pessoas específicas, em três centros específicos, em um período
específico. O interesse, porém, nunca é aquelas 184 pessoas: é o próximo
paciente, que não participou de nada.

Entre o que se observou e o que se quer saber existe, portanto, um salto. Aquele
70,7% é uma **estimativa pontual**: o melhor palpite disponível sobre a
proporção de cicatrização que o tratamento produziria na população de onde a
amostra veio. Como todo palpite, ele tem margem de erro, e o trabalho deste
capítulo é medir essa margem.

Um número sozinho esconde a margem. Um intervalo de confiança a mostra.

## O que o intervalo de confiança diz

O intervalo de confiança de 95% da proporção de cicatrização no grupo do
aspirado vai de 60,7% a 79,0%.

A definição formal é incômoda e vale enfrentá-la: se o estudo inteiro fosse
repetido muitas vezes, e em cada repetição se calculasse um intervalo por esse
mesmo método, 95% dos intervalos conteriam o valor verdadeiro. A confiança está
no procedimento, ao longo das repetições, não neste intervalo em particular.

Na prática do dia a dia, o intervalo é lido como a **faixa de valores
compatíveis com os dados observados**. Uma taxa verdadeira de 62% é compatível
com o que este estudo viu. Uma taxa verdadeira de 45% não é, e uma de 85% também
não. O intervalo é a resposta honesta à pergunta "quanto eu sei?", e sua largura
é a medida da ignorância que restou.

::: atencao O que o intervalo não é
Não é a faixa onde estão 95% dos pacientes. Aquela faixa se descreve com
quartis, e foi assunto do Capítulo 8. O intervalo de confiança descreve a
incerteza sobre uma estimativa, não a variação entre pessoas. Confundir as duas
coisas leva a afirmar que "95% dos pacientes cicatrizam entre 60,7% e 79,0%",
uma frase que não significa nada.
:::

### A largura importa mais que os extremos

Compare os dois intervalos do desfecho primário:

| Grupo | Estimativa | Intervalo de confiança de 95% |
|---|---|---|
| Aspirado | 70,7% | 60,7% a 79,0% |
| Controle | 53,3% | 43,1% a 63,1% |

Cada um tem cerca de dezoito pontos percentuais de largura. Isso é muito, e é o
preço de noventa e dois participantes por grupo. Um estudo com quatro vezes mais
gente teria intervalos com metade dessa largura, porque a precisão melhora com a
raiz quadrada do tamanho da amostra: para reduzir a incerteza pela metade, é
preciso quadruplicar o estudo. Essa relação é a razão de o Capítulo 6 existir, e
é também a razão de estudos pequenos raramente resolverem alguma coisa.

## O intervalo do que interessa: a diferença

Os dois intervalos acima se sobrepõem, entre 60,7% e 63,1%. Um leitor apressado
concluiria daí que os grupos não diferem. Ele estaria cometendo um erro comum, e
a demonstração de que é erro vem a seguir: o intervalo que interessa não é o de
cada grupo, é o **da diferença**.

| Medida de efeito | Estimativa | Intervalo de confiança de 95% |
|---|---|---|
| Diferença absoluta de risco | 17,4 pontos percentuais | 3,6 a 31,2 |
| Risco relativo | 1,33 | 1,05 a 1,67 |
| Razão de chances | 2,11 | 1,15 a 3,88 |
| Número necessário para tratar | 5,8 | 3,2 a 27,9 |

O intervalo da diferença não inclui o zero. Os dados são incompatíveis com a
hipótese de que o tratamento não faz diferença alguma, ainda que os intervalos
individuais se sobreponham. Sobreposição de intervalos individuais não é
critério para nada: o intervalo da diferença é uma quantidade diferente, com
erro padrão próprio.

::: calculadora intervalo
:::

A calculadora abre com os números do desfecho primário deste estudo. Ponha os
seus e confira contra a saída do jamovi: os intervalos usam o método de Wilson,
explicado nas abas mais adiante.

### Ler cada medida pelo que ela diz

A **diferença absoluta** é a mais útil na clínica: tratar cem pacientes produz
cerca de dezessete cicatrizações a mais. É a única medida que fala em pacientes,
e não em razões.

O **risco relativo** de 1,33 diz que a chance de cicatrizar aumenta em um terço.
Ele parece mais impressionante que a diferença absoluta quando o desfecho é raro,
e é por isso que a indústria e a imprensa preferem citá-lo. Aqui o desfecho é
frequente, e as duas medidas contam a mesma história.

O **número necessário para tratar** é a diferença absoluta virada do avesso:
5,8 significa que, para cada seis pacientes tratados, um cicatriza que não teria
cicatrizado. Repare no intervalo dele: de 3,2 a 27,9. É assimétrico e muito
largo, porque o NNT é o inverso de um número pequeno, e inverter amplia a
incerteza. Um NNT sem intervalo é uma promessa sem lastro.

### O tamanho de efeito de uma variável contínua

Para a redução de área em quatro semanas, o raciocínio é o mesmo, com outra
aritmética:

| Medida | Valor |
|---|---|
| Média no grupo aspirado | 45,4% (DP 45,0), n = 95 |
| Média no grupo controle | 30,6% (DP 42,6), n = 99 |
| Diferença de médias | 14,8 pontos percentuais (IC95% 2,4 a 27,2) |
| d de Cohen | 0,34 |

O **d de Cohen** expressa a diferença em desvios padrão: 0,34 é um efeito
pequeno pelas convenções usuais, que classificam 0,2 como pequeno, 0,5 como
médio e 0,8 como grande. Essas convenções são úteis para comparar áreas
diferentes e péssimas para decidir conduta clínica, porque não sabem nada sobre
a doença. Quatorze pontos percentuais a mais de redução de área em quatro
semanas é um efeito pequeno em desvios padrão e um efeito relevante para quem
convive com uma úlcera aberta há um ano.

::: jamovi
1. Para a proporção e seu intervalo, vá em **Analyses**, **Frequencies**,
   **2 Outcomes (Binomial test)**, e marque **Confidence interval**.
2. Para comparar os dois grupos, use **Frequencies**, **Independent Samples**,
   com `grupo` em **Rows** e `cicatrizacao_12sem` em **Columns**. Em
   **Comparative Measures**, marque **Difference in proportions**,
   **Relative risk** e **Odds ratio**, todos com intervalo de confiança.
3. Para a variável contínua, use **T-Tests**, **Independent Samples T-Test**, com
   `reducao_area_4sem_pct` em **Dependent Variables** e `grupo` em **Grouping
   Variable**. Marque **Mean difference**, **Confidence interval** e
   **Effect size** com intervalo.

O jamovi não calcula o número necessário para tratar. Ele sai da diferença
absoluta: 1 dividido por 0,174 resulta em 5,8, e o intervalo se obtém invertendo
os dois extremos do intervalo da diferença, na ordem contrária.
:::

::: abas
== O intervalo pelo método de Wald
É o que se aprende primeiro: a estimativa mais ou menos 1,96 erro padrão. Para
65 de 92, a proporção é 0,707 e o erro padrão é a raiz de 0,707 vezes 0,293
dividido por 92, ou 0,0475. O intervalo vai de 0,614 a 0,800.

Funciona bem no meio da escala e falha nas pontas: com proporções perto de zero
ou de um, ele produz limites impossíveis, abaixo de zero ou acima de cem por
cento.

== O intervalo de Wilson
É o que este livro usa, e o que o jamovi oferece: 60,7% a 79,0%. Ele resolve o
problema das pontas porque não trata a proporção como se fosse simétrica, e
nunca ultrapassa os limites lógicos de zero e um.

A diferença entre os dois métodos é pequena quando a proporção está perto de
50% e o estudo é grande, e é grande justamente nas situações em que mais
importa: eventos raros e amostras pequenas. Use Wilson e esqueça Wald.
:::

::: revisor
**"Os autores relatam apenas o valor de p."** É a devolutiva mais frequente das
revistas clínicas desde a década de 1990, e continua sendo necessária. Todo
resultado principal precisa de estimativa e intervalo. O p vem depois, se vier.

**"O intervalo de confiança do desfecho primário não está informado."** Repare
que a exigência é do desfecho **primário**: encher o artigo de intervalos para
desfechos exploratórios não substitui o que falta no principal.

**"O NNT é apresentado sem intervalo de confiança."** E o intervalo do NNT é
assimétrico. Quando a diferença absoluta não é significativa, o intervalo do NNT
passa pelo infinito e deixa de fazer sentido apresentá-lo.

**"Os autores concluem que não há diferença porque os intervalos se
sobrepõem."** Erro conceitual. O que decide é o intervalo da diferença, e é
perfeitamente possível que intervalos individuais se sobreponham enquanto o da
diferença exclui o zero, como acontece neste estudo.

**"Não se distingue desvio padrão de intervalo de confiança nas figuras."**
Barras de erro sem legenda são inúteis. Escreva na legenda o que a barra
representa.
:::

::: quiz
? [facil] O intervalo de confiança de 95% da diferença absoluta deste estudo vai de 3,6 a 31,2 pontos percentuais. O que ele indica?
+ Que os dados são compatíveis com benefícios entre quase quatro e trinta e uma cicatrizações a mais por cem tratados. | Correto. Como até o limite inferior é benefício, o estudo aponta efeito real, sem permitir dizer se ele é modesto ou expressivo. É essa indefinição que justificaria um estudo maior.
- Que 95% dos pacientes terão benefício nessa faixa. | Confunde incerteza sobre a estimativa com variação entre pessoas. A faixa em que estão os pacientes se descreve com quartis.
- Que há 95% de certeza de que o efeito é de 17,4 pontos. | O intervalo descreve a incerteza em torno da estimativa, e não uma certeza sobre o valor pontual.
- Que o tratamento funciona em 95% dos casos. | Nada no intervalo diz respeito à proporção de pacientes que respondem.
- Que o estudo precisa de mais 95 participantes. | O intervalo não indica quantos participantes faltam, embora sua largura sugira que o estudo é pequeno para a precisão desejada.
@ cap-9-o-intervalo-do-que-interessa-a-diferenca

? [facil] Dois grupos têm intervalos de confiança que se sobrepõem. O que se conclui sobre a diferença entre eles?
+ Nada: o que decide é o intervalo da diferença, que é outra quantidade, com erro padrão próprio. | Correto. Neste estudo os intervalos individuais se sobrepõem entre 60,7% e 63,1%, e ainda assim o intervalo da diferença exclui o zero.
- Que não há diferença estatisticamente detectável. | É o erro mais comum na leitura de gráficos com barras de erro.
- Que a diferença é significativa, porque a sobreposição é pequena. | O tamanho da sobreposição não é critério para nada.
- Que os grupos têm a mesma variabilidade. | Sobreposição de intervalos não informa sobre variabilidade.
- Que a amostra é insuficiente. | Pode ser, e isso se avalia pela largura dos intervalos, não pela sobreposição.
@ cap-9-o-intervalo-do-que-interessa-a-diferenca

? [media] O número necessário para tratar deste estudo é 5,8, com intervalo de 3,2 a 27,9. Por que ele é tão assimétrico?
+ Porque o NNT é o inverso da diferença absoluta, e inverter uma escala a distorce. | Correto. O limite superior da diferença, 31,2 pontos, vira 3,2; o inferior, 3,6 pontos, vira 27,9. Diferenças pequenas no denominador produzem NNT enormes.
- Porque o cálculo do NNT usa uma distribuição assimétrica. | Não há distribuição envolvida: o NNT é uma transformação determinística da diferença.
- Porque houve perdas de seguimento desiguais. | As perdas foram iguais nos dois grupos e não afetam a forma do intervalo.
- Porque a amostra é pequena. | A amostra afeta a largura, e não a assimetria, que decorre da inversão.
- Porque o desfecho é binário. | Desfechos binários não produzem, por si, intervalos assimétricos nessa escala.
@ cap-9-o-intervalo-do-que-interessa-a-diferenca

? [media] Um estudo quadruplica o tamanho da amostra e observa exatamente as mesmas proporções. O que acontece?
+ A estimativa não muda e o intervalo encolhe para cerca de metade da largura. | Correto. A precisão melhora com a raiz quadrada do tamanho da amostra: para reduzir a incerteza pela metade, é preciso quadruplicar o estudo.
- A estimativa não muda e o intervalo encolhe para um quarto da largura. | Seria assim se a precisão melhorasse linearmente, o que não ocorre.
- A estimativa aumenta e o intervalo encolhe. | O tamanho da amostra não desloca a estimativa pontual.
- Nada muda, porque as proporções são as mesmas. | O intervalo depende do tamanho da amostra e encolhe.
- O valor de p permanece igual. | O p diminui bastante, porque depende do tamanho da amostra.
@ cap-9-o-que-o-intervalo-de-confianca-diz

? [media] Por que este livro prefere o intervalo de Wilson ao de Wald para proporções?
+ Porque Wilson não produz limites impossíveis, abaixo de zero ou acima de cem por cento, nas situações em que mais importa: eventos raros e amostras pequenas. | Correto. A diferença entre os dois é pequena perto de 50% com amostra grande, e grande justamente nas pontas.
- Porque Wilson é mais simples de calcular à mão. | Wald é mais simples; Wilson é mais correto.
- Porque Wald não pode ser usado em desfechos binários. | Pode, e é o método clássico; o problema é o comportamento nas pontas.
- Porque Wilson produz intervalos sempre mais estreitos. | Nem sempre; ele produz intervalos com cobertura mais adequada.
- Porque o jamovi não oferece o método de Wald. | O jamovi oferece opções, e a escolha é metodológica.
@ cap-9-o-que-o-intervalo-de-confianca-diz

? [dificil] Um colega afirma: "há 95% de probabilidade de a taxa verdadeira estar entre 60,7% e 79,0%". Como avaliar essa frase?
+ Tecnicamente incorreta na estatística frequentista, porque a taxa verdadeira é fixa e a confiança está no procedimento ao longo de repetições. | Correto. A leitura de probabilidade seria legítima em um intervalo de credibilidade bayesiano, e é por isso que o erro é tão comum e tão pouco danoso na prática, sem deixar de ser erro em um artigo.
- Correta, e é assim que o intervalo deve ser interpretado. | É a leitura intuitiva, e ela atribui probabilidade a um parâmetro fixo.
- Incorreta porque o intervalo deveria ser de 99%. | O nível de confiança é uma escolha, e não a origem do erro.
- Incorreta porque a taxa verdadeira nunca é conhecível. | Não é conhecível, e isso não é o que torna a frase incorreta.
- Correta apenas se a distribuição for normal. | A forma da distribuição não converte confiança em probabilidade do parâmetro.
@ cap-9-o-que-o-intervalo-de-confianca-diz

? [dificil] O d de Cohen da redução de área em quatro semanas foi 0,34, classificado como efeito pequeno. Um revisor conclui que o achado é clinicamente irrelevante. Qual a resposta adequada?
+ O d apenas expressa a diferença em desvios padrão, e a variabilidade dessa variável é enorme; relevância clínica se argumenta com conhecimento da doença. | Correto. Quinze pontos percentuais a mais de redução em quatro semanas antecipam a cicatrização, e a própria redução de 40% em quatro semanas é marcador prognóstico reconhecido, como mostra o Capítulo 13.
- O revisor está certo, e o desfecho deveria ser abandonado. | Aceitar a tabela de pontos de corte como veredito clínico é justamente o erro.
- O d de Cohen não se aplica a desfechos percentuais. | Aplica-se a qualquer variável contínua.
- O correto seria recalcular o d com a amostra completa. | O cálculo já usa os participantes com a medida disponível.
- Deve-se apresentar apenas o valor de p, que foi significativo. | Trocar o tamanho de efeito pelo valor de p é retroceder ao problema que o Capítulo 10 descreve.
@ cap-9-o-intervalo-do-que-interessa-a-diferenca
:::

## Exercícios

::: exercicio 1
O intervalo de confiança de 95% da diferença absoluta vai de 3,6 a 31,2 pontos
percentuais. Escreva, em uma frase que um clínico entenda, o que isso significa
para a decisão de usar o tratamento.

--- gabarito
Os dados são compatíveis com um benefício tão pequeno quanto quase quatro
cicatrizações a mais por cem pacientes tratados, e tão grande quanto trinta e
uma. Como até o limite inferior é um benefício, o estudo aponta para um efeito
real, mas não permite dizer se ele é modesto ou expressivo. É essa indefinição,
e não a existência do efeito, que justificaria um estudo maior.
:::

::: exercicio 2
O intervalo do número necessário para tratar vai de 3,2 a 27,9. Por que ele é
tão assimétrico em torno da estimativa de 5,8?

--- gabarito
Porque o NNT é o inverso da diferença absoluta, e inverter uma escala a distorce.
O limite superior da diferença, 31,2 pontos percentuais, vira 1 dividido por
0,312, ou 3,2. O limite inferior, 3,6 pontos percentuais, vira 1 dividido por
0,036, ou 27,9. Uma diferença absoluta pequena no denominador produz um NNT
enorme, e é por isso que a incerteza se concentra toda no extremo superior.
:::

::: exercicio 3
Um colega afirma: "o intervalo de confiança de 95% da cicatrização no grupo
tratado é de 60,7% a 79,0%, logo há 95% de probabilidade de a taxa verdadeira
estar nesse intervalo". Essa frase está correta?

--- gabarito
Ela está tecnicamente incorreta, embora seja a leitura que quase todo mundo faz.
Na estatística frequentista, a taxa verdadeira é um valor fixo e desconhecido:
ou está no intervalo ou não está, e não há probabilidade envolvida. Os 95%
descrevem o desempenho do método ao longo de repetições do estudo, não a chance
deste intervalo específico.

Vale dizer que a interpretação de probabilidade seria legítima em um intervalo
de credibilidade bayesiano, que responde exatamente a essa pergunta, e que na
prática os dois costumam coincidir numericamente quando não há informação prévia
forte. Isso explica por que o erro é tão comum e tão pouco danoso na prática,
mas ele continua sendo um erro quando escrito em um artigo.
:::

::: exercicio 4
No jamovi, calcule o intervalo de confiança de 95% da proporção de infecção da
ferida no grupo controle, que foi de 10 em 100. Compare com o método de Wald.

--- gabarito
A proporção é 10%. Por Wilson, o intervalo vai de 5,5% a 17,4%.
Por Wald, de 4,1% a 15,9%. A diferença entre os dois já é perceptível aqui,
porque a proporção está longe de 50%, e cresceria se o evento fosse mais raro.
Com dois eventos em cem, por exemplo, Wald produziria um limite inferior
negativo, que é impossível.
:::

::: exercicio 5
A diferença de médias na redução de área em quatro semanas foi de 14,8 pontos
percentuais, com intervalo de 2,4 a 27,2, e d de Cohen de 0,34. Um revisor
escreve que "o efeito é pequeno e provavelmente sem importância clínica".
Responda.

--- gabarito
O revisor confundiu tamanho padronizado com relevância clínica. O d de 0,34 diz
apenas que a diferença equivale a cerca de um terço do desvio padrão, e o desvio
padrão dessa variável é grande porque a evolução das úlceras é muito
heterogênea. A pergunta clínica é outra: quinze pontos percentuais a mais de
redução de área em quatro semanas antecipam a cicatrização e reduzem o tempo de
curativo. Além disso, a própria redução de 40% em quatro semanas é um marcador
prognóstico reconhecido, como mostra o Capítulo 13. Relevância clínica se
argumenta com conhecimento da doença, nunca com uma tabela de pontos de corte de
d.
:::

::: exercicio 6
Se o estudo tivesse incluído 400 participantes por grupo em vez de 92, e as
proporções observadas fossem exatamente as mesmas, o que aconteceria com a
estimativa e com o intervalo?

--- gabarito
A estimativa continuaria 70,7% e 53,3%, e a diferença continuaria 17,4 pontos
percentuais: o tamanho da amostra não muda a estimativa pontual. O intervalo,
sim, encolheria a pouco mais da metade da largura atual, porque a precisão
melhora com a raiz quadrada do tamanho da amostra e a raiz de 400 dividida pela
raiz de 92 é cerca de 2,1. O estudo maior não encontraria um efeito diferente:
saberia com mais precisão qual é o efeito.
:::

::: agora
1. Percorra o seu manuscrito e verifique se **todo** resultado principal tem
   estimativa e intervalo de confiança. Onde só houver valor de p, acrescente.
2. Se o seu desfecho é binário, calcule a diferença absoluta e o número
   necessário para tratar na calculadora deste capítulo, e apresente os dois.
3. Leia o limite inferior do intervalo do seu desfecho primário e pergunte: se o
   efeito verdadeiro fosse exatamente esse, eu ainda recomendaria o tratamento?
   A resposta é o que deve estar na sua conclusão.
:::

## Recursos

- [CONSORT Statement](https://www.consort-statement.org/) — item 17b, sobre
  apresentar tamanho de efeito e precisão para cada desfecho.
- [jamovi](https://www.jamovi.org/) — os intervalos de Wilson estão em
  Frequencies, e os de diferença de médias, em T-Tests.
- [Statement on p-values, American Statistical Association](https://doi.org/10.1080/00031305.2016.1154108)
  — a declaração de 2016, cujo princípio final recomenda relatar estimativa e
  incerteza no lugar de decisões dicotômicas.

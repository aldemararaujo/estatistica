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

? [facil] O estudo observou 70,7% de cicatrização no grupo do aspirado. O que esse número é?
+ Uma estimativa pontual: o melhor palpite sobre a proporção que o tratamento produziria na população de onde a amostra veio. | Correto. O estudo mediu o que aconteceu com 184 pessoas específicas, e o interesse nunca são elas: é o próximo paciente, que não participou de nada. Entre uma coisa e outra existe um salto, e o intervalo de confiança é a medida desse salto.
- O valor verdadeiro da eficácia do tratamento. | Se fosse o valor verdadeiro, não haveria incerteza a relatar e o intervalo de confiança não existiria. Nenhum estudo mede o valor verdadeiro; todos estimam.
- A probabilidade de o próximo paciente cicatrizar. | O próximo paciente pode diferir dos participantes em idade, gravidade da úlcera e adesão à compressão. A estimativa vale para a população de onde a amostra veio, e transportá-la exige julgamento clínico.
- A proporção de pacientes que cicatrizariam sem tratamento algum. | Essa é a proporção do grupo controle, 53,3%. Os 70,7% descrevem quem recebeu o aspirado somado à terapia compressiva.
- Um valor sem utilidade, por vir de amostra pequena. | A amostra é pequena para a precisão desejada, e isso se expressa na largura do intervalo, não na inutilidade da estimativa. Estimativa imprecisa continua sendo informação.
@ cap-9-todo-resultado-e-uma-estimativa

? [facil] Um artigo escreve: "95% dos pacientes cicatrizam entre 60,7% e 79,0%". Qual o problema?
+ A frase confunde incerteza sobre uma estimativa com variação entre pessoas, e assim não significa nada. | Correto. O intervalo de confiança descreve o quanto se sabe sobre uma proporção única, e não a faixa em que os pacientes se distribuem. A faixa entre pessoas se descreve com quartis, como no Capítulo 8.
- Falta apenas dizer que o intervalo é de 95% de confiança. | Acrescentar a palavra confiança não conserta a frase, porque o erro está em atribuir ao paciente uma faixa que descreve a estimativa.
- O intervalo deveria ser o da diferença entre os grupos. | O intervalo da diferença é de fato o que interessa para a conclusão do estudo, e ainda assim o erro desta frase persistiria em qualquer intervalo.
- Os limites estão trocados, e o correto seria de 79,0% a 60,7%. | Os limites estão na ordem certa. O problema é conceitual, e não de ordenação.
- Nenhum: é a leitura habitual do intervalo de confiança. | É uma leitura frequente e é errada. Cada paciente cicatriza ou não cicatriza; nenhum deles cicatriza "70,7%".
@ cap-9-o-que-o-intervalo-de-confianca-diz

? [facil] Uma figura traz barras de erro sobre as médias de cada grupo, sem dizer o que elas representam. Por que isso é um problema?
+ Porque barra de desvio padrão e barra de intervalo de confiança têm larguras muito diferentes e significados diferentes, e o leitor não tem como saber qual está vendo. | Correto. O desvio padrão descreve a dispersão entre pacientes; o intervalo descreve a incerteza sobre a média. A legenda precisa dizer qual dos dois foi desenhado, e é devolutiva frequente de revisor quando não diz.
- Porque barras de erro não devem aparecer em artigos clínicos. | Elas devem aparecer, e são a maneira usual de mostrar incerteza em uma figura. O que não pode faltar é a legenda.
- Porque a figura deveria mostrar cada paciente individualmente. | Mostrar os pontos individuais é uma boa prática em amostras pequenas, e não é o que resolve a ambiguidade da barra sem legenda.
- Porque o desvio padrão nunca deve ser representado graficamente. | Pode ser, e às vezes é o mais informativo. O problema é apresentá-lo sem identificação.
- Porque a barra de erro substitui o valor de p. | Uma coisa não substitui a outra, e o capítulo defende justamente apresentar estimativa e intervalo. A falha aqui é de legenda.
@ cap-9-o-que-o-intervalo-de-confianca-diz

? [facil] O número necessário para tratar deste estudo é 5,8. O que isso quer dizer para o clínico?
+ Que para cada seis pacientes tratados, um cicatriza que não teria cicatrizado. | Correto. O NNT é a diferença absoluta virada do avesso, e é a medida que fala em pacientes. Arredonda-se para cima, porque não se trata seis décimos de paciente.
- Que 5,8% dos pacientes se beneficiam do tratamento. | O NNT não é porcentagem. A proporção que se beneficia é a própria diferença absoluta, de 17,4 pontos percentuais.
- Que são necessárias 5,8 semanas para observar o efeito. | O NNT não tem unidade de tempo. O tempo de observação deste estudo é de doze semanas, definido no protocolo.
- Que o tratamento é 5,8 vezes melhor que o controle. | Uma razão entre os grupos seria o risco relativo, de 1,33, ou a razão de chances, de 2,11. O NNT não é razão entre grupos.
- Que a cada 5,8 pacientes um sofre evento adverso. | Esse seria o número necessário para causar dano, calculado sobre o desfecho de segurança, e não sobre a cicatrização.
@ cap-9-ler-cada-medida-pelo-que-ela-diz

? [media] O mesmo desfecho deste estudo produz risco relativo de 1,33 e razão de chances de 2,11. Por que os dois números são tão diferentes?
+ Porque a razão de chances se afasta do risco relativo quando o desfecho é frequente, e aqui mais da metade dos pacientes cicatrizou. | Correto. Com desfecho comum, a razão de chances exagera a impressão de efeito em relação ao risco relativo. Quando o desfecho é raro, as duas quase coincidem, e é daí que vem o hábito de tratá-las como intercambiáveis.
- Porque um foi calculado com as perdas e o outro sem. | Ambas saem da mesma tabela de contingência, com os mesmos 184 participantes analisados.
- Porque a razão de chances corrige para as variáveis basais. | Ajuste por variáveis basais é assunto da regressão, no Capítulo 12. A razão de chances bruta desta tabela não ajusta nada.
- Porque a razão de chances é sempre o dobro do risco relativo. | Não há relação fixa entre as duas. A distância entre elas depende de quão frequente é o desfecho.
- Porque uma usa o método de Wilson e a outra o de Wald. | O método do intervalo afeta os limites, e não a estimativa pontual de cada medida.
@ cap-9-ler-cada-medida-pelo-que-ela-diz

? [media] Por que a imprensa e a indústria costumam preferir o risco relativo à diferença absoluta?
+ Porque, quando o desfecho é raro, o risco relativo soa impressionante enquanto a diferença absoluta é minúscula. | Correto. Dobrar um risco de um em dez mil produz risco relativo de 2,00 e diferença absoluta de um em dez mil. As duas descrevem o mesmo dado e causam impressões opostas. Neste estudo o desfecho é frequente e as duas medidas contam a mesma história.
- Porque o risco relativo é mais fácil de calcular. | Ambos saem da mesma tabela com uma conta de uma linha. A preferência é retórica, e não operacional.
- Porque a diferença absoluta não pode ser calculada em ensaios clínicos. | Pode, e é a medida mais útil na clínica, por ser a única que fala em pacientes em vez de razões.
- Porque o risco relativo tem intervalo de confiança mais estreito. | A largura de cada intervalo depende da escala em que a medida vive. Não há garantia de que o do risco relativo seja mais estreito, e não é isso que motiva a escolha.
- Porque a diferença absoluta depende de o desfecho ser binário. | As duas medidas dependem de desfecho binário. Para variável contínua, usa-se diferença de médias, como na segunda tabela deste capítulo.
@ cap-9-ler-cada-medida-pelo-que-ela-diz

? [media] Em um estudo cuja diferença absoluta não é estatisticamente significativa, o que acontece com o intervalo do número necessário para tratar?
+ Ele passa pelo infinito, e deixa de fazer sentido apresentá-lo. | Correto. Se o intervalo da diferença cruza o zero, invertê-lo faz o NNT saltar para o infinito e reaparecer do outro lado, como número necessário para causar dano. Apresentá-lo nessa situação confunde mais do que informa.
- Ele fica muito estreito, porque a diferença é pequena. | É o oposto: quanto mais próximo de zero o denominador, mais largo e instável fica o NNT.
- Ele se torna negativo em toda a extensão. | Só a parte além do zero corresponde a dano. O intervalo não vira negativo por inteiro; ele se parte.
- Ele permanece válido, bastando arredondar os extremos. | Arredondar não conserta uma descontinuidade. O problema é estrutural, e não de apresentação.
- Nada muda, porque o NNT independe do intervalo da diferença. | O NNT é uma transformação direta da diferença absoluta, e seu intervalo sai da inversão dos extremos dela.
@ cap-9-ler-cada-medida-pelo-que-ela-diz

? [media] Cada intervalo de proporção deste estudo tem cerca de dezoito pontos percentuais de largura. O que essa largura representa?
+ A ignorância que restou depois de estudar noventa e dois pacientes por grupo. | Correto. A largura é a resposta honesta à pergunta "quanto eu sei?". Dezoito pontos é muito, e é o preço do tamanho escolhido no Capítulo 6.
- A variação da cicatrização entre os pacientes do estudo. | Variação entre pacientes se descreve com desvio padrão e quartis. O intervalo descreve incerteza sobre a estimativa.
- A margem de erro da aferição da área da úlcera. | Erro de aferição é outro assunto, tratado na concordância entre observadores. O intervalo aqui vem do tamanho da amostra, e não do instrumento.
- A diferença entre os dois grupos do estudo. | A diferença entre os grupos é 17,4 pontos percentuais, e tem intervalo próprio, de 3,6 a 31,2.
- A probabilidade de o estudo estar errado. | Nenhuma largura de intervalo mede probabilidade de erro do estudo. Vieses de seleção e de aferição não entram nessa conta.
@ cap-9-a-largura-importa-mais-que-os-extremos

? [media] Em um desfecho de segurança com 2 eventos em 100 participantes, o método de Wald produz limite inferior negativo. Por quê?
+ Porque Wald trata a proporção como simétrica em torno da estimativa, e perto de zero essa simetria leva a valores impossíveis. | Correto. É a falha do método justamente nas situações em que ele mais seria necessário: eventos raros e amostras pequenas. Wilson não ultrapassa os limites lógicos de zero e um, e é o que este livro usa.
- Porque duas observações são poucas para calcular qualquer intervalo. | Há métodos que funcionam com contagens pequenas, e Wilson é um deles. O problema é do método de Wald, e não da existência de intervalo.
- Porque o cálculo exige correção de continuidade. | A correção de continuidade atenua o problema em alguns casos e não é o que resolve a violação do limite lógico.
- Porque o desfecho de segurança precisa de nível de confiança de 99%. | Ampliar o nível de confiança alarga o intervalo e agrava a ultrapassagem, em vez de corrigi-la.
- Porque o denominador deveria ser o total dos dois grupos. | O intervalo é da proporção dentro de um grupo, e o denominador correto é o daquele grupo.
@ cap-9-o-que-o-intervalo-de-confianca-diz

? [media] O d de Cohen da redução de área em quatro semanas foi 0,34. O que exatamente esse número expressa?
+ Que a diferença entre as médias equivale a cerca de um terço de um desvio padrão daquela variável. | Correto. É uma diferença expressa em unidades de dispersão, e serve para comparar resultados de áreas diferentes. As convenções de 0,2, 0,5 e 0,8 são úteis para isso e péssimas para decidir conduta clínica, porque não sabem nada sobre a doença.
- Que 34% dos pacientes tiveram redução maior no grupo tratado. | O d não é proporção de pacientes. A comparação de proporções seria outra análise, com outro desfecho.
- Que a redução média foi 34% maior no grupo tratado. | A diferença observada foi de 14,8 pontos percentuais entre médias de 45,4% e 30,6%. O d é uma padronização dessa diferença, e não uma razão entre elas.
- Que o efeito tem 34% de probabilidade de ser real. | Nenhuma medida de tamanho de efeito exprime probabilidade de o efeito existir. Essa pergunta é do Capítulo 10, e nem lá se responde assim.
- Que a variável precisa de 0,34 de correção antes da análise. | Não existe tal correção. O d é resultado da análise, e não um ajuste aplicado aos dados.
@ cap-9-o-tamanho-de-efeito-de-uma-variavel-continua

? [dificil] Dois intervalos de confiança de 95% de grupos distintos **não** se sobrepõem. O que se pode concluir?
+ Que a diferença em regra é estatisticamente significativa, embora a conclusão correta continue vindo do intervalo da diferença. | Correto. A relação é assimétrica, e é isso que quase todo leitor erra: não se sobrepor implica, em geral, significância; sobrepor-se não implica coisa alguma. Como o critério da não sobreposição é conservador, o hábito certo é sempre olhar o intervalo da diferença.
- Que a diferença certamente não é significativa. | É a inversão do raciocínio. A não sobreposição aponta para diferença, e não contra ela.
- Nada, exatamente como no caso da sobreposição. | Aqui há assimetria: a sobreposição é que não permite concluir. A não sobreposição é informativa, ainda que grosseira.
- Que os dois grupos têm variabilidades diferentes. | Sobreposição, ou sua ausência, não informa sobre variabilidade dentro dos grupos.
- Que a amostra foi suficiente para o desfecho estudado. | Suficiência se julga pela largura do intervalo da diferença e pela relevância clínica do que ele exclui, e não pela posição relativa de dois intervalos.
@ cap-9-o-intervalo-do-que-interessa-a-diferenca

? [dificil] O intervalo do risco relativo deste estudo vai de 1,05 a 1,67. Por que a ausência do zero nesse intervalo não é o que importa?
+ Porque em medidas de razão o valor de nenhum efeito é 1, e não 0: é a exclusão do 1 que indica diferença entre os grupos. | Correto. Diferença absoluta e razão vivem em escalas distintas, e cada uma tem seu valor nulo. Para a diferença de 17,4 pontos, o nulo é o zero; para o risco relativo e a razão de chances, é o um.
- Porque o zero é impossível em qualquer intervalo de confiança. | O zero é perfeitamente possível, e aparece sempre que uma diferença absoluta não é significativa.
- Porque o risco relativo não admite interpretação por intervalo. | Admite, e é assim que ele deve ser apresentado. O que muda é o valor de referência.
- Porque o intervalo do risco relativo é calculado em escala logarítmica. | Ele de fato é construído em escala logarítmica, o que explica a assimetria dos limites, e não é isso que define qual valor representa ausência de efeito.
- Porque só a diferença absoluta pode sustentar conclusão clínica. | A diferença absoluta é a mais útil na clínica, e as medidas de razão sustentam conclusão igualmente, desde que lidas na escala correta.
@ cap-9-o-intervalo-do-que-interessa-a-diferenca

? [dificil] Um pesquisador quer reduzir a largura do intervalo do seu desfecho primário a um terço da atual. Quantas vezes maior precisa ser a amostra?
+ Cerca de nove vezes, porque a precisão melhora com a raiz quadrada do tamanho da amostra. | Correto. Para dividir a largura por três é preciso multiplicar o tamanho por três ao quadrado. É a mesma relação que faz quadruplicar o estudo reduzir a largura pela metade, e é a razão de estudos pequenos raramente resolverem alguma coisa.
- Três vezes maior, na mesma proporção da redução desejada. | Seria assim se a precisão melhorasse linearmente com o tamanho, e ela não melhora. Triplicar a amostra reduz a largura a cerca de 58% da atual, e não a um terço.
- Seis vezes maior, o dobro da redução desejada. | Não há fator dois envolvido. A relação é quadrática, e não proporcional nem duplicada.
- Vinte e sete vezes maior, pelo cubo da redução. | O expoente é dois, e não três. A raiz que governa a precisão é a quadrada.
- Não é possível saber sem conhecer a proporção observada. | A proporção afeta a largura absoluta do intervalo, e não a relação entre tamanho de amostra e ganho de precisão, que vale em geral.
@ cap-9-a-largura-importa-mais-que-os-extremos

? [dificil] Um ensaio termina com diferença absoluta de 2,0 pontos percentuais e intervalo de menos 1,5 a mais 5,5. A menor diferença clinicamente relevante havia sido fixada em 10 pontos no protocolo. O que se conclui?
+ Que o estudo, apesar de não significativo, excluiu com boa precisão o efeito que interessava: o limite superior fica bem abaixo dos 10 pontos. | Correto. É a conclusão negativa útil, e ela só é possível porque a menor diferença relevante foi declarada antes. Dizer apenas "não houve diferença" desperdiçaria a informação mais valiosa do estudo.
- Que o estudo foi inconclusivo por falta de poder. | Inconclusivo seria um intervalo largo, admitindo desde prejuízo até benefício relevante. Aqui o intervalo é estreito e responde à pergunta.
- Que o tratamento tem efeito, porque a estimativa é positiva. | A estimativa é positiva e o intervalo cruza o zero: os dados são compatíveis com pequeno prejuízo. O que se sustenta é a exclusão de efeito relevante, e não a afirmação de efeito.
- Que a menor diferença relevante foi mal escolhida e deve ser revista. | Revisar o limiar depois de ver o resultado é justamente o que o registro prévio impede. Ele foi fixado antes exatamente para permitir esta leitura.
- Que é preciso repetir o estudo com amostra maior. | Um estudo maior estreitaria ainda mais um intervalo que já respondeu à pergunta clínica formulada.
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

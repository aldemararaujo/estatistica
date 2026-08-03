::: caso
Até aqui o desfecho primário foi tratado como uma pergunta de sim ou não:
cicatrizou em doze semanas ou não cicatrizou. Isso desperdiça informação. Uma
úlcera que fechou aos vinte dias e outra que fechou aos oitenta e três entraram
na mesma casinha da tabela, e não deveriam. Este capítulo recupera o tempo.
:::

## O problema que só a análise de sobrevida resolve

Chama-se análise de sobrevida por razões históricas, porque nasceu estudando
morte, mas o método serve a qualquer evento cuja data importe: cicatrização,
recidiva, alta, falha de prótese, engravidar. O nome moderno, análise de tempo
até o evento, descreve melhor.

O que a torna necessária é a **censura**. Ao fim das doze semanas, 86 das 200
úlceras não haviam cicatrizado. Elas não são fracassos definitivos: são pessoas
cujo evento ainda não tinha ocorrido quando a observação parou. Além delas, 16
participantes saíram do estudo antes do fim, e sobre eles se sabe apenas que não
haviam cicatrizado até o dia em que sumiram.

Nenhuma das duas situações cabe em uma média de tempo. Excluir os censurados
enviesa o resultado, porque os que demoram mais são justamente os que ainda não
tiveram o evento. Tratá-los como se tivessem cicatrizado no último dia é pior
ainda. A análise de sobrevida existe para usar exatamente a informação que cada
um traz: este aqui esteve sob observação por 84 dias sem cicatrizar, aquele saiu
aos 37 sem cicatrizar, e este outro cicatrizou aos 22.

::: atencao Duas colunas que só existem juntas
No banco, `tempo_ate_cicatrizacao_dias` e `evento_cicatrizacao` são inseparáveis.
Um tempo de 84 dias com evento igual a 1 significa uma úlcera que cicatrizou no
último dia; o mesmo 84 com evento igual a 0 significa uma úlcera que nunca
cicatrizou. Analisar a coluna de tempo sozinha, calculando sua média, é o erro
mais frequente de quem começa neste assunto, e produz um número sem sentido
algum.
:::

## A curva de Kaplan-Meier

O método de Kaplan-Meier constrói a curva em degraus: a cada dia em que alguém
cicatriza, a proporção de úlceras ainda abertas cai um degrau, e o tamanho do
degrau leva em conta quantas pessoas ainda estavam sob observação naquele
momento. Quem foi censurado antes deixa de contar dali em diante, sem puxar a
curva para lado nenhum.

Os resultados do estudo:

| | Aspirado | Controle |
|---|---|---|
| Eventos | 65 de 100 | 49 de 100 |
| Cicatrização acumulada em 4 semanas | 23,4% | 7,0% |
| Cicatrização acumulada em 8 semanas | 53,9% | 35,0% |
| Cicatrização acumulada em 12 semanas | 69,3% | 51,3% |
| Tempo mediano até cicatrizar | 50 dias | 82 dias |

A tabela conta uma história que o desfecho binário não contava. A diferença entre
os grupos aparece cedo e é proporcionalmente maior na quarta semana, quando o
grupo tratado já triplica o controle. O tempo mediano cai de 82 para 50 dias: um
mês inteiro a menos de curativo, consulta e ferida aberta.

::: nota Por que o tempo mediano aqui não é o mesmo do protocolo
Se você calcular a mediana do tempo apenas entre os que cicatrizaram, obterá 36 e
46 dias. É um número diferente e responde a outra pergunta: quanto demoraram os
que cicatrizaram. A mediana de Kaplan-Meier, 50 e 82 dias, é o tempo em que
metade de **todos** os participantes já havia cicatrizado, contando os que não
cicatrizaram. É essa a medida que se publica, porque a outra descarta em silêncio
justamente os piores casos.
:::

## O teste de log-rank

Comparar duas curvas exige um teste próprio, porque a pergunta não é sobre uma
proporção em um momento, e sim sobre o comportamento inteiro das curvas.

O log-rank percorre cada instante em que houve evento, calcula quantos eventos se
esperariam em cada grupo se as curvas fossem iguais, e acumula as diferenças. No
estudo, ele devolve qui-quadrado de 9,26, com um grau de liberdade, e p de 0,002.

Compare com o valor de p do desfecho binário, que foi 0,015. O mesmo estudo, com
os mesmos pacientes, produz evidência mais forte quando a informação do tempo é
usada. Não houve truque: houve aproveitamento de dados que a dicotomização
jogava fora. Essa é a razão prática para preferir o desfecho de tempo até o
evento sempre que a data for conhecida.

## O modelo de Cox

O log-rank compara curvas, mas não estima o tamanho do efeito nem permite
ajustar por outras variáveis. Quem faz isso é o modelo de riscos proporcionais de
Cox, que é para o tempo até o evento o que a regressão logística é para o
desfecho binário.

| Modelo | Razão de riscos do tratamento | IC 95% | p |
|---|---|---|---|
| Bruto | 1,76 | 1,21 a 2,55 | 0,003 |
| Ajustado | 2,10 | 1,43 a 3,08 | < 0,001 |

E o modelo ajustado completo:

| Variável | Razão de riscos | IC 95% | p |
|---|---|---|---|
| Aspirado de medula óssea | 2,10 | 1,43 a 3,08 | < 0,001 |
| Logaritmo da área inicial | 0,59 | 0,46 a 0,76 | < 0,001 |
| Logaritmo da duração | 0,74 | 0,55 a 0,99 | 0,044 |
| Diabetes | 0,50 | 0,29 a 0,85 | 0,011 |
| Adesão adequada | 2,22 | 1,36 a 3,62 | 0,001 |

A razão de riscos de 2,10 significa que, a cada instante, entre os que ainda têm
a úlcera aberta, a taxa de cicatrização no grupo tratado é 2,1 vezes a do
controle. Note o que ela **não** diz: não diz que o dobro dos pacientes
cicatriza, nem que cicatrizam na metade do tempo. Razão de riscos é razão de
taxas instantâneas, e é por isso que ela convive tranquilamente com uma diferença
absoluta de 17,4 pontos percentuais em doze semanas.

As demais linhas repetem, com outra régua, o que a regressão logística do
Capítulo 12 já havia mostrado: área e duração pioram, diabetes piora, adesão
melhora. Que dois modelos diferentes, sobre desfechos diferentes, concordem tão
bem é um bom sinal sobre a consistência interna do estudo.

### A suposição que dá nome ao modelo

O modelo de Cox supõe **riscos proporcionais**: a razão entre as taxas dos dois
grupos é a mesma ao longo de todo o seguimento. Se o tratamento agisse só nas
primeiras semanas e depois perdesse efeito, a suposição estaria violada e a razão
de riscos única seria uma média enganosa de dois períodos diferentes.

Verificar é obrigatório, e há três caminhos: olhar se as curvas de Kaplan-Meier
se cruzam, o que aqui não acontece; examinar o gráfico dos resíduos de
Schoenfeld contra o tempo, que deve ser plano; e incluir no modelo um termo de
interação entre o tratamento e o tempo, que não deve ser significativo. Quando a
suposição falha, relatam-se as curvas e a diferença de cicatrização em momentos
definidos, em vez de uma razão de riscos única.

::: jamovi
1. A análise de sobrevida não vem no jamovi básico. Abra **Modules**, a
   **jamovi library**, e procure por survival: o módulo mais usado para isso se
   chama **Death Watch**.
2. Instalado o módulo, informe `tempo_ate_cicatrizacao_dias` como tempo,
   `evento_cicatrizacao` como estado, com 1 marcando o evento, e `grupo` como
   fator.
3. Marque a **curva de Kaplan-Meier**, a tabela de sobrevida em tempos
   escolhidos, o **log-rank** e a **mediana com intervalo de confiança**.
4. Para o modelo de Cox, acrescente as covariáveis e peça as razões de riscos com
   intervalo de confiança e o teste da suposição de proporcionalidade.
5. Na figura, sempre inclua a **tabela de participantes sob risco** abaixo do
   eixo do tempo. Sem ela, o leitor não sabe se a ponta direita da curva se apoia
   em oitenta pessoas ou em três.
:::

::: abas
== Quando usar o desfecho de tempo até o evento
Sempre que a data do evento for conhecida, que o seguimento for longo o bastante
para haver variação de tempo, e que houver censura, seja por fim de estudo, seja
por perda. Ganha-se poder estatístico e ganha-se uma informação clinicamente
importante, que é a rapidez do efeito.

== Quando o binário basta
Quando o evento só pode ser avaliado em um momento fixo, como uma resposta
aferida em consulta única; quando o seguimento é curto e quase todos são
avaliados no mesmo instante; e quando a data do evento é imprecisa. Uma data de
cicatrização anotada como "entre a consulta de quatro e a de oito semanas" é
dado intervalar, e forçá-la em uma análise de sobrevida comum introduz um erro
que ninguém enxerga depois.
:::

::: revisor
**"Os autores calcularam a média do tempo até o evento incluindo os
censurados."** Sem sentido. Use Kaplan-Meier e relate a mediana.

**"Os pacientes censurados foram excluídos da análise."** Isso enviesa o
resultado, e para o lado otimista, porque exclui preferencialmente quem demora
mais.

**"A curva de Kaplan-Meier é apresentada sem a tabela de pacientes sob risco."**
Exigência básica do CONSORT para figuras de sobrevida.

**"A suposição de riscos proporcionais não foi verificada."** Descreva como
verificou. Se as curvas se cruzam, não relate razão de riscos única.

**"A razão de riscos é interpretada como se fosse risco relativo."** São coisas
diferentes. Razão de riscos compara taxas instantâneas ao longo do tempo; risco
relativo compara proporções acumuladas em um momento.

**"O número de eventos não está informado."** Em análise de sobrevida, o que
determina a precisão é o número de eventos, não o de participantes. Um estudo
com quinhentos pacientes e doze eventos é um estudo pequeno.
:::

## Exercícios

::: exercicio 1
No banco, o participante P003 tem tempo de 84 dias e evento igual a 0, e o P005
tem tempo de 77 dias e evento igual a 1. Descreva o que aconteceu com cada um.

--- gabarito
P003 foi seguido pelas doze semanas completas e chegou ao fim do estudo com a
úlcera ainda aberta: é uma observação censurada pelo fim do seguimento. P005
cicatrizou no septuagésimo sétimo dia, dentro do período de observação: é um
evento. Os dois contribuem para a curva de maneiras diferentes, e nenhum dos dois
pode ser descartado.
:::

::: exercicio 2
O valor de p do log-rank foi 0,002, e o do qui-quadrado sobre o desfecho binário
foi 0,015. Por que a mesma comparação, nos mesmos pacientes, produz evidência
mais forte na análise de sobrevida?

--- gabarito
Porque a análise de sobrevida usa a informação de quando cada evento ocorreu,
enquanto a dicotomização em doze semanas trata como iguais uma úlcera que fechou
aos vinte dias e outra que fechou aos oitenta e três. Mais informação aproveitada
produz estimativa mais precisa e, portanto, teste mais poderoso. É o mesmo
princípio que desaconselha dicotomizar variáveis contínuas, visto no Capítulo 11.
:::

::: exercicio 3
A razão de riscos ajustada foi 2,10. Um colega escreve na discussão que "o
tratamento dobra a chance de cicatrização". Corrija a frase.

--- gabarito
A frase confunde razão de riscos com risco relativo. O correto é dizer que, entre
os pacientes que ainda tinham a úlcera aberta, a taxa instantânea de cicatrização
foi 2,1 vezes maior no grupo tratado. Se o colega quiser falar em proporção de
pacientes, o número é outro: 69,3% contra 51,3% em doze semanas, com risco
relativo de 1,33.
:::

::: exercicio 4
Por que o tempo mediano até a cicatrização no grupo controle, 82 dias, está tão
perto do fim do seguimento? O que aconteceria se o estudo tivesse durado apenas
oito semanas?

--- gabarito
Porque pouco mais da metade dos participantes do grupo controle cicatrizou dentro
das doze semanas, e a mediana é justamente o instante em que a curva cruza os
50%. Com oito semanas de seguimento, o grupo controle teria acumulado apenas 35%
de cicatrização e a mediana **não seria atingida**: o relato correto seria
"mediana não alcançada", e não um número inventado por extrapolação. É um bom
lembrete de que o tempo de seguimento se decide junto com o desfecho, no
planejamento.
:::

::: exercicio 5
No jamovi, com o módulo de sobrevida instalado, produza a curva de Kaplan-Meier
por grupo e localize nela os três números da tabela deste capítulo: 23,4%, 53,9%
e 69,3%.

--- gabarito
São os valores de cicatrização acumulada do grupo tratado em 28, 56 e 84 dias,
que na curva de sobrevida aparecem como o complemento, isto é, 76,6%, 46,1% e
30,7% de úlceras ainda abertas. Muitos programas desenham a curva descendente, de
úlceras abertas, e não a ascendente, de cicatrizações acumuladas. Verifique
sempre qual das duas está no eixo antes de ler qualquer número.
:::

::: exercicio 6
Suponha que as curvas dos dois grupos se cruzassem na oitava semana. O que isso
significaria clinicamente e o que você faria com o modelo de Cox?

--- gabarito
Significaria que o efeito do tratamento muda de direção ao longo do tempo, por
exemplo acelerando a cicatrização no início e perdendo efeito depois. A suposição
de riscos proporcionais estaria violada e a razão de riscos única seria uma média
enganosa. A conduta é abandonar a razão de riscos como medida principal e relatar
as curvas com diferenças de cicatrização em momentos definidos, ou usar modelos
que admitam efeito dependente do tempo.
:::

::: agora
1. Verifique se a sua ficha de coleta registra a **data** do evento, e não apenas
   se ele ocorreu. Se registrar, você tem um desfecho de tempo até evento e
   deveria usá-lo: ganha poder sem aumentar a amostra.
2. Confira se o seu banco tem as duas colunas inseparáveis, tempo e status, e se
   quem digita entendeu a diferença entre censurado e sem evento.
3. Escreva no plano de análise como a suposição de riscos proporcionais será
   verificada. Decidir isso depois de ver as curvas é escolher o método pelo
   resultado.
:::

## Recursos

- [CONSORT Statement](https://www.consort-statement.org/) — orientações sobre
  figuras de sobrevida e a tabela de participantes sob risco.
- [jamovi library](https://library.jamovi.org/) — onde se instala o
  módulo de análise de sobrevida.
- [EQUATOR Network](https://www.equator-network.org/) — recomendações de relato
  por tipo de estudo.

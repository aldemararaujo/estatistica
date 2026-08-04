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

::: quiz
? [facil] A área inicial das úlceras tem média de 10,5 cm² e mediana de 7,7 cm². Qual resumo deve ir para a Tabela 1?
+ Mediana e quartis, porque a distribuição é assimétrica à direita. | Correto. Apenas 67 das 200 úlceras têm área acima da média, e um resumo que descreve mal dois terços da amostra não serve, por mais correta que esteja a aritmética.
- Média e desvio padrão, porque são as medidas usuais. | Usuais não significa adequadas. Aqui a média é puxada por poucas úlceras enormes, uma delas de 66,4 cm².
- Os dois pares, para o leitor escolher. | Poluir a tabela transfere ao leitor uma decisão que era do autor.
- Média e amplitude, que mostra os extremos. | A amplitude depende inteiramente dos dois valores mais extremos e é a medida de dispersão menos estável.
- Moda e amplitude interquartil. | A moda quase nunca informa em variáveis contínuas.
@ cap-8-cada-tipo-de-variavel-pede-um-resumo

? [facil] Qual a diferença entre desvio padrão e erro padrão?
+ O desvio padrão descreve o quanto os participantes variam entre si; o erro padrão descreve a precisão com que a média foi estimada. | Correto. O desvio padrão entra na descrição da amostra; o erro padrão, na construção do intervalo de confiança do Capítulo 9.
- São a mesma coisa, com nomes diferentes. | São grandezas distintas, e o erro padrão encolhe conforme a amostra cresce, enquanto o desvio padrão não.
- O erro padrão descreve a variação entre participantes e o desvio padrão, a precisão da média. | É a troca invertida, e ela é frequente.
- O desvio padrão só se aplica a distribuições normais. | Pode ser calculado em qualquer distribuição, embora descreva melhor as simétricas.
- O erro padrão é o desvio padrão dividido pelo número de participantes. | É dividido pela **raiz** do número de participantes, e essa diferença é o motivo de a precisão melhorar devagar.
@ cap-8-cada-tipo-de-variavel-pede-um-resumo

? [media] Por que a Tabela 1 de um ensaio randomizado não deve trazer coluna de valor de p?
+ Porque se sabe de antemão que qualquer desequilíbrio surgiu por acaso: foi um sorteio que alocou os participantes. | Correto. Testar o que já se sabe verdadeiro responde a uma pergunta sem interesse e sugere que p acima de 0,05 autorizaria concluir comparabilidade, o que não autoriza.
- Porque a Tabela 1 é descritiva e testes não cabem em tabelas descritivas. | O argumento é lógico, e não formal: o problema é a pergunta que o teste responderia.
- Porque as variáveis basais raramente são normais. | A distribuição não é a questão aqui.
- Porque isso aumentaria o número de comparações múltiplas. | Multiplicidade é um problema real e adicional, e não o motivo central.
- Porque o CONSORT proíbe qualquer valor de p em tabelas. | O CONSORT desaconselha essa coluna específica, e valores de p aparecem legitimamente na tabela de desfechos.
@ cap-8-a-tabela-1-do-estudo

? [media] Como decidir se uma distribuição comporta a média?
+ Olhando o histograma: se a cauda de um lado for visivelmente mais longa, a mediana descreve melhor. | Correto. O teste de normalidade responde a uma pergunta que não interessa e responde mal: com amostra pequena quase nunca rejeita, e com amostra grande rejeita quase sempre.
- Aplicando o teste de Shapiro-Wilk e decidindo pelo valor de p. | É a pior herança dos manuais antigos: um critério que erra nas duas pontas e substitui o julgamento por um p.
- Verificando se média e mediana são exatamente iguais. | Coincidência exata é rara mesmo em distribuições simétricas; o que importa é a proximidade e a forma.
- Calculando o coeficiente de variação. | Mede dispersão relativa e não indica assimetria.
- Comparando a amostra com uma tabela de valores normais. | Não existe tal procedimento, e a forma se avalia pela própria distribuição observada.
@ cap-8-cada-tipo-de-variavel-pede-um-resumo

? [media] A redução de área em 12 semanas tem mediana de 100% nos dois grupos, embora a cicatrização tenha sido de 70,7% e 53,3%. Qual a explicação?
+ Efeito teto: em ambos os grupos mais da metade cicatrizou, e uma úlcera cicatrizada tem exatamente 100% de redução. | Correto. Como o participante do meio está, nos dois casos, dentro do conjunto dos que cicatrizaram, a mediana é 100% nos dois grupos. A mediana só discrimina onde ainda há variação na escala.
- Erro no cálculo das medianas. | O cálculo está certo, e a coincidência é consequência da escala, não de engano.
- As duas informações se contradizem e uma delas está errada. | Não se contradizem: descrevem aspectos diferentes dos mesmos dados.
- A mediana não deve ser usada para variáveis percentuais. | Pode ser usada; o que a inutiliza aqui é a saturação da escala.
- O grupo controle teve mais valores extremos. | Teve mais dispersão, o que aparece no desvio padrão, e não é o que explica a mediana idêntica.
@ cap-8-quando-o-resumo-esconde-o-resultado

? [dificil] Um artigo descreve a área inicial como "10,5 ± 9,4 cm²". Aponte os dois problemas.
+ A escolha do resumo, inadequado para distribuição assimétrica, e a notação, que não informa o que vem depois do símbolo. | Correto. O leitor não sabe se 9,4 é desvio padrão, erro padrão ou metade de um intervalo, e a notação sugere um limite inferior de 1,1 cm², implausível para uma amostra cujo menor valor é 0,8.
- Apenas a notação: o resumo está correto. | O resumo também está inadequado, pela assimetria.
- Apenas o resumo: a notação com ± é padrão consagrado. | É comum e ambíguo, e as recomendações de relato pedem que se escreva o que está entre parênteses.
- O número de casas decimais e a unidade de medida. | A precisão está razoável e a unidade está presente.
- A ausência do valor de p e do tamanho da amostra. | Nenhum dos dois pertence a essa descrição.
@ cap-8-cada-tipo-de-variavel-pede-um-resumo

? [dificil] Na Tabela 1 do caso condutor, o diabetes aparece em 17% do grupo tratado e 27% do controle. Qual conduta é correta?
+ Descrever o desequilíbrio e considerá-lo na análise ajustada, sem testá-lo. | Correto. O que decide é o tamanho do desequilíbrio e o efeito conhecido do diabetes sobre a cicatrização, e não a significância dele, que se sabe de antemão ser fruto do acaso.
- Aplicar um qui-quadrado e, se p for menor que 0,05, ajustar a análise. | Usar o p da Tabela 1 como gatilho para decidir o ajuste é exatamente o que o capítulo desaconselha.
- Refazer a randomização até obter grupos equilibrados. | Isso destruiria a aleatoriedade, que é a única propriedade que equilibra também o que ninguém mediu.
- Excluir participantes diabéticos para restaurar o equilíbrio. | Excluir depois da alocação quebra a randomização e a análise por intenção de tratar.
- Ignorar, porque a randomização garante comparabilidade. | Ela equilibra em média, ao longo de repetições, e não garante equilíbrio perfeito em um estudo particular.
@ cap-8-a-tabela-1-do-estudo

? [facil] Como se resume, na Tabela 1, uma variável nominal como diabetes?
+ Número absoluto e percentual: 17 (17,0). | Correto. Nominal e ordinal se resumem assim, com a diferença de que a ordinal segue a ordem natural das categorias. Média de variável nominal não existe, ainda que o programa a calcule quando a variável está codificada como 0 e 1.
- Média e desvio padrão dos códigos 0 e 1. | O jamovi calcula, porque leu a coluna como numérica, e o resultado não descreve nada. É por isso que o capítulo manda conferir o tipo de cada variável no Setup antes de qualquer análise.
- Mediana e quartis. | Mediana exige que os valores possam ser ordenados. Ter ou não ter diabetes não define uma ordem.
- Apenas o percentual, que é mais fácil de ler. | O número absoluto precisa aparecer, porque 17% de 100 e 17% de 12 são informações muito diferentes.
- Amplitude entre a menor e a maior categoria. | Amplitude é medida de dispersão de variável numérica, e não se aplica a categorias.
@ cap-8-cada-tipo-de-variavel-pede-um-resumo

? [facil] Para que serve a Tabela 1 de um artigo clínico?
+ Para mostrar com quem o estudo foi feito, de modo que o leitor julgue se aqueles resultados valem para os pacientes dele. | Correto. Ela descreve, e não compara. É a tabela que responde à pergunta "esses pacientes se parecem com os meus?", e é ela que decide se o artigo interessa a quem o lê.
- Para demonstrar que a randomização funcionou. | A randomização funciona por construção, e sua propriedade é probabilística, não verificável em um único estudo. Desequilíbrios são esperados e não indicam falha.
- Para comparar os grupos e mostrar que eles não diferem. | Comparar a linha de base de um ensaio randomizado é justamente o que o CONSORT desaconselha, e a coluna de valor de p não deve estar ali.
- Para apresentar os desfechos primário e secundários. | Os desfechos vêm nas tabelas seguintes. A Tabela 1 fica na linha de base, antes de qualquer resultado.
- Para justificar o tamanho da amostra escolhido. | O tamanho da amostra se justifica nos métodos, com a conta do Capítulo 6.
@ cap-8-a-tabela-1-do-estudo

? [facil] O tabagismo do estudo tem três categorias: nunca fumou, ex-fumante e fumante atual. Como resumi-lo?
+ Número absoluto e percentual de cada categoria, apresentadas na ordem natural. | Correto. É variável ordinal, e a ordem carrega informação: apresentar "ex-fumante" antes de "nunca fumou" desperdiça o que a escala tem de melhor.
- Média e desvio padrão, tratando as categorias como 1, 2 e 3. | Atribuir números às categorias não as torna numéricas. A distância entre nunca fumar e ser ex-fumante não é comparável à distância entre ex-fumante e fumante atual.
- Apenas a categoria mais frequente. | Informar só a moda descarta a distribuição inteira, e é justamente o tipo de omissão que o capítulo alerta a evitar.
- Mediana e amplitude interquartil das três categorias. | Mediana de variável ordinal com poucas categorias existe, e não é o resumo usual da Tabela 1, que pede a distribuição completa.
- Número absoluto e percentual, em ordem decrescente de frequência. | Reordenar por frequência destrói a ordem natural, que é o que distingue ordinal de nominal.
@ cap-8-cada-tipo-de-variavel-pede-um-resumo

? [facil] Um artigo informa "idade média de 62,34 anos" em um estudo com duzentos participantes. Qual o problema?
+ Precisão excessiva: as duas casas decimais sugerem uma exatidão que os dados não têm. | Correto. Uma casa basta para idade, peso e escores, e percentuais em estudo com duzentos participantes não precisam de decimal algum. É devolutiva frequente de revisor, e custa uma rodada de revisão.
- A idade deveria ser resumida por mediana. | A idade deste estudo é aproximadamente simétrica, e média com desvio padrão é o resumo adequado. O problema é o número de casas.
- Falta o intervalo de confiança da média. | A Tabela 1 descreve a amostra, e não estima parâmetros populacionais. Intervalo de confiança entra nos desfechos, no Capítulo 9.
- Falta comparar a idade entre os grupos. | Comparar a linha de base de um ensaio randomizado é o que este capítulo desaconselha.
- Nenhum: mais casas decimais significam mais rigor. | Mais casas significam mais dígitos, e não mais informação. Precisão inventada é uma forma discreta de imprecisão.
@ cap-8-a-tabela-1-do-estudo

? [media] A área da úlcera tem quartis de 4,7 e 12,7 cm². Por que a amplitude interquartil acompanha a mediana?
+ Porque as duas resumem o espalhamento sem sofrer com os valores extremos que a mediana já escolheu ignorar. | Correto. É a mesma coerência que faz o desvio padrão acompanhar a média. Misturar mediana com desvio padrão, ou média com quartis, entrega ao leitor um par que não conversa entre si.
- Porque a amplitude interquartil é sempre menor que o desvio padrão. | Não há relação fixa entre as duas, e a comparação de tamanhos não é o motivo do pareamento.
- Porque os quartis são exigidos pelo CONSORT em toda variável contínua. | O CONSORT pede que se descreva adequadamente, e não impõe um par específico para toda variável.
- Porque a amplitude interquartil não pode ser calculada em distribuições simétricas. | Pode, e às vezes é informativa. O que decide o par é a coerência com a medida de centro escolhida.
- Porque a mediana precisa de dois números para ser interpretada. | Uma mediana isolada já é interpretável. O que ela não traz sozinha é a dispersão, e é isso que os quartis acrescentam.
@ cap-8-o-caso-da-area-da-ulcera

? [media] A pressão transcutânea de oxigênio tem doze valores ausentes por falha do equipamento. O que a Tabela 1 precisa informar?
+ Que o resumo dessa linha se refere a 188 participantes, e não a 200. | Correto. Toda tabela precisa dizer sobre quantas pessoas cada número foi calculado, e nenhuma pode deixar o leitor supondo que foram todas. Neste estudo há ainda dezesseis perdas de seguimento, que afetam as tabelas de desfecho.
- Que os doze ausentes foram substituídos pela média dos demais. | Substituir por média é uma imputação simples, que subestima a variabilidade e não deve ser feita sem declarar. Descrever com o n disponível é o correto aqui.
- Que a variável foi excluída da análise por ter dados faltantes. | Doze ausentes em duzentos não justificam descartar a variável, e a falha do equipamento é o tipo de ausência que menos ameaça a validade, como o Capítulo 7 explica.
- Nada: o leitor supõe que o n é o do cabeçalho da coluna. | É exatamente a suposição que a tabela não pode permitir, e é devolutiva frequente de revisor.
- Que o equipamento falhou, sem necessidade de informar o n. | A causa é útil na seção de métodos. O que a tabela precisa trazer é o denominador de cada número.
@ cap-8-a-tabela-1-do-estudo

? [media] No grupo controle, o primeiro quartil da redução de área em quatro semanas é −1,8%. O que esse número revela?
+ Que um quarto daqueles participantes tinha, em quatro semanas, úlcera do mesmo tamanho ou maior do que no início. | Correto. É um fato clínico que a média de 30,6% nunca teria revelado, e é o argumento mais concreto deste capítulo a favor de descrever a distribuição em vez de um número só.
- Que houve erro de medição, já que redução não pode ser negativa. | Redução negativa significa piora, e é perfeitamente possível em úlcera venosa. A escala foi construída para admitir esse valor.
- Que a área foi medida em unidade errada nesses participantes. | Não há troca de unidade: o sinal negativo é informação clínica, e não artefato.
- Que esses participantes abandonaram o seguimento. | Quem abandonou não tem medida de quatro semanas. Estes têm, e a medida mostra piora.
- Que a mediana do grupo controle também é negativa. | A mediana do controle é 38,3%. O quartil inferior descreve a quarta parte pior, e não o centro.
@ cap-8-quando-o-resumo-esconde-o-resultado

? [media] A duração da úlcera no grupo controle tem média de 16,0 meses, desvio padrão de 11,8 e mediana de 12,5. Como decidir o resumo sem ver o histograma?
+ Pelos dois indícios: a média é bem maior que a mediana, e o desvio padrão é quase do tamanho da média, o que em variável positiva indica cauda longa à direita. | Correto. Um desvio padrão quase igual à média implicaria, em distribuição simétrica, uma proporção considerável de valores negativos, impossíveis para duração de doença. Mediana e quartis, portanto.
- Pela regra de que duração de doença é sempre simétrica. | É quase sempre assimétrica à direita, junto com área de ferida, tempo de internação, custo e contagem de células.
- Aplicando o teste de Shapiro-Wilk aos dados. | É o critério que este capítulo desaconselha: erra nas duas pontas e substitui o julgamento por um valor de p.
- Não é possível decidir sem o histograma. | O histograma é o melhor caminho e não é o único. A relação entre média, mediana e desvio padrão já responde neste caso.
- Comparando o desvio padrão com o do grupo tratado. | A comparação entre grupos não informa sobre a forma da distribuição de nenhum deles.
@ cap-8-como-decidir-se-a-distribuicao-e-simetrica

? [media] Um artigo descreve a amostra usando erro padrão em vez de desvio padrão. Qual a consequência?
+ A variabilidade entre os participantes parece muito menor do que é, e tanto mais quanto maior a amostra. | Correto. O erro padrão encolhe conforme a amostra cresce, e o desvio padrão não. É por isso que a troca costuma passar despercebida por quem a comete: o número fica menor, e parecer mais preciso soa como virtude.
- Nenhuma, desde que a legenda informe qual foi usado. | Informar é indispensável e não conserta a escolha: descrever a amostra pede a medida que descreve os participantes, e não a que descreve a precisão da média.
- O leitor conclui que a amostra é maior do que foi. | O tamanho da amostra vem informado à parte. O que se distorce é a percepção da variabilidade.
- Os intervalos de confiança do artigo ficam inválidos. | O intervalo de confiança se constrói justamente a partir do erro padrão, e continua correto. O problema é usá-lo na descrição.
- A média deixa de ser interpretável. | A média permanece a mesma. O que muda é o número entre parênteses ao lado dela.
@ cap-8-cada-tipo-de-variavel-pede-um-resumo

? [media] O capítulo afirma que apenas 67 das 200 úlceras têm área acima da média. Por que esse número vale mais que qualquer teste?
+ Porque mostra, sem intermediários, que o resumo descreve mal dois terços da amostra. | Correto. Um teste de normalidade devolveria um valor de p, que ainda precisaria ser interpretado; a contagem devolve o fato. Quando um resumo descreve mal dois terços da amostra, ele não serve, por mais correta que esteja a aritmética que o produziu.
- Porque contagens são estatisticamente superiores a testes. | Não há hierarquia entre tipos de número. O que torna esta contagem convincente é responder diretamente à pergunta que interessa.
- Porque prova que a distribuição não é normal. | Provar não normalidade não é o objetivo, e o capítulo argumenta que essa nem é a pergunta certa.
- Porque 67 é menos de um terço, e um terço é o limite aceito de assimetria. | Não existe esse limite. O argumento é sobre o resumo ser representativo, e não sobre cruzar um patamar.
- Porque permite calcular a assimetria exata da distribuição. | Coeficientes de assimetria existem e não são necessários aqui. A contagem já resolveu a decisão prática.
@ cap-8-o-caso-da-area-da-ulcera

? [dificil] Um autor defende manter a coluna de valor de p na Tabela 1 do ensaio, argumentando que p acima de 0,05 mostraria que os grupos são comparáveis. Onde está o erro?
+ Um p alto não autoriza concluir comparabilidade, e o que decide é o tamanho do desequilíbrio, e não sua significância. | Correto. O desequilíbrio de dez pontos percentuais no diabetes atrapalha a interpretação do resultado qualquer que seja o valor de p que produza. E, sendo a alocação sorteada, já se sabia de antemão que a diferença veio do acaso.
- O erro é usar qui-quadrado onde caberia o teste exato de Fisher. | A escolha do teste não é a questão. Nenhum teste responde a uma pergunta cuja resposta já se conhece.
- O erro é não corrigir os testes da Tabela 1 para multiplicidade. | Multiplicidade é problema adicional e real, e não o motivo central da recomendação do CONSORT.
- O erro é comparar variáveis contínuas e categóricas na mesma tabela. | Tabelas de linha de base misturam os dois tipos rotineiramente, cada um com o resumo adequado.
- Não há erro: é a prática mais comum na literatura clínica. | É de fato comum, e o CONSORT a desaconselha explicitamente. Frequência não é argumento.
@ cap-8-por-que-nao-ha-valor-de-p-nesta-tabela

? [dificil] Em um estudo observacional, a comparação das características basais entre os grupos faz sentido?
+ Faz, porque ali não houve sorteio: um desequilíbrio pode refletir diferença real entre as populações comparadas, e não o acaso. | Correto. É a diferença que o capítulo aponta e que o Capítulo 12 desenvolve: na coorte do livro, quem recebeu o aspirado tinha úlcera com o dobro da área, e isso não é acaso, é indicação clínica. Ainda assim, o que orienta o ajuste é o raciocínio causal, e não o valor de p da linha de base.
- Não, pelas mesmas razões que valem no ensaio randomizado. | As razões não são as mesmas. No ensaio se sabe que a diferença veio do sorteio; no observacional, não se sabe.
- Faz, e o valor de p da linha de base deve ser o critério para incluir a variável no modelo. | Selecionar covariáveis pelo p da comparação basal é prática difundida e frágil. A escolha se faz por conhecimento causal, como o Capítulo 12 detalha.
- Não, porque estudos observacionais não permitem comparação entre grupos. | Permitem, e é para isso que existem. O que exigem é cautela com o confundimento.
- Faz, mas apenas se o estudo for prospectivo. | A distinção entre prospectivo e retrospectivo não muda a lógica da comparação basal.
@ cap-8-por-que-nao-ha-valor-de-p-nesta-tabela

? [dificil] O efeito teto da redução de área em doze semanas foi contornado neste estudo. Como, e o que isso ensina?
+ Medindo também a área em quatro semanas, quando quase ninguém havia cicatrizado; a solução foi de planejamento, e não de análise. | Correto. Nenhum resumo e nenhum teste recuperam informação que a própria escala destruiu. Quem só percebe o teto na hora de analisar já perdeu o dado, e é por isso que este livro trata de desfecho no Capítulo 4, muito antes de chegar aqui.
- Aplicando transformação logarítmica à variável saturada. | Transformar não devolve variação a uma escala que saturou: quem cicatrizou tem 100%, e continua tendo 100% em qualquer escala.
- Trocando a mediana pela média, que não sofre efeito teto. | A média de fato difere entre os grupos, 88,2% contra 73,0%, e continua descrevendo uma variável que perdeu poder de discriminar na parte superior.
- Excluindo da análise os participantes que cicatrizaram. | Excluir quem teve o melhor desfecho é o oposto do que se quer, e destruiria a comparação entre os grupos.
- Aumentando o tamanho da amostra para recuperar a variação. | Mais participantes produzem mais valores de 100%. O teto não é problema de tamanho.
@ cap-8-quando-o-resumo-esconde-o-resultado

? [dificil] O capítulo abre dizendo que descrever é decidir o que omitir. Qual é a consequência prática dessa frase?
+ Que todo resumo perde informação de propósito, e cabe ao pesquisador escolher qual perda é aceitável, sob pena de o resumo mentir sem que ninguém perceba. | Correto. Os cinco mil e duzentos valores do banco viram algumas dezenas de números na Tabela 1, e a média da área da úlcera é o exemplo de escolha malfeita: aritmética correta, descrição falsa.
- Que se deve apresentar o máximo de estatísticas possível, para não omitir nada. | Tabela poluída é tabela que ninguém confere, e acumular medidas transfere ao leitor a decisão que era do autor.
- Que os dados brutos devem sempre substituir a descrição. | Os dados brutos precisam estar disponíveis, como este livro faz, e não substituem o resumo: ninguém lê cinco mil valores.
- Que a escolha do resumo é convenção editorial, sem consequência sobre a leitura. | A escolha muda o que o leitor conclui. Média de 10,5 e mediana de 7,7 descrevem a mesma amostra e sugerem pacientes diferentes.
- Que apenas variáveis com distribuição conhecida devem ser descritas. | Toda variável coletada precisa ser descrita, e a forma da distribuição é o que decide como, e não se.
@ cap-8-descrever-e-decidir-o-que-omitir
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

::: agora
1. Monte a Tabela 1 do seu estudo, mesmo que com os dados parciais que você já
   tem. Ela revela cedo quais variáveis faltam na ficha de coleta.
2. Para cada variável contínua, olhe o histograma e decida entre média e mediana.
   Anote a decisão: o revisor vai perguntar, e "porque o Shapiro deu 0,03" não é
   resposta.
3. Se a sua Tabela 1 tem coluna de valor de p e o estudo é randomizado, apague a
   coluna agora.
4. Escreva, em cada tabela, o que está entre parênteses.
:::

## Recursos

- [CONSORT Statement](https://www.consort-statement.org/) — a recomendação para
  relato de ensaios clínicos randomizados, incluindo a orientação sobre a
  Tabela 1.
- [jamovi](https://www.jamovi.org/) — o programa usado no livro, gratuito, para
  Windows, macOS e Linux.
- Curran-Everett D, Benos DJ. [*Guidelines for reporting statistics in journals
  published by the American Physiological Society*](https://doi.org/10.1152/japplphysiol.00513.2004)
  — as diretrizes da American Physiological Society, ainda úteis, com uma seção
  específica sobre a confusão entre desvio padrão e erro padrão.

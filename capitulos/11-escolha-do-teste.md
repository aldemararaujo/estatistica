::: caso
O estudo tem, além do desfecho primário, quatro desfechos secundários e uma
dúzia de variáveis basais. Cada comparação pede um teste, e nenhum deles é o
mesmo. Este capítulo é o mapa que leva de uma pergunta a um teste, e ele cabe em
três perguntas.
:::

## As três perguntas que decidem tudo

Escolher teste estatístico parece exigir memorizar uma lista. Não exige. Exige
responder, nesta ordem:

1. **Que tipo de variável é o desfecho?** Categórica ou numérica?
2. **Quantos grupos estão sendo comparados, e eles são independentes ou
   pareados?** Pareado quer dizer que cada valor de um grupo tem um par
   correspondente no outro, tipicamente porque é a mesma pessoa medida duas
   vezes.
3. **Se o desfecho é numérico, a distribuição comporta a média?** Assimetria
   forte, amostra pequena ou presença de valores extremos empurram para os
   testes baseados em postos.

Com as três respostas, a tabela abaixo resolve praticamente toda a pesquisa
clínica de rotina.

## A tabela de decisão

| Desfecho | Comparação | Teste | Alternativa por postos |
|---|---|---|---|
| Categórico, dois grupos independentes | proporções | qui-quadrado | Fisher, se esperado < 5 |
| Categórico, dois momentos na mesma pessoa | proporções pareadas | McNemar | — |
| Categórico, mais de dois grupos | proporções | qui-quadrado de r x c | Fisher-Freeman-Halton |
| Numérico, dois grupos independentes | médias | t de Student ou de Welch | Mann-Whitney |
| Numérico, dois momentos na mesma pessoa | médias pareadas | t pareado | Wilcoxon dos postos sinalizados |
| Numérico, três ou mais grupos independentes | médias | ANOVA de uma via | Kruskal-Wallis |
| Numérico, três ou mais momentos na mesma pessoa | médias | ANOVA de medidas repetidas | Friedman |
| Duas variáveis numéricas | associação | correlação de Pearson | correlação de Spearman |
| Tempo até um evento | curvas | log-rank | — |
| Qualquer um, com ajuste por outras variáveis | modelo | regressão | — |

As duas últimas linhas são os Capítulos 14 e 12. As demais são este capítulo.

::: atencao O erro de esquecer o pareamento
Aplicar um teste para amostras independentes a dados pareados é o erro que mais
custa poder estatístico. A dor deste estudo foi medida na mesma pessoa, antes e
depois: são 184 pares, não dois grupos de 184 pessoas. O teste pareado usa a
diferença dentro de cada indivíduo e elimina a variabilidade entre pessoas, que é
justamente a maior fonte de ruído. Tratar os dados como independentes joga fora
essa vantagem e pode transformar um efeito evidente em resultado não
significativo.
:::

## O mito da normalidade

A pergunta 3 costuma ser respondida errado, e a origem do erro é uma frase
repetida em disciplinas de metodologia: "o teste t exige que os dados sejam
normais".

Não exige. O que o teste t supõe é que a **distribuição das médias amostrais**
seja aproximadamente normal, o que é coisa bem diferente. Pelo teorema central
do limite, essa distribuição se aproxima da normal conforme a amostra cresce,
mesmo quando os dados individuais são assimétricos. Com noventa participantes por
grupo, como neste estudo, o teste t é robusto a assimetrias consideráveis.

O que de fato compromete o teste t são valores extremos, que puxam a média, e
amostras pequenas combinadas com assimetria forte. E a decisão, de novo, se toma
olhando a distribuição, não aplicando um teste de normalidade, pelas razões
expostas no Capítulo 8.

O quadro abaixo mostra o que acontece na prática, com os dados deste estudo:

| Comparação | Teste paramétrico | Teste por postos |
|---|---|---|
| Redução de área em 4 semanas, entre grupos | t de Welch: t = 2,35, p = 0,020 | Mann-Whitney: U = 5.584, p = 0,024 |
| Dor antes e depois, na mesma pessoa | t pareado: t = 23,48, p < 0,001 | Wilcoxon: W = 72, p < 0,001 |

Os pares de valores praticamente coincidem. Isso é o normal, e não a exceção:
quando os dois testes discordam de maneira relevante, a causa quase sempre é um
punhado de valores extremos, e o que se deve investigar é aquele punhado, não a
escolha do teste.

## Os testes deste estudo, um a um

**Desfecho primário, cicatrização em 12 semanas.** Categórico, dois grupos
independentes: qui-quadrado. Resultado no Capítulo 10.

**Redução de área em 4 semanas.** Numérica, dois grupos independentes. A
distribuição tem cauda à esquerda, com valores negativos de piora, mas o tamanho
da amostra basta: t de Welch, com Mann-Whitney como análise de sensibilidade. A
diferença é de 14,8 pontos percentuais, p = 0,020.

::: nota Por que Welch, e não o t de Student clássico
O t de Student supõe que os dois grupos tenham a mesma variância. O de Welch não
supõe nada disso e, quando as variâncias são de fato iguais, seus resultados são
praticamente idênticos aos do clássico. Não há motivo para testar igualdade de
variâncias antes: use Welch sempre. É a recomendação corrente da literatura
metodológica e o padrão do jamovi.
:::

**Dor, antes e depois.** Numérica, dois momentos na mesma pessoa: t pareado. A
mediana caiu de 5 para 3, com p < 0,001. Repare que o teste não diz que a queda
se deve ao tratamento: os dois grupos melhoraram, porque a úlcera cicatriza
também sob compressão isolada. Comparar a queda **entre** os grupos é outra
análise, e é ela que responde sobre eficácia.

**Dor alta, antes e depois.** Se a dor for dicotomizada em alta ou baixa,
usando 5 como corte, a comparação passa a ser de proporções pareadas: McNemar.
Foram 84 participantes que saíram de dor alta para dor baixa e apenas 1 que fez o
contrário, com qui² de 79,11 e p < 0,001. O teste olha só os discordantes, que
são os únicos que carregam informação sobre mudança.

**Comparação entre os três centros.** Numérica, três grupos independentes:
ANOVA de uma via, F = 0,52, p = 0,595, com Kruskal-Wallis confirmando, H = 1,09,
p = 0,581. Não há sinal de que os centros tenham obtido resultados diferentes, o
que é uma verificação de rotina em estudo multicêntrico.

**Área inicial e tempo até cicatrizar.** Duas variáveis numéricas: correlação.
Pearson devolve r = 0,19 e Spearman, rô = 0,28. A discrepância entre os dois é
informativa: a área é assimétrica, e Pearson, que trabalha com os valores brutos,
é puxado pelos extremos, enquanto Spearman, que trabalha com postos, capta melhor
a tendência monótona. Com variáveis assimétricas, prefira Spearman.

::: jamovi
1. **Duas proporções independentes:** Frequencies, Independent Samples (χ²).
2. **Proporções pareadas:** Frequencies, Paired Samples (McNemar). Exige as duas
   variáveis dicotômicas na mesma linha do banco.
3. **Duas médias independentes:** T-Tests, Independent Samples T-Test. Marque
   **Welch's** e, em Additional Statistics, **Mann-Whitney U**: o jamovi mostra
   os dois lado a lado, que é como este livro recomenda relatar.
4. **Duas médias pareadas:** T-Tests, Paired Samples T-Test, com **Wilcoxon
   rank** marcado.
5. **Três ou mais grupos:** ANOVA, One-Way ANOVA. Para a versão por postos,
   ANOVA, One-Way ANOVA (Non-parametric), que é o Kruskal-Wallis.
6. **Correlação:** Regression, Correlation Matrix, marcando Pearson e Spearman.

Em todos eles, marque **Effect size** e **Confidence interval** quando o jamovi
oferecer. Um teste sem tamanho de efeito devolve metade da resposta.
:::

::: abas
== Quando usar o teste por postos
Use quando a amostra for pequena, digamos abaixo de trinta por grupo, e a
distribuição for visivelmente assimétrica; quando houver valores extremos que
você não pode nem excluir nem justificar; e quando o desfecho for ordinal por
natureza, como um escore de dor de 0 a 10 ou uma escala de satisfação.

== O que se perde com ele
Os testes por postos comparam distribuições, não médias, e por isso não produzem
uma estimativa de efeito interpretável na escala original. Você fica com um valor
de p e sem a diferença de médias em pontos percentuais, que é o que o clínico
entende. Por isso este livro sugere relatar o intervalo de confiança da diferença
mesmo quando o valor de p vem do teste por postos: o leitor precisa do tamanho do
efeito, e ele não está no U de Mann-Whitney.
:::

::: revisor
**"Não está descrito qual teste foi usado para cada desfecho."** A seção de
métodos precisa dizer, desfecho a desfecho, qual teste e por quê. Uma frase
genérica do tipo "os dados foram analisados no programa X" não passa.

**"Os autores usaram teste de amostras independentes em medidas repetidas."**
Erro grave: infla o erro padrão e derruba o poder. Se a mesma pessoa foi medida
duas vezes, o teste é pareado.

**"A escolha entre paramétrico e não paramétrico foi baseada no teste de
Shapiro-Wilk."** Descreva a distribuição e justifique pela forma dela e pelo
tamanho da amostra.

**"Foi usado qui-quadrado com valores esperados menores que 5."** Use o teste
exato de Fisher. O jamovi informa o menor valor esperado no rodapé da tabela.

**"Os autores dicotomizaram uma variável contínua para facilitar a análise."**
Dicotomizar joga informação fora e reduz poder. Faça isso apenas quando o ponto
de corte tiver significado clínico próprio, como o corte de 40% de redução em
quatro semanas usado no Capítulo 13, e nunca escolhendo o corte que produz o
menor valor de p.
:::

::: quiz
? [facil] Quais são as três perguntas que decidem a escolha do teste?
+ Que tipo de variável é o desfecho, quantos grupos há e se são pareados, e se a distribuição comporta a média. | Correto. Com essas três respostas, a tabela de decisão resolve praticamente toda a pesquisa clínica de rotina.
- Qual o tamanho da amostra, qual o valor de p desejado e qual o programa disponível. | Nenhuma das três define o teste adequado.
- Se os dados são normais, se há valores extremos e se a amostra é grande. | São considerações que entram na terceira pergunta, e deixam de fora tipo de desfecho e pareamento.
- Qual o delineamento, qual o desfecho primário e qual o comparador. | Definem a pergunta de pesquisa, e não diretamente o teste.
- Quantas variáveis há no banco, quantos grupos e quantos desfechos. | O número de variáveis no banco não influencia a escolha do teste de um desfecho.
@ cap-11-as-tres-perguntas-que-decidem-tudo

? [facil] A dor foi medida na inclusão e em 12 semanas, nos mesmos participantes. Qual teste compara os dois momentos?
+ Teste t pareado, ou Wilcoxon dos postos sinalizados. | Correto. São 184 pares, e não dois grupos independentes. O teste pareado usa a diferença dentro de cada indivíduo e elimina a variabilidade entre pessoas.
- Teste t para amostras independentes. | É o erro que mais custa poder estatístico: trata como independentes medidas que vêm da mesma pessoa.
- Qui-quadrado. | O desfecho aqui é numérico, e não categórico.
- ANOVA de uma via. | Compara três ou mais grupos independentes.
- Correlação de Pearson. | Mede associação entre duas variáveis, e não mudança entre dois momentos.
@ cap-11-a-tabela-de-decisao

? [media] O que o teste t realmente supõe sobre a distribuição?
+ Que a distribuição das médias amostrais seja aproximadamente normal, o que o teorema central do limite garante em amostras razoáveis mesmo com dados assimétricos. | Correto. Com noventa participantes por grupo, o teste é robusto a assimetrias consideráveis. O que de fato o compromete são valores extremos e amostras pequenas com assimetria forte.
- Que os dados individuais sigam distribuição normal. | É a frase repetida nas disciplinas de metodologia, e ela confunde a distribuição dos dados com a das médias.
- Que as duas amostras tenham exatamente o mesmo tamanho. | Não exige, e o teste funciona com grupos desiguais.
- Que as variâncias sejam iguais, sem exceção. | O de Welch dispensa essa suposição e deve ser o padrão.
- Que não haja valores faltantes. | Faltantes reduzem o n disponível e não invalidam a suposição do teste.
@ cap-11-o-mito-da-normalidade

? [media] Por que este livro recomenda o teste t de Welch em vez do t de Student clássico?
+ Porque Welch não supõe variâncias iguais e, quando elas são iguais, entrega resultados praticamente idênticos. | Correto. Não há motivo para testar igualdade de variâncias antes: usar Welch sempre é a recomendação corrente da literatura metodológica e o padrão do jamovi.
- Porque Welch tem mais poder estatístico em qualquer situação. | Não tem mais poder por princípio; tem validade mais ampla.
- Porque o t de Student só serve a amostras pareadas. | O t de Student clássico é para amostras independentes; o pareado é outro teste.
- Porque Welch dispensa a suposição de normalidade. | A suposição sobre a distribuição das médias continua valendo.
- Porque o t de Student exige amostras de tamanho igual. | Não exige, embora seu desempenho piore com grupos desiguais e variâncias diferentes.
@ cap-11-os-testes-deste-estudo-um-a-um

? [media] No teste de McNemar aplicado à dor deste estudo, 84 participantes saíram de dor alta para baixa e 1 fez o caminho contrário. Por que o teste ignora os que não mudaram?
+ Porque quem permaneceu na mesma categoria não traz informação sobre a direção da mudança. | Correto. Cinquenta pessoas com dor alta antes e depois são compatíveis tanto com melhora quanto com nada ter acontecido. O que discrimina são os discordantes.
- Porque eles seriam contados duas vezes. | Não haveria dupla contagem; eles simplesmente não informam sobre mudança.
- Porque o teste exige tabelas de duas por duas com casas iguais. | Não exige nada disso.
- Porque quem não mudou provavelmente não aderiu ao tratamento. | É especulação clínica, e não a razão estatística.
- Porque incluí-los violaria a suposição de independência. | A independência entre pares não é afetada pelos concordantes.
@ cap-11-os-testes-deste-estudo-um-a-um

? [dificil] A correlação entre área inicial e tempo até cicatrizar deu r de Pearson de 0,19 e rô de Spearman de 0,28. O que explica a diferença e qual relatar?
+ A área é fortemente assimétrica, e Pearson, que trabalha com valores brutos, é sensível aos extremos; relatar Spearman, que usa postos e capta relação monótona. | Correto. Com variável assimétrica, prefira Spearman e diga no texto por que a escolheu.
- Um dos dois foi calculado errado, já que deveriam coincidir. | Não precisam coincidir: medem coisas diferentes sobre a mesma relação.
- Pearson é sempre superior por usar a informação completa dos valores. | Usa mais informação da escala, e isso o torna vulnerável justamente quando a escala é distorcida.
- A diferença indica ausência de relação entre as variáveis. | Ambos apontam relação positiva, ainda que modesta.
- Deve-se relatar os dois sem escolher, deixando a decisão ao leitor. | Relatar ambos é aceitável, e a escolha e sua justificativa continuam sendo do autor.
@ cap-11-os-testes-deste-estudo-um-a-um

? [dificil] O que se perde ao relatar apenas o resultado de um teste por postos, como Mann-Whitney?
+ A estimativa do efeito na escala original, porque o teste compara distribuições e não produz diferença de médias interpretável. | Correto. Por isso o livro sugere relatar o intervalo de confiança da diferença mesmo quando o valor de p vem do teste por postos: o clínico precisa do tamanho do efeito, e ele não está no U.
- Nada: o teste por postos fornece as mesmas informações. | Fornece o valor de p, e não a magnitude na unidade do desfecho.
- Perde-se poder estatístico em qualquer situação. | Em distribuições assimétricas ele pode ter mais poder que o paramétrico.
- Perde-se a possibilidade de calcular o valor de p. | O valor de p é exatamente o que ele fornece.
- Perde-se a capacidade de ajustar por covariáveis. | Ajuste exige modelo de regressão, o que também não é oferecido pelo teste paramétrico simples.
@ cap-11-a-tabela-de-decisao

? [facil] O que quer dizer, exatamente, que dois conjuntos de dados são pareados?
+ Que cada valor de um tem um correspondente no outro, tipicamente por serem a mesma pessoa medida duas vezes. | Correto. É a segunda das três perguntas que decidem o teste, e ela muda tudo: com pares, a análise trabalha com a diferença dentro de cada indivíduo, e não com dois amontoados de valores.
- Que os dois grupos têm o mesmo número de participantes. | Grupos independentes podem ter tamanhos iguais por acaso ou por delineamento, e continuam independentes. O que define pareamento é a correspondência um a um.
- Que os participantes foram sorteados aos pares para os dois grupos. | A randomização em blocos pode alocar em pares, e ainda assim cada participante entra em um grupo só, sem correspondente no outro.
- Que as duas variáveis medem a mesma coisa. | Medir a mesma coisa é condição para a comparação fazer sentido, e não é o que constitui o par. O par se define pela unidade observada.
- Que os dados foram coletados no mesmo dia. | A data da coleta não cria correspondência entre observações de pessoas diferentes.
@ cap-11-as-tres-perguntas-que-decidem-tudo

? [facil] A redução de área foi comparada entre os três centros do estudo. Qual o teste indicado?
+ ANOVA de uma via, com Kruskal-Wallis como alternativa por postos. | Correto. Desfecho numérico, três grupos independentes. Neste estudo a ANOVA deu F de 0,52 com p de 0,595, e o Kruskal-Wallis confirmou, o que é a verificação de rotina em estudo multicêntrico.
- Três testes t, comparando os centros dois a dois. | Três comparações a 5% inflam a taxa de falso positivo, exatamente o problema do Capítulo 10. A ANOVA responde à pergunta com um teste só.
- Qui-quadrado de r por c. | Serve a desfecho categórico em mais de dois grupos. Redução de área é numérica.
- ANOVA de medidas repetidas. | Seria o teste se os três valores viessem da mesma pessoa em três momentos. Os centros são grupos independentes de pessoas diferentes.
- Correlação de Spearman entre centro e redução. | Centro é variável nominal, sem ordem, e correlação exige variáveis que possam ser ordenadas.
@ cap-11-a-tabela-de-decisao

? [facil] Uma tabela de contingência dois por dois tem menor valor esperado igual a 3. Qual o teste correto?
+ O teste exato de Fisher. | Correto. Abaixo de 5, a aproximação do qui-quadrado pela distribuição teórica deixa de ser confiável. O jamovi informa o menor valor esperado no rodapé da tabela, e é ali que se confere.
- Qui-quadrado de Pearson, como de hábito. | É justamente o que a devolutiva do revisor cobra: qui-quadrado com esperados pequenos não se sustenta.
- Qui-quadrado com correção de continuidade, que resolve o problema. | A correção atenua a discrepância entre distribuição contínua e contagem discreta, e não substitui o teste exato quando as casas estão pouco povoadas.
- McNemar, que funciona com casas pequenas. | McNemar é para proporções pareadas. O problema aqui é o tamanho do esperado, e não a natureza da comparação.
- Teste t, que dispensa a suposição sobre esperados. | O desfecho é categórico, e o teste t compara médias de variáveis numéricas.
@ cap-11-a-tabela-de-decisao

? [facil] A seção de métodos de um artigo diz apenas: "os dados foram analisados no jamovi, adotando-se significância de 5%". O que falta?
+ Dizer, desfecho a desfecho, qual teste foi usado e por quê. | Correto. O programa e o limiar não são o método. Sem saber qual teste respondeu a cada pergunta, o leitor não consegue julgar se a escolha foi adequada nem reproduzir a análise.
- Informar a versão exata do programa utilizado. | A versão é boa prática de reprodutibilidade e não é o que falta aqui. A ausência crítica é a do teste de cada desfecho.
- Declarar que os dados eram normais. | Declarar normalidade seria repetir o mito que este capítulo desfaz. O que se descreve é a forma da distribuição e o tamanho da amostra.
- Acrescentar o valor de p de cada comparação. | Os valores de p pertencem aos resultados, e não aos métodos. O que falta nos métodos é a escolha do teste.
- Nada: a frase é o padrão aceito na literatura clínica. | É uma frase frequente e insuficiente, e está entre as devolutivas mais comuns de revisor neste capítulo.
@ cap-11-as-tres-perguntas-que-decidem-tudo

? [media] Um autor escreve que aplicou Shapiro-Wilk e, como o resultado foi significativo, optou pelo teste não paramétrico. Qual o problema?
+ A decisão deve vir da forma da distribuição e do tamanho da amostra, e não do resultado de um teste de normalidade. | Correto. Em amostra grande, o Shapiro-Wilk acusa desvios triviais e empurra para o teste por postos sem necessidade; em amostra pequena, não detecta nem desvios importantes. É justamente onde ele decidiria bem que ele não enxerga.
- Nenhum: é o procedimento correto e recomendado. | É o procedimento mais ensinado e um dos mais criticados pela literatura metodológica, e aparece como devolutiva de revisor neste capítulo.
- O erro foi usar Shapiro-Wilk em vez de Kolmogorov-Smirnov. | Trocar um teste de normalidade por outro não muda a natureza do problema, que é delegar a decisão a um teste.
- O erro foi não corrigir o teste de normalidade para múltiplas comparações. | Multiplicidade é assunto do Capítulo 10 e não é o defeito aqui. O defeito é o critério de escolha do teste principal.
- O erro foi aplicar o teste de normalidade aos dados brutos em vez dos resíduos. | Em modelos de regressão a distinção importa, e ainda assim a crítica central permanece: descreva a distribuição em vez de testá-la.
@ cap-11-o-mito-da-normalidade

? [media] Na redução de área em quatro semanas, o t de Welch devolveu p de 0,020 e o Mann-Whitney, 0,024. Como se lê essa proximidade?
+ Como o resultado esperado: quando a amostra é razoável, os dois caminhos concordam, e a escolha entre eles deixa de ser dramática. | Correto. É o normal, e não a exceção. Quando os dois discordam de maneira relevante, a causa quase sempre é um punhado de valores extremos, e o que se investiga é aquele punhado, não a escolha do teste.
- Como sinal de que um dos dois foi calculado incorretamente. | Os dois testam hipóteses ligeiramente diferentes sobre os mesmos dados, e valores próximos, porém distintos, são exatamente o que se espera.
- Como prova de que os dados são normais. | Nada aqui testa normalidade, e o capítulo argumenta que essa não é a pergunta certa a fazer.
- Como indicação de que se deve relatar o menor dos dois. | Escolher o menor depois de ver os dois é a prática que o Capítulo 10 chama de p-hacking. O teste se declara antes, no protocolo.
- Como evidência de que o teste por postos é desnecessário em qualquer estudo. | Ele continua indicado em amostras pequenas com assimetria forte, com valores extremos irremovíveis e com desfechos ordinais por natureza.
@ cap-11-o-mito-da-normalidade

? [media] A dor caiu de mediana 5 para 3, com p abaixo de 0,001 no teste pareado. O que esse resultado autoriza concluir?
+ Que a dor diminuiu ao longo do seguimento, sem dizer nada sobre a eficácia do aspirado. | Correto. Os dois grupos melhoraram, porque a úlcera cicatriza também sob compressão isolada. Comparar a queda **entre** os grupos é outra análise, e é ela que responde sobre eficácia.
- Que o aspirado de medula óssea reduz a dor. | O teste comparou dois momentos, e não dois tratamentos. Atribuir a queda ao aspirado é concluir sobre uma comparação que não foi feita.
- Que a dor caiu mais no grupo tratado. | Essa afirmação exige comparar as quedas entre os grupos, o que é uma terceira análise, distinta desta.
- Que a compressão isolada não tem efeito sobre a dor. | O grupo controle também melhorou, o que aponta na direção contrária.
- Que o desfecho de dor deveria ter sido o primário. | O desfecho primário se declara no protocolo, antes da coleta, e um p pequeno encontrado depois não promove desfecho algum.
@ cap-11-os-testes-deste-estudo-um-a-um

? [media] Em que situações o teste por postos é a escolha indicada?
+ Amostra pequena com assimetria visível, valores extremos que não se pode excluir nem justificar, e desfecho ordinal por natureza, como um escore de dor de 0 a 10. | Correto. São as três situações em que ele ganha do paramétrico. Fora delas, e sobretudo com amostras como a deste estudo, o ganho é pequeno e o custo é perder a estimativa na escala original.
- Sempre que o teste de normalidade der resultado significativo. | É o critério que este capítulo desaconselha. A decisão vem da forma da distribuição e do tamanho da amostra.
- Sempre que o desfecho for percentual. | Percentual é variável numérica contínua, e a redução de área deste estudo foi analisada por t de Welch sem problema.
- Sempre que houver mais de dois grupos. | Com três ou mais grupos a escolha continua sendo entre ANOVA e Kruskal-Wallis, pelos mesmos critérios.
- Sempre que houver dados faltantes no desfecho. | Faltantes reduzem o n disponível e se tratam como o Capítulo 7 descreve. Nada nisso favorece o teste por postos.
@ cap-11-a-tabela-de-decisao

? [media] A dor foi medida na inclusão, em quatro semanas e em doze semanas, nos mesmos participantes. Qual teste compara os três momentos?
+ ANOVA de medidas repetidas, com Friedman como alternativa por postos. | Correto. Três ou mais momentos na mesma pessoa mantêm o pareamento, agora com mais de dois níveis. Ignorar isso e usar ANOVA de uma via desperdiça a estrutura dos dados.
- ANOVA de uma via, com Kruskal-Wallis. | Serve a três ou mais grupos independentes, de pessoas diferentes. Aqui é a mesma pessoa três vezes.
- Três testes t pareados, comparando os momentos dois a dois. | Preserva o pareamento e cria três comparações, com a inflação de erro tipo I do Capítulo 10. A ANOVA de medidas repetidas responde com um teste só.
- Teste de McNemar aplicado três vezes. | McNemar é para proporções pareadas, e a dor aqui é numérica.
- Correlação de Pearson entre os três momentos. | Correlação mede associação entre variáveis, e não mudança ao longo do tempo.
@ cap-11-a-tabela-de-decisao

? [media] Um coautor propõe dicotomizar a área inicial em "grande" e "pequena" pelo corte que produzir o menor valor de p. Como responder?
+ Recusar: dicotomizar já joga informação fora, e escolher o corte pelo valor de p transforma perda em viés. | Correto. Dicotomizar reduz poder, e o corte escolhido nos próprios dados quase nunca se reproduz em outra amostra. Só se dicotomiza quando o ponto de corte tem significado clínico próprio, como o de 40% de redução em quatro semanas usado no Capítulo 13.
- Aceitar, desde que o corte seja relatado com transparência. | Relatar não conserta. O corte otimizado nos dados continua sendo uma escolha feita depois de ver o resultado.
- Aceitar, porque dicotomizar sempre facilita a interpretação clínica. | Facilita a leitura e custa poder estatístico. A facilidade não paga a informação perdida, salvo quando o corte já existe na clínica.
- Recusar, porque variáveis contínuas nunca podem ser categorizadas. | Podem, e às vezes devem, quando o limiar tem significado próprio. O que não se admite é escolhê-lo pelo valor de p.
- Aceitar, desde que se aplique correção de Bonferroni aos cortes testados. | Corrigir por um número de cortes testados que ninguém declarou antes é remendo sobre um procedimento que já nasceu torto.
@ cap-11-os-testes-deste-estudo-um-a-um

? [dificil] Por que aplicar um teste de amostras independentes a dados pareados custa tanto poder estatístico?
+ Porque o teste independente carrega a variabilidade entre pessoas no erro padrão, enquanto o pareado a elimina ao trabalhar com a diferença dentro de cada indivíduo. | Correto. A variabilidade entre pessoas costuma ser a maior fonte de ruído, e quem sente muita dor no início tende a sentir muita dor depois. Descartar essa informação pode transformar um efeito evidente em resultado não significativo.
- Porque o teste independente exige o dobro de participantes para o mesmo cálculo. | O número de observações é o mesmo nos dois casos. O que muda é o que entra no denominador do teste.
- Porque a suposição de normalidade é mais exigente no teste independente. | A suposição é da mesma natureza nos dois. A diferença está na estrutura de correlação dos dados, e não na forma da distribuição.
- Porque o teste independente não admite grupos de tamanhos iguais. | Admite qualquer combinação de tamanhos. A questão é outra: os dados não formam dois grupos.
- Porque o erro tipo I aumenta ao ignorar o pareamento. | O prejuízo típico é de poder, isto é, de erro tipo II. O teste fica conservador demais e deixa de detectar o que existe.
@ cap-11-as-tres-perguntas-que-decidem-tudo

? [dificil] Por que um teste de normalidade tende a decidir mal justamente quando sua decisão seria mais importante?
+ Porque em amostra grande ele acusa desvios irrelevantes, quando o teste t já é robusto, e em amostra pequena não detecta desvios importantes, quando a robustez não existe. | Correto. O poder do teste de normalidade cresce com o tamanho da amostra, e a necessidade de proteção contra a não normalidade diminui com ele. As duas curvas correm em direções opostas, e é isso que torna o critério inútil.
- Porque ele confunde assimetria com presença de valores extremos. | Ele responde a ambos, e o defeito não é de sensibilidade a um ou outro, e sim de descompasso com o tamanho da amostra.
- Porque só funciona corretamente em desfechos binários. | Testes de normalidade se aplicam a variáveis numéricas. Em desfecho binário a pergunta sequer se coloca.
- Porque exige que as variâncias dos grupos sejam iguais. | Igualdade de variâncias é outra suposição, resolvida pelo uso do teste de Welch.
- Porque não pode ser aplicado quando há dados faltantes. | Faltantes reduzem o n analisado e não são a origem do descompasso descrito.
@ cap-11-o-mito-da-normalidade

? [dificil] Um estudo compara a área da úlcera medida por planimetria digital e por régua, e relata correlação de Pearson de 0,94 como prova de que os métodos concordam. O argumento se sustenta?
+ Não: correlação mede se os valores caminham juntos, e dois métodos podem correlacionar quase perfeitamente enquanto um deles mede sistematicamente mais que o outro. | Correto. Concordância se avalia com a diferença entre os métodos, e não com a associação entre eles. O caminho é o gráfico de Bland e Altman, cuja referência está no Apêndice E, e essa distinção precisa ser resolvida antes da coleta.
- Sustenta-se: correlação acima de 0,90 é o critério aceito de concordância. | Não existe tal critério, e a correlação alta é exatamente o que o argumento de Bland e Altman mostra ser insuficiente.
- Não, porque a correlação de Pearson não se aplica a medidas de área. | Aplica-se a qualquer par de variáveis numéricas. O problema não é de aplicabilidade, e sim de pergunta.
- Não, porque o correto seria usar Spearman com variáveis assimétricas. | Trocar Pearson por Spearman continuaria respondendo à pergunta errada, que é a da associação e não a da concordância.
- Sustenta-se, desde que o valor de p da correlação também seja relatado. | O valor de p da correlação apenas indica que a associação não é nula, e associação não é concordância.
@ cap-11-os-testes-deste-estudo-um-a-um

? [dificil] Suponha que a ANOVA entre os três centros tivesse dado p de 0,01, em vez dos 0,595 observados. O que se poderia concluir?
+ Que pelo menos um centro difere de algum outro, sem saber qual, o que exigiria comparações posteriores com controle de multiplicidade. | Correto. A ANOVA responde a uma pergunta global, e não localiza a diferença. Sair comparando os pares sem controle reintroduz o problema de múltiplos testes do Capítulo 10.
- Que os três centros diferem entre si. | O teste global não autoriza afirmar que todos diferem. É perfeitamente possível que dois sejam iguais e o terceiro destoe.
- Que o centro com maior média é superior aos demais. | Ordenar as médias observadas e declarar vencedor é conclusão sobre comparações que não foram testadas.
- Que o estudo multicêntrico deve ser descartado. | Heterogeneidade entre centros é achado a investigar e relatar, e não motivo para descartar o estudo.
- Que o desfecho primário do estudo fica invalidado. | A comparação entre centros é verificação de rotina, e um resultado dela não anula a análise do desfecho primário, que compara grupos randomizados.
@ cap-11-a-tabela-de-decisao
:::

## Exercícios

::: exercicio 1
Você quer comparar a proporção de infecção da ferida entre os dois grupos. Foram
6 casos em 100 no grupo do aspirado e 10 em 100 no controle. Qual teste?

--- gabarito
Desfecho categórico, dois grupos independentes: qui-quadrado. Mas confira os
valores esperados: com 16 eventos em 200 participantes, o esperado na casa dos
infectados é 8 por grupo, portanto acima de 5, e o qui-quadrado é aceitável.
Se os eventos fossem 2 e 4, o esperado cairia abaixo de 5 e o teste exato de
Fisher passaria a ser obrigatório.
:::

::: exercicio 2
O escore de dor foi medido na inclusão e em 12 semanas. Você quer saber se a dor
diminuiu. Qual teste, e por quê ele é diferente do que se usaria para comparar a
dor entre os dois grupos de tratamento?

--- gabarito
Para a queda da dor, o teste é pareado, t pareado ou Wilcoxon, porque cada
participante fornece duas medidas e o interesse está na diferença dentro de cada
pessoa. Para comparar os grupos, o teste é de amostras independentes, aplicado à
variação da dor, e aí cada participante contribui com um único valor, que é a
diferença entre suas duas medidas. São perguntas diferentes: a primeira é "a dor
melhorou?" e a segunda é "o tratamento fez a dor melhorar mais?".
:::

::: exercicio 3
No teste de McNemar deste capítulo, 84 participantes saíram de dor alta para dor
baixa, 1 fez o caminho contrário, e todos os demais permaneceram na mesma
categoria. Por que o teste ignora os que permaneceram?

--- gabarito
Porque quem não mudou não traz informação sobre a direção da mudança. Se
cinquenta pessoas tinham dor alta antes e depois, elas são compatíveis tanto com
a hipótese de melhora quanto com a de nada ter acontecido. O que discrimina são
os discordantes: 84 para um lado contra 1 para o outro é um desequilíbrio
enorme, e é dele que sai o valor de p.
:::

::: exercicio 4
A correlação entre área inicial e tempo até cicatrizar deu r de Pearson de 0,19 e
rô de Spearman de 0,28. Explique a diferença e diga qual você relataria.

--- gabarito
A área inicial é fortemente assimétrica, com poucas úlceras muito grandes.
Pearson mede associação linear sobre os valores brutos e é sensível a esses
extremos, que podem tanto inflar quanto diluir o coeficiente. Spearman substitui
os valores por postos, elimina o efeito da escala e capta qualquer relação
monótona. Com uma variável assimétrica como essa, relate Spearman, e diga no
texto por que o escolheu.
:::

::: exercicio 5
Um colega quer comparar os três centros quanto à proporção de cicatrização.
Qual teste? E se um dos centros tivesse recrutado apenas oito pacientes?

--- gabarito
Desfecho categórico com três grupos independentes: qui-quadrado de três por dois.
Com um centro de apenas oito pacientes, os valores esperados provavelmente
cairiam abaixo de 5 e a alternativa seria o teste exato de Fisher-Freeman-Halton,
disponível em programas estatísticos. Vale lembrar que comparar centros não era
um desfecho declarado: é uma análise exploratória, e deve ser apresentada como
tal.
:::

::: exercicio 6
Percorra o banco no jamovi e escolha o teste adequado para estas três perguntas:
(a) a idade difere entre os grupos? (b) a proporção de fumantes difere entre os
três centros? (c) o índice tornozelo-braquial se associa à redução de área em
quatro semanas?

--- gabarito
(a) Numérica, dois grupos independentes, distribuição aproximadamente simétrica:
teste t de Welch. Vale a ressalva do Capítulo 8: em um ensaio randomizado, não se
testa diferença basal.
(b) Categórica, três grupos independentes: qui-quadrado de três por três, já que
o tabagismo tem três categorias.
(c) Duas variáveis numéricas: correlação. O índice tornozelo-braquial é
aproximadamente simétrico e a redução de área tem cauda, então relate Spearman ou
os dois coeficientes.
:::

::: agora
1. Faça uma tabela de duas colunas com todos os seus desfechos e, ao lado de cada
   um, o teste que você vai usar. Essa tabela é o rascunho do seu plano de
   análise, e ela precisa existir antes da coleta terminar.
2. Verifique se algum desfecho medido duas vezes na mesma pessoa está sendo
   tratado como se fossem dois grupos independentes. É o erro que mais custa
   poder estatístico.
3. Escreva o parágrafo de métodos estatísticos do seu artigo agora, com base
   nessa tabela. Escrever depois dos resultados é como a troca de teste acontece
   sem que ninguém perceba.
:::

## Recursos

- [jamovi](https://www.jamovi.org/) — todos os testes deste capítulo estão nos
  menus Frequencies, T-Tests, ANOVA e Regression.
- Curran-Everett D, Benos DJ. [*Guidelines for reporting statistics in journals
  published by the American Physiological Society*](https://doi.org/10.1152/japplphysiol.00513.2004)
  — orientações sobre descrever a análise nos métodos.
- [EQUATOR Network](https://www.equator-network.org/) — reúne as recomendações de
  relato para cada tipo de estudo, e cada uma delas tem um item sobre métodos
  estatísticos.

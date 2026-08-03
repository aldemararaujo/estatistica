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

## Recursos

- [jamovi](https://www.jamovi.org/) — todos os testes deste capítulo estão nos
  menus Frequencies, T-Tests, ANOVA e Regression.
- [Guidelines for reporting statistics](https://journals.physiology.org/doi/full/10.1152/japplphysiol.00513.2004)
  — orientações sobre descrever a análise nos métodos.
- [EQUATOR Network](https://www.equator-network.org/) — reúne as recomendações de
  relato para cada tipo de estudo, e cada uma delas tem um item sobre métodos
  estatísticos.

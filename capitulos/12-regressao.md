::: caso
Suponha que o estudo nunca tivesse sido randomizado. Suponha que os cirurgiões
simplesmente indicassem o aspirado de medula óssea a quem julgassem precisar
mais, e que depois se comparasse quem recebeu com quem não recebeu. É o que a
maioria dos estudos publicados faz, e é o que este capítulo vai fazer, com um
banco construído exatamente para isso: `coorte-observacional.csv`, trezentos
pacientes, o mesmo tratamento, o mesmo desfecho e o mesmo efeito verdadeiro do
ensaio randomizado.
:::

## O que a coorte responde

Nessa coorte, 144 dos 300 pacientes receberam o aspirado. O resultado bruto é
este:

| Grupo | Cicatrização em 12 semanas |
|---|---|
| Recebeu o aspirado | 59,0% |
| Não recebeu | 66,7% |

Razão de chances bruta: 0,72, com intervalo de confiança de 0,45 a 1,15 e p de
0,172. Lido ao pé da letra, o estudo diz que o aspirado de medula óssea tende a
**prejudicar** a cicatrização, sem significância estatística.

Sabemos que essa conclusão é falsa. Sabemos porque o efeito foi embutido na
simulação, e é exatamente o mesmo do ensaio randomizado, que encontrou razão de
chances de 2,11. A coorte não errou por azar nem por conta pequena: ela errou o
**sinal** do efeito.

### Por que ela errou

Basta olhar quem recebeu o tratamento:

| Característica | Recebeu | Não recebeu |
|---|---|---|
| Área inicial mediana | 12,2 cm² | 6,0 cm² |
| Duração mediana da úlcera | 18 meses | 10 meses |
| Diabetes | 35,4% | 21,2% |

Os grupos não são comparáveis, e não são comparáveis de um jeito perfeitamente
compreensível: o cirurgião indicou a terapia celular para a úlcera grande, antiga
e do paciente diabético, que é o que qualquer bom cirurgião faria. A indicação
seguiu a gravidade, e a gravidade determina o desfecho. O benefício do tratamento
foi engolido pelo prognóstico ruim de quem o recebeu.

Isso se chama **confundimento por indicação**, e é a razão pela qual, neste
livro, o caso condutor foi desenhado como ensaio randomizado.

## O que é um confundidor

Uma variável é confundidora quando cumpre três condições ao mesmo tempo:

1. **Associa-se ao desfecho**, independentemente da exposição. A área inicial
   prevê cicatrização, tenha o paciente recebido o que for.
2. **Associa-se à exposição**. Úlceras maiores receberam mais aspirado.
3. **Não está no caminho causal entre exposição e desfecho.** A área da úlcera
   existia antes de qualquer tratamento; ela não é consequência dele.

A terceira condição é a mais esquecida, e ela distingue confundidor de
**mediador**. Se uma variável é consequência do tratamento e causa do desfecho,
ajustar por ela remove justamente o efeito que se quer medir.

::: atencao Um problema real neste estudo
A adesão à terapia compressiva foi medida ao longo das doze semanas, isto é,
**depois** da randomização. Se o aspirado de medula óssea reduzir a dor e com
isso melhorar a adesão, então parte do benefício do tratamento passa por ela, e
ajustar por adesão subtrai esse pedaço do efeito. Neste livro a adesão entra nos
modelos porque ela ilustra bem o funcionamento da regressão, mas em um artigo
real ela deveria ficar fora do modelo principal e aparecer, no máximo, em análise
secundária. A regra prática é curta: no modelo de ajuste de um ensaio, só entram
variáveis medidas **antes** da alocação.
:::

## A regressão como ferramenta de ajuste

A regressão permite estimar o efeito de uma variável mantendo as outras
constantes. Aplicada à coorte, com ajuste por área, duração, diabetes e adesão:

| Análise da coorte | Razão de chances | IC 95% | p |
|---|---|---|---|
| Bruta | 0,72 | 0,45 a 1,15 | 0,172 |
| Ajustada | 1,87 | 0,98 a 3,56 | 0,058 |
| Ensaio randomizado, para comparação | 2,11 | 1,15 a 3,88 | 0,016 |

O ajuste resgatou o efeito: de aparentemente prejudicial para provavelmente
benéfico. Duas lições saem daí, e a segunda é mais importante que a primeira.

A primeira é que a regressão funciona. Sem ela, a coorte teria publicado uma
conclusão invertida.

A segunda é que **o ajuste não chegou lá**. A estimativa ajustada, 1,87, ficou
abaixo do valor verdadeiro, e seu intervalo cruza o 1. O ajuste corrige apenas o
que foi medido, e nesta coorte ficaram de fora o índice tornozelo-braquial, a
pressão transcutânea de oxigênio, o estado nutricional, a técnica do cirurgião e
tudo o mais que influencia cicatrização e não entrou no banco. Isso se chama
confundimento residual, e nenhum modelo o elimina.

> A randomização não é uma técnica estatística: é a única maneira conhecida de
> equilibrar também aquilo que ninguém mediu.

## Lendo uma regressão logística

O modelo ajustado do ensaio randomizado, com os 184 participantes que têm
desfecho observado:

| Variável | Razão de chances | IC 95% | p |
|---|---|---|---|
| Aspirado de medula óssea | 2,25 | 1,13 a 4,45 | 0,020 |
| Logaritmo da área inicial | 0,49 | 0,31 a 0,78 | 0,002 |
| Logaritmo da duração | 0,48 | 0,28 a 0,83 | 0,008 |
| Diabetes | 0,33 | 0,15 a 0,74 | 0,007 |
| Adesão adequada | 2,90 | 1,36 a 6,19 | 0,006 |

Como se lê cada linha:

- **Aspirado, 2,25**: mantidas constantes as demais variáveis do modelo, a chance
  de cicatrizar é 2,25 vezes maior no grupo tratado. Compare com a razão de
  chances bruta, 2,11: o ajuste mudou pouco, porque a randomização já havia
  equilibrado os grupos. **Esse é o comportamento esperado em um ensaio, e é ele
  que dá confiança no resultado principal.**
- **Área, 0,49**: a chance de cicatrizar cai pela metade a cada aumento de uma
  unidade no logaritmo da área, o que corresponde a multiplicar a área por 2,7.
  Entrou em logaritmo justamente porque a variável é assimétrica e porque o efeito
  de crescer de 2 para 4 cm² não é o mesmo de crescer de 40 para 42.
- **Diabetes, 0,33**: reduz a chance de cicatrizar a um terço. É um efeito
  grande, coerente com a clínica.
- **Adesão, 2,90**: quase triplica a chance, e é o maior efeito da tabela, o que
  deve provocar uma reflexão desconfortável em quem pesquisa terapias caras.

::: nota Quantas variáveis cabem no modelo
A regra prática mais usada pede pelo menos **dez eventos por variável**
independente. Este estudo teve 114 cicatrizações, o que comporta com folga as
cinco variáveis do modelo, e comportaria até onze. Modelos com mais variáveis do
que o número de eventos permite produzem coeficientes instáveis e intervalos
absurdamente largos, e é comum vê-los em teses com quarenta desfechos e quinze
preditores.
:::

## A regressão linear, quando o desfecho é numérico

Para a redução de área em quatro semanas, o modelo é linear, e os coeficientes
já vêm na unidade do desfecho, o que os torna muito mais fáceis de comunicar:

| Variável | Coeficiente | IC 95% | p |
|---|---|---|---|
| Aspirado de medula óssea | +12,0 pontos percentuais | −0,4 a 24,4 | 0,059 |
| Logaritmo da área inicial | −9,6 pontos percentuais | −17,4 a −1,8 | 0,016 |
| Diabetes | −20,5 pontos percentuais | −35,6 a −5,5 | 0,008 |
| Adesão adequada | +12,9 pontos percentuais | −1,4 a 27,1 | 0,079 |

O R² do modelo é 0,115: as cinco variáveis explicam cerca de 11% da variação da
redução de área. Parece pouco, e é o normal em pesquisa clínica, onde a
variabilidade entre pacientes é enorme. R² baixo não invalida um coeficiente:
são perguntas diferentes, uma sobre previsão individual e outra sobre efeito
médio.

Repare que o coeficiente do tratamento aqui, 12,0 pontos percentuais, tem p de
0,059, enquanto a comparação simples entre os dois grupos, feita no Capítulo 9,
deu 14,8 pontos com p de 0,020. Não há contradição: são estimativas de coisas
diferentes, uma ajustada e outra bruta, com incertezas diferentes. Um resultado
que atravessa a fronteira dos 0,05 conforme o modelo é, antes de tudo, um
resultado frágil, e é assim que ele deve ser descrito.

::: jamovi
1. **Regressão logística:** Analyses, Regression, **2 Outcomes (Binomial)**.
   Ponha `cicatrizacao_12sem` em **Dependent Variable**, e `grupo`, `diabetes` e
   `adesao_compressao` em **Factors**, com as variáveis numéricas em
   **Covariates**.
2. Em **Reference Levels**, confira qual categoria é a referência. É o erro de
   interpretação mais comum: se a referência for "Sim" em vez de "Não", todas as
   razões de chances aparecem invertidas.
3. Em **Model Coefficients**, marque **Odds ratio** e **Confidence interval**.
4. Para transformar a área em logaritmo, use **Data**, **Compute**, com a fórmula
   `LN(area_inicial_cm2)`.
5. **Regressão linear:** Regression, **Linear Regression**, com
   `reducao_area_4sem_pct` como dependente. Marque **Estimate** e **Confidence
   interval** em Model Coefficients.
:::

::: revisor
**"Os autores ajustaram por variáveis medidas após a intervenção."** É o erro do
mediador. Em ensaio clínico, o modelo de ajuste só admite variáveis basais, e
elas precisam estar pré-especificadas no protocolo.

**"O modelo inclui quinze variáveis para vinte e dois eventos."** Sobreajuste.
Reduza o modelo ao que a regra de dez eventos por variável comporta e justifique
a escolha das variáveis por conhecimento clínico, não por seleção automática de
passo a passo.

**"As variáveis foram selecionadas por *stepwise*."** A seleção automática
capitaliza o acaso, produz intervalos de confiança inválidos e não reproduz em
outra amostra. Escolha as covariáveis por raciocínio causal.

**"Os autores concluem causalidade a partir de uma coorte ajustada."** Ajuste
não é randomização. A conclusão deve reconhecer o confundimento residual, e o
verbo "associar" não deve virar "causar" no meio da discussão.

**"A categoria de referência não está informada."** Sem ela, nenhuma razão de
chances pode ser interpretada.

**"O ajuste alterou o efeito de 0,72 para 1,87 e os autores relatam apenas o
ajustado."** Relate os dois. A diferença entre bruto e ajustado é informação
sobre o confundimento, e escondê-la impede o leitor de julgar.
:::

::: quiz
? [facil] Quais são as três condições para uma variável ser confundidora?
+ Associa-se ao desfecho, associa-se à exposição e não está no caminho causal entre elas. | Correto. A terceira é a mais esquecida, e é ela que distingue confundidor de mediador.
- Associa-se ao desfecho, tem muitos valores faltantes e é contínua. | Faltantes e tipo de variável não têm relação com confundimento.
- Associa-se à exposição, é medida depois da intervenção e afeta o desfecho. | Ser medida depois da intervenção caracteriza um mediador, e não um confundidor.
- É clinicamente relevante, foi coletada e tem distribuição normal. | Nenhum dos três é critério de confundimento.
- Difere entre os grupos com valor de p abaixo de 0,05. | Significância na comparação basal não é o critério: o que importa é o tamanho do desequilíbrio e a relação com o desfecho.
@ cap-12-o-que-e-um-confundidor

? [facil] Na coorte observacional do livro, quem recebeu o aspirado tinha úlcera com o dobro da área e quase o dobro de duração. Como se chama esse fenômeno?
+ Confundimento por indicação. | Correto. O cirurgião indicou a terapia celular para a úlcera grande, antiga e do paciente diabético, que é o que qualquer bom cirurgião faria, e a indicação seguiu a gravidade.
- Viés de aferição. | Diz respeito a como o desfecho é medido, e não a quem recebe o tratamento.
- Efeito teto. | É a saturação de uma escala, discutida no Capítulo 8.
- Viés de publicação. | Ocorre depois do estudo, na decisão de publicar.
- Regressão à média. | Fenômeno de medidas repetidas em valores extremos, sem relação com a indicação do tratamento.
@ cap-12-o-que-a-coorte-responde

? [media] Na coorte, a razão de chances passou de 0,72 na análise bruta para 1,87 na ajustada, e o ensaio randomizado deu 2,11. Qual a lição mais importante?
+ O ajuste corrige apenas o que foi medido, e o que sobra é confundimento residual, impossível de dimensionar com os próprios dados. | Correto. A primeira lição é que a regressão funciona; a segunda, mais importante, é que ela não chegou lá.
- Que a regressão resolve o confundimento de estudos observacionais. | Resolveu parte dele, e a estimativa ajustada continuou abaixo do valor verdadeiro, com intervalo cruzando o 1.
- Que a coorte tinha amostra insuficiente. | Tinha 300 participantes, mais que o ensaio. O problema era comparabilidade, não tamanho.
- Que o modelo escolheu variáveis erradas. | As variáveis escolhidas eram as corretas e conhecidas; faltaram as não medidas.
- Que o ensaio randomizado superestimou o efeito. | O efeito do ensaio corresponde ao valor verdadeiro embutido na simulação.
@ cap-12-a-regressao-como-ferramenta-de-ajuste

? [media] No ensaio randomizado, a razão de chances bruta foi 2,11 e a ajustada, 2,25. O que essa proximidade indica?
+ Que a randomização equilibrou as covariáveis, de modo que ajustar por elas quase não altera a estimativa. | Correto. Essa estabilidade é uma verificação valiosa: em um ensaio, diferença grande entre bruto e ajustado levantaria suspeita sobre a alocação.
- Que o ajuste foi malfeito, por não ter alterado o resultado. | O ajuste funcionou como esperado em um estudo randomizado.
- Que as covariáveis escolhidas não têm relação com o desfecho. | Têm, e forte: área, duração e diabetes aparecem com efeitos expressivos no próprio modelo.
- Que o modelo está sobreajustado. | Cinco variáveis para 114 eventos está bem dentro do limite de dez eventos por variável.
- Que o tamanho da amostra foi insuficiente para o ajuste. | Foi suficiente, e a proximidade não decorre de falta de poder.
@ cap-12-lendo-uma-regressao-logistica

? [media] Um modelo tem 22 eventos e o pesquisador quer incluir 15 variáveis. Qual o problema?
+ A regra de dez eventos por variável comporta apenas duas: o modelo produziria coeficientes instáveis e intervalos absurdamente largos. | Correto. É comum ver isso em teses com quarenta desfechos e quinze preditores.
- Nenhum, desde que todas as variáveis sejam clinicamente relevantes. | Relevância não cria informação: o que limita é o número de eventos.
- O problema é o número de participantes, e não o de eventos. | Em modelos para desfechos binários e de sobrevida, o que limita é o número de eventos.
- Basta aumentar o nível de significância para 10%. | Elevar o alfa não resolve instabilidade de estimativas.
- Basta usar seleção automática por stepwise para reduzir o modelo. | A seleção automática capitaliza o acaso e produz intervalos inválidos.
@ cap-12-lendo-uma-regressao-logistica

? [dificil] Por que ajustar por uma variável medida depois da intervenção pode subestimar o efeito do tratamento?
+ Porque, se ela é consequência do tratamento e causa do desfecho, o ajuste remove o caminho pelo qual parte do efeito se realiza. | Correto. É o caso da adesão à compressão: se o aspirado reduz a dor e melhora a tolerância à compressão, ajustar por adesão subtrai esse pedaço do benefício.
- Porque variáveis medidas depois têm mais dados faltantes. | Podem ter, e não é isso que causa a subestimação.
- Porque o modelo passa a ter variáveis demais. | O problema é a natureza causal da variável, e não a quantidade.
- Porque a variável deixa de ser confundidora e passa a ser modificadora de efeito. | Modificação de efeito é interação, e é outro fenômeno.
- Porque a randomização não equilibra variáveis medidas depois. | Ela de fato não as equilibra necessariamente, e a razão da subestimação é a mediação.
@ cap-12-o-que-e-um-confundidor

? [dificil] Um artigo relata apenas o efeito ajustado de uma coorte, omitindo o bruto. Por que isso é um problema?
+ Porque a diferença entre bruto e ajustado é informação sobre o confundimento, e escondê-la impede o leitor de julgar. | Correto. Na coorte do livro, essa diferença é a distância entre 0,72 e 1,87, e é justamente ela que revela o tamanho do problema.
- Porque o efeito bruto é sempre mais confiável. | Não é: em estudo observacional, o bruto costuma ser o mais enviesado dos dois.
- Porque o CONSORT exige os dois valores. | O CONSORT trata de ensaios; para observacionais, a recomendação é o STROBE, que pede relato de ambos.
- Porque o ajustado só é válido se o bruto for significativo. | Não há tal dependência entre os dois.
- Porque omitir o bruto impede calcular o intervalo de confiança. | Cada estimativa tem seu próprio intervalo, calculável independentemente.
@ cap-12-a-regressao-como-ferramenta-de-ajuste

? [facil] O que a regressão permite fazer que a comparação simples entre dois grupos não permite?
+ Estimar o efeito de uma variável mantendo as outras constantes. | Correto. É essa a operação que resgata o efeito na coorte do livro: comparar tratados e não tratados entre pacientes com a mesma área, a mesma duração e o mesmo estado glicêmico, em vez de comparar dois amontoados de gente diferente.
- Provar que a exposição causa o desfecho. | Ajuste não é randomização. A regressão melhora a comparação e não converte associação em causa, e o próprio capítulo mostra por quê.
- Eliminar os dados faltantes do banco. | Faltantes se tratam como o Capítulo 7 descreve. A regressão, ao contrário, costuma descartar quem tem qualquer covariável ausente.
- Aumentar o poder estatístico do estudo. | Pode aumentar a precisão em algumas situações, e não é isso que a define. A função central é o ajuste.
- Corrigir erros de aferição das variáveis. | Erro de medida é problema de coleta, e o modelo o carrega para dentro em vez de corrigi-lo.
@ cap-12-a-regressao-como-ferramenta-de-ajuste

? [facil] No modelo ajustado do ensaio, o diabetes aparece com razão de chances de 0,33. Como se lê essa linha?
+ Mantidas constantes as demais variáveis do modelo, ter diabetes reduz a chance de cicatrizar a um terço. | Correto. É um efeito grande e coerente com a clínica, e é justamente por isso que o desequilíbrio de dez pontos percentuais no diabetes, visto na Tabela 1 do Capítulo 8, merecia ajuste.
- Que 33% dos diabéticos cicatrizaram. | A razão de chances não é proporção de pacientes. Ela compara chances entre quem tem e quem não tem a característica.
- Que o diabetes explica 33% da variação da cicatrização. | Proporção de variação explicada é o R², e aparece na regressão linear deste capítulo, não na logística.
- Que a chance de cicatrizar cai 33% entre os diabéticos. | Cair 33% seria razão de chances de 0,67. Uma razão de 0,33 reduz a chance a um terço, isto é, uma queda de dois terços.
- Que o diabetes tem 33% de probabilidade de influenciar o desfecho. | Nenhum coeficiente exprime probabilidade de a variável importar. Essa leitura confunde estimativa com valor de p.
@ cap-12-lendo-uma-regressao-logistica

? [facil] Por que a categoria de referência precisa estar informada no artigo?
+ Porque sem ela nenhuma razão de chances pode ser interpretada: não se sabe em relação a quem a comparação foi feita. | Correto. Se a referência for "Sim" em vez de "Não", todas as razões aparecem invertidas, e um efeito protetor vira efeito de risco sem que nada no número denuncie a troca. É por isso que o capítulo manda conferir os Reference Levels no jamovi.
- Porque o programa exige que ela seja declarada no texto. | O programa escolhe uma referência sozinho, e é exatamente esse automatismo que torna a conferência necessária.
- Porque ela determina o tamanho da amostra do modelo. | O n do modelo depende de quem tem todas as variáveis observadas, e não da escolha de referência.
- Porque sem ela o intervalo de confiança fica assimétrico. | O intervalo da razão de chances é assimétrico por ser construído em escala logarítmica, independentemente da referência.
- Porque a referência precisa ser sempre a categoria mais frequente. | Não precisa. A escolha é do autor, e o que se exige é que ela seja informada.
@ cap-12-lendo-uma-regressao-logistica

? [facil] Na regressão linear deste capítulo, o coeficiente do tratamento é "+12,0 pontos percentuais". Qual a vantagem dessa apresentação sobre a razão de chances?
+ O coeficiente já vem na unidade do desfecho, e por isso é muito mais fácil de comunicar. | Correto. Doze pontos percentuais a mais de redução de área em quatro semanas é uma frase que o clínico entende de imediato, ao contrário de uma razão de chances, que exige tradução antes de virar decisão.
- O coeficiente linear dispensa intervalo de confiança. | Não dispensa, e o deste modelo vai de −0,4 a 24,4, cruzando o zero. Toda estimativa precisa de sua medida de incerteza.
- O coeficiente linear prova causalidade, e a razão de chances não. | A escala do coeficiente nada tem a ver com inferência causal, que depende do delineamento.
- O coeficiente linear serve a desfechos binários e a razão de chances não. | É o inverso: a razão de chances é a medida da regressão logística, para desfecho binário; a linear se aplica a desfecho numérico.
- O coeficiente linear não depende das demais variáveis do modelo. | Depende, e a leitura correta é sempre "mantidas constantes as demais", igual à da logística.
@ cap-12-a-regressao-linear-quando-o-desfecho-e-numerico

? [media] Por que a área inicial entrou no modelo em logaritmo, e não em centímetros quadrados?
+ Porque a variável é assimétrica e porque crescer de 2 para 4 cm² não tem o mesmo peso que crescer de 40 para 42. | Correto. Em escala logarítmica, o que conta é multiplicar a área, e não somar centímetros. O coeficiente de 0,49 lê-se assim: a chance de cicatrizar cai pela metade a cada vez que a área é multiplicada por 2,7.
- Porque a regressão logística exige que todas as covariáveis sejam logaritmizadas. | Não exige nada disso. Idade, escores e índices entram em escala natural sem problema.
- Porque o logaritmo elimina os valores extremos do banco. | Ele comprime a cauda e não remove observação alguma. A úlcera de 66,4 cm² continua no modelo.
- Porque assim o coeficiente passa a ser interpretável como porcentagem. | O coeficiente continua sendo razão de chances. O que muda é a unidade da variável explicativa.
- Porque o jamovi não aceita variáveis assimétricas como covariáveis. | Aceita qualquer variável numérica. A transformação é decisão do pesquisador, e se faz em Data, Compute.
@ cap-12-lendo-uma-regressao-logistica

? [media] Um autor selecionou as covariáveis do modelo por *stepwise*. Qual a crítica?
+ A seleção automática capitaliza o acaso, produz intervalos de confiança inválidos e não se reproduz em outra amostra. | Correto. As covariáveis se escolhem por raciocínio causal e conhecimento clínico, declarados antes de olhar os dados. O modelo deste capítulo inclui diabetes porque o diabetes atrasa cicatrização, e não porque um algoritmo o selecionou.
- Nenhuma: é o método objetivo por excelência, já que não depende do pesquisador. | A aparência de objetividade é justamente o que a torna perigosa. A decisão continua sendo tomada, agora pelos dados, e sem quem responda por ela.
- A crítica é o custo computacional em bancos grandes. | O custo é irrelevante em bancos desta ordem. O problema é estatístico e conceitual.
- A crítica é que o stepwise só funciona em regressão linear. | Existe em ambas as regressões, e a objeção vale igualmente nas duas.
- A crítica é que ele exige mais eventos por variável que a seleção manual. | A exigência de eventos por variável é a mesma. O que muda é a validade do que sai do procedimento.
@ cap-12-a-regressao-como-ferramenta-de-ajuste

? [media] O R² do modelo linear é 0,115. O que isso significa, e o que não significa?
+ Significa que as variáveis explicam cerca de 11% da variação da redução de área, e não invalida coeficiente algum do modelo. | Correto. São perguntas diferentes: o R² fala de previsão individual, e o coeficiente, de efeito médio. R² baixo é o normal em pesquisa clínica, onde a variabilidade entre pacientes é enorme.
- Significa que o modelo está errado e precisa de mais variáveis. | Acrescentar variáveis aumenta o R² quase sempre, inclusive variáveis sem sentido clínico. Perseguir R² é a maneira mais rápida de sobreajustar.
- Significa que apenas 11% dos participantes foram bem classificados. | R² não é taxa de acerto. Classificação correta é medida de outros modelos, e aparece no Capítulo 13.
- Significa que há 11% de probabilidade de o modelo estar correto. | Nenhuma medida de ajuste exprime probabilidade de o modelo estar correto.
- Significa que 11% dos dados foram usados no cálculo. | Todos os participantes com as variáveis observadas entram no modelo. O R² descreve variação explicada, e não fração de dados.
@ cap-12-a-regressao-linear-quando-o-desfecho-e-numerico

? [media] No modelo logístico do ensaio, a adesão adequada à compressão tem razão de chances de 2,90, o maior efeito da tabela. O que fazer com essa informação?
+ Registrá-la com honestidade, notando que a intervenção mais barata do estudo produziu o maior efeito estimado, e lembrando que a adesão foi medida depois da alocação. | Correto. É uma reflexão desconfortável para quem pesquisa terapias caras, e ao mesmo tempo a variável precisa ser lida com cautela: por ter sido medida ao longo do seguimento, ela pode ser mediadora do próprio tratamento.
- Concluir que a compressão é mais eficaz que o aspirado. | Comparar coeficientes de um modelo observacional de covariáveis como se fossem efeitos de intervenções testadas é passo largo demais. Só o aspirado foi sorteado.
- Remover a adesão do modelo, já que ela domina os demais coeficientes. | Remover uma variável porque seu efeito é grande inverte o critério: variáveis entram ou saem por raciocínio causal, e não por magnitude.
- Concluir que o efeito do aspirado é espúrio. | O aspirado mantém razão de chances de 2,25, com intervalo que exclui o 1, no mesmo modelo em que a adesão aparece.
- Transformar a adesão em desfecho primário de um novo estudo, com base neste p. | Achado de covariável em modelo de ajuste gera hipótese, e transformá-lo em desfecho exige o percurso inteiro do livro, começando pela pergunta.
@ cap-12-lendo-uma-regressao-logistica

? [media] Um artigo escreve, na discussão, que a coorte ajustada "demonstra que o aspirado melhora a cicatrização". Qual a correção?
+ Trocar por linguagem de associação, reconhecendo o confundimento residual: ajuste não é randomização. | Correto. É devolutiva frequente de revisor, e a coorte deste capítulo mostra por quê: mesmo depois de ajustada, a estimativa ficou abaixo do valor verdadeiro, com intervalo cruzando o 1.
- Nenhuma: o ajuste por covariáveis autoriza conclusão causal. | Se autorizasse, a randomização seria desnecessária. O que o ajuste corrige é apenas o que foi medido.
- Trocar apenas se o intervalo de confiança cruzar o valor nulo. | O problema é de delineamento, e não de significância. Um intervalo estreito e distante do nulo continuaria não autorizando o verbo "demonstrar".
- Acrescentar mais covariáveis ao modelo até a conclusão causal se sustentar. | Nenhum número de covariáveis medidas fecha a porta do que não foi medido.
- Trocar o modelo logístico por um linear, que permite conclusão causal. | A escala do desfecho não muda a natureza da inferência.
@ cap-12-a-regressao-como-ferramenta-de-ajuste

? [media] O coeficiente do tratamento na regressão linear deu 12,0 pontos percentuais com p de 0,059, enquanto a comparação bruta do Capítulo 9 deu 14,8 com p de 0,020. Como descrever isso no artigo?
+ Relatando as duas estimativas e reconhecendo que um resultado que atravessa a fronteira dos 0,05 conforme o modelo é, antes de tudo, frágil. | Correto. Não há contradição: são estimativas de coisas diferentes, uma ajustada e outra bruta, com incertezas diferentes. Escolher a que agrada seria a troca que o Capítulo 10 chama de p-hacking.
- Relatando apenas a bruta, que alcançou significância. | Escolher pela significância depois de ver as duas é exatamente a prática que o registro prévio do protocolo existe para coibir.
- Relatando apenas a ajustada, que é metodologicamente superior. | A ajustada não é automaticamente superior, e em ensaio randomizado a análise principal costuma ser a pré-especificada, com a outra como sensibilidade.
- Concluindo que houve erro em uma das análises. | Ambas estão corretas. A diferença entre elas é informação, e não defeito.
- Concluindo que o tratamento não tem efeito sobre esse desfecho. | O intervalo da estimativa ajustada vai de −0,4 a 24,4, e admite desde efeito nulo até benefício expressivo. Concluir ausência é o erro do Capítulo 10.
@ cap-12-a-regressao-linear-quando-o-desfecho-e-numerico

? [dificil] Qual a diferença entre um confundidor e um modificador de efeito?
+ O confundidor distorce a estimativa e deve ser ajustado; o modificador faz o efeito ser genuinamente diferente entre estratos, e deve ser relatado por estrato. | Correto. Ajustar por um modificador esconde a informação mais interessante do estudo, que é o efeito variar. A distinção se investiga por interação, e a análise precisa estar declarada antes, pelas razões do Capítulo 10.
- São o mesmo fenômeno, com nomes distintos em escolas diferentes. | São fenômenos distintos: um é problema a corrigir, o outro é achado a descrever.
- O modificador é sempre uma variável medida depois da intervenção. | Isso caracteriza o mediador. Modificadores costumam ser características basais, como idade ou gravidade.
- O confundidor associa-se ao desfecho e o modificador não. | O modificador também se relaciona ao desfecho, e o que o define é alterar a magnitude do efeito do tratamento.
- A diferença é apenas o valor de p da interação. | O valor de p ajuda a avaliar a evidência de interação e não define o conceito, que é causal.
@ cap-12-o-que-e-um-confundidor

? [dificil] Por que o confundimento residual não pode ser dimensionado com os próprios dados do estudo?
+ Porque ele vem justamente das variáveis que não foram medidas, e sobre elas o banco não guarda nenhuma informação. | Correto. Nesta coorte ficaram de fora o índice tornozelo-braquial, a pressão transcutânea de oxigênio, o estado nutricional e a técnica do cirurgião. Por isso a randomização não é uma técnica estatística: é a única maneira conhecida de equilibrar também aquilo que ninguém mediu.
- Porque exigiria aumentar o tamanho da amostra. | Uma coorte dez vezes maior estimaria o efeito enviesado com mais precisão. Tamanho não corrige comparabilidade.
- Porque os métodos para calculá-lo ainda não foram desenvolvidos. | Existem análises de sensibilidade que exploram cenários de confundimento não medido, e todas exigem suposições externas aos dados, que é precisamente o ponto.
- Porque o intervalo de confiança já o incorpora. | O intervalo descreve a incerteza amostral, e supõe que o modelo esteja correto. Viés sistemático não entra nele.
- Porque o valor de p do modelo ajustado o resume. | Nenhum valor de p informa sobre variáveis ausentes do banco.
@ cap-12-a-regressao-como-ferramenta-de-ajuste

? [dificil] Na coorte, a estimativa ajustada é 1,87 com intervalo de 0,98 a 3,56 e p de 0,058. Um autor conclui que "o aspirado não teve efeito". Onde está o erro?
+ O intervalo admite desde efeito praticamente nulo até efeito grande, e por isso o estudo é inconclusivo, e não negativo. | Correto. É o mesmo erro do Capítulo 10, agora dentro de um modelo: um intervalo largo que quase não exclui nada foi lido como demonstração de ausência. E sabemos, neste caso, que o efeito verdadeiro existe e é maior que 1,87.
- Não há erro: com p acima de 0,05 conclui-se ausência de efeito. | Ausência de evidência não é evidência de ausência, e essa distinção depende do intervalo, não do limiar.
- O erro é usar razão de chances em vez de risco relativo. | A escolha da medida não muda a leitura da incerteza. O intervalo continuaria largo em qualquer escala.
- O erro é o modelo não incluir variáveis suficientes. | O modelo de fato sofre confundimento residual, o que empurra a estimativa para baixo. Ainda assim, o erro apontado na conclusão é de interpretação do intervalo.
- O erro é comparar a coorte com o ensaio randomizado. | A comparação é didática e legítima, e é ela que revela o tamanho do problema.
@ cap-12-a-regressao-como-ferramenta-de-ajuste

? [dificil] Um pesquisador seleciona as covariáveis do modelo incluindo toda variável com p abaixo de 0,20 na análise univariada. Qual a objeção?
+ O critério é estatístico onde deveria ser causal: uma variável pode ser confundidora importante sem alcançar aquele limiar, e outra pode alcançá-lo sendo mediadora. | Correto. Confundimento se decide pelas três condições do capítulo, e não por um valor de p de triagem. A adesão à compressão deste estudo passaria com folga em qualquer triagem, e ainda assim não deveria entrar no modelo principal do ensaio.
- Nenhuma: 0,20 é o limiar consagrado para triagem de covariáveis. | O limiar circula em manuais e continua sendo um automatismo, com os mesmos defeitos do stepwise, de que é primo próximo.
- A objeção é que 0,20 é liberal demais, e o correto seria 0,05. | Apertar o limiar não conserta o critério. O problema não é onde se corta, é cortar por p.
- A objeção é que a análise univariada não pode preceder a multivariada. | Descrever associações uma a uma é útil e legítimo. O que não se admite é que essa descrição decida sozinha o modelo.
- A objeção é que o procedimento exige mais eventos por variável. | Ele tende a inflar o modelo, e a crítica central é de validade, e não de contagem.
@ cap-12-o-que-e-um-confundidor
:::

## Exercícios

::: exercicio 1
Na coorte observacional, a razão de chances bruta foi 0,72 e a ajustada, 1,87.
Explique, em termos clínicos, o que aconteceu entre um número e outro.

--- gabarito
O tratamento foi dado preferencialmente a pacientes com pior prognóstico: úlceras
com o dobro da área, quase o dobro de duração e mais diabetes. Na comparação
bruta, o prognóstico ruim desses pacientes se somou ao efeito do tratamento e o
superou, produzindo a impressão de que o tratamento prejudica. O ajuste compara
pacientes com área, duração, diabetes e adesão semelhantes, e nessa comparação o
benefício reaparece. O que mudou não foi o tratamento: foi com quem ele estava
sendo comparado.
:::

::: exercicio 2
Por que a razão de chances ajustada da coorte, 1,87, ainda subestima o efeito
verdadeiro, que o ensaio estimou em 2,11?

--- gabarito
Porque o ajuste só corrige o que foi medido. Ficaram de fora da coorte variáveis
que influenciam a cicatrização e que também podem ter pesado na decisão de
indicar o tratamento: o índice tornozelo-braquial, a pressão transcutânea de
oxigênio, o estado nutricional, a experiência do cirurgião. Esse resíduo se chama
confundimento residual, e é impossível saber seu tamanho a partir dos próprios
dados, o que é justamente o problema.
:::

::: exercicio 3
No modelo do ensaio randomizado, a razão de chances bruta do tratamento foi 2,11
e a ajustada, 2,25. Por que a diferença é tão pequena aqui e tão grande na
coorte?

--- gabarito
Porque a randomização equilibrou os grupos quanto às covariáveis, de modo que
ajustar por elas quase não altera a estimativa do efeito. Essa estabilidade é uma
verificação valiosa: em um ensaio, uma diferença grande entre bruto e ajustado
levantaria suspeita sobre a alocação. Na coorte, os grupos eram desiguais desde a
origem, e o ajuste tinha muito o que corrigir.
:::

::: exercicio 4
A adesão à terapia compressiva teve razão de chances de 2,90, a maior do modelo.
Por que este livro recomenda, ainda assim, deixá-la fora do modelo principal de
um ensaio clínico?

--- gabarito
Porque ela foi medida depois da alocação e pode ser afetada pelo tratamento. Se o
aspirado reduz a dor e o paciente com menos dor tolera melhor a compressão, então
parte do benefício do tratamento passa pela adesão. Ajustar por ela subtrai esse
caminho e subestima o efeito total. Variáveis pós-randomização podem ser
analisadas em separado, como mediadores, mas não entram no ajuste do desfecho
primário.
:::

::: exercicio 5
Rode no jamovi a regressão logística do ensaio sem a variável adesão. O
coeficiente do tratamento sobe ou desce? O que isso diz?

--- gabarito
Ele muda pouco, porque a adesão está aproximadamente equilibrada entre os grupos,
75% contra 72%, graças à randomização. Uma variável só confunde se estiver
desbalanceada entre os grupos: por mais forte que seja seu efeito sobre o
desfecho, ela não distorce a comparação quando está igualmente distribuída. É
por isso que, em ensaios, o ajuste serve mais para ganhar precisão do que para
corrigir viés.
:::

::: exercicio 6
Um pesquisador quer estudar, em uma coorte, se o uso de bota de Unna melhora a
cicatrização, e pretende ajustar por "tempo até a cicatrização". Comente.

--- gabarito
Não faz sentido, e por dois motivos. O tempo até a cicatrização é uma forma do
próprio desfecho, e ajustar o desfecho por ele mesmo não é ajuste, é
circularidade. Além disso, ele é medido depois da exposição, e portanto violaria
a terceira condição de confundimento. O ajuste deve incluir características
basais que prevejam o desfecho, como área, duração, índice tornozelo-braquial e
comorbidades.
:::

::: agora
1. Liste as covariáveis do seu ajuste e escreva, ao lado de cada uma, **quando**
   ela foi medida. Toda variável medida depois da intervenção sai do modelo
   principal.
2. Conte os eventos do seu desfecho e divida por dez. Esse é o número máximo de
   variáveis que o seu modelo comporta. Se o seu modelo tem mais, corte.
3. Se o seu estudo é observacional, escreva agora, com todas as letras, o
   parágrafo sobre confundimento residual. Ele será cobrado, e escrevê-lo antes
   evita que a discussão prometa causalidade que o desenho não sustenta.
4. Apresente o efeito bruto e o ajustado lado a lado. A diferença entre os dois é
   informação, não constrangimento.
:::

## Recursos

- [STROBE Statement](https://www.strobe-statement.org/) — a recomendação para
  relato de estudos observacionais, com itens específicos sobre confundimento.
- [jamovi](https://www.jamovi.org/) — regressão logística e linear no menu
  Regression.
- [CONSORT Statement](https://www.consort-statement.org/) — item 12a, sobre
  declarar previamente os métodos de análise, incluindo o ajuste.

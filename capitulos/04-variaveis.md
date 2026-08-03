::: caso
O protocolo do estudo está escrito, o delineamento decidido, e chega a hora de
preencher a ficha de coleta. O que exatamente vai ser anotado sobre cada
paciente? A resposta parece administrativa e é a decisão mais determinante que
resta: variável mal definida não se conserta depois, e desfecho mal escolhido
inutiliza um estudo inteiro.
:::

## Os quatro tipos de variável

Toda a estatística deste livro depende de classificar corretamente cada coluna do
banco.

| Tipo | O que é | No estudo |
|---|---|---|
| **Nominal** | categorias sem ordem | sexo, grupo, centro, diabetes |
| **Ordinal** | categorias com ordem, sem distância definida | tabagismo, escore de dor |
| **Discreta** | contagem, valores inteiros | duração da úlcera em meses, número de recidivas |
| **Contínua** | mede-se, admite frações | área da úlcera, índice tornozelo-braquial, TcPO₂ |

A distinção entre ordinal e contínua é a que mais gera discussão. A escala visual
analógica de dor vai de 0 a 10, e é tentador tratá-la como contínua. O problema é
que a distância entre 2 e 3 não é necessariamente igual à distância entre 8 e 9:
a escala tem ordem, mas não tem régua. Na prática, escores com muitas categorias
são frequentemente analisados como contínuos, e a decisão precisa ser justificada
no protocolo, não improvisada na análise.

::: atencao Nunca dicotomize sem motivo clínico
Transformar uma variável contínua em duas categorias é a mutilação de dados mais
comum na pesquisa clínica. Ao trocar a área da úlcera pelos rótulos "grande" e
"pequena", perde-se informação, perde-se poder estatístico e cria-se a ilusão de
que 9,9 cm² e 10,1 cm² são casos diferentes enquanto 10,1 e 60,0 são iguais.

Dicotomize apenas quando o ponto de corte tiver significado clínico próprio e
anterior aos dados, como o corte de 40% de redução em quatro semanas usado no
Capítulo 13. E nunca escolha o corte testando vários e ficando com o que produz o
menor valor de p.
:::

## O papel de cada variável no estudo

Além do tipo, cada variável tem uma função, e confundir funções é o que produz as
análises erradas do Capítulo 12.

- **Desfecho, ou variável dependente:** o que o estudo quer explicar. Aqui, a
  cicatrização.
- **Exposição, ou variável independente principal:** o que se acredita influenciar
  o desfecho. Aqui, o grupo de tratamento.
- **Covariáveis prognósticas:** influenciam o desfecho e servem para ajustar e
  ganhar precisão. Área inicial, duração, diabetes.
- **Confundidoras:** covariáveis que também se associam à exposição. Em ensaio
  randomizado, em princípio não existem; em estudo observacional, dominam tudo.
- **Mediadoras:** estão no caminho causal entre exposição e desfecho, e não devem
  entrar no ajuste. A adesão à compressão, medida após a alocação, é a candidata
  neste estudo.

## O desfecho primário

Um estudo tem **um** desfecho primário. Não dois, não cinco. Ele define o cálculo
do tamanho da amostra, define a conclusão e é o único protegido contra a
multiplicidade discutida no Capítulo 10.

Escolher bem exige três qualidades:

**Ser importante para o paciente.** Cicatrização completa é o que o paciente
quer. Redução de área é um passo no caminho, e nível sérico de fator de
crescimento não interessa a ninguém fora do laboratório.

**Ser mensurável com objetividade.** É aqui que se ganha ou se perde o estudo,
e é aqui que entra a operacionalização.

**Ocorrer com frequência suficiente.** Desfecho raro exige amostra enorme, como o
Capítulo 6 demonstra com números.

### Operacionalizar é escrever a definição que não admite dúvida

"Cicatrização" não é uma definição: é uma palavra. A definição do protocolo é
esta:

> Epitelização completa da úlcera, sem necessidade de curativo, confirmada por
> avaliador cego em fotografia planimetrada e mantida por 14 dias.

Cada pedaço dessa frase evita um problema concreto. "Epitelização completa"
exclui a ferida quase fechada. "Sem necessidade de curativo" dá um critério
observável a quem não é especialista. "Avaliador cego" evita que a expectativa do
pesquisador influencie o julgamento. "Fotografia planimetrada" torna a avaliação
auditável meses depois. "Mantida por 14 dias" evita contar como cicatrizada uma
úlcera que reabriu na semana seguinte.

Um protocolo que diga apenas "cicatrização em 12 semanas" produzirá tantas
definições quantos forem os avaliadores.

::: nota Desfecho substituto: a tentação a evitar
Desfecho substituto é aquele que se mede no lugar do que interessa, por ser mais
rápido ou mais fácil: densidade óssea no lugar de fratura, carga viral no lugar
de sobrevida, redução de área no lugar de cicatrização. Ele acelera a pesquisa e
já enganou muita gente, porque tratamentos que melhoram o substituto às vezes
pioram o desfecho real. Se o estudo usar um substituto, isso precisa estar
explícito no título, no resumo e na conclusão.
:::

## Desfechos compostos, e por que este estudo não usou um

Desfecho composto reúne vários eventos em um só: por exemplo, "cicatrização ou
redução de área superior a 60%". Ele aumenta o número de eventos e reduz o
tamanho da amostra necessário, o que é tentador.

O preço é a interpretação. Se os componentes têm importâncias diferentes para o
paciente, o resultado passa a ser dominado pelo mais frequente, que costuma ser o
menos grave. Um composto que junta morte com internação é, na prática, um estudo
sobre internação. Quando o composto for inevitável, os componentes devem ser
relatados separadamente, e a conclusão não pode se apoiar apenas no agregado.

## As variáveis deste estudo, e por que cada uma está ali

| Variável | Tipo | Função | Por que foi coletada |
|---|---|---|---|
| `cicatrizacao_12sem` | nominal | desfecho primário | responde à pergunta do estudo |
| `reducao_area_4sem_pct` | contínua | desfecho secundário | mede evolução sem efeito teto |
| `tempo_ate_cicatrizacao_dias` | contínua | desfecho secundário | aproveita a informação do tempo |
| `area_inicial_cm2` | contínua | covariável prognóstica | maior preditor isolado da cicatrização |
| `duracao_ulcera_meses` | discreta | covariável prognóstica | úlcera antiga cicatriza menos |
| `itb` | contínua | critério de elegibilidade | exclui componente arterial |
| `tcpo2_basal` | contínua | teste índice | avaliado como preditor no Capítulo 13 |
| `adesao_compressao` | nominal | possível mediadora | descrever, não ajustar |
| `infeccao_ferida` | nominal | segurança | todo estudo precisa medir dano |

Repare no que **não** está na lista: dezenas de exames que poderiam ter sido
coletados e não foram. Ficha de coleta longa é ficha mal preenchida, e cada
variável a mais é um convite à análise exploratória que ninguém pediu.

::: jamovi
1. Importado o banco, vá à aba **Data** e clique em **Setup**. O jamovi mostra o
   tipo que atribuiu a cada variável, com três ícones: régua para contínua, barras
   para ordinal e círculos para nominal.
2. Corrija o que ele errou. `evento_cicatrizacao` vem como contínua, porque está
   codificada em 0 e 1, e precisa virar **nominal**.
3. Em variáveis nominais, use **Levels** para ordenar as categorias como você
   quer que apareçam nas tabelas, e para definir a categoria de referência das
   regressões.
4. Marque `tabagismo` como **ordinal** e ordene os níveis de "Nunca fumou" a
   "Fumante atual". Sem isso, as tabelas sairão em ordem alfabética, que não
   significa nada.

Nenhuma análise deste livro funciona corretamente se os tipos estiverem errados,
e o jamovi não avisa: ele simplesmente entrega um resultado sem sentido.
:::

::: revisor
**"O desfecho primário não está claramente definido."** Nome, momento da
aferição, critério e quem afere.

**"O artigo apresenta cinco desfechos primários."** Então não há desfecho
primário. Escolha um e reclassifique os demais.

**"O desfecho relatado difere do registrado no protocolo."** É troca de desfecho,
e o registro prévio existe justamente para expô-la. Se houve mudança, ela deve
ser declarada, datada e justificada.

**"Variável contínua dicotomizada sem justificativa."** Perde poder e infla o
risco de o corte ter sido escolhido pelos dados.

**"Desfecho composto sem relato dos componentes."** Apresente cada um
separadamente.

**"Não há desfecho de segurança."** Estudo de intervenção que só mede benefício
está incompleto.
:::

::: quiz
? [facil] A variável `tabagismo`, com as categorias "nunca fumou", "ex-fumante" e "fumante atual", é de que tipo?
+ Ordinal: categorias com ordem, mas sem distância definida entre elas. | Correto. Há uma ordem natural de exposição, e não se pode afirmar que a distância entre "nunca" e "ex" seja igual à distância entre "ex" e "atual".
- Nominal: categorias sem ordem. | Existe ordem, e ignorá-la faz as tabelas saírem em ordem alfabética, que não significa nada.
- Discreta: contagem de valores inteiros. | Não há contagem: são categorias, não números.
- Contínua: admite qualquer valor em uma faixa. | Não admite frações nem valores intermediários.
- Binária, depois de agrupar ex-fumantes com fumantes atuais. | Agrupar é uma decisão posterior e opcional; a variável, como está, tem três categorias ordenadas.
@ cap-4-os-quatro-tipos-de-variavel

? [facil] Quantos desfechos primários deve ter um estudo?
+ Um. | Correto. Ele define o cálculo do tamanho da amostra, define a conclusão e é o único protegido contra a multiplicidade discutida no Capítulo 10.
- Dois, um clínico e um laboratorial. | Dois desfechos primários significam, na prática, nenhum: a conclusão passa a poder se apoiar no que der certo.
- Quantos forem clinicamente relevantes. | Relevância clínica define quais desfechos medir, e não quantos são primários.
- Nenhum, se o estudo for exploratório. | Mesmo estudos exploratórios ganham em declarar o desfecho principal, e ensaios sempre exigem um.
- Depende do número de grupos comparados. | O número de grupos não altera essa regra.
@ cap-4-o-desfecho-primario

? [media] Por que a adesão à terapia compressiva não deve entrar no modelo de ajuste do desfecho primário?
+ Porque foi medida depois da alocação e pode ser consequência do próprio tratamento. | Correto. Se o aspirado reduz a dor e com isso melhora a tolerância à compressão, parte do benefício passa pela adesão, e ajustar por ela subtrai esse caminho.
- Porque tem muitos dados faltantes. | A adesão não tem faltantes no banco, e a razão para excluí-la é outra.
- Porque é uma variável nominal, e o modelo exige variáveis contínuas. | Modelos aceitam variáveis nominais sem problema.
- Porque seu efeito é pequeno demais para importar. | O efeito dela é o maior da tabela do Capítulo 12, com razão de chances de 2,90.
- Porque a randomização já a equilibrou entre os grupos. | O equilíbrio é real e é o que faz o ajuste alterar pouco, mas não é a razão para excluí-la: a razão é ela ser potencial mediadora.
@ cap-4-o-papel-de-cada-variavel-no-estudo

? [media] Qual é o problema de usar "redução percentual da área em 12 semanas" como desfecho primário deste estudo?
+ Ela satura em 100% para a maioria dos participantes e deixa de discriminar entre os grupos. | Correto. É o efeito teto: a mediana é 100% nos dois grupos, e nenhuma análise recupera informação que a escala destruiu.
- Ela não pode ser medida com precisão suficiente. | A planimetria mede bem; o problema é o limite superior da escala, e não a precisão.
- Ela exigiria uma amostra muito maior. | O tamanho não resolve um efeito teto.
- Ela é uma variável nominal, imprópria para desfecho primário. | É contínua. O problema é a distribuição, não o tipo.
- Ela não tem definição operacional possível. | Tem, e é objetiva: área inicial menos área final, dividida pela inicial.
@ cap-4-o-desfecho-primario

? [media] O que caracteriza uma definição operacional adequada de desfecho?
+ Diz o que é, quando se afere, com que critério e quem afere, de modo que dois avaliadores cheguem à mesma conclusão. | Correto. "Cicatrização" é uma palavra; a definição do protocolo especifica epitelização completa, sem curativo, confirmada por avaliador cego e mantida por catorze dias.
- Cita a referência bibliográfica de onde o desfecho foi tirado. | A referência ajuda a justificar a escolha, e não substitui a especificação operacional.
- Descreve o teste estatístico que será aplicado ao desfecho. | O teste vem depois e é assunto do Capítulo 11.
- Indica o valor considerado clinicamente relevante. | Isso é ingrediente do cálculo do tamanho da amostra, e não a definição do desfecho.
- Estabelece a unidade de medida e o número de casas decimais. | Necessário para variáveis contínuas, e muito longe de suficiente.
@ cap-4-o-desfecho-primario

? [dificil] Um pesquisador propõe o desfecho composto "cicatrização completa ou redução de área superior a 60%". Qual a principal consequência dessa escolha?
+ O resultado passa a ser dominado pelo componente mais frequente, que costuma ser o menos grave, e a interpretação clínica se torna ambígua. | Correto. Compostos aumentam o número de eventos e reduzem a amostra necessária, e o preço é a interpretação. Os componentes precisam ser relatados separadamente.
- O estudo passa a exigir amostra maior. | Ocorre o contrário: mais eventos exigem menos participantes, e é justamente essa tentação que leva ao composto.
- O desfecho deixa de ser binário e passa a ser contínuo. | Continua binário: o participante atinge ou não atinge o composto.
- O composto elimina a necessidade de definição operacional. | Ao contrário: cada componente precisa da sua.
- O composto impede o cálculo do risco relativo. | O risco relativo continua calculável.
@ cap-4-desfechos-compostos-e-por-que-este-estudo-nao-usou-um

? [dificil] Em que situação dicotomizar uma variável contínua é defensável?
+ Quando o ponto de corte tem significado clínico próprio e anterior aos dados, como a redução de 40% em quatro semanas. | Correto. O corte precisa existir antes e por razões clínicas. Escolher o corte que produz o menor valor de p é o que o livro condena.
- Sempre que a distribuição for assimétrica. | Assimetria se resolve com mediana e quartis, ou com transformação, e não descartando informação.
- Quando o programa estatístico não aceita variáveis contínuas no modelo. | Todos os programas aceitam, e a limitação não existe.
- Quando facilita a apresentação dos resultados em tabela. | Conveniência de apresentação não justifica perder poder estatístico.
- Quando o número de participantes é pequeno. | Amostra pequena é razão para preservar informação, e não para descartá-la.
@ cap-4-os-quatro-tipos-de-variavel
:::

## Exercícios

::: exercicio 1
Classifique quanto ao tipo: `centro`, `idade`, `dor_eva_basal`, `itb` e
`ulcera_recidivante`.

--- gabarito
`centro` é nominal, três categorias sem ordem. `idade` é discreta, contada em
anos completos, e na prática tratada como contínua. `dor_eva_basal` é ordinal,
embora frequentemente analisada como contínua, decisão que deve constar do
protocolo. `itb` é contínua. `ulcera_recidivante` é nominal dicotômica.
:::

::: exercicio 2
Escreva a definição operacional do desfecho "infecção da ferida", com detalhe
suficiente para que dois avaliadores diferentes cheguem à mesma conclusão.

--- gabarito
Uma definição aceitável: presença de pelo menos dois dos seguintes sinais, na
avaliação clínica presencial, confirmados por médico assistente e registrados em
prontuário: eritema perilesional maior que 2 cm, edema, calor local, secreção
purulenta, dor de início recente ou aumento súbito da área. Culturas positivas
sem sinais clínicos não constituem infecção, por representarem colonização. O
importante é que a definição liste os critérios, exija um número mínimo deles e
diga quem avalia e quando.
:::

::: exercicio 3
Um pesquisador propõe usar como desfecho primário "a redução percentual da área
em 12 semanas". Aponte o problema, com base no que o Capítulo 8 mostrou.

--- gabarito
Essa variável tem efeito teto: mais da metade dos participantes atinge 100% de
redução, e a mediana é 100% nos dois grupos, o que a torna incapaz de discriminar.
Além disso, ela é um desfecho substituto da cicatrização, que é o que interessa
ao paciente. Como desfecho primário, a cicatrização completa é superior; a
redução de área tem seu lugar como desfecho secundário, e de preferência aferida
em quatro semanas.
:::

::: exercicio 4
Por que a adesão à terapia compressiva não deve entrar no modelo de ajuste do
desfecho primário?

--- gabarito
Porque foi medida depois da alocação e pode ser consequência do tratamento. Se o
aspirado reduzir a dor e com isso melhorar a tolerância à compressão, parte do
benefício passa por ela, e ajustar removeria esse caminho. Variáveis
pós-randomização são potenciais mediadoras, não confundidoras, e o Capítulo 12
detalha a distinção.
:::

::: exercicio 5
Você tem uma variável "grau de dor" com as categorias ausente, leve, moderada e
intensa. Quais análises são legítimas e quais não são?

--- gabarito
É ordinal. São legítimas: descrever com número e percentual por categoria,
comparar grupos com qui-quadrado ou com testes por postos como Mann-Whitney, e
usar regressão logística ordinal. Não é legítimo calcular média sem justificar,
porque as distâncias entre categorias não são conhecidas, nem afirmar que
"intensa é o dobro de leve".
:::

::: exercicio 6
Abra o banco no jamovi e corrija os tipos de todas as variáveis. Depois produza
uma tabela de frequência de `tabagismo` antes e depois de ordenar os níveis.

--- gabarito
Antes da ordenação, as categorias aparecem em ordem alfabética: Ex-fumante,
Fumante atual, Nunca fumou. Depois, na ordem lógica: Nunca fumou, Ex-fumante,
Fumante atual. Os números são idênticos; o que muda é a legibilidade, e é essa
tabela que vai para o artigo. O exercício mostra que boa parte do trabalho
estatístico é organização, não cálculo.
:::

::: agora
1. Escreva a definição operacional do seu desfecho primário e peça a um colega
   que a aplique a três pacientes sem falar com você. Se ele classificar
   diferente, a definição ainda não está pronta.
2. Liste todas as variáveis da sua ficha de coleta e escreva, ao lado de cada
   uma, o tipo e a função. As que não tiverem função devem sair da ficha.
3. Confira se alguma variável que você pretende usar no ajuste é medida **depois**
   da intervenção. Se for, ela é candidata a mediadora e não entra no modelo
   principal.
:::

## Recursos

- [CONSORT Statement](https://www.consort-statement.org/) — item 6a, sobre
  definir completamente os desfechos primário e secundários.
- [SPIRIT](https://www.spirit-statement.org/) — a recomendação para conteúdo de
  protocolos de ensaios clínicos, que detalha a definição de desfechos.
- [jamovi](https://www.jamovi.org/) — os tipos de variável ficam na aba Data,
  botão Setup.

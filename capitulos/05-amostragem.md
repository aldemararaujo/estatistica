::: caso
Os duzentos participantes do estudo vieram de três ambulatórios de cirurgia
vascular, entre pacientes que procuraram atendimento e aceitaram participar. A
conclusão do estudo, no entanto, não é sobre eles: é sobre pacientes com úlcera
venosa em geral. Este capítulo trata da distância entre uma coisa e outra, e do
que se pode honestamente afirmar apesar dela.
:::

## Três populações, não uma

Todo estudo lida com três conjuntos encaixados, e confundi-los produz conclusões
que não se sustentam.

**População-alvo.** Todos os pacientes sobre os quais se quer concluir alguma
coisa: adultos com úlcera venosa ativa de membro inferior, no Brasil e fora dele.
É a população que interessa e à qual não se tem acesso.

**População acessível.** A parte dela que o pesquisador poderia alcançar:
pacientes com úlcera venosa atendidos naqueles três ambulatórios, no período do
estudo.

**Amostra.** Os 200 que efetivamente entraram.

A validade de um estudo se decide em dois saltos. O primeiro, da amostra para a
população acessível, é problema de amostragem e de tamanho, e a estatística
resolve. O segundo, da população acessível para a população-alvo, **a estatística
não resolve**: é julgamento clínico sobre semelhança. Nenhum intervalo de
confiança cobre a diferença entre um ambulatório universitário de Maceió e um
posto de saúde rural.

## Quem entra, quem fica de fora

Antes de qualquer técnica de amostragem, a população acessível é definida pelos
critérios de elegibilidade. São eles, e não a técnica, que decidem a quem o
resultado se aplica.

| Critérios de inclusão | Critérios de exclusão |
|---|---|
| Idade ≥ 18 anos | Índice tornozelo-braquial < 0,80 |
| Úlcera venosa ativa, CEAP C6 | Úlcera de etiologia não venosa |
| Duração ≥ 4 semanas | Infecção ativa em tratamento |
| Área entre 1 e 50 cm² | Discrasia sanguínea ou uso de anticoagulante pleno |
| Consentimento assinado | Neoplasia ativa ou expectativa de vida < 6 meses |

Cada exclusão é uma troca. Excluir índice tornozelo-braquial abaixo de 0,80
protege o estudo, porque úlcera de componente arterial responde de outro jeito, e
ao mesmo tempo retira da conclusão uma parcela grande dos pacientes reais, que
frequentemente têm doença mista. Critérios apertados aumentam a validade interna
e reduzem a externa. Critérios frouxos fazem o contrário.

Não existe escolha certa: existe escolha declarada. O que não se admite é
descobrir os critérios depois, olhando quem deu certo.

## As técnicas de amostragem

Antes de percorrê-las, uma distinção que evita confusão constante: a **técnica**
de amostragem responde a *como* se seleciona, e é assunto deste capítulo; o
**tamanho** da amostra responde a *quantos*, e é assunto do próximo. São decisões
independentes, e a segunda não conserta a primeira. Uma amostra de dez mil
pessoas mal selecionadas descreve com enorme precisão uma realidade que não
existe.

### Probabilísticas

Todo elemento da população tem probabilidade conhecida e não nula de ser
sorteado. São as únicas que autorizam, em rigor, a inferência estatística
clássica.

- **Aleatória simples:** sorteio direto a partir de uma lista completa da
  população, o chamado marco amostral. Exige a lista, o que em pesquisa clínica
  quase nunca existe.
- **Sistemática:** sorteia-se o primeiro e depois se toma um a cada k. Simples e
  eficiente, e perigosa se a lista tiver periodicidade oculta.
- **Estratificada:** divide-se a população em estratos e sorteia-se dentro de
  cada um, garantindo representação de subgrupos pequenos. É o que se faria para
  assegurar diabéticos suficientes.
- **Por conglomerados:** sorteiam-se grupos inteiros, como unidades de saúde, e
  não indivíduos. Barata para estudos populacionais, e exige análise que leve em
  conta a correlação dentro de cada conglomerado, sob pena de intervalos falsamente
  estreitos.

### Não probabilísticas

- **Consecutiva:** incluem-se todos os elegíveis, na ordem em que aparecem, até
  completar o tamanho previsto. É a mais usada e a melhor das não probabilísticas,
  porque não deixa margem para o pesquisador escolher.
- **Por conveniência:** quem estiver à mão. Rápida e frágil.
- **Intencional:** o pesquisador escolhe quem julga representativo. Legítima em
  pesquisa qualitativa, indefensável em estudo quantitativo de eficácia.
- **Bola de neve:** cada participante indica outros. Útil em populações de difícil
  acesso, como portadores de condições estigmatizadas, com o custo de amostrar
  redes sociais em vez de indivíduos.
- **Por cotas:** definem-se números a atingir em cada subgrupo, e a vaga de cada
  cota é preenchida por conveniência. É a irmã não probabilística da
  estratificada, e a diferença entre as duas está exatamente aí: a estratificada
  **sorteia** dentro do estrato, a por cotas apenas **preenche** a vaga. A
  composição da amostra fica parecida com a da população, sem que isso garanta
  representatividade.

Este estudo usou **amostragem consecutiva**, que é o padrão dos ensaios clínicos,
e o registrou no protocolo.

::: nota Amostragem qualitativa não se dimensiona, se satura
Em pesquisa qualitativa, a amostragem costuma ser intencional e o critério de
parada não é um número calculado de antemão: é a **saturação teórica**, o ponto a
partir do qual novas entrevistas deixam de trazer conteúdo novo. O procedimento
precisa ser descrito com o mesmo rigor de um cálculo amostral, dizendo como a
saturação foi constatada e por quem. Não é uma versão relaxada da amostragem: é
outra lógica, com outro critério de suficiência.
:::

::: atencao Amostragem aleatória e randomização não são a mesma coisa
Esta é a confusão mais comum do assunto, e ela custa caro na hora de interpretar.

**Amostragem aleatória** decide *quem entra* no estudo, a partir da população.
Protege a **validade externa**, ou seja, a possibilidade de generalizar.

**Randomização** decide, entre os que já entraram, *quem vai para qual grupo*.
Protege a **validade interna**, ou seja, a comparabilidade entre os grupos.

Este estudo é randomizado e **não** tem amostra aleatória, o que é a situação de
praticamente todo ensaio clínico do mundo. A comparação entre os grupos é
protegida; a extrapolação para outros serviços é argumento clínico, não garantia
estatística.
:::

## Vieses de seleção

**Viés do voluntário.** Quem aceita participar difere de quem recusa: costuma ser
mais aderente, mais motivado e mais bem informado. Em estudo de tratamento que
depende de adesão, como a terapia compressiva, isso tende a produzir resultados
melhores do que a prática real.

**Viés de sobrevivência.** Estudar apenas pacientes que chegaram ao ambulatório
terciário exclui os que cicatrizaram antes na atenção básica, e a amostra fica
mais grave que a população.

**Viés do trabalhador sadio**, nas coortes ocupacionais, e **viés de Berkson**,
quando se recrutam apenas internados: variantes do mesmo problema, que é a
amostra ter sido filtrada por algo relacionado ao desfecho.

O antídoto não é eliminar o viés, o que raramente é possível, e sim descrever o
recrutamento com detalhe suficiente para o leitor julgar a direção e o tamanho
provável dele. É por isso que o diagrama CONSORT começa com o número de pacientes
avaliados para elegibilidade, e não com o número de randomizados.

## O que a amostra deste estudo representa

Vale aplicar o raciocínio ao próprio caso condutor. A amostra tem idade mediana
de 62 anos, quase metade de mulheres, 22% de diabéticos, área mediana de úlcera
de 7,7 cm² e duração mediana de 13 meses, e todos com índice tornozelo-braquial
acima de 0,80.

O resultado se aplica com tranquilidade a pacientes semelhantes a esses. Aplica-se
com cautela a idosos com doença arterial associada, que foram excluídos, e a
úlceras muito maiores que 50 cm², que também foram. E não se aplica a úlceras de
outra etiologia, que nunca estiveram no estudo.

Descrever isso na discussão não enfraquece o artigo: é o que permite que outra
pessoa o use.

::: jamovi
O jamovi não sorteia amostras, porque não é essa a sua função. Mas dá para
demonstrar o efeito do acaso amostral com o próprio banco, e o exercício vale
mais que muita teoria:

1. Em **Data**, **Compute**, crie uma variável com a fórmula `UNIF(0, 1)`, que
   gera um número aleatório para cada participante.
2. Ordene o banco por ela e tome os 30 primeiros como se fossem uma amostra do
   estudo.
3. Calcule nessa subamostra a proporção de cicatrização por grupo, e compare com
   os 70,7% e 53,3% do estudo completo.
4. Repita o procedimento algumas vezes.

Você verá a estimativa oscilar bastante de uma repetição para outra. Essa
oscilação é exatamente o que o intervalo de confiança do Capítulo 9 mede, e ver
com os próprios olhos costuma ensinar mais do que a fórmula.
:::

::: revisor
**"Não está descrito como os participantes foram recrutados."** Diga o local, o
período, o método de amostragem e quem convidou.

**"O número de pacientes avaliados para elegibilidade não é informado."** Sem
ele, não há como julgar viés de seleção. É o primeiro quadro do diagrama
CONSORT.

**"Os motivos de exclusão não estão detalhados."** Quantos foram excluídos por
cada critério, e quantos recusaram.

**"Os autores generalizam para a atenção primária um resultado obtido em serviço
terciário."** Discuta a validade externa em vez de ignorá-la.

**"O estudo afirma ter usado amostra aleatória quando descreve, na verdade, a
randomização."** São coisas diferentes e a troca aparece com frequência
constrangedora.

**"Amostragem por conveniência apresentada como se fosse consecutiva."** Se
houve seleção do pesquisador, isso muda a interpretação e precisa estar escrito.
:::

## Exercícios

::: exercicio 1
Explique, em duas frases, a diferença entre a randomização e a amostragem
aleatória neste estudo.

--- gabarito
A randomização sorteou, entre os 200 participantes já incluídos, quem receberia o
aspirado e quem receberia apenas compressão, e é ela que torna os dois grupos
comparáveis. A amostragem aleatória teria sorteado quais pacientes com úlcera
venosa do país entrariam no estudo, o que não aconteceu: os participantes foram
os que procuraram três ambulatórios específicos e aceitaram participar.
:::

::: exercicio 2
O estudo excluiu pacientes com índice tornozelo-braquial abaixo de 0,80. Qual o
ganho e qual o custo dessa decisão?

--- gabarito
O ganho é de validade interna: úlceras com componente arterial têm fisiopatologia
e prognóstico diferentes, e incluí-las adicionaria ruído e possivelmente
mascararia o efeito do tratamento. O custo é de validade externa: doença venosa e
arterial coexistem com frequência na população idosa, e o resultado não se aplica
a esses pacientes, que são numerosos na prática. A decisão é defensável desde que
a limitação seja declarada.
:::

::: exercicio 3
Um pesquisador convida para o estudo apenas pacientes que ele considera "bons
aderentes", para reduzir perdas. Que tipo de viés ele introduz e o que acontece
com o resultado?

--- gabarito
É amostragem intencional, e o viés é de seleção. O efeito provável é
superestimar o benefício do tratamento, porque pacientes aderentes usam melhor a
compressão, que é a base da terapia nos dois grupos, e comparecem às avaliações.
O estudo passaria a responder "qual o efeito em pacientes selecionados como
ideais", que não é a pergunta clínica relevante. Além disso, a seleção depende do
julgamento subjetivo do pesquisador, que não é reprodutível por ninguém.
:::

::: exercicio 4
Descreva como você faria uma amostragem estratificada para garantir que
diabéticos fossem 30% da amostra, e diga por que alguém faria isso.

--- gabarito
Dividiria a população acessível em dois estratos, com e sem diabetes, e
recrutaria dentro de cada um até completar 60 diabéticos e 140 não diabéticos.
Faria isso quem pretende analisar o efeito do tratamento no subgrupo de
diabéticos com poder suficiente, já que a proporção natural, de cerca de 22%,
resultaria em poucos casos. O preço é que a amostra deixa de refletir a
proporção real da população, e qualquer estimativa global precisa ser ponderada.
:::

::: exercicio 5
Por que o diagrama CONSORT exige informar quantos pacientes foram avaliados para
elegibilidade, e não apenas quantos foram randomizados?

--- gabarito
Porque a razão entre avaliados e incluídos revela quão selecionada é a amostra.
Um estudo que avaliou 210 e incluiu 200 recrutou quase todo mundo que apareceu, e
sua amostra se parece com a população atendida. Outro que avaliou 2.000 para
incluir 200 aplicou um filtro pesado, e o leitor precisa saber qual foi, para
julgar a quem o resultado se aplica.
:::

::: exercicio 6
Uma pesquisadora quer que sua amostra tenha 30% de diabéticos e recruta, na sala
de espera, os primeiros pacientes que encontra até completar 60 diabéticos e 140
não diabéticos. Que técnica ela usou? É a mesma coisa que amostragem
estratificada?

--- gabarito
Ela usou amostragem **por cotas**, que é não probabilística. A composição final da
amostra fica idêntica à que uma estratificada produziria, e é justamente isso que
engana: a semelhança é só de aparência. Na estratificada, o participante de cada
estrato é **sorteado**, e cada elegível tem probabilidade conhecida de entrar; na
por cotas, a vaga é preenchida por quem estava à mão, o que reintroduz o viés de
conveniência dentro de cada subgrupo. Quem chega cedo à sala de espera difere de
quem chega tarde, e a cota não protege contra isso.
:::

::: exercicio 7
Faça o exercício do jamovi descrito neste capítulo, tomando três subamostras de
30 participantes. Anote a proporção de cicatrização de cada uma e compare com a
do estudo completo.

--- gabarito
Não há resposta única, e é esse o ponto. Com trinta participantes, as proporções
observadas costumam variar em uma faixa larga em torno dos valores do estudo
completo, e não é raro que uma das subamostras inverta a direção da diferença
entre os grupos. Essa é a variabilidade amostral, é ela que o intervalo de
confiança quantifica, e é também o argumento mais concreto a favor de calcular o
tamanho da amostra antes de começar, assunto do próximo capítulo.
:::

## Recursos

- [Simulador de amostragem](https://aldemararaujo.github.io/amostra/) — mostra,
  em tempo real, o que este capítulo argumenta: aumentar o número de
  participantes ajuda, e não resolve uma técnica de seleção ruim.
- [CONSORT Statement](https://www.consort-statement.org/) — o diagrama de fluxo e
  os itens sobre elegibilidade e recrutamento.
- [STROBE Statement](https://www.strobe-statement.org/) — itens equivalentes para
  estudos observacionais.
- [jamovi](https://www.jamovi.org/) — a função UNIF, em Data, Compute, permite a
  demonstração deste capítulo.

### Para aprofundar

- Szwarcwald CL et al. [Inquéritos nacionais de saúde: visão geral sobre técnicas
  de amostragem em pesquisas brasileiras](https://www.scielosp.org/article/ress/2023.v32n3/e2023431/pt/).
  *Epidemiol Serv Saude*. 2023;32(3). Como os grandes inquéritos brasileiros
  combinam estratificação e conglomerados para representar um país de dimensões
  continentais.
- Fontanella BJB et al. [Amostragem em pesquisas qualitativas: proposta de
  procedimentos de constatação de saturação teórica](https://www.scielo.br/j/csp/a/3bsWNzMMdvYthrNCXmY9kJQ/).
  *Cad Saude Publica*. 2011;27(2):389-94. O critério de parada da amostragem
  qualitativa, tratado com o rigor que ele exige.
- Miot HA. [Tamanho da amostra em estudos clínicos e
  experimentais](https://www.scielo.br/j/jvb/a/Dxg84WBMPnNrVcpKMXyVfHd/).
  *J Vasc Bras*. 2011;10(4):275-8. Faz a ponte com o Capítulo 6.
- Pablos-Mendez A et al. [Run-in periods in clinical trials: implications for the
  selection of patients](https://pubmed.ncbi.nlm.nih.gov/9556634/). *JAMA*.
  1998;279(3):222-5. Como os critérios de seleção iniciais "limpam" a amostra e
  produzem resultados que não se reproduzem no paciente real.

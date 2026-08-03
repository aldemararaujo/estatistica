::: caso
Um cirurgião vascular acompanha uma paciente de 64 anos com úlcera venosa há
catorze meses. Ele já tentou tudo o que sabe. Leu sobre uma terapia nova, viu
relatos favoráveis, e precisa decidir se oferece aquilo a ela. A pergunta que ele
tem diante de si não é estatística: é clínica. A estatística entra porque é a
única maneira conhecida de responder a ela sem se enganar.
:::

## O que é

Estatística aplicada à pesquisa clínica é o conjunto de decisões que permitem
concluir alguma coisa sobre pessoas que não foram estudadas, a partir de pessoas
que foram.

Essa definição é diferente da que costuma abrir os manuais, que falam em coleta,
organização e análise de dados. A diferença é deliberada. Coletar e organizar são
tarefas; o que caracteriza a disciplina é o **salto**: da amostra para a
população, do que aconteceu para o que tende a acontecer, dos duzentos pacientes
do estudo para a paciente de 64 anos do ambulatório.

Todo este livro trata desse salto: de quando ele é legítimo, de quanto se pode
confiar nele e das decisões que o tornam possível.

Note também o que a estatística **não** é. Não é matemática aplicada no sentido
de cálculo: nenhuma fórmula deste livro exige mais do que uma raiz quadrada. Não
é programa de computador. E não é uma etapa do fim do projeto, embora seja
tratada assim na maioria das dissertações, quando já não há o que corrigir.

## Qual a importância

Sem ela, o pesquisador fica à mercê de três armadilhas que a intuição clínica não
detecta.

**O acaso.** Doze de quinze pacientes cicatrizaram. É bom? Depende de quantos
cicatrizariam sem tratamento algum, e depende de quinze ser um número pequeno o
bastante para que o resultado se inverta na próxima rodada. A intuição não sabe
responder; o Capítulo 9 sabe.

**O confundimento.** Quem recebeu o tratamento novo tinha úlceras piores. A
comparação bruta mede gravidade, não tratamento, e produz uma conclusão invertida
sem que nada no processo pareça errado. O Capítulo 12 mostra isso acontecendo com
números.

**A si mesmo.** Esta é a mais séria. Quem passou dois anos coletando dados quer
que o resultado seja positivo, e existe uma quantidade enorme de decisões
pequenas, cada uma defensável, que empurram o resultado na direção desejada:
excluir aquele paciente atípico, testar mais um desfecho, escolher o corte que
funciona melhor, trocar o teste que deu 0,06 pelo que deu 0,04. Nenhuma dessas
decisões é fraude, e o conjunto delas produz literatura não reprodutível.

A estatística, feita como este livro propõe, é sobretudo um sistema de
compromissos assumidos antes de olhar os dados. É por isso que o desfecho
primário é um só, que o tamanho da amostra se calcula antes e que o protocolo se
registra: não porque a conta seja difícil, mas porque a tentação é real.

## Quem deve fazer

O pesquisador, com auxílio de estatístico quando necessário. As duas metades
dessa frase importam.

O pesquisador precisa dominar as decisões deste livro porque **elas são
clínicas**, não matemáticas. Qual a menor diferença que mudaria a conduta? O
desfecho substituto é aceitável? Aquela variável foi medida antes ou depois da
intervenção? Um estatístico não tem como responder a nenhuma delas sozinho, e
entregar a ele um banco pronto com a pergunta "o que dá significativo aqui?" é a
maneira mais eficiente de produzir um estudo ruim.

O estatístico é indispensável quando o delineamento é complexo, quando há análise
interina, dados hierárquicos, desfechos múltiplos, dados faltantes em grande
volume ou modelagem sofisticada. E ele deve ser chamado **no planejamento**. A
frase de Ronald Fisher continua exata: consultar o estatístico depois do
experimento terminado costuma ser pedir a ele um exame *post mortem*, que dirá, no
máximo, do que o estudo morreu.

## Quando fazer

Antes, durante e depois, nesta proporção:

| Etapa | Trabalho estatístico | Peso |
|---|---|---|
| Planejamento | pergunta, delineamento, desfecho, tamanho da amostra, plano de análise | 60% |
| Coleta | banco, dicionário, monitoramento de qualidade e de perdas | 25% |
| Análise e relato | executar o plano, relatar conforme a recomendação | 15% |

A distribuição costuma surpreender, e é o resumo da tese deste livro. A análise
propriamente dita, que é o que a maioria chama de "a estatística", é a menor
fração do trabalho, e é a única que não pode consertar nada do que veio antes.

## Onde fazer

Em qualquer lugar, com um computador comum. Este livro usa o **jamovi**, que é
gratuito, funciona por cliques, roda em Windows, macOS e Linux, e produz saídas
que se copiam direto para o manuscrito. Não há neste livro nenhuma análise que
exija programa pago.

Programas mudam. As decisões deste livro, não. Quem entender por que se escolhe
uma mediana em vez de uma média fará isso no jamovi, no R, no SPSS ou no que
vier depois deles.

## Como fazer

Seguindo o percurso das decisões, que é a ordem dos capítulos:

1. A dúvida clínica vira pergunta estruturada (Capítulo 2).
2. A pergunta determina o delineamento (Capítulo 3).
3. O delineamento exige definir o que medir (Capítulo 4) e em quem (Capítulo 5).
4. O desfecho determina quantos participantes (Capítulo 6).
5. A coleta produz um banco que precisa ser analisável (Capítulo 7).
6. Os dados se descrevem antes de se testar (Capítulo 8).
7. O resultado se expressa como estimativa com incerteza (Capítulo 9), e só
   então como valor de p (Capítulo 10).
8. O teste se escolhe pela natureza do desfecho e do delineamento (Capítulo 11).
9. Quando é preciso ajustar, entra a regressão (Capítulo 12).
10. Perguntas especiais pedem ferramentas próprias: acurácia diagnóstica
    (Capítulo 13) e tempo até o evento (Capítulo 14).
11. E tudo termina em um relato que permita a outra pessoa julgar (Capítulo 15).

Cada capítulo acompanha o mesmo estudo clínico, do começo ao fim, e cada um traz
uma seção sobre os erros que fazem um artigo ser rejeitado, e outra com o que
fazer, naquele tema, no seu próprio projeto.

## Quanto custa

Menos do que se imagina, e o cálculo vale ser feito.

**Programa:** zero. O jamovi é gratuito, assim como o R.

**Tempo:** o custo real. Aprender o conteúdo deste livro leva algumas semanas de
estudo aplicado a um projeto próprio. Consultar um estatístico no planejamento
custa algumas horas de reunião.

**O custo de não fazer:** um estudo subdimensionado consome dois anos de trabalho
e não responde à pergunta. Um desfecho mal definido inviabiliza a análise. Um
banco malfeito obriga a redigitar tudo. Uma conclusão exagerada volta da revisão,
quando não é aceita e induz conduta errada.

A pergunta "quanto custa fazer estatística direito" tem, portanto, uma resposta
curta: muito menos do que custa fazer errado, e o pagamento é antecipado, o que é
justamente o que o torna difícil.

::: nota Uma observação sobre o exemplo deste livro
O estudo que acompanha os capítulos é fictício e seus dados são simulados. O
banco está disponível, todos os números impressos podem ser reproduzidos, e as
decisões que ele obriga a tomar são as mesmas de qualquer estudo real. Um estudo
verdadeiro dessa natureza exigiria aprovação em Comitê de Ética em Pesquisa,
registro prévio em plataforma pública e consentimento livre e esclarecido, temas
do Capítulo 2.
:::

::: revisor Aqui é onde o projeto naufraga
Os erros deste capítulo não aparecem em uma seção de métodos: aparecem na história
inteira do projeto.

**"O estatístico foi consultado após o término da coleta."** Ele fará o que puder,
e o que puder será pouco.

**"O projeto trata a análise estatística como etapa final."** O cronograma revela
isso: quando "análise dos dados" ocupa duas semanas no fim e não há nenhuma
atividade metodológica no começo, o problema já está instalado.

**"O pesquisador não sabe explicar por que escolheu aquele desfecho."** Se a
resposta for "porque é o que dá para medir", o estudo responderá a uma pergunta
que ninguém fez.

**"O projeto não tem pergunta, tem tema."** "Úlcera venosa" é um tema. Perguntas
têm ponto de interrogação, e o Capítulo 2 mostra como chegar a uma.
:::

::: quiz
? [facil] Segundo este capítulo, qual fração do trabalho estatístico de um estudo acontece na fase de planejamento?
+ Cerca de 60%, contra 25% na coleta e 15% na análise. | Correto. É a tese central do livro: a análise, que a maioria chama de "a estatística", é a menor parte do trabalho, e é a única incapaz de consertar o que veio antes.
- Cerca de 15%, porque planejar é rápido e analisar é demorado. | Inverte a proporção. Analisar é a etapa mais rápida e a mais dependente de tudo o que foi decidido antes.
- Cerca de 50%, dividido igualmente com a análise. | O peso do planejamento é maior, e a coleta também consome mais que a análise.
- Nenhuma: a estatística começa quando os dados chegam. | É exatamente a crença que este livro combate, e a que produz estudos irrecuperáveis.
- Depende do programa estatístico usado. | A escolha do programa não altera onde está o trabalho intelectual do estudo.
@ cap-1-quando-fazer

? [facil] O que caracteriza a estatística aplicada à pesquisa clínica, na definição deste capítulo?
+ O conjunto de decisões que permite concluir sobre pessoas que não foram estudadas, a partir das que foram. | Correto. O que define a disciplina é o salto da amostra para a população, e não as tarefas de coletar e organizar.
- A coleta, a organização e a apresentação de dados. | É a definição dos manuais tradicionais, e ela descreve tarefas, não o que caracteriza a disciplina.
- O cálculo de médias, desvios e valores de p. | Cálculo é a menor parte, e nenhuma fórmula deste livro exige mais que uma raiz quadrada.
- O domínio de um programa estatístico. | Programas mudam; as decisões, não. Quem entende por que escolhe a mediana fará isso em qualquer programa.
- A aplicação de testes de hipótese aos resultados obtidos. | Reduz a disciplina à sua etapa final, que é justamente a que não conserta nada.
@ cap-1-o-que-e

? [media] Um pesquisador terminou a coleta de 60 pacientes e procura um estatístico perguntando "o que dá significativo aqui?". Qual o problema central dessa abordagem?
+ As decisões que determinam se o estudo responde à pergunta já foram tomadas, e nenhuma análise as desfaz. | Correto. O estatístico poderá, no máximo, dizer do que o estudo morreu, na imagem de Fisher citada no capítulo.
- Nenhum, desde que o estatístico seja experiente. | Experiência não recupera variáveis não coletadas, desfecho mal definido nem amostra insuficiente.
- O problema é apenas de custo, porque a consultoria fica mais cara. | O custo é o menor dos problemas: o estudo pode simplesmente não ter resposta a dar.
- O erro é procurar um estatístico, já que o pesquisador deveria analisar sozinho. | O capítulo defende o contrário: o estatístico é indispensável em situações complexas, mas precisa ser chamado no planejamento.
- Procurar "o que dá significativo" é aceitável em estudos exploratórios. | Mesmo em estudo exploratório, garimpar significância sem declarar o que se procurava produz achados que não se replicam.
@ cap-1-quem-deve-fazer

? [media] Entre as decisões abaixo, qual **não** pode ser delegada ao estatístico?
+ Qual a menor diferença que mudaria a conduta clínica. | Correto. É decisão clínica, não estatística, e é o ingrediente que o Capítulo 6 mostra ser o mais errado de todos no cálculo do tamanho da amostra.
- Qual teste se aplica a um desfecho binário com dois grupos independentes. | Essa é técnica, e o estatístico responde com facilidade.
- Como tratar dados faltantes em grande volume. | Exige método, e é uma das situações em que o capítulo recomenda explicitamente consultar um estatístico.
- Como modelar dados hierárquicos de um estudo por conglomerados. | Também é técnica e complexa, e o capítulo a lista entre as que exigem estatístico.
- Como calcular o intervalo de confiança de uma razão de riscos. | É conta, e o programa a faz.
@ cap-1-quem-deve-fazer

? [media] O capítulo afirma que a terceira armadilha, enganar a si mesmo, é a mais séria. Por quê?
+ Porque cada decisão isolada parece defensável, e o viés nasce da direção em que todas elas pendem. | Correto. Excluir um caso atípico, testar mais um desfecho, ajustar um corte: nada disso é fraude, e o conjunto produz literatura que não se replica.
- Porque a maioria dos pesquisadores age de má-fé. | O capítulo diz o oposto: nenhuma dessas decisões é fraude, e é justamente por isso que o problema passa despercebido.
- Porque os programas estatísticos têm erros de cálculo. | Não é disso que se trata. A conta costuma estar certa; a escolha do que calcular é que foi contaminada.
- Porque o acaso é imprevisível. | O acaso é a primeira armadilha, e é diferente desta.
- Porque revisores não conseguem detectar erros de análise. | Muitos erros são detectáveis, e o livro dedica uma seção por capítulo a eles. O que não se detecta é a decisão que não foi relatada.
@ cap-1-qual-a-importancia

? [dificil] Um serviço tem verba para um único estudo e hesita entre gastar em consultoria metodológica no planejamento ou em análise estatística ao final. Com base neste capítulo, qual argumento sustenta a primeira opção?
+ O custo de um estudo subdimensionado ou mal desenhado é o desperdício de todo o investimento restante, e a consultoria inicial é a fração mínima que protege o resto. | Correto. É o raciocínio da seção sobre custo: o pagamento é antecipado, e é isso que o torna difícil de aceitar.
- Consultoria no planejamento é mais barata que a análise final. | Pode até ser, mas o argumento decisivo não é o preço relativo, e sim o que cada uma consegue evitar.
- A análise final pode ser feita gratuitamente no jamovi. | O programa é gratuito, mas executar uma análise não substitui decidir o que analisar.
- Comitês de ética exigem consultoria metodológica prévia. | Comitês exigem cálculo de tamanho de amostra, o que não é a mesma coisa, e o argumento aqui é de mérito, não de exigência formal.
- A análise só pode ser feita por estatístico, e o planejamento pode ser feito pelo pesquisador. | Inverte a divisão de trabalho proposta pelo capítulo, que atribui ao pesquisador as decisões clínicas do planejamento.
@ cap-1-quanto-custa

? [dificil] Por que o capítulo afirma que "estatística não é matemática aplicada no sentido de cálculo"?
+ Porque o que a caracteriza são decisões sobre delineamento, medida e inferência, e não a execução de fórmulas. | Correto. Nenhuma fórmula do livro exige mais que uma raiz quadrada, e ainda assim o livro tem dezesseis capítulos: o conteúdo está nas decisões.
- Porque os cálculos são feitos por computador e não interessam mais. | O computador executa, e continuar sem entender o que ele executa é justamente o que produz resultados sem sentido.
- Porque a matemática envolvida é elementar demais para ser chamada assim. | O grau de dificuldade da conta não é o critério, e sim a natureza do trabalho.
- Porque a estatística clínica é qualitativa, e não quantitativa. | Ela é quantitativa. O que se nega é que seu conteúdo se reduza ao ato de calcular.
- Porque a inferência é subjetiva e depende do pesquisador. | A inferência tem regras, e o livro inteiro trata delas. Reconhecer que há decisões não é dizer que tudo é subjetivo.
@ cap-1-o-que-e
:::

## Exercícios

::: exercicio 1
Explique, em três linhas, por que a maior parte do trabalho estatístico de um
estudo acontece antes da coleta de dados.

--- gabarito
Porque as decisões que determinam se o estudo poderá responder à pergunta são
todas anteriores: o delineamento, a definição do desfecho, o tamanho da amostra e
o plano de análise. Depois da coleta, nenhuma técnica recupera informação que não
foi coletada, corrige um desfecho mal definido ou compensa uma amostra
insuficiente. A análise executa um plano; ela não o inventa.
:::

::: exercicio 2
Um colega diz: "vou coletar os dados primeiro e depois procuro um estatístico
para ver o que dá para fazer". Responda a ele.

--- gabarito
O estatístico só poderá analisar o que foi coletado, do jeito que foi coletado.
Se o desfecho não tiver definição operacional, se faltarem variáveis
prognósticas, se a amostra for insuficiente para a diferença que interessa ou se
o delineamento não permitir comparação, não haverá conserto. É o exame post
mortem de que falava Fisher: dirá do que o estudo morreu. A consulta útil é no
planejamento, e custa menos.
:::

::: exercicio 3
Dos três riscos apresentados na seção sobre importância, qual você considera o
mais difícil de perceber no próprio trabalho, e por quê?

--- gabarito
O terceiro, o de enganar a si mesmo, porque ele não se manifesta como erro. Cada
decisão isolada parece razoável e defensável: excluir um caso atípico, testar mais
um desfecho, ajustar um corte. O viés nasce do conjunto e da direção em que todas
as decisões pendem, que é a direção do resultado desejado. É por isso que o
antídoto não é atenção redobrada, e sim compromisso registrado antes de ver os
dados.
:::

::: exercicio 4
Estime o custo, em tempo e dinheiro, do estudo do caso condutor: 200 pacientes,
três centros, doze semanas de seguimento. Onde a estatística entra nesse custo?

--- gabarito
Não há resposta única, e o exercício vale pelo raciocínio. O custo dominante é o
seguimento clínico: consultas, curativos, planimetria e o próprio procedimento. A
estatística entra com um custo direto próximo de zero em programa, algumas horas
de consultoria no planejamento e algumas semanas de trabalho do pesquisador. E
entra sobretudo como seguro: ela é a fração mínima do orçamento que decide se o
restante terá servido para alguma coisa.
:::

::: exercicio 5
Escreva a sua pergunta de pesquisa como ela está hoje, sem consultar o Capítulo
2. Guarde para comparar depois.

--- gabarito
Não há gabarito. Ao fim do Capítulo 2, releia o que escreveu e verifique se a
frase original dizia em quem, o que, comparado com o quê, medido como e em quanto
tempo. Na esmagadora maioria dos casos, faltam pelo menos dois desses elementos, e
é exatamente essa falta que o próximo capítulo corrige.
:::

::: agora
1. **Escreva a sua pergunta de pesquisa em uma folha**, do jeito impreciso que ela
   está hoje na sua cabeça, e guarde. Ao fim do Capítulo 2 você vai reescrevê-la,
   e a distância entre as duas versões é o melhor indicador de que o livro está
   funcionando.
2. **Instale o jamovi** a partir de jamovi.org e abra o banco do livro,
   `coorte-condutor.csv`. Não analise nada ainda: olhe as colunas e leia o
   dicionário de variáveis.
3. **Pegue o cronograma do seu projeto** e conte quantas semanas estão reservadas
   para decisões metodológicas **antes** da coleta. Se forem zero, o problema já
   começou, e ainda dá tempo de corrigir.
:::

## Recursos

- [jamovi](https://www.jamovi.org/) — o programa usado no livro.
- [EQUATOR Network](https://www.equator-network.org/) — as recomendações de
  relato, úteis desde o planejamento.
- [Plataforma Brasil](https://plataformabrasil.saude.gov.br/) — submissão de
  projetos ao sistema CEP/CONEP.

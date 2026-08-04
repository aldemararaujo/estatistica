::: caso
O desfecho primário do estudo deu 70,7% contra 53,3%, com diferença de 17,4
pontos percentuais e intervalo de confiança de 3,6 a 31,2. Falta responder à
pergunta que dá nome a este capítulo, e que é a única que muitos pesquisadores
fazem: o acaso é o responsável por esse resultado? O teste qui-quadrado devolve
5,90, com um grau de liberdade, e um valor de p de 0,015.
:::

## O que o valor de p é

O valor de p responde a uma pergunta muito específica, e é indispensável
enunciá-la por inteiro, porque é da abreviação dela que nascem quase todos os
erros.

> Supondo que o tratamento não tenha efeito algum, qual é a probabilidade de
> observar uma diferença tão grande quanto a que eu observei, ou maior?

O p de 0,015 significa: se o aspirado de medula óssea fosse inerte, um resultado
tão distante quanto este apareceria em pouco mais de um a cada setenta estudos
iguais a este. Isso é pouco. Diante de um resultado assim, ou o tratamento tem
algum efeito, ou este estudo foi um dos poucos azarados. A convenção estabelece
que 0,05 é o limite a partir do qual se prefere a primeira explicação.

Note tudo o que está embutido nessa frase. O p supõe que a hipótese nula seja
verdadeira: ele não a testa, ele parte dela. E mede a raridade do resultado sob
essa suposição, nada além disso.

## O que o valor de p não é

Aqui é onde se ganha ou se perde um capítulo inteiro de pesquisa clínica.

**O p não é a probabilidade de a hipótese nula ser verdadeira.** Ele é calculado
*supondo* que ela é verdadeira, e uma probabilidade calculada sob uma suposição
não pode ser a probabilidade daquela suposição. Dizer "há 1,5% de chance de o
tratamento não funcionar" é inverter a condicional, e é o erro mais frequente da
literatura clínica.

**O p não mede o tamanho do efeito.** Um p de 0,015 não quer dizer que o efeito
seja maior que um efeito com p de 0,04. O valor de p depende de três coisas ao
mesmo tempo: do tamanho do efeito, do tamanho da amostra e da variabilidade dos
dados. Um efeito minúsculo em um estudo enorme produz um p minúsculo. Um efeito
grande em um estudo pequeno produz um p grande.

**O p não mede a importância clínica.** Ele não sabe o que é uma úlcera.

**O p acima de 0,05 não prova que não há efeito.** Ausência de evidência não é
evidência de ausência, e essa distinção depende do intervalo de confiança: um
resultado não significativo cujo intervalo vai de 1% a 3% de diferença exclui
efeitos grandes, enquanto outro cujo intervalo vai de 20% negativos a 25%
positivos não exclui nada. Os dois têm p acima de 0,05 e significam coisas
opostas.

::: atencao Os seis princípios da American Statistical Association
Em 2016, diante do uso indiscriminado do valor de p, a American Statistical
Association publicou uma declaração formal, coisa raríssima na história da
entidade. Em resumo: o p pode indicar quão incompatíveis os dados são com um
modelo; não mede a probabilidade da hipótese nem a de os dados terem surgido por
acaso; decisões científicas não devem se basear apenas em ele cruzar um limiar;
a inferência exige transparência total sobre tudo o que foi testado; o p não
mede tamanho de efeito nem importância; e, isoladamente, ele é uma medida pobre
de evidência.

Em 2019, uma edição inteira do *The American Statistician* voltou ao tema com o
título "Movendo-se para um mundo além de p < 0,05". A recomendação central é a
que este livro adota: relate estimativa e intervalo, e trate o p como uma
informação a mais, nunca como o veredito.
:::

## O que acontece por trás do teste

O teste qui-quadrado compara o que se observou com o que se esperaria se não
houvesse associação alguma.

| | Cicatrizou | Não cicatrizou | Total |
|---|---|---|---|
| Aspirado | 65 | 27 | 92 |
| Controle | 49 | 43 | 92 |
| Total | 114 | 70 | 184 |

Se o grupo não tivesse relação com o desfecho, a proporção de cicatrização seria
a mesma nos dois grupos, isto é, 114 dividido por 184, ou 62,0%. Esperar-se-iam
então 57 cicatrizações em cada grupo, e não 65 e 49. A estatística qui-quadrado
soma, para cada uma das quatro casas, o quadrado da diferença entre observado e
esperado, dividido pelo esperado. O resultado é 5,90.

Falta traduzir 5,90 em probabilidade. Sob a hipótese nula, essa estatística segue
uma distribuição conhecida, e a área da cauda além de 5,90 é 0,015. Esse é o
valor de p, e é só isso que ele é: uma área sob uma curva teórica.

| Teste aplicado à mesma tabela | Valor de p |
|---|---|
| Qui-quadrado de Pearson | 0,015 |
| Qui-quadrado com correção de continuidade | 0,023 |
| Teste exato de Fisher | 0,022 |

Três valores diferentes para os mesmos dados, e nenhum deles é errado. Eles
resolvem de maneiras distintas o fato de a distribuição teórica ser contínua e a
contagem de pacientes ser discreta. Quem escolhe qual reportar depois de ver os
três está fazendo o que a literatura chama de *p-hacking*, e é por isso que a
escolha do teste se declara antes, no protocolo, como o Capítulo 11 detalha.

::: jamovi
1. Vá em **Analyses**, **Frequencies**, **Independent Samples**, o teste
   qui-quadrado de duas vias.
2. Ponha `grupo` em **Rows** e `cicatrizacao_12sem` em **Columns**.
3. Em **Statistics**, o χ² já vem marcado. Marque também **χ² continuity
   correction** e **Fisher's exact test** para ver os três valores lado a lado.
4. Em **Cells**, marque **Row** em percentages: é o que produz os 70,7% e 53,3%.

Repare no rodapé da tabela de contingência: o jamovi informa o menor valor
esperado. Quando ele fica abaixo de 5, o qui-quadrado deixa de ser confiável e o
teste exato de Fisher passa a ser a escolha obrigatória. Aqui o menor esperado é
35, e não há problema.
:::

## Significância estatística e relevância clínica

São duas perguntas diferentes, e o quadro abaixo resume o que fazer diante de
cada combinação:

| | Efeito clinicamente relevante | Efeito irrelevante |
|---|---|---|
| **p < 0,05** | Resultado útil: é o caso deste estudo | Estudo grande demais para uma pergunta pequena. Reporte o tamanho do efeito e não comemore |
| **p ≥ 0,05** | O caso mais delicado: pode ser falta de poder. Olhe o intervalo antes de concluir qualquer coisa | Provável ausência de efeito relevante, se o intervalo for estreito |

A linha inferior esquerda é a que mais adoece a literatura. Um estudo pequeno,
com intervalo de confiança larguíssimo, produz p acima de 0,05 e é publicado
com a conclusão de que "não houve diferença entre os grupos". A conclusão
correta seria que o estudo não tinha tamanho para responder.

### Poder, e por que não se calcula poder depois

O estudo foi planejado para ter 80% de poder para detectar uma diferença de 20
pontos percentuais, com 89 participantes por grupo. Observou 17,4 pontos, um
pouco menos do que o planejado.

É tentador recalcular o poder usando a diferença observada. Com 17,4 pontos e 92
participantes por grupo, esse cálculo devolve 68,3%. **Esse número não serve
para nada.** O chamado poder observado, ou poder *post hoc*, é apenas uma
transformação matemática do valor de p: quanto menor o p, maior o poder
calculado, sempre, em qualquer estudo. Ele não traz informação nova e não pode
ser usado para explicar um resultado não significativo. Quem quer saber o que o
estudo conseguiu excluir olha o intervalo de confiança, que é a ferramenta certa
para isso.

Poder se calcula antes, no planejamento, e o Capítulo 6 trata disso.

### Quando se testa muita coisa

O estudo tem um desfecho primário e quatro secundários, além de dois desfechos
de segurança e uma dúzia de variáveis basais. Se cada um for testado a 5%, a
probabilidade de pelo menos um falso positivo entre vinte testes independentes
passa de 60%.

Daí a regra que este livro repete em vários capítulos: **um desfecho primário,
declarado antes de olhar os dados**. Os demais são exploratórios, geram
hipóteses e não sustentam conclusão. Quando é mesmo necessário testar vários
desfechos com igual peso, existem correções, e a de Bonferroni, que divide o
limiar pelo número de testes, é a mais simples e a mais conservadora. Ela não
substitui, porém, a disciplina de decidir antes o que importa.

::: revisor
**"Os autores afirmam que o valor de p indica a probabilidade de a hipótese nula
ser verdadeira."** Reescreva. O p é a probabilidade dos dados sob a hipótese
nula, não o contrário.

**"O estudo conclui ausência de efeito a partir de p = 0,21."** Sem o intervalo
de confiança, essa conclusão não se sustenta. Apresente o intervalo e diga o que
ele exclui.

**"Os autores relatam p = 0,000."** Não existe p igual a zero. Escreva p < 0,001.

**"O valor de p é apresentado sem a estimativa correspondente."** Todo p deve
vir acompanhado do efeito e do intervalo, no mesmo parágrafo ou na mesma linha
da tabela.

**"O poder foi calculado a partir do efeito observado."** Retire. Poder
observado é redundante com o valor de p e não explica resultado nenhum.

**"Foram testados dezoito desfechos e três resultaram significativos, tratados
na discussão como confirmatórios."** Declare qual era o primário e classifique o
resto como exploratório.
:::

::: quiz
? [facil] O desfecho primário deste estudo teve p de 0,015. O que exatamente esse número significa?
+ Se o tratamento fosse inerte, uma diferença tão grande quanto a observada apareceria em cerca de 1,5% dos estudos deste tamanho. | Correto. O valor de p é a probabilidade dos dados, ou de dados mais extremos, calculada **supondo** que a hipótese nula seja verdadeira. É só isso, e é sempre isso.
- Há 1,5% de probabilidade de o tratamento não funcionar. | Esta é a inversão da condicional, o erro mais comum da literatura clínica. O p é calculado supondo a hipótese nula verdadeira, e uma probabilidade calculada sob uma suposição não pode ser a probabilidade daquela suposição.
- Há 98,5% de probabilidade de o tratamento funcionar. | Mesma inversão da alternativa anterior, agora pelo complemento. O p não diz nada sobre a probabilidade de nenhuma hipótese ser verdadeira.
- O tratamento aumenta a cicatrização em 1,5%. | O valor de p não é uma medida de efeito. O efeito deste estudo foi de 17,4 pontos percentuais, e está no intervalo de confiança, não no p.
- O estudo tem 1,5% de chance de estar errado. | O p não mede a probabilidade de o estudo estar errado. Erros de delineamento, de aferição e de seleção não entram nessa conta, e nenhum deles é detectado por um valor de p.
@ cap-10-o-que-o-valor-de-p-e

? [facil] Um estudo comparou dois curativos e concluiu, com p de 0,31, que "não houve diferença entre os grupos". Qual informação é indispensável para julgar essa conclusão?
+ O intervalo de confiança da diferença. | Correto. Um intervalo estreito em torno do nulo permite concluir ausência de efeito relevante; um intervalo largo significa apenas que o estudo não teve tamanho para decidir. Os dois produzem p acima de 0,05 e significam coisas opostas.
- O poder calculado a partir do efeito observado. | O poder observado é uma transformação matemática do próprio valor de p e não acrescenta nenhuma informação. Quanto menor o p, maior o poder calculado, sempre.
- O valor de p com mais casas decimais. | A precisão do p não muda nada. Um p de 0,3142 continua sem dizer se o estudo excluiu efeitos grandes.
- O teste de normalidade dos dados. | Não é disso que depende a conclusão. A questão aqui é a precisão da estimativa, e não a escolha do teste.
- O tamanho da amostra isoladamente. | O tamanho da amostra ajuda, mas o que resume a informação relevante é o intervalo de confiança, que já incorpora tamanho e variabilidade.
@ cap-10-significancia-estatistica-e-relevancia-clinica

? [media] Dois estudos medem a mesma intervenção. O primeiro, com 40 pacientes, encontra 20 pontos percentuais de diferença e p de 0,08. O segundo, com 4.000 pacientes, encontra 2 pontos percentuais e p de 0,001. O que se pode afirmar?
+ O segundo tem mais evidência contra a hipótese nula, e o primeiro estimou um efeito maior, embora com muita imprecisão. | Correto. O valor de p mistura tamanho de efeito, tamanho de amostra e variabilidade. Separar as três coisas exige olhar a estimativa e o intervalo de cada estudo.
- O segundo estudo encontrou um efeito maior, porque tem p menor. | O p menor não significa efeito maior. Aqui, o efeito do segundo estudo é dez vezes menor que o do primeiro, e o p é menor apenas porque a amostra é cem vezes maior.
- O primeiro estudo provou que não há efeito. | Um p de 0,08 com 40 pacientes é o retrato de um estudo sem tamanho para decidir, e não uma prova de ausência de efeito.
- Os dois estudos se contradizem e um deles está errado. | Não há contradição. São estimativas diferentes com precisões diferentes, e a diferença entre elas é compatível com o acaso amostral.
- O segundo estudo é clinicamente mais relevante. | Dois pontos percentuais podem ser clinicamente irrelevantes, por mais impressionante que seja o valor de p. Significância estatística e relevância clínica são perguntas diferentes.
@ cap-10-o-que-o-valor-de-p-nao-e

? [media] No caso condutor, o mesmo desfecho produziu p de 0,015 pelo qui-quadrado de Pearson, 0,023 com correção de continuidade e 0,022 pelo teste exato de Fisher. Qual conduta é correta?
+ Declarar o teste no protocolo, antes de ver os dados, e relatar o que foi declarado. | Correto. Os três valores são legítimos e diferem pelo modo de lidar com a natureza discreta da contagem. Escolher depois de ver os três é o que a literatura chama de *p-hacking*.
- Relatar o menor dos três, que é o mais favorável ao estudo. | É exatamente a prática que o registro prévio do protocolo existe para coibir.
- Relatar os três e deixar o leitor decidir. | Parece transparente e não é: transfere ao leitor uma decisão que era do pesquisador e que deveria ter sido tomada antes da coleta.
- Usar sempre o teste exato de Fisher, que é o mais rigoroso. | O teste exato é obrigatório quando os valores esperados são pequenos, e não é "mais rigoroso" em toda situação. Aqui o menor esperado é 35.
- Refazer a coleta até que os três valores concordem. | Não faz sentido metodológico nem ético, e a discordância entre eles não é um defeito dos dados.
@ cap-10-o-que-acontece-por-tras-do-teste

? [media] O estudo foi planejado com 80% de poder para detectar 20 pontos percentuais, e observou 17,4. Um revisor pede o "poder observado" recalculado com o efeito encontrado. Como responder?
+ Explicar que o poder observado é redundante com o valor de p e não explica resultado nenhum. | Correto. O poder calculado a partir do efeito observado é uma função matemática do próprio p: quanto menor o p, maior o poder, sempre e em qualquer estudo. Quem quer saber o que o estudo excluiu olha o intervalo de confiança.
- Calcular e relatar os 68,3%, atendendo ao pedido. | Atender ao pedido propaga um erro. O número existe, é calculável e não informa nada além do que o p já informou.
- Recalcular o tamanho da amostra necessário e relatá-lo. | Isso responde a outra pergunta, sobre estudos futuros, e não sobre o que este estudo conseguiu mostrar.
- Aumentar a amostra até atingir 80% de poder com o efeito observado. | Continuar coletando até alcançar significância é uma das formas mais eficientes de produzir falso positivo.
- Relatar o poder do desfecho secundário, que foi maior. | Trocar o desfecho para exibir um número melhor é troca de desfecho, e o registro prévio existe para expô-la.
@ cap-10-significancia-estatistica-e-relevancia-clinica

? [dificil] Um projeto declara um desfecho primário e testa, além dele, quatro secundários, dois de segurança e doze variáveis basais, todos a 5%. Supondo independência entre os testes e nenhuma diferença verdadeira, qual a probabilidade aproximada de pelo menos um resultado significativo?
+ Cerca de 60%. | Correto. Com dezenove testes independentes a 5%, a probabilidade de nenhum falso positivo é 0,95 elevado a 19, algo em torno de 0,38. Logo, a de pelo menos um passa de 60%. É a razão de existir desfecho primário único.
- Cerca de 5%, porque cada teste é independente. | Os 5% valem para **cada** teste isoladamente. A pergunta é sobre pelo menos um entre dezenove, e as probabilidades se acumulam.
- Cerca de 19%, somando os riscos. | Somar diretamente superestima em situações grandes e não é o cálculo correto: a conta é feita pelo complemento, com 0,95 elevado ao número de testes.
- Cerca de 95%, porque quase sempre aparece algo. | Exagera. Com dezenove testes a probabilidade fica em torno de 62%, e não perto da certeza.
- Não é possível calcular sem conhecer o tamanho da amostra. | O tamanho da amostra afeta o poder, e não a taxa de erro tipo I, que permanece em 5% por teste independentemente do n.
@ cap-10-significancia-estatistica-e-relevancia-clinica

? [dificil] Qual das afirmações abaixo é compatível com os seis princípios da American Statistical Association sobre o valor de p?
+ O valor de p pode indicar quão incompatíveis os dados são com um modelo estatístico especificado. | Correto. É a formulação do primeiro princípio, e ela é deliberadamente modesta: incompatibilidade com um modelo, e não prova, nem probabilidade de hipótese, nem medida de efeito.
- O valor de p mede a probabilidade de a hipótese estudada ser verdadeira. | A declaração afirma exatamente o contrário, em seu segundo princípio.
- Conclusões científicas devem se basear em o valor de p cruzar ou não um limiar. | O terceiro princípio desaconselha explicitamente decidir por limiar isolado.
- Um valor de p pequeno é, por si só, boa medida da magnitude do efeito. | O quinto princípio nega isso: o p não mede tamanho de efeito nem importância de um resultado.
- Relatar apenas os testes que resultaram significativos é aceitável se o método estiver descrito. | O quarto princípio exige transparência total sobre tudo o que foi testado; relatar seletivamente invalida a interpretação do p.
@ cap-10-o-que-o-valor-de-p-nao-e

? [facil] Ao calcular um valor de p, o que se supõe verdadeiro?
+ Que a hipótese nula é verdadeira, isto é, que o tratamento não tem efeito algum. | Correto. O p parte da hipótese nula, não a testa: ele mede a raridade do resultado observado dentro de um mundo em que o tratamento é inerte.
- Que a hipótese alternativa é verdadeira. | É o oposto. Se o cálculo partisse da existência do efeito, ele não teria como medir a compatibilidade dos dados com a ausência de efeito.
- Que os dois grupos são idênticos em todas as características basais. | O que se supõe é ausência de efeito do tratamento, e não igualdade perfeita dos grupos, que a randomização torna provável mas nunca garante.
- Que a amostra é grande o bastante para o teste. | O tamanho influencia o resultado do cálculo, mas não é a suposição sobre a qual o p se define. Exigências de tamanho aparecem nas condições de validade do teste, não no significado do p.
- Que não houve perdas de seguimento. | As perdas ameaçam a validade e se tratam por análise de sensibilidade. Não são a suposição sobre a qual o p é construído.
@ cap-10-o-que-o-valor-de-p-e

? [facil] Um manuscrito relata, na tabela de resultados, "p = 0,000". O que está errado?
+ Não existe valor de p igual a zero, e a notação correta é p < 0,001. | Correto. O p é uma área sob uma curva, e essa área pode ser pequeníssima, jamais nula: sempre resta alguma probabilidade de observar um resultado extremo sob a hipótese nula. O que apareceu na tela foi um arredondamento na terceira casa.
- Nada está errado: o programa calculou e o autor transcreveu. | O programa arredondou para três casas. Transcrever o arredondamento como valor exato transforma uma limitação de exibição em afirmação matemática falsa.
- Falta apenas acrescentar ao lado qual teste foi utilizado. | O teste de fato deve constar, e isso não conserta o "0,000", que continua sendo um valor impossível.
- O erro é usar três casas decimais em vez de duas. | O número de casas é convenção editorial. O problema não é a precisão, é afirmar uma probabilidade nula.
- O valor deveria estar em porcentagem, como 0,0%. | Trocar a escala não resolve nada: 0,0% seria igualmente impossível.
@ cap-10-o-que-o-valor-de-p-e

? [facil] O teste qui-quadrado aplicado ao desfecho primário deste estudo compara o quê, exatamente?
+ As cicatrizações observadas em cada grupo, 65 e 49, com as 57 que se esperariam em cada um se o grupo não tivesse relação com o desfecho. | Correto. A estatística soma, nas quatro casas da tabela, o quadrado da diferença entre observado e esperado, dividido pelo esperado. O esperado sai da proporção global de 62,0%, isto é, 114 em 184.
- As proporções de 70,7% e 53,3% diretamente uma com a outra. | É o que a leitura clínica faz, e não é o que o teste faz. O qui-quadrado trabalha com contagens e com o que se esperaria sob independência, não com a subtração das duas proporções.
- A média de cicatrização de um grupo com a do outro. | Cicatrização aqui é variável nominal, e não há média a calcular. Médias entram nos testes do Capítulo 11, para variáveis numéricas.
- O intervalo de confiança de cada grupo, verificando se eles se sobrepõem. | Comparar sobreposição dos intervalos de cada grupo é atalho impreciso, e não é o que o teste faz. O intervalo que interessa é o da diferença, e está no Capítulo 9.
- Os 92 participantes de um grupo com os 92 do outro, um a um. | Não há pareamento neste estudo: os grupos são independentes, formados por sorteio, e nenhum participante tem correspondente no outro grupo.
@ cap-10-o-que-acontece-por-tras-do-teste

? [facil] Um artigo apresenta, na tabela principal, apenas os valores de p de cada comparação. O que falta?
+ A estimativa do efeito e o intervalo de confiança, ao lado de cada p. | Correto. O p diz quão raro seria o resultado sob a hipótese nula, e não diz o tamanho do efeito nem a precisão da estimativa. Sem as duas, o leitor não julga nem magnitude nem incerteza.
- O valor da estatística do teste, como o qui-quadrado de 5,90. | É informação secundária e legítima. O leitor precisa antes do efeito e do intervalo, que são o que sustenta uma decisão clínica.
- O poder do estudo para cada comparação. | Poder é assunto de planejamento, e calculado depois não informa nada. O que falta na tabela é a estimativa com seu intervalo.
- O teste de normalidade aplicado a cada variável. | Não é isso que falta, e nem sempre é necessário. A ausência crítica é a da estimativa e da precisão.
- Nada falta: o valor de p resume a comparação. | É exatamente a crença que a declaração da American Statistical Association combate. Isoladamente, o p é uma medida pobre de evidência.
@ cap-10-o-que-o-valor-de-p-nao-e

? [media] O rodapé da tabela de contingência do jamovi informa o menor valor esperado. Para que serve essa informação?
+ Para decidir se o qui-quadrado é confiável: abaixo de 5, o teste exato de Fisher passa a ser obrigatório. | Correto. Neste estudo o menor esperado é 35, bem acima do limite, e por isso o qui-quadrado se sustenta. Em tabelas com casas pouco povoadas, a aproximação pela distribuição teórica falha.
- Para verificar se a randomização equilibrou os grupos. | O equilíbrio basal se lê na Tabela 1. O menor esperado é uma quantidade calculada a partir das margens da tabela de contingência, e nada diz sobre randomização.
- Para calcular o poder do estudo. | Poder se calcula no planejamento, com o efeito que se pretende detectar. O menor esperado não entra nessa conta.
- Para escolher entre o qui-quadrado de Pearson e o com correção de continuidade. | A correção de continuidade responde a outro problema, o da natureza discreta da contagem. O limite de 5 decide entre a aproximação e o teste exato.
- Para saber quantos participantes se perderam no seguimento. | As perdas se leem no total da tabela e no diagrama de fluxo. O valor esperado é um número teórico, e não uma contagem de gente.
@ cap-10-o-que-acontece-por-tras-do-teste

? [media] A estatística qui-quadrado deste estudo vale 5,90, com um grau de liberdade, e o p correspondente é 0,015. Como se passa de um número ao outro?
+ Sob a hipótese nula, a estatística segue uma distribuição teórica conhecida, e 0,015 é a área da cauda além de 5,90. | Correto. O valor de p é isso, e apenas isso: uma área sob uma curva teórica. Nada nesse cálculo consulta a clínica, o custo do tratamento ou a plausibilidade biológica.
- Divide-se 5,90 pelo número de participantes e ajusta-se pelo grau de liberdade. | Não existe tal conta. A conversão é feita pela distribuição de referência, e não por aritmética sobre a estatística.
- Compara-se 5,90 com o valor crítico de 3,84 e converte-se a diferença em probabilidade. | O valor crítico de 3,84 serve para decidir por limiar a 5%, e não para obter o p. A área da cauda é informação mais fina que a simples comparação com o crítico.
- Aplica-se a correção de continuidade, que transforma a estatística em probabilidade. | A correção altera a própria estatística antes da conversão, e foi ela que produziu o p alternativo de 0,023 na tabela deste capítulo.
- O 0,015 é obtido por simulação, reamostrando os dados milhares de vezes. | Reamostragem é caminho legítimo em outros contextos, e não é o que o qui-quadrado de Pearson faz: ele usa uma distribuição teórica fechada.
@ cap-10-o-que-acontece-por-tras-do-teste

? [media] Um ensaio com 12.000 participantes encontra diferença de 0,4 ponto percentual na cicatrização, com p de 0,003. Como se relata isso?
+ Como resultado estatisticamente significativo cujo efeito é clinicamente irrelevante, apresentando estimativa e intervalo sem comemorar. | Correto. É a casa superior direita do quadro deste capítulo: estudo grande demais para uma pergunta pequena. O p minúsculo veio do tamanho da amostra, e não da magnitude do benefício.
- Como resultado positivo, já que o p ficou abaixo de 0,05. | Significância estatística e relevância clínica são perguntas diferentes. Quatro décimos de ponto percentual não mudam conduta, por menor que seja o p.
- Como resultado negativo, já que o efeito é pequeno. | Também não. O efeito existe e foi estimado com muita precisão; o que não se sustenta é a conclusão de importância clínica.
- Como inconclusivo, pedindo um estudo maior. | Um estudo maior estimaria o mesmo efeito com precisão ainda maior. O problema não é falta de tamanho, é a irrelevância da magnitude encontrada.
- Como evidência de que o tratamento funciona em algum subgrupo. | Concluir sobre subgrupo exige análise declarada antes da coleta, e nada no enunciado autoriza essa migração.
@ cap-10-significancia-estatistica-e-relevancia-clinica

? [media] Dois ensaios terminam com p acima de 0,05. No primeiro, a diferença estimada é de 1 ponto percentual, com intervalo de menos 1 a mais 3. No segundo, é de 2 pontos, com intervalo de menos 20 a mais 25. O que se conclui?
+ O primeiro exclui efeitos clinicamente relevantes; o segundo não exclui nada e é apenas inconclusivo. | Correto. Os dois têm o mesmo veredito de significância e significados opostos. É por isso que "não houve diferença entre os grupos" só se sustenta acompanhada do intervalo.
- Nos dois casos se conclui que o tratamento não funciona. | Só o primeiro autoriza afirmar ausência de efeito relevante. No segundo, o intervalo admite desde prejuízo grande até benefício grande.
- O segundo é mais informativo, porque estimou efeito maior. | Estimar efeito maior com imprecisão enorme não é ser mais informativo. A largura do intervalo é a medida exata do que o estudo não conseguiu decidir.
- Nenhum dos dois permite conclusão, porque ambos falharam no teste. | O primeiro permite uma conclusão útil, ainda que negativa: os dados são incompatíveis com efeitos grandes. Ficar acima do limiar não é o mesmo que nada saber.
- Ambos precisam do poder observado calculado para serem interpretados. | O poder observado é redundante com o p. O que separa os dois casos é o intervalo, que já está no enunciado.
@ cap-10-o-que-o-valor-de-p-nao-e

? [media] Dois desfechos do mesmo estudo produzem p de 0,049 e p de 0,051. O que de fato distingue os dois resultados?
+ Praticamente nada, e tratá-los como opostos é o que a American Statistical Association desaconselha. | Correto. O limiar de 0,05 é convenção, e não fronteira da natureza. Dois resultados quase idênticos viram "positivo" e "negativo" apenas porque alguém escolheu um número redondo.
- O primeiro comprova o efeito e o segundo o refuta. | É a leitura dicotômica que o terceiro princípio da declaração combate expressamente. Nenhum dos dois comprova nem refuta coisa alguma sozinho.
- O primeiro corresponde a um efeito maior que o segundo. | O p não mede tamanho de efeito. Os dois efeitos podem ter qualquer magnitude, e é a estimativa que diz qual é maior.
- O segundo exige correção para múltiplos testes e o primeiro não. | A correção, quando cabe, aplica-se ao conjunto dos testes, e não seletivamente ao que caiu do lado indesejado do limiar.
- O primeiro é confiável e o segundo pede repetição do estudo. | A confiabilidade de cada um depende do delineamento, da precisão e do intervalo, e não de dois milésimos no valor de p.
@ cap-10-o-que-o-valor-de-p-nao-e

? [media] Suponha que o desfecho primário deste estudo tivesse dado p de 0,08 e que um dos quatro secundários tivesse dado 0,01, e que o artigo fosse escrito em torno do secundário. Como se chama isso?
+ Troca de desfecho, prática que o CONSORT nomeia e que o registro prévio do protocolo existe para expor. | Correto. O primário não significativo precisa ser relatado com estimativa e intervalo, e o secundário entra como achado exploratório, gerador de hipótese, jamais como conclusão do estudo.
- Análise de sensibilidade, legítima quando o primário é inconclusivo. | Análise de sensibilidade é refazer a mesma pergunta sob outra suposição sobre os dados. Trocar a pergunta por outra que deu certo é coisa inteiramente diferente.
- Correção para múltiplos testes, feita na direção correta. | Não há correção alguma aqui. Ao contrário: o problema é ignorar que cinco desfechos foram testados.
- Achado secundário confirmatório, aceitável por ter p menor que o do primário. | Nenhum desfecho secundário é confirmatório, por menor que seja seu p. A hierarquia se declara antes da coleta, e não depois do resultado.
- Análise interina, que autoriza concluir pelo desfecho que alcançou significância. | Análise interina é uma parada planejada durante a coleta, com regras escritas no protocolo, e nada tem a ver com escolher desfecho depois de ver os dados.
@ cap-10-quando-se-testa-muita-coisa

? [dificil] Para responder "qual a probabilidade de a hipótese nula ser verdadeira, dados estes resultados?", o valor de p não basta. O que mais seria necessário?
+ A probabilidade que se atribuía à hipótese antes de ver os dados. | Correto. Passar de "probabilidade dos dados supondo a hipótese" para "probabilidade da hipótese dados os dados" exige inverter uma condicional, e a inversão só se faz com a probabilidade prévia. É o mesmo raciocínio que o Capítulo 13 aplica à probabilidade pré-teste de um exame.
- Um valor de p calculado com mais precisão. | Nenhuma precisão adicional converte uma condicional na outra. O problema é da estrutura do raciocínio, e não do número de casas decimais.
- O tamanho da amostra e o poder do estudo. | Ambos influenciam o valor de p, e nenhum dos dois fornece a informação que falta, que é externa aos dados deste estudo.
- O intervalo de confiança da diferença. | O intervalo informa precisão e magnitude, o que é muito, e ainda assim continua sendo afirmação sobre os dados, e não sobre a probabilidade da hipótese.
- A correção de Bonferroni aplicada ao número de desfechos. | A correção ajusta a taxa de erro em múltiplos testes. Ela não altera a natureza do que o valor de p mede.
@ cap-10-o-que-o-valor-de-p-nao-e

? [dificil] Dois estudos, um com 30 e outro com 3.000 participantes, terminam com exatamente o mesmo valor de p, no mesmo tipo de teste. O que se pode dizer do poder observado de cada um?
+ Será o mesmo nos dois, porque o poder observado é uma transformação do próprio valor de p. | Correto. É essa dependência que o torna inútil: ele não acrescenta informação, apenas reexpressa o p em outra escala. Dois estudos com efeitos e tamanhos opostos, mas com o mesmo p, recebem o mesmo poder observado.
- Será maior no estudo com 3.000 participantes, que tem mais poder. | O poder planejado seria maior, mas poder observado não é poder planejado: ele se calcula com o efeito encontrado, e por isso acompanha o p, e não o tamanho da amostra.
- Será maior no estudo com 30, porque ali o efeito encontrado teve de ser maior. | O efeito de fato precisou ser bem maior para produzir aquele p com amostra pequena, e ainda assim o poder observado sai igual. É justamente o que revela o quanto ele é vazio.
- Não é possível dizer sem conhecer a variabilidade dos dados. | A variabilidade já está incorporada ao valor de p. Fixado o p, o poder observado fica determinado.
- Será igual apenas se os dois tiverem o mesmo tamanho de efeito. | Se tivessem o mesmo efeito e tamanhos tão diferentes, os valores de p não seriam iguais. O enunciado fixa o p justamente para expor a relação.
@ cap-10-poder-e-por-que-nao-se-calcula-poder-depois

? [dificil] Aplicada aos dezenove testes deste projeto, a correção de Bonferroni levaria o limiar de 5% para cerca de 0,0026, e o p de 0,015 do desfecho primário deixaria de ser significativo. O que isso significa?
+ Nada muda para o primário: ele é único, foi declarado antes da coleta e por isso não entra na correção. | Correto. A correção existe para conjuntos de testes tratados com igual peso. Declarar um desfecho primário é a alternativa disciplinar à correção, e é por isso que o livro insiste nisso desde o Capítulo 4.
- O estudo perdeu seu resultado principal e a conclusão precisa ser revista. | Só se o protocolo tivesse tratado os dezenove desfechos como igualmente confirmatórios, o que não é o caso. Aplicar Bonferroni onde há hierarquia declarada penaliza justamente quem fez a coisa certa.
- Bonferroni deve ser aplicada sempre que houver mais de um teste no artigo. | Se assim fosse, todo artigo com uma Tabela 1 e uma dúzia de variáveis basais precisaria corrigir seu desfecho primário, o que não tem sentido metodológico.
- O correto seria aplicar a correção apenas aos quatro desfechos secundários. | Os secundários são exploratórios e não sustentam conclusão, com ou sem correção. Corrigi-los lhes daria aparência confirmatória que eles não têm.
- A correção mostra que o estudo precisaria de amostra maior. | Bonferroni redistribui a taxa de erro tipo I entre testes. Não é cálculo de tamanho de amostra e nada diz sobre ele.
@ cap-10-quando-se-testa-muita-coisa

? [dificil] Terminada a análise principal, um coautor sugere verificar se o efeito é maior entre diabéticos, entre fumantes e entre os de úlcera maior. No subgrupo dos diabéticos aparece p de 0,04. Qual a leitura correta?
+ É achado exploratório: três comparações não declaradas foram feitas depois de ver os dados, e a taxa de falso positivo já não é a nominal. | Correto. O problema não está em olhar subgrupos, e sim em olhar depois e relatar só o que apareceu. O achado gera hipótese para outro estudo, e nada além disso.
- É resultado válido, porque o p ficou abaixo de 0,05. | O limiar de 5% pressupõe uma comparação declarada antes. Depois de três buscas não planejadas, o 0,04 não tem o significado que aparenta.
- É resultado válido desde que a interação entre grupo e diabetes também seja testada. | Testar a interação é a análise tecnicamente correta para subgrupos, e é mais exigente que comparar dentro de cada estrato. Feita depois e não declarada, ainda assim permanece exploratória.
- Deve ser descartado e não mencionado no artigo. | Descartar em silêncio é o outro extremo, e alimenta o viés de publicação. O quarto princípio da American Statistical Association pede transparência sobre tudo o que foi testado.
- Confirma o efeito principal e reforça a conclusão do estudo. | Um subgrupo não confirma o todo. Se o efeito principal já é significativo, o subgrupo apenas descreve onde ele pareceu maior nesta amostra, e isso oscila muito com o acaso.
@ cap-10-quando-se-testa-muita-coisa
:::

## Exercícios

::: exercicio 1
Traduza o p de 0,015 deste estudo em uma frase completa, sem usar as palavras
"significativo" ou "chance de o tratamento funcionar".

--- gabarito
Se o aspirado de medula óssea não tivesse efeito algum sobre a cicatrização, uma
diferença de 17,4 pontos percentuais ou maior entre os grupos apareceria em
cerca de 1,5% dos estudos com este mesmo tamanho. Como isso é pouco, os dados
são pouco compatíveis com a hipótese de que o tratamento é inerte.
:::

::: exercicio 2
O mesmo estudo, com a mesma diferença de 17,4 pontos percentuais, teria sido
conduzido com 30 participantes por grupo. O valor de p seria maior ou menor? E o
intervalo de confiança?

--- gabarito
O p seria maior, provavelmente acima de 0,05, e o intervalo de confiança seria
muito mais largo, cruzando o zero. A estimativa do efeito, no entanto,
continuaria 17,4 pontos percentuais. É a demonstração de que o valor de p mistura
tamanho de efeito com tamanho de amostra, e de que só o intervalo separa as duas
coisas.
:::

::: exercicio 3
Um artigo relata: "não houve diferença entre os grupos (p = 0,31)". Quais duas
informações você exigiria antes de aceitar essa conclusão?

--- gabarito
A estimativa do efeito e seu intervalo de confiança. Se o intervalo for estreito
e próximo do nulo, a conclusão de ausência de efeito relevante se sustenta. Se
for largo, o estudo apenas não teve tamanho para decidir, e a frase correta seria
que o estudo foi inconclusivo, não que não há diferença.
:::

::: exercicio 4
No jamovi, refaça o teste do desfecho primário e compare os três valores de p da
tabela deste capítulo. Em seguida, refaça o teste incluindo os dezesseis
participantes perdidos como se não tivessem cicatrizado. O p muda? A conclusão
muda?

--- gabarito
Incluir as perdas como não cicatrizadas é uma das análises de sensibilidade
clássicas, e no caso deste estudo, como as perdas foram equilibradas, oito em
cada grupo, o p se altera pouco e a conclusão permanece. O exercício ensina que a
robustez de um resultado se demonstra mostrando que ele sobrevive a suposições
diferentes sobre os dados faltantes, assunto retomado nos Capítulos 12 e 15.
:::

::: exercicio 5
Explique por que a frase "o resultado foi altamente significativo (p < 0,001)"
não autoriza dizer que o efeito é grande.

--- gabarito
Porque o valor de p diminui tanto pelo aumento do efeito quanto pelo aumento da
amostra. Um estudo com dez mil pacientes detecta com p < 0,001 uma diferença de
um ponto percentual, clinicamente desprezível. O adjetivo "altamente" descreve a
raridade do resultado sob a hipótese nula, não a magnitude do benefício, que se
lê na estimativa e no intervalo.
:::

::: exercicio 6
O estudo tem um desfecho primário e quatro secundários. Suponha que o primário
tivesse dado p = 0,08 e que um dos secundários tivesse dado p = 0,01. Como o
artigo deve ser escrito?

--- gabarito
O artigo deve dizer que o desfecho primário não alcançou significância, com sua
estimativa e intervalo, e que um desfecho secundário mostrou diferença, tratada
como achado exploratório e gerador de hipótese. Escrever a conclusão em torno do
secundário, com o primário escondido na discussão, é a prática que o CONSORT
chama de troca de desfecho, e é a razão de o registro prévio do protocolo
existir.
:::

::: agora
1. Procure no seu texto toda frase do tipo "não houve diferença" e acrescente o
   intervalo de confiança ao lado. Depois releia: em boa parte dos casos a frase
   terá de virar "o estudo não teve tamanho para decidir".
2. Se houver cálculo de poder feito depois da coleta, com o efeito observado,
   apague. Ele não informa nada além do que o valor de p já informou.
3. Conte quantos desfechos você pretende testar e circule **um**. Esse é o
   primário. Os demais entram no texto como exploratórios, e a conclusão não se
   apoia neles.
:::

## Recursos

- [ASA Statement on p-Values and Statistical Significance](https://doi.org/10.1080/00031305.2016.1154108)
  — os seis princípios, em quatro páginas.
- [Moving to a World Beyond "p < 0.05"](https://doi.org/10.1080/00031305.2019.1583913)
  — a editorial de 2019 que abre a edição especial do *The American Statistician*.
- [Scientists rise up against statistical significance](https://www.nature.com/articles/d41586-019-00857-9)
  — o manifesto na *Nature*, assinado por mais de oitocentos pesquisadores.

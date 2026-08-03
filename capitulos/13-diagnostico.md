::: caso
Uma úlcera venosa que não cicatriza em doze semanas custa curativos, consultas e
sofrimento. Se fosse possível, na quarta semana, saber quem não vai cicatrizar,
esses pacientes poderiam ser encaminhados mais cedo para outra conduta. O estudo
mediu duas coisas que poderiam servir a isso: a pressão transcutânea de oxigênio
na inclusão e a redução da área da úlcera em quatro semanas. Qual delas serve?
:::

## O que se pergunta a um teste

Um teste diagnóstico ou prognóstico não acerta ou erra: ele acerta e erra em
proporções que precisam ser medidas, e a medida depende de comparar o teste com
um padrão de referência.

Aqui o padrão de referência é o desfecho observado: a úlcera cicatrizou ou não
cicatrizou em doze semanas. O teste índice é a redução de área em quatro semanas,
com o ponto de corte clássico de 40%. A tabela de quatro casas fica assim:

| | Cicatrizou | Não cicatrizou | Total |
|---|---|---|---|
| **Redução ≥ 40%** | 81 (verdadeiro positivo) | 14 (falso positivo) | 95 |
| **Redução < 40%** | 33 (falso negativo) | 56 (verdadeiro negativo) | 89 |
| Total | 114 | 70 | 184 |

Dela saem todas as medidas do capítulo.

## As medidas, e a pergunta que cada uma responde

**Sensibilidade: 71,1%.** Dos que cicatrizaram, quantos o teste havia apontado?
81 de 114. Responde à pergunta do pesquisador que já sabe o desfecho, e mede a
capacidade do teste de não deixar escapar quem tem a condição.

**Especificidade: 80,0%.** Dos que não cicatrizaram, quantos o teste havia
descartado? 56 de 70.

Sensibilidade e especificidade são propriedades do teste e, dentro de certos
limites, não mudam com a população. Mas nenhuma das duas responde à pergunta que
o clínico realmente faz, que é o contrário: **este paciente aqui, cujo resultado
eu acabei de ver, vai cicatrizar?**

**Valor preditivo positivo: 85,3%.** Dos que o teste apontou, quantos de fato
cicatrizaram? 81 de 95.

**Valor preditivo negativo: 62,9%.** Dos que o teste descartou, quantos de fato
não cicatrizaram? 56 de 89.

Esses dois respondem à pergunta do clínico, e têm um defeito grave: **dependem da
prevalência**. Nesta amostra, 62,0% cicatrizaram. Em um serviço terciário, que
recebe as úlceras refratárias, a proporção seria bem menor, e o mesmo teste, com
a mesma sensibilidade e a mesma especificidade, teria valor preditivo positivo
muito pior.

::: atencao O erro que mata a interpretação de exames
Valores preditivos publicados em um artigo não se transportam para outro
serviço. Sensibilidade e especificidade viajam; valores preditivos, não. Ao ler
um estudo de acurácia diagnóstica, a primeira coisa a verificar é a prevalência
da condição na amostra estudada, e a segunda é se ela se parece com a do seu
consultório.
:::

## As razões de verossimilhança, que resolvem o problema

A razão de verossimilhança combina as duas propriedades do teste e permite levar
o resultado para qualquer população.

**Razão de verossimilhança positiva: 3,55.** É a sensibilidade dividida por um
menos a especificidade. Significa que um resultado positivo é 3,55 vezes mais
provável em quem vai cicatrizar do que em quem não vai.

**Razão de verossimilhança negativa: 0,36.**

O uso prático é este: parta da probabilidade que você atribuía ao paciente antes
do teste, converta em chance, multiplique pela razão de verossimilhança e
converta de volta.

| Paciente | Probabilidade pré-teste | Após redução ≥ 40% | Após redução < 40% |
|---|---|---|---|
| Deste estudo | 62% | 85% | 37% |
| De um serviço terciário | 30% | 60% | 13% |

A mesma informação do teste leva a conclusões diferentes conforme o paciente, e é
assim que deve ser. Uma regra grosseira ajuda a julgar utilidade: razões
positivas acima de 10 e negativas abaixo de 0,1 mudam conduta com frequência;
entre 5 e 10, ou entre 0,1 e 0,2, ajudam; e valores próximos de 1 não informam
quase nada.

::: calculadora fagan
:::

A calculadora abre com os valores deste estudo: prevalência de 62%,
sensibilidade de 71,1% e especificidade de 80,0%. Baixe a probabilidade
pré-teste para 30%, que é a de um serviço terciário, e observe o valor preditivo
positivo desabar sem que o teste tenha mudado.

Ela pode divergir do texto na última casa decimal, e a razão é instrutiva: o
livro calcula a partir dos 184 participantes, enquanto a calculadora parte da
sensibilidade e da especificidade já arredondadas que você digitou. É o mesmo
motivo pelo qual dois artigos podem publicar 3,55 e 3,56 para a mesma razão de
verossimilhança, e é uma boa razão para não relatar mais casas do que os dados
sustentam.

## Escolher o corte é escolher o erro que se prefere cometer

Nenhum ponto de corte é o certo. Cada um troca sensibilidade por especificidade:

| Redução de área em 4 semanas | Sensibilidade | Especificidade | VPP | RV+ |
|---|---|---|---|---|
| ≥ 30% | 76,3% | 65,7% | 78,4% | 2,23 |
| ≥ 40% | 71,1% | 80,0% | 85,3% | 3,55 |
| ≥ 50% | 63,2% | 92,9% | 93,5% | 8,84 |

A escolha é clínica, não estatística. Se o objetivo é não deixar escapar ninguém
que vá cicatrizar sozinho, evitando indicar cirurgia desnecessária, prefere-se
sensibilidade alta. Se o objetivo é selecionar, para um tratamento caro e
arriscado, apenas quem realmente não vai cicatrizar, prefere-se especificidade
alta. O corte de 50% tem razão de verossimilhança positiva de 8,84, quase no
patamar em que um teste muda conduta.

## A curva ROC e a comparação entre dois testes

A curva ROC percorre todos os cortes possíveis e desenha sensibilidade contra um
menos especificidade. A área sob ela resume a capacidade de discriminação em um
número: 0,5 é o acaso, e 1,0 é a separação perfeita.

| Teste | Área sob a curva | IC 95% |
|---|---|---|
| TcPO₂ na inclusão | 0,656 | 0,574 a 0,737 |
| Redução de área em 4 semanas | 0,824 | 0,766 a 0,883 |

Os intervalos mal se tocam, e a conclusão é clara: a redução de área em quatro
semanas discrimina bem, e a pressão transcutânea de oxigênio medida na inclusão
discrimina pouco. Repare no que isso significa na prática: o exame mais
sofisticado e mais caro perdeu para a medida da própria ferida com uma régua,
feita quatro semanas depois. O melhor preditor da evolução de uma úlcera é a
evolução da úlcera.

Vale olhar o TcPO₂ com atenção, porque a tabela dele explica o que uma área de
0,656 quer dizer na clínica:

| TcPO₂ | Sensibilidade | Especificidade | RV+ |
|---|---|---|---|
| ≥ 30 mmHg | 85,3% | 26,2% | 1,16 |
| ≥ 35 mmHg | 63,3% | 60,0% | 1,58 |
| ≥ 40 mmHg | 38,5% | 84,6% | 2,50 |

Não há corte bom. Em 30 mmHg, o teste quase não descarta ninguém; em 40, deixa
escapar dois terços dos que cicatrizariam. É o retrato de um teste que não
resolve, e publicá-lo escolhendo o corte de melhor aparência seria desonesto.

::: jamovi
1. Para a tabela de quatro casas, use **Frequencies**, **Independent Samples**,
   com a variável dicotomizada nas linhas e o desfecho nas colunas. Antes disso,
   crie a variável do corte em **Data**, **Compute**, com a fórmula
   `IF(reducao_area_4sem_pct >= 40, "Positivo", "Negativo")`.
2. Sensibilidade, especificidade e valores preditivos saem por divisão direta das
   quatro casas, como neste capítulo. Faça a conta uma vez à mão: entender de
   onde vem cada número vale mais do que qualquer botão.
3. A **curva ROC** não vem no jamovi básico. Ela está em um módulo adicional:
   clique no ícone de mais, em Modules, abra a **jamovi library** e procure por
   ROC. Instalado o módulo, o procedimento pede a variável contínua e a variável
   de desfecho, e devolve a curva, a área e o corte ótimo por Youden.
4. Desconfie do corte ótimo automático. O índice de Youden trata um falso
   positivo e um falso negativo como igualmente ruins, e na clínica eles quase
   nunca são.
:::

::: revisor
**"O padrão de referência não está descrito."** Sem ele, nenhuma medida de
acurácia significa coisa alguma. Descreva quem aplicou, quando e com que
critério.

**"O avaliador do teste índice conhecia o desfecho."** É viés de revisão, e
infla a acurácia. Neste estudo, quem media a área desconhecia a alocação, e isso
precisa estar escrito.

**"O ponto de corte foi escolhido a partir dos próprios dados e apresentado sem
validação."** O corte que maximiza a acurácia na amostra em que foi encontrado
sempre parece melhor do que é. Ou se usa um corte previamente publicado, como o
de 40% em quatro semanas, ou se valida em outra amostra.

**"Os autores relatam apenas a área sob a curva."** A área é um resumo, e resume
demais: dois testes com a mesma área podem se comportar de maneiras opostas na
faixa de decisão que interessa. Apresente sensibilidade, especificidade e razões
de verossimilhança nos cortes clinicamente relevantes.

**"Os valores preditivos foram transportados para uma população com prevalência
diferente."** Recalcule com as razões de verossimilhança.

**"Os intervalos de confiança das medidas de acurácia não foram apresentados."**
Sensibilidade de 71,1% baseada em 114 pacientes tem incerteza considerável.
:::

## Exercícios

::: exercicio 1
Com o corte de 40%, o valor preditivo positivo foi 85,3%. Calcule qual seria esse
valor em um serviço onde apenas 30% das úlceras cicatrizam em doze semanas,
usando a mesma sensibilidade e especificidade.

--- gabarito
Em mil pacientes com prevalência de 30%, haveria 300 que cicatrizam e 700 que
não. Com sensibilidade de 71,1%, o teste apontaria 213 dos 300. Com
especificidade de 80,0%, apontaria erradamente 140 dos 700. O valor preditivo
positivo seria 213 dividido por 353, ou cerca de 60%, bem abaixo dos 85,3% do
estudo. O teste não piorou: a população mudou.

A calculadora deste capítulo devolve 60,4%, e a conta à mão acima devolve 60,3%,
porque ela arredondou os 213,3 verdadeiros positivos para 213. A diferença não
tem importância clínica alguma, e serve de lembrete sobre quantas casas decimais
um resultado desses comporta.
:::

::: exercicio 2
Por que a sensibilidade cai quando se aumenta o ponto de corte de 30% para 50%?

--- gabarito
Porque um corte mais exigente classifica menos pacientes como positivos. Alguns
dos que perdem o rótulo de positivo eram verdadeiros positivos, que passam a ser
falsos negativos, e a sensibilidade cai. Em compensação, também saem de positivo
alguns falsos positivos, e a especificidade sobe. É uma troca inevitável, e é
exatamente ela que a curva ROC desenha.
:::

::: exercicio 3
A área sob a curva do TcPO₂ foi 0,656, com intervalo de 0,574 a 0,737. Esse teste
é melhor que o acaso? Ele serve para uso clínico?

--- gabarito
É melhor que o acaso, porque o intervalo de confiança não inclui 0,5. Mas as duas
perguntas são diferentes, e a resposta à segunda é não: nenhum ponto de corte
oferece uma combinação útil de sensibilidade e especificidade, e a razão de
verossimilhança positiva não passa de 2,50 nem a negativa desce abaixo de 0,56.
Um teste pode ser estatisticamente melhor que o acaso e clinicamente inútil, e
essa distinção é o motivo de este capítulo insistir em razões de verossimilhança
e não em área sob a curva.
:::

::: exercicio 4
Um artigo relata que "a acurácia global do teste foi de 74,5%". Por que essa
medida isolada é insuficiente?

--- gabarito
A acurácia global é a proporção de acertos, e mistura em um único número os dois
tipos de erro, que têm consequências clínicas diferentes. Além disso, ela depende
da prevalência: em uma condição rara, um teste que diga sempre "negativo" tem
acurácia altíssima e utilidade nenhuma. Relate sensibilidade e especificidade
separadamente.
:::

::: exercicio 5
No jamovi, construa a tabela de quatro casas para o corte de 50% e calcule as
seis medidas do capítulo. Confira com a tabela de cortes apresentada aqui.

--- gabarito
Com o corte de 50%, os números são 72 verdadeiros positivos, 5 falsos positivos,
42 falsos negativos e 65 verdadeiros negativos. Daí saem sensibilidade de 63,2%,
especificidade de 92,9%, valor preditivo positivo de 93,5%, valor preditivo
negativo de 60,7%, razão de verossimilhança positiva de 8,84 e negativa de 0,40.
Repare que a razão positiva quase triplicou em relação ao corte de 40%, ao custo
de oito pontos de sensibilidade: é o tipo de troca que se decide na clínica.
:::

::: exercicio 6
Um paciente seu tem, na sua avaliação, 40% de probabilidade de cicatrizar sem
intervenção adicional. Ele volta na quarta semana com redução de área de 55%.
Qual a sua estimativa agora?

--- gabarito
A chance pré-teste é 40 para 60, ou 0,67. Com o corte de 50%, a razão de
verossimilhança positiva é 8,84, e a chance pós-teste é 0,67 vezes 8,84, ou 5,9.
Convertida de volta, a probabilidade é 5,9 dividido por 6,9, ou cerca de 86%.
O paciente saiu de uma dúvida genuína para uma expectativa francamente favorável,
e é isso que se espera de um teste útil.
:::

::: agora
1. Verifique de onde veio o seu ponto de corte. Se ele foi escolhido nos seus
   próprios dados, diga isso no texto e trate o resultado como exploratório.
2. Calcule as razões de verossimilhança do seu teste e leve-as para a
   prevalência do **seu** serviço, usando a calculadora deste capítulo. Os
   valores preditivos do artigo que você leu não valem no seu ambulatório.
3. Confirme que quem interpretou o teste índice desconhecia o padrão de
   referência. Se não desconhecia, a acurácia que você mediu está inflada e isso
   precisa constar das limitações.
:::

## Recursos

- [STARD 2015](https://www.equator-network.org/reporting-guidelines/stard/) — a
  recomendação para relato de estudos de acurácia diagnóstica.
- [jamovi library](https://library.jamovi.org/) — onde se instalam os
  módulos adicionais, incluindo o de curva ROC.
- [EQUATOR Network](https://www.equator-network.org/) — reúne o STARD e as
  demais recomendações de relato.

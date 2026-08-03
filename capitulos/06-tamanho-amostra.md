::: caso
O protocolo precisa responder a uma pergunta que o Comitê de Ética vai cobrar e
que o revisor vai conferir: por que duzentos pacientes? Não cento e cinquenta,
não trezentos. A resposta é uma conta de quatro ingredientes, e este capítulo a
refaz do início ao fim, com os números do estudo.
:::

## Por que a conta é obrigatória

Um estudo pequeno demais não consegue responder à pergunta e expõe pacientes a
risco sem nenhum ganho de conhecimento. Um estudo grande demais gasta recursos,
atrasa a resposta e expõe pacientes desnecessariamente à intervenção que se
mostrará inferior. As duas coisas são falhas éticas, e é por isso que o cálculo
do tamanho da amostra é exigido pelas resoluções brasileiras de ética em pesquisa
e por qualquer periódico sério.

Note a consequência: o cálculo é feito **antes**, e nunca depois. Justificar o
tamanho depois de coletar é justificar o que se conseguiu, não o que se
precisava.

## Os quatro ingredientes

Toda conta de tamanho de amostra combina os mesmos quatro elementos, qualquer que
seja o desfecho.

**1. O nível de significância, alfa.** A probabilidade que se aceita de concluir
que há efeito quando não há, o erro tipo I. Convencionalmente 5%, bilateral. Usar
teste unilateral reduz o tamanho da amostra e só se justifica quando um dos lados
é clinicamente impossível ou irrelevante, o que quase nunca é verdade.

**2. O poder, ou 1 menos beta.** A probabilidade de detectar o efeito, se ele
existir. Convencionalmente 80%, cada vez mais 90%. Um poder de 80% significa
aceitar 20% de chance de perder um efeito real, o que é bastante generoso quando
se pensa bem.

**3. A menor diferença clinicamente relevante.** O ingrediente que a estatística
não fornece: é decisão clínica. Neste estudo, 20 pontos percentuais.

**4. A variabilidade esperada.** Para desfechos binários, as proporções
esperadas; para contínuos, o desvio padrão. Vem da literatura, de estudo piloto
ou, na pior hipótese, de estimativa conservadora.

::: atencao O ingrediente que todo mundo erra
A menor diferença clinicamente relevante não é a diferença que você espera
encontrar, nem a que apareceu em um estudo piloto pequeno. É a menor diferença
que, existindo, mudaria a conduta clínica. Colocar ali um número otimista é a
maneira mais eficiente de produzir um estudo subdimensionado com aparência de
rigor: a conta fica bonita no protocolo e o estudo nasce condenado.
:::

## A conta deste estudo, passo a passo

Proporção de cicatrização esperada: 55% no controle, com base na literatura de
compressão isolada, e 75% no grupo tratado, o que representa os 20 pontos
percentuais considerados relevantes.

A fórmula para comparação de duas proporções independentes:

```
             [ z(1-α/2)·√(2·p̄·q̄) + z(1-β)·√(p₁q₁ + p₂q₂) ]²
n por grupo = ────────────────────────────────────────────────
                            (p₁ - p₂)²
```

Substituindo, com p₁ = 0,75, p₂ = 0,55, p̄ = 0,65, z(0,975) = 1,96 e
z(0,80) = 0,842:

```
n = [ 1,96·√(2 × 0,65 × 0,35) + 0,842·√(0,75×0,25 + 0,55×0,45) ]² / 0,20²
n = [ 1,96 × 0,6745 + 0,842 × 0,6595 ]² / 0,04
n = [ 1,3220 + 0,5553 ]² / 0,04
n = 3,5243 / 0,04 = 88,1
```

Arredondando para cima, **89 participantes por grupo**.

Prevendo 10% de perdas de seguimento, divide-se por 0,90 e chega-se a 99, que o
protocolo arredondou para **100 por grupo, 200 randomizados**.

O estudo terminou com 8% de perdas, um pouco abaixo do previsto, e com 92
participantes analisados por grupo, acima dos 89 necessários. O planejamento se
sustentou.

## Quanto custa cada ponto percentual

A relação entre a diferença a detectar e o tamanho da amostra é o argumento mais
convincente deste capítulo, e ela não é linear:

| Diferença a detectar | n por grupo | Total |
|---|---|---|
| 10 pontos percentuais | 376 | 752 |
| 15 pontos percentuais | 163 | 326 |
| 20 pontos percentuais | 89 | 178 |
| 25 pontos percentuais | 54 | 108 |

Reduzir pela metade a diferença que se quer detectar multiplica o tamanho da
amostra por aproximadamente quatro. É a mesma relação de raiz quadrada que
aparece no Capítulo 9: precisão é cara, e fica exponencialmente mais cara.

Daí uma conclusão prática e desconfortável: estudos de intervenções com efeito
modesto exigem centenas ou milhares de pacientes, e é por isso que efeitos
modestos só são estabelecidos por estudos multicêntricos ou por metanálise. Um
estudo de cinquenta pacientes não vai resolver a questão, e propor um é planejar
um resultado inconclusivo.

## Outros desfechos, outras contas

**Desfecho contínuo.** O que entra no lugar das proporções é o desvio padrão
esperado, e a diferença relevante vai na mesma unidade do desfecho. Para detectar
uma diferença de 15 pontos percentuais na redução de área em quatro semanas, com
desvio padrão de 44 pontos, alfa de 5% e poder de 80%, seriam necessários cerca
de 136 participantes por grupo. Repare que é mais do que os 89 do desfecho
binário: variabilidade alta custa caro, e o desvio padrão desse desfecho é
enorme.

**Tempo até o evento.** O que determina a precisão não é o número de
participantes, e sim o **número de eventos**. Calcula-se primeiro quantos eventos
são necessários para detectar a razão de riscos desejada, e depois quantos
participantes e quanto tempo de seguimento produzem esses eventos. Em doenças de
evolução lenta, aumentar o seguimento costuma ser mais barato que aumentar a
amostra.

**Estudo de acurácia diagnóstica.** O cálculo se faz sobre a precisão desejada do
intervalo de confiança da sensibilidade e da especificidade, e o que limita é o
número de doentes e de não doentes, não o total.

::: nota E quando a amostra é a que existe?
A situação real de boa parte das dissertações: "tenho acesso a 40 pacientes por
ano". Nesse caso o cálculo se inverte, e passa a responder outra pergunta: com 40
por grupo, qual a menor diferença detectável com 80% de poder? A resposta, para
proporções em torno de 55%, é cerca de 30 pontos percentuais.

Essa inversão é honesta e deve constar do protocolo com todas as letras. Ela
permite a decisão consciente: se 30 pontos percentuais é um efeito improvável
para essa intervenção, o estudo não deve ser feito como está, e as saídas são
buscar mais centros, escolher um desfecho mais frequente ou mudar a pergunta.
Fazer assim mesmo e escrever depois "não houve diferença" é o desperdício que
este livro tenta evitar.
:::

::: jamovi
1. O cálculo de poder não vem no jamovi básico. Abra **Modules**, a **jamovi
   library**, e instale o **jpower**.
2. Para comparar duas proporções, informe as duas proporções esperadas, o alfa e
   o poder desejado, e o módulo devolve o n por grupo.
3. Para desfecho contínuo, informe a diferença de médias esperada e o desvio
   padrão. O jpower aceita o tamanho de efeito padronizado, mas prefira informar
   diferença e desvio padrão separadamente: é mais fácil justificar cada um
   diante do comitê de ética.
4. Use a **curva de poder** que o módulo desenha. Ela mostra, de uma vez, como o
   poder varia conforme o tamanho da amostra, e é a figura mais útil para discutir
   viabilidade com um orientador ou com um financiador.
:::

::: revisor
**"Não há cálculo do tamanho da amostra."** Devolução automática em qualquer
revista clínica, e reprovação garantida no comitê de ética.

**"O cálculo não informa a diferença considerada clinicamente relevante nem sua
origem."** Cite a fonte: literatura, piloto, consenso de especialistas.

**"O tamanho da amostra foi calculado após a coleta."** Contradição em termos.

**"O estudo previu 10% de perdas e teve 30%, sem discutir o impacto."** O poder
efetivo caiu, e isso precisa aparecer nas limitações.

**"O cálculo se baseia em um desfecho diferente do desfecho primário
declarado."** Precisa ser o primário, sempre.

**"Teste unilateral usado sem justificativa."** Reduz artificialmente a amostra.
Justifique ou refaça bilateral.
:::

## Exercícios

::: exercicio 1
Refaça a conta do estudo supondo poder de 90% em vez de 80%. O que acontece com o
tamanho da amostra?

--- gabarito
O único termo que muda é z(1-β), que passa de 0,842 para 1,282. O numerador vira
[1,3220 + 1,282 × 0,6595]², ou [1,3220 + 0,8455]², igual a 4,6981. Dividido por
0,04, resulta em 118 participantes por grupo, contra 89. Aumentar o poder de 80%
para 90% custou cerca de um terço a mais de pacientes, o que ilustra por que 80%
continua sendo a escolha comum apesar de generosa.
:::

::: exercicio 2
Um pesquisador quer detectar uma diferença de 10 pontos percentuais no mesmo
desfecho. Ele consegue recrutar 120 pacientes por ano e o estudo pode durar dois
anos. É viável?

--- gabarito
Não, sem ajuda. Detectar 10 pontos percentuais exige 376 por grupo, ou 752
randomizados, e com 10% de perdas o número sobe para cerca de 836. Em dois anos
ele recrutaria 240. As saídas são estender o recrutamento para mais centros,
aumentar a duração do estudo, aceitar detectar uma diferença maior, ou trocar
para um desfecho contínuo, que costuma exigir menos participantes.
:::

::: exercicio 3
Por que o cálculo do tamanho da amostra deve usar o desfecho primário, e não o
que der o menor n?

--- gabarito
Porque o desfecho primário é aquele sobre o qual a conclusão do estudo será
construída, e é ele que precisa de poder adequado. Calcular o n sobre um desfecho
secundário mais fácil de detectar produz um estudo que responde bem à pergunta
que não interessa e mal à que interessa. Além disso, escolher o desfecho pelo n
que ele gera é uma forma de manipulação do protocolo, que o registro prévio
existe para coibir.
:::

::: exercicio 4
Com 40 participantes por grupo, qual a menor diferença detectável com 80% de
poder, partindo de 55% no controle? Use a tabela deste capítulo para estimar por
interpolação.

--- gabarito
A tabela mostra que 54 por grupo detectam 25 pontos percentuais. Com apenas 40
por grupo, a diferença detectável é maior, em torno de 29 a 30 pontos
percentuais. Isso significaria esperar que o tratamento levasse a cicatrização de
55% para cerca de 85%, o que é implausível para terapia adjuvante em úlcera
venosa. A conclusão prática é que 40 por grupo não é um tamanho adequado para
esta pergunta.
:::

::: exercicio 5
O estudo previu 10% de perdas e teve 8%. Se as perdas tivessem sido de 25%, o
estudo ainda teria o tamanho planejado? O que se deveria escrever no artigo?

--- gabarito
Com 25% de perdas, restariam 75 participantes por grupo, abaixo dos 89
necessários, e o poder efetivo cairia para cerca de 72%. O estudo continuaria
interpretável, mas o artigo deveria declarar a perda de poder nas limitações,
apresentar análise de sensibilidade com diferentes suposições sobre os dados
faltantes, e evitar concluir ausência de efeito caso o resultado fosse não
significativo.
:::

::: exercicio 6
No jamovi, com o jpower instalado, reproduza o cálculo de 89 por grupo e depois
desenhe a curva de poder para tamanhos entre 40 e 200 por grupo.

--- gabarito
A curva deve mostrar poder em torno de 50% com 40 por grupo, cruzar os 80% em
torno de 89, chegar a cerca de 90% em torno de 118 e aproximar-se de 98% com 200
por grupo. O formato importa mais que os números: o ganho de poder é acentuado no
começo e vai se achatando, de modo que aumentar de 40 para 90 pacientes muda
muito, e de 150 para 200 muda pouco. É essa curva que ajuda a decidir onde parar.
:::

## Recursos

- [jamovi library](https://library.jamovi.org/) — onde se instala o
  módulo jpower.
- [CONSORT Statement](https://www.consort-statement.org/) — item 7a, sobre como
  o tamanho da amostra foi determinado.
- [SPIRIT](https://www.spirit-statement.org/) — o que o protocolo precisa conter
  sobre dimensionamento.

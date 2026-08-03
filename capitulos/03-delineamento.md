::: caso
A pergunta está pronta: o aspirado de medula óssea aumenta a cicatrização de
úlceras venosas em doze semanas? Restam duas maneiras de respondê-la. A primeira
é observar o que já acontece: identificar quem recebeu o tratamento, quem não
recebeu, e comparar. A segunda é sortear. A diferença entre elas parece
burocrática e é a diferença entre acertar e errar o sinal do efeito.
:::

## O delineamento decide o que se pode concluir

Nenhuma análise estatística conserta um delineamento inadequado. Um estudo
transversal não estabelece que a exposição veio antes do desfecho; uma série de
casos não tem com quem comparar; uma coorte pode ser destruída por um confundidor
que ninguém mediu. O Capítulo 12 mostra isso com números, e a demonstração é
brutal: a coorte simulada deste livro, com o mesmo tratamento e o mesmo efeito
verdadeiro do ensaio, conclui que o aspirado **prejudica** a cicatrização.

Por isso a ordem dos capítulos: pergunta, delineamento e só então medida,
amostra, coleta e análise. Escolher o teste estatístico é a menor das decisões, e
é a única em que a maioria dos pesquisadores pensa.

## Os delineamentos, e a pergunta que cada um responde

| Delineamento | Responde bem a | Não responde a |
|---|---|---|
| Ensaio clínico randomizado | eficácia de intervenção | frequência na população, efeitos raros e tardios |
| Coorte | prognóstico, incidência, dano de exposição não randomizável | eficácia, quando há confundimento por indicação |
| Caso-controle | etiologia de doença rara | incidência, risco absoluto |
| Transversal | prevalência, acurácia diagnóstica | temporalidade, causalidade |
| Série de casos | descrever o inédito | qualquer comparação |
| Revisão sistemática | sintetizar tudo o que existe | criar evidência que não existe |

A chamada hierarquia da evidência, que põe o ensaio randomizado acima da coorte e
esta acima do caso-controle, vale **para perguntas de eficácia**. Para
prevalência, um transversal bem-feito é superior a qualquer ensaio; para dano
raro de longo prazo, a coorte é insubstituível; para a experiência do paciente, é
a pesquisa qualitativa que responde. Delineamento não é bom ou ruim em abstrato:
é adequado ou inadequado à pergunta.

## Por que este estudo foi randomizado

A formulação clínica original do caso condutor era observacional: comparar quem
usa o aspirado com quem não usa. Ela foi recusada, e o motivo é o **confundimento
por indicação**.

Na prática real, o cirurgião indica terapia celular para a úlcera grande, antiga,
refratária, do paciente diabético. Ou seja, indica para quem tem pior
prognóstico. O grupo tratado começa a corrida com desvantagem, e o benefício do
tratamento é engolido por ela. Os números da coorte simulada, detalhados no
Capítulo 12, mostram o tamanho do estrago: quem recebeu tinha úlcera com o dobro
da área e quase o dobro de duração, e o resultado bruto aponta razão de chances
de 0,72, isto é, aparente prejuízo, quando o efeito verdadeiro é de benefício.

O sorteio resolve isso de uma maneira que nenhuma técnica estatística consegue
imitar: ele equilibra, em média, **tudo**, inclusive o que ninguém mediu e o que
ninguém sabe que existe. É essa a propriedade que faz do ensaio randomizado o
padrão para perguntas de eficácia, e ela não tem substituto.

## As três proteções de um ensaio, e o que cada uma protege

**Randomização.** Torna os grupos comparáveis na origem. Feita em blocos
permutados de quatro, como neste estudo, mantém os grupos com tamanhos parecidos
ao longo do recrutamento; estratificada por centro, garante equilíbrio dentro de
cada serviço.

**Sigilo de alocação.** Impede que quem recruta saiba qual será a próxima
alocação. É diferente de cegamento e é ainda mais importante: se o cirurgião
souber que o próximo envelope é do grupo tratado, poderá, mesmo sem má-fé, adiar
a inclusão de um paciente grave para a semana seguinte. Estudos sem sigilo de
alocação superestimam sistematicamente o efeito. Neste estudo, a alocação vinha de
central independente, por telefone.

**Cegamento.** Impede que o conhecimento da alocação influencie o cuidado ou a
aferição do desfecho. Aqui ele é parcial, e é preciso dizer isso com todas as
letras: não há como cegar quem aspira medula óssea nem quem a recebe. Cega-se
quem mede a área da úlcera e adjudica a cicatrização, por fotografia planimetrada
identificada apenas por código.

::: nota Cegamento não é tudo ou nada
A pergunta certa não é "o estudo foi cego?", e sim "quem foi cegado?". Paciente,
profissional que aplica, profissional que cuida, avaliador do desfecho,
estatístico: são cinco papéis, e cada um pode ou não ser cegado. Em pesquisa
cirúrgica, cegar paciente e operador é quase sempre impossível, e o que se exige é
o cegamento do avaliador, que é justamente onde o viés de aferição entraria. Um
desfecho objetivo, como a morte, sofre pouco com a falta de cegamento; um desfecho
julgado, como "melhora do aspecto da ferida", sofre muito.
:::

## Variantes do ensaio clínico

**Paralelo.** Cada participante recebe um tratamento. É o deste estudo e o mais
comum.

**Cruzado.** Cada participante recebe os dois, em ordem sorteada, e serve de
controle de si mesmo. Exige condição estável e efeito reversível, e por isso
**não serviria aqui**: uma úlcera cicatrizada não volta ao estado inicial para
receber o outro tratamento.

**Por conglomerados.** Sorteiam-se serviços, e não pacientes. Útil quando a
intervenção é organizacional, como um protocolo de curativo, e exige análise que
leve em conta a correlação dentro de cada serviço.

**Fatorial.** Testam-se duas intervenções ao mesmo tempo, em quatro
combinações. Econômico, e só funciona quando não se espera interação entre elas.

**Escalonado no tempo.** Todos os centros acabam recebendo a intervenção, em
ordem sorteada. Muito usado em pesquisa de implementação, quando negar a
intervenção a alguém seria inaceitável.

## Os vieses, e onde cada um entra

| Viés | Onde nasce | Antídoto |
|---|---|---|
| Seleção | quem entra e quem vai para cada grupo | randomização com sigilo de alocação |
| Aferição | como o desfecho é medido | cegamento do avaliador, desfecho objetivo |
| Atrito | quem sai do estudo | seguimento ativo, intenção de tratar, análise de sensibilidade |
| Relato | o que se publica do que se mediu | registro prévio, protocolo público |

Repare que três dos quatro se combatem no delineamento, e nenhum se combate na
análise. É por isso que este capítulo antecede todos os de estatística.

## Quando não se pode randomizar

Nem toda pergunta admite sorteio, e insistir seria antiético ou impossível:

- **Exposições danosas.** Ninguém sorteia tabagismo.
- **Desfechos raros ou tardios.** Um ensaio para detectar um efeito que ocorre em
  1 a cada 10 mil pacientes após quinze anos é inviável.
- **Ausência de incerteza.** Se já se sabe que um braço é superior, não há
  equipoise.
- **Intervenções já disseminadas.** Quando a prática já mudou, randomizar de volta
  costuma ser recusado por pacientes e profissionais.

Nesses casos a coorte é o melhor disponível, e o que se exige dela é honestidade:
medir os confundidores conhecidos, ajustar como o Capítulo 12 ensina, discutir o
confundimento residual e escrever "associação", não "causa".

::: revisor
**"O delineamento não está declarado no título nem no resumo."** Uma palavra
resolve: randomizado, coorte, transversal.

**"Não está descrito como a sequência de randomização foi gerada."** "Os
pacientes foram randomizados" não basta. Diga o método, o tamanho dos blocos e a
estratificação.

**"O sigilo de alocação não é mencionado."** É o item cuja ausência mais se
associa a efeitos superestimados na literatura.

**"O estudo se declara duplo-cego sem explicar quem foi cegado."** O termo é
ambíguo e vem caindo em desuso justamente por isso.

**"Conclusão causal a partir de estudo transversal."** Sem temporalidade, não há
causalidade. Reescreva como associação.

**"Estudo observacional apresentado como se comparasse tratamentos de forma
válida, sem discutir confundimento por indicação."** É a falha mais comum na
literatura cirúrgica.
:::

## Exercícios

::: exercicio 1
Qual delineamento você usaria para cada pergunta? (a) Qual a prevalência de
úlcera venosa em maiores de 60 anos no município? (b) O uso prolongado de
corticoide aumenta o risco de úlcera de perna? (c) A bota de Unna cicatriza mais
que a faixa elástica?

--- gabarito
(a) Transversal, com amostragem probabilística da população do município.
(b) Coorte, ou caso-controle se o desfecho for pouco frequente; randomizar
corticoide para observar dano seria antiético.
(c) Ensaio clínico randomizado, porque é pergunta de eficácia entre duas opções
disponíveis, ambas padrão de cuidado, o que garante equipoise.
:::

::: exercicio 2
Por que o delineamento cruzado não serviria para o caso condutor?

--- gabarito
Porque o desfecho é irreversível dentro do horizonte do estudo. No delineamento
cruzado, cada participante recebe os dois tratamentos em sequência, o que exige
que a condição volte ao estado inicial entre os períodos. Uma úlcera que
cicatrizou não reabre para receber o segundo tratamento, e o efeito de arrasto
seria total. O cruzado serve a condições crônicas e estáveis, como dor
neuropática ou asma.
:::

::: exercicio 3
Explique a diferença entre sigilo de alocação e cegamento, e diga qual dos dois
teria sido possível manter integralmente no caso condutor.

--- gabarito
O sigilo de alocação protege o momento da inclusão: impede que quem recruta
saiba, de antemão, para qual grupo o próximo paciente irá, evitando que ele
escolha quem incluir. O cegamento protege o período posterior: impede que o
conhecimento da alocação influencie o cuidado prestado e a aferição do desfecho.
No caso condutor, o sigilo de alocação foi mantido integralmente, por central
telefônica independente, enquanto o cegamento só foi possível para o avaliador do
desfecho.
:::

::: exercicio 4
Um estudo observacional conclui que pacientes que receberam terapia celular
tiveram pior cicatrização, e recomenda abandonar a técnica. Que pergunta você
faria aos autores?

--- gabarito
Como eram os pacientes de cada grupo antes do tratamento. Se quem recebeu tinha
úlceras maiores, mais antigas e mais comorbidades, a comparação bruta mede
gravidade, não tratamento. Perguntaria também quais confundidores foram medidos e
ajustados, e como os autores avaliam o confundimento residual daquilo que não foi
medido. A recomendação de abandonar uma técnica não se sustenta em análise bruta
de estudo observacional.
:::

::: exercicio 5
O caso condutor tem cegamento apenas do avaliador. Que desfechos deste estudo são
mais vulneráveis à ausência de cegamento do paciente, e por quê?

--- gabarito
Os desfechos relatados pelo próprio paciente, com destaque para a dor na escala
visual analógica. Quem sabe que recebeu uma terapia celular tende a relatar mais
melhora, por expectativa. A cicatrização completa é bem menos vulnerável, porque
é aferida por avaliador cego em fotografia planimetrada e tem critério objetivo.
Essa diferença de vulnerabilidade deve ser discutida no artigo, e é um bom
argumento para não construir a conclusão principal sobre desfechos subjetivos em
estudo sem cegamento do paciente.
:::

::: exercicio 6
Você quer avaliar se um novo protocolo de curativo, aplicado por toda a equipe de
enfermagem de uma unidade, reduz o tempo de cicatrização. Qual delineamento, e
qual cuidado especial a análise exige?

--- gabarito
Ensaio randomizado por conglomerados, sorteando unidades e não pacientes, porque
a intervenção é da equipe e não do indivíduo, e porque randomizar pacientes dentro
da mesma unidade contaminaria os grupos. O cuidado especial é que pacientes da
mesma unidade se parecem entre si, o que reduz a informação efetiva: a análise
precisa levar em conta essa correlação intraconglomerado, e o cálculo do tamanho
da amostra exige inflar o número de participantes pelo efeito de delineamento.
Ignorar isso produz intervalos de confiança falsamente estreitos.
:::

::: agora
1. Escreva o delineamento do seu estudo em uma frase, com todos os adjetivos que
   ele merece. Essa frase vai para o título e para o resumo.
2. Se o seu estudo for observacional e comparar tratamentos, liste por escrito
   quem recebe cada um na prática e por quê. Essa lista é o seu confundimento por
   indicação, e ela precisa aparecer nas limitações.
3. Se for randomizado, descreva em parágrafos separados a geração da sequência e
   o sigilo da alocação. São dois itens distintos e quase sempre aparecem
   fundidos em uma frase vaga.
4. Liste quem será cegado, papel por papel, e o que você fará onde o cegamento
   for impossível.
5. **Baixe o checklist da recomendação de relato do seu delineamento e responda a
   ele antes de coletar o primeiro dado.** Ele foi feito para relatar, e usá-lo
   como roteiro de planejamento é a melhor maneira de não descobrir uma falha
   estrutural quando não houver mais conserto.
:::

## Recursos

- [CONSORT Statement](https://www.consort-statement.org/) — o checklist e o
  diagrama de fluxo para ensaios randomizados.
- [STROBE Statement](https://www.strobe-statement.org/) — o equivalente para
  estudos observacionais.
- [EQUATOR Network](https://www.equator-network.org/) — reúne as recomendações de
  relato de todos os delineamentos.

::: caso
O estudo terminou, o artigo foi submetido, o revisor pediu duas análises
adicionais e elas foram feitas em vinte minutos, porque o banco estava
organizado e as análises, em um script. É um final feliz que depende inteiramente
de decisões tomadas lá no começo. Este capítulo olha para trás, para os lados e
para a frente.
:::

## O passado: como a estatística entrou na medicina

A pesquisa clínica moderna tem data de nascimento razoavelmente precisa. Em 1948,
o Medical Research Council britânico publicou o ensaio da estreptomicina para
tuberculose pulmonar, planejado por Austin Bradford Hill, com alocação
verdadeiramente aleatória e sigilo de alocação. Não foi o primeiro estudo
comparativo da história, mas foi o primeiro a tratar o sorteio como instrumento
metodológico deliberado, e é dele que descende tudo o que este livro ensinou.

Antes disso, o século havia produzido o arcabouço matemático. Ronald Fisher
formalizou a análise de variância, o princípio da aleatorização em experimentos
agrícolas e, para o bem e para o mal, o limiar de 0,05, sugerido como
conveniência de cálculo e transformado pela posteridade em fronteira sagrada.
Jerzy Neyman e Egon Pearson acrescentaram os erros tipo I e tipo II e a ideia de
poder. Bradford Hill trouxe tudo isso para o leito do paciente.

O que se seguiu foi meio século de expansão: metanálise nos anos 1970, medicina
baseada em evidências nos anos 1990, CONSORT em 1996, registro obrigatório de
ensaios em 2005. A cada etapa, a exigência de transparência aumentou, e sempre
depois de um escândalo.

## O presente: uma disciplina em revisão

Três movimentos definem o momento atual, e este livro é filho dos três.

**A crise de reprodutibilidade.** A partir de 2011, tentativas sistemáticas de
replicar achados publicados encontraram taxas de sucesso desconfortavelmente
baixas, primeiro em psicologia, depois em oncologia pré-clínica e em várias
outras áreas. As causas são conhecidas: amostras pequenas, flexibilidade
analítica, seleção de desfechos, viés de publicação.

**A revisão do valor de p.** A declaração da American Statistical Association, em
2016, e a edição especial de 2019 do *The American Statistician* fizeram o que
parecia impossível, que foi colocar em dúvida institucional o ritual do p < 0,05.
Não houve substituto único, e a orientação prática consolidada é a que este livro
segue: estimativa, intervalo e magnitude clínica em primeiro plano; valor de p
como informação acessória.

**A ciência aberta.** Registro prévio de protocolos, publicação de planos de
análise estatística, dados e códigos disponíveis, e o formato dos relatórios
registrados, em que a revista avalia o protocolo e aceita o artigo antes de
conhecer os resultados, o que elimina de uma vez o viés de publicação. É a
mudança estrutural mais promissora dos últimos vinte anos.

::: nota O que isso muda para quem faz uma dissertação
Muda três coisas concretas. Primeiro, registrar o protocolo antes de coletar
deixou de ser formalidade e virou credencial. Segundo, o desfecho primário único
e declarado é hoje o principal sinal de seriedade metodológica que um leitor
consegue verificar. Terceiro, ninguém mais deveria escrever "não houve diferença
(p = 0,21)" sem apresentar o intervalo de confiança ao lado.
:::

## O futuro: quatro apostas

**Dados abertos como padrão.** A tendência é que o banco anonimizado passe a ser
condição de publicação, como já ocorre em várias revistas. Quem organiza o banco
desde o começo, como o Capítulo 7 recomenda, chega pronto; quem improvisa, terá
de refazer.

**Métodos bayesianos na prática clínica.** Eles respondem à pergunta que o
clínico realmente faz, que é "qual a probabilidade de este tratamento ser melhor,
dado o que eu observei", e permitem incorporar formalmente o conhecimento
anterior. Já são padrão em ensaios adaptativos e em avaliação de dispositivos, e a
barreira restante é mais cultural e computacional do que conceitual.

**Metanálise viva e evidência acumulada.** Em vez de estudos isolados, revisões
que se atualizam a cada novo ensaio. A pergunta deixa de ser "o meu estudo deu
positivo?" e passa a ser "o que o meu estudo acrescenta ao conjunto?", que é uma
pergunta mais honesta e mais útil.

**Inteligência artificial na análise estatística.** Modelos de linguagem já
escrevem código de análise, sugerem testes, redigem métodos e explicam resultados,
e farão isso cada vez melhor. Vale ser específico sobre o que muda e o que não
muda.

O que a ferramenta faz bem: gerar o código de uma análise descrita em palavras,
lembrar qual teste se aplica a que situação, revisar um manuscrito contra o
checklist CONSORT, encontrar inconsistências entre tabelas, explicar uma saída de
programa em linguagem clara.

O que ela não faz: decidir a pergunta de pesquisa, escolher a menor diferença
clinicamente relevante, julgar se um desfecho substituto é aceitável, saber que a
adesão à compressão foi medida depois da randomização e por isso não entra no
ajuste, ou reconhecer que uma mediana de 100% nos dois grupos é efeito teto e não
ausência de diferença.

Ou seja: ela executa e não julga. Todas as decisões deste livro, da pergunta ao
relato, continuam sendo do pesquisador, e um erro cometido com auxílio de
inteligência artificial continua sendo um erro do autor. A vantagem prática é que
o tempo antes gasto em cálculo pode ser gasto em pensar, que é onde os estudos se
ganham e se perdem.

## O que fazer amanhã de manhã

O livro cabe em uma lista, e ela é curta:

1. Escreva sua pergunta em PICO, em uma frase. Se não couber, ela não está pronta.
2. Escolha o delineamento pela pergunta, não pela conveniência.
3. Defina **um** desfecho primário, com definição operacional que dois avaliadores
   apliquem do mesmo jeito.
4. Calcule o tamanho da amostra antes, e declare a menor diferença clinicamente
   relevante.
5. Registre o protocolo antes de incluir o primeiro participante.
6. Monte o banco no dia em que a coleta começa: uma linha por participante, uma
   informação por célula, dicionário escrito.
7. Descreva antes de testar, e olhe as distribuições em vez de testar
   normalidade.
8. Relate estimativa e intervalo; o valor de p vem depois.
9. Ajuste apenas por variáveis basais, escolhidas por raciocínio clínico.
10. Siga a recomendação de relato do seu delineamento, e siga desde o começo.

## Uma palavra final

A estatística na pesquisa clínica não é um obstáculo entre o pesquisador e a
publicação. É a disciplina que impede que ele engane a si mesmo, que é o erro
mais fácil de cometer e o mais difícil de perceber. Quem randomiza está admitindo
que não sabe qual braço é melhor. Quem calcula o tamanho da amostra está
admitindo que sua impressão clínica pode estar errada. Quem publica o intervalo
de confiança está admitindo o tamanho de sua ignorância.

Essa disposição de admitir vale mais do que qualquer teste deste livro. Os testes
mudam; a disposição, não.

::: agora
Uma última tarefa, e ela não é de análise:

1. Pegue o seu projeto, aquele que está em andamento ou na gaveta.
2. Percorra a lista de dez itens deste capítulo, marcando o que já está resolvido
   e o que não está.
3. O primeiro item não marcado é onde você deve trabalhar amanhã.

Se o item não marcado estiver entre os cinco primeiros, e a coleta já tiver
começado, pare a coleta. É desconfortável e é mais barato do que descobrir o
problema na banca.
:::

## Exercícios

::: exercicio 1
O ensaio da estreptomicina, de 1948, é considerado o marco inicial da pesquisa
clínica moderna. O que ele fez que estudos anteriores não faziam?

--- gabarito
Usou alocação verdadeiramente aleatória, com sigilo, tratando o sorteio como
instrumento metodológico deliberado e não como conveniência administrativa. Isso
garantiu comparabilidade entre os grupos e, principalmente, impediu que o
pesquisador influenciasse, mesmo sem intenção, quem receberia o novo tratamento.
É a mesma propriedade que o Capítulo 12 demonstra ser insubstituível.
:::

::: exercicio 2
Explique, com o que aprendeu no livro, por que a crise de reprodutibilidade tem
relação com amostras pequenas.

--- gabarito
Estudos pequenos têm pouco poder e intervalos largos. Entre eles, os que atingem
significância estatística são justamente aqueles em que o acaso produziu um efeito
exagerado, e são esses que acabam publicados, porque resultados negativos são
publicados menos. A literatura passa então a conter estimativas
sistematicamente infladas, que não se replicam quando alguém tenta repetir o
estudo com tamanho adequado.
:::

::: exercicio 3
Que tarefas da sua pesquisa você delegaria a uma ferramenta de inteligência
artificial, e quais não delegaria?

--- gabarito
Delegáveis: escrever o código de uma análise já decidida, converter tabelas de
formato, revisar o manuscrito contra o checklist CONSORT, verificar se os números
do texto batem com os das tabelas, explicar uma saída de programa. Não
delegáveis: definir a pergunta, escolher o delineamento, definir a menor
diferença clinicamente relevante, decidir quais variáveis entram no ajuste,
julgar relevância clínica e assinar a conclusão. A regra prática é que a
ferramenta executa e o pesquisador julga, e a responsabilidade é sempre de quem
assina.
:::

::: exercicio 4
Por que o formato dos relatórios registrados, em que a revista aceita o artigo
antes de conhecer os resultados, elimina o viés de publicação?

--- gabarito
Porque a decisão editorial passa a se basear na relevância da pergunta e na
qualidade do método, que são conhecidos antes da coleta, e não na direção do
resultado, que é conhecida depois. Um estudo bem desenhado é publicado dando
positivo ou negativo, e a literatura deixa de ser um catálogo enviesado de
achados favoráveis.
:::

::: exercicio 5
Releia a lista de dez itens e identifique em qual capítulo cada um foi tratado.

--- gabarito
1 no Capítulo 2; 2 no Capítulo 3; 3 no Capítulo 4; 4 no Capítulo 6; 5 no Capítulo
2, com reforço no 15; 6 no Capítulo 7; 7 no Capítulo 8, com o mito da normalidade
no 11; 8 nos Capítulos 9 e 10; 9 no Capítulo 12; 10 no Capítulo 15. Repare que
sete dos dez itens são anteriores à análise: é a tese central do livro,
enunciada em forma de lista.
:::

::: exercicio 6
Escreva, em um parágrafo, o que você faria diferente no seu próximo estudo depois
de ler este livro.

--- gabarito
Não há resposta única, e a pergunta é séria. O parágrafo mais valioso costuma
citar uma decisão concreta e datada: registrar o protocolo antes de coletar,
substituir um desfecho substituto pelo desfecho que importa ao paciente, refazer
o cálculo do tamanho da amostra com uma diferença relevante mais modesta, montar
o dicionário de variáveis antes da primeira consulta, ou trocar a coluna de valor
de p da Tabela 1 por uma coluna de diferença com intervalo de confiança.
:::

## Recursos

- [ASA Statement on p-Values](https://www.tandfonline.com/doi/full/10.1080/00031305.2016.1154108)
  e [Moving to a World Beyond "p < 0.05"](https://www.tandfonline.com/doi/full/10.1080/00031305.2019.1583913).
- [EQUATOR Network](https://www.equator-network.org/) — recomendações de relato.
- [Cochrane Library](https://www.cochranelibrary.com/) — revisões sistemáticas e
  metanálises.
- [Center for Open Science](https://www.cos.io/) — registro de protocolos e
  relatórios registrados.

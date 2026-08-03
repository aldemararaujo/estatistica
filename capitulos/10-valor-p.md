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
três está fazendo o que a literatura chama de p-hacking, e é por isso que a
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
para nada.** O chamado poder observado, ou poder pós-hoc, é apenas uma
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

## Recursos

- [ASA Statement on p-Values and Statistical Significance](https://www.tandfonline.com/doi/full/10.1080/00031305.2016.1154108)
  — os seis princípios, em quatro páginas.
- [Moving to a World Beyond "p < 0.05"](https://www.tandfonline.com/doi/full/10.1080/00031305.2019.1583913)
  — a editorial de 2019 que abre a edição especial do *The American Statistician*.
- [Scientists rise up against statistical significance](https://www.nature.com/articles/d41586-019-00857-9)
  — o manifesto na *Nature*, assinado por mais de oitocentos pesquisadores.

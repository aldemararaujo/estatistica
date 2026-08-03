# O caso condutor do livro

Estudo fictício que atravessa a obra do Capítulo 2 ao 15. O leitor o acompanha
sendo formulado, desenhado, dimensionado, tabulado, descrito, analisado e
relatado. Os dados são simulados; nada aqui é resultado real.

---

## 1. O ponto de partida clínico

Úlcera venosa de membro inferior é a complicação mais incapacitante da doença
venosa crônica. A terapia compressiva é o tratamento padrão, mas uma parcela
importante das úlceras não cicatriza em 12 semanas mesmo com compressão bem
feita. O aspirado de medula óssea autólogo, aplicado no leito e nas bordas da
úlcera, tem sido proposto como terapia celular adjuvante, com relatos de séries
pequenas e sem ensaio de tamanho adequado.

**Dúvida do pesquisador:** o aspirado de medula óssea acelera e aumenta a
cicatrização, ou o que se vê nas séries publicadas é o efeito da compressão bem
supervisionada que esses pacientes recebem junto?

## 2. A pergunta em formato PICO

| Componente | Conteúdo |
|---|---|
| **O** | A diferença de proporção de úlceras completamente cicatrizadas (aferida em 12 semanas, conforme a definição operacional adiante) |
| **P** | Adultos com úlcera venosa ativa de membro inferior (CEAP C6), com 4 semanas ou mais de duração, área entre 1 e 50 cm², índice tornozelo-braquial ≥ 0,80 |
| **I** | Aspirado de medula óssea autólogo aplicado no leito e nas bordas da úlcera, em sessão única, associado à terapia compressiva inelástica |
| **C** | Terapia compressiva inelástica isolada, com o mesmo protocolo de curativos |

**Pergunta:** qual a diferença de proporção de úlceras completamente cicatrizadas
em adultos com úlcera venosa ativa de membro inferior que utilizaram o aspirado
de medula óssea autólogo associado à terapia compressiva comparado à terapia
compressiva isolada?

A pergunta é de **estimação**, não de teste: ela pede um número com margem de
erro, e não um sim ou um não. Essa escolha percorre o livro inteiro. É por isso
que o desfecho primário é relatado como diferença absoluta de risco com intervalo
de confiança, e não como "houve diferença significativa".

**Objetivo geral:** estimar a diferença de proporção de úlceras completamente
cicatrizadas em 12 semanas entre os dois grupos.

**Hipótese nula:** a diferença de proporção é zero.

## 3. Delineamento

**Ensaio clínico randomizado, paralelo, 1:1, multicêntrico (três centros),
com avaliador de desfecho cego.**

Esta é uma decisão deliberada do livro, e o Capítulo 3 a discute abertamente. A
formulação clínica original ("quem usa comparado com quem não usa") descreve um
estudo observacional, e um estudo observacional aqui seria devastado pelo
**confundimento por indicação**: o cirurgião indica terapia celular justamente
para a úlcera grande, antiga e refratária, ou seja, para a que tem pior
prognóstico. O efeito verdadeiro apareceria invertido.

O caso observacional não é descartado: ele existe de fato, em
`dados/coorte-observacional.csv`, gerado com o **mesmo efeito verdadeiro** do
ensaio e com uma única diferença, a de que ninguém sorteou nada e o aspirado foi
indicado a quem tinha a úlcera maior, mais antiga e mais diabética. O resultado
bruto dessa coorte é uma razão de chances de 0,72, isto é, o tratamento pareceria
prejudicar. O ajuste por área, duração, diabetes e adesão recupera 1,87, ainda
abaixo do 2,25 do ensaio. É a demonstração central do Capítulo 12, e o argumento
mais forte do livro inteiro a favor da randomização.

**Cegamento.** Não há como cegar quem aplica nem quem recebe o aspirado. Cega-se
quem mede a área da úlcera e adjudica a cicatrização, por fotografia planimetrada
identificada apenas por código. É a situação real da maioria dos ensaios
cirúrgicos, e é o que o Capítulo 3 usa para ensinar que cegamento não é tudo ou nada.

**Randomização.** Blocos permutados de quatro, estratificados por centro,
alocação por central telefônica independente (sigilo de alocação).

**Recrutamento.** Amostragem consecutiva nos três centros. Foram avaliados para
elegibilidade **246** pacientes, dos quais 46 não entraram: 19 por índice
tornozelo-braquial abaixo de 0,80, 12 por úlcera de etiologia não venosa, 9 por
recusa em participar e 6 por outros critérios de exclusão. Restaram os **200**
randomizados.

Estes números do recrutamento não estão no banco de dados, porque um banco só
contém quem entrou. Eles existem apenas aqui e alimentam o diagrama CONSORT do
Capítulo 15, que é justamente o lugar onde a informação sobre quem ficou de fora
precisa aparecer.

## 4. Desfechos

**Primário.** Cicatrização completa em 12 semanas: epitelização total da úlcera,
sem necessidade de curativo, confirmada por avaliador cego e mantida por 14 dias.
Binário.

**Secundários.**
1. Redução percentual da área da úlcera em 4 semanas (contínuo). Marcador
   prognóstico consagrado na úlcera venosa: redução ≥ 40% em 4 semanas prediz
   cicatrização.
2. Tempo até a cicatrização completa, em dias, com censura em 84 dias
   (tempo até evento).
3. Redução percentual da área em 12 semanas (contínuo, com efeito teto).
4. Variação da dor pela escala visual analógica entre a inclusão e 12 semanas.

**Segurança.** Infecção da ferida e dor no sítio de punção medular.

## 5. Cálculo do tamanho da amostra

Proporção esperada de cicatrização em 12 semanas: **55% no grupo controle**
(compressão isolada, literatura) e **75% no grupo intervenção**, diferença
mínima clinicamente relevante de 20 pontos percentuais.

Com α = 5% bilateral e poder de 80%, pela fórmula de comparação de duas
proporções independentes:

```
n por grupo = [ z(1-α/2)·√(2·p̄·q̄) + z(1-β)·√(p1·q1 + p2·q2) ]² / (p1 - p2)²
            = [ 1,96·√(2·0,65·0,35) + 0,842·√(0,55·0,45 + 0,75·0,25) ]² / 0,20²
            = 89 participantes por grupo
```

Prevendo 10% de perdas de seguimento: **100 por grupo, 200 randomizados**.

Este cálculo é refeito passo a passo no Capítulo 6, e a mesma conta é executada
no jamovi. O banco tem exatamente esse tamanho, o que permite ao leitor comparar
o que foi planejado com o que de fato se observou.

## 6. O que o estudo encontrou (para uso do autor, não do leitor)

Resultados do banco `dados/coorte-condutor.csv`, entre os 184 participantes com
desfecho primário observado:

| Medida | Valor |
|---|---|
| Cicatrização em 12 semanas, grupo aspirado | 70,7% (65/92), IC95% 60,7 a 79,0 |
| Cicatrização em 12 semanas, grupo controle | 53,3% (49/92), IC95% 43,1 a 63,1 |
| Diferença absoluta | 17,4 pontos percentuais (IC95% 3,6 a 31,2) |
| Risco relativo | 1,33 (IC95% 1,05 a 1,67) |
| Número necessário para tratar | 5,8 (IC95% 3,2 a 27,9) |
| Qui-quadrado (1 gl) | 5,90, p = 0,015 |
| Tempo mediano até cicatrizar (Kaplan-Meier) | 50 dias contra 82 dias |
| Log-rank | qui² 9,26, p = 0,002 |
| Razão de riscos de Cox, ajustada | 2,10 (IC95% 1,43 a 3,08) |
| Perdas de seguimento | 8 em cada grupo (8%) |
| Área da curva ROC, TcPO₂ basal | 0,656 (IC95% 0,574 a 0,737) |
| Área da curva ROC, redução de área em 4 semanas | 0,824 (IC95% 0,766 a 0,883) |

Todos esses números são produzidos por `analises/analises-do-livro.py`, que lê o
banco e escreve `analises/resultados.md`. Nenhum resultado impresso no livro vem
de outro lugar, e é assim que capítulos escritos com meses de distância não se
contradizem.

Três propriedades foram construídas de propósito, e cada uma sustenta uma lição:

1. **O estudo planejou 20 pontos percentuais e observou 17,4.** O resultado
   continua significativo, mas por pouco. É o material do Capítulo 10: o valor de
   p não mede o tamanho do efeito, e o intervalo de confiança da diferença
   mostra o que o p esconde.
2. **O TcPO₂ é um teste mediano e a redução em 4 semanas é um teste bom.** O
   Capítulo 13 compara as duas curvas ROC em vez de apresentar uma só, que é o
   que se faz na prática.
3. **A área em 12 semanas satura**: mais da metade dos participantes chega a
   100% de redução, e a mediana é zero nos dois grupos. É a demonstração de por
   que a aferição de 4 semanas existe, e de por que média e mediana divergem.

## 7. Onde o caso entra em cada capítulo

| Cap. | Uso do caso |
|---|---|
| 2 | A dúvida clínica vira PICO |
| 3 | Por que ensaio randomizado e não coorte; confundimento por indicação; cegamento parcial |
| 4 | Tipos de variável no banco; desfecho binário contra contínuo contra tempo até evento |
| 5 | Como os três centros recrutaram; amostragem consecutiva e sua consequência |
| 6 | O cálculo dos 89 por grupo, refeito no jamovi |
| 7 | O banco: uma linha por participante, dicionário, faltantes, ficha de coleta |
| 8 | Tabela 1 do artigo: descrever os dois grupos na linha de base |
| 9 | Intervalo de confiança da diferença de proporções e do risco relativo |
| 10 | Valor de p do desfecho primário; o que ele responde e o que não responde |
| 11 | Fluxograma de decisão: qui-quadrado, t, Mann-Whitney, McNemar (dor pareada) |
| 12 | Regressão logística ajustada por área inicial, duração e diabetes; a versão coorte do mesmo caso |
| 13 | Curvas ROC do TcPO₂ e da redução em 4 semanas; sensibilidade, especificidade, razões de verossimilhança |
| 14 | Kaplan-Meier do tempo até cicatrização, log-rank, modelo de Cox; censura pelas perdas |
| 15 | Diagrama CONSORT do estudo, tabela de resultados, o que o revisor devolveria |

## 8. Situação ética (para a apresentação do livro)

O estudo é fictício e os dados são simulados. Isso precisa estar escrito na
apresentação da obra, sem meias palavras, junto com a observação de que um estudo
real dessa natureza exigiria aprovação em Comitê de Ética em Pesquisa, registro
prévio em plataforma pública de ensaios clínicos e consentimento livre e
esclarecido, temas que o Capítulo 2 aborda.

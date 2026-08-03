::: caso
Todos os números impressos neste livro vêm de dois bancos de dados. Este apêndice
descreve os dois, diz como obtê-los e explica como conferir qualquer resultado da
obra.
:::

## Uma advertência antes de tudo

**Os dados são simulados.** Nenhum paciente real foi estudado, nenhum aspirado de
medula óssea foi aplicado e nenhum dos resultados deste livro constitui evidência
sobre o tratamento de úlceras venosas. O estudo é fictício; as decisões que ele
obriga a tomar são as mesmas de qualquer estudo real, e é para isso que ele
existe.

Um estudo verdadeiro dessa natureza exigiria aprovação em Comitê de Ética em
Pesquisa, registro prévio em plataforma pública de ensaios clínicos e
consentimento livre e esclarecido de cada participante.

## O ensaio randomizado

**Arquivo:** `coorte-condutor.csv` · 200 linhas · 26 variáveis · UTF-8, separador
vírgula, ponto decimal.

Ensaio clínico randomizado, paralelo, 1:1, multicêntrico, com avaliador de
desfecho cego, comparando aspirado de medula óssea autólogo associado à terapia
compressiva contra terapia compressiva isolada, em úlcera venosa de membro
inferior. Desfecho primário: cicatrização completa em 12 semanas.

### As variáveis

| Variável | Tipo | Descrição |
|---|---|---|
| `id` | texto | código do participante, P001 a P200 |
| `centro` | nominal | Centro A, B ou C |
| `grupo` | nominal | Aspirado ou Controle |
| `idade` | discreta | anos completos |
| `sexo` | nominal | Feminino ou Masculino |
| `imc` | contínua | kg/m²; 3 ausentes, não aferidos |
| `diabetes` | nominal | Sim ou Não |
| `tabagismo` | ordinal | Nunca fumou, Ex-fumante, Fumante atual |
| `itb` | contínua | índice tornozelo-braquial; abaixo de 0,80 era exclusão |
| `area_inicial_cm2` | contínua | planimetria na inclusão; assimétrica à direita |
| `duracao_ulcera_meses` | discreta | tempo de existência da úlcera atual |
| `ulcera_recidivante` | nominal | Sim ou Não |
| `adesao_compressao` | nominal | Adequada ou Inadequada; medida ao longo do seguimento |
| `tcpo2_basal` | contínua | mmHg; 12 ausentes por falha do equipamento |
| `dor_eva_basal` | discreta | escala visual analógica, 0 a 10 |
| `area_4sem_cm2` | contínua | planimetria em 4 semanas |
| `reducao_area_4sem_pct` | contínua | redução percentual em 4 semanas; negativa indica piora |
| `area_12sem_cm2` | contínua | planimetria em 12 semanas |
| `reducao_area_12sem_pct` | contínua | redução percentual em 12 semanas; satura em 100% |
| `dor_eva_12sem` | discreta | escala visual analógica em 12 semanas |
| `cicatrizacao_12sem` | nominal | **desfecho primário**; 16 ausentes por perda de seguimento |
| `tempo_ate_cicatrizacao_dias` | contínua | tempo até o evento ou até a censura |
| `evento_cicatrizacao` | binária | 1 evento, 0 censurado |
| `perda_seguimento` | nominal | Sim ou Não |
| `infeccao_ferida` | nominal | evento adverso |
| `dor_sitio_puncao` | nominal | só existe no grupo aspirado; ausência estrutural |

### As três naturezas de ausência

O banco foi construído com os três tipos que o Capítulo 7 distingue, e é
proposital:

- **Falha de aferição:** `imc` e `tcpo2_basal`. Não ameaçam a validade.
- **Perda de seguimento:** todos os desfechos de 12 semanas, em 16 participantes.
  É a ausência que ameaça a validade e motiva a análise por intenção de tratar.
- **Ausência estrutural:** `dor_sitio_puncao`, que não se aplica a quem não
  recebeu o aspirado. Não é dado faltante e não se imputa.

### Advertência sobre o tempo

`tempo_ate_cicatrizacao_dias` **não** pode ser analisada sozinha. Um valor de 84
significa uma úlcera que cicatrizou no último dia se `evento_cicatrizacao` for 1,
e uma úlcera que nunca cicatrizou se for 0. As duas colunas se leem juntas,
sempre. *Capítulo 14.*

## A coorte observacional

**Arquivo:** `coorte-observacional.csv` · 300 linhas · 12 variáveis.

Mesma pergunta, mesmo tratamento, mesmo desfecho e **o mesmo efeito verdadeiro**
do ensaio. A única diferença é que ninguém sorteou: o aspirado foi indicado a
quem tinha a úlcera maior, mais antiga e mais diabética, como faria qualquer bom
cirurgião.

Serve exclusivamente ao Capítulo 12, e serve a uma demonstração: a comparação
bruta dessa coorte devolve razão de chances de 0,72, isto é, aparente prejuízo,
quando o tratamento na verdade beneficia.

| Variável | Descrição |
|---|---|
| `id` | O001 a O300 |
| `recebeu_aspirado` | Sim ou Não; **não** foi sorteado |
| `idade`, `sexo`, `diabetes`, `tabagismo` | características basais |
| `area_inicial_cm2`, `duracao_ulcera_meses` | gravidade da úlcera; determinam a indicação |
| `ulcera_recidivante`, `tcpo2_basal` | prognósticas, não usadas no ajuste do capítulo |
| `adesao_compressao` | Adequada ou Inadequada |
| `cicatrizacao_12sem` | desfecho |
| `tempo_ate_cicatrizacao_dias`, `evento_cicatrizacao` | tempo até o evento |

## Como reproduzir tudo

Os arquivos e scripts da obra:

| Arquivo | O que faz |
|---|---|
| `dados/gerar-banco.py` | gera o banco do ensaio randomizado, semente 2026 |
| `dados/gerar-coorte-observacional.py` | gera a coorte observacional, semente 512 |
| `dados/dicionario.md` | dicionário completo de variáveis |
| `analises/analises-do-livro.py` | calcula **todos** os números impressos no livro |
| `analises/resultados.md` | a saída do script acima |
| `CASO-CONDUTOR.md` | o protocolo do estudo fictício |

Como as sementes são fixas, o mesmo comando produz sempre o mesmo banco. Qualquer
número deste livro pode ser conferido rodando o script de análises e comparando
com `resultados.md`, e é essa possibilidade que o Capítulo 7 chama de
reprodutibilidade.

::: nota Por que um livro de estatística usa dados simulados
Por três motivos. Primeiro, ética: dados reais de pacientes não podem ser
distribuídos livremente, e um livro que promete reprodutibilidade precisa
entregar o banco. Segundo, controle didático: o efeito verdadeiro é conhecido, o
que permite mostrar quando um método acerta e quando erra, coisa impossível com
dados reais, em que ninguém sabe a resposta. Terceiro, honestidade: um exemplo
inventado apresentado como real seria pior do que um exemplo inventado
apresentado como tal.
:::

## Exercícios

::: exercicio 1
Abra os dois bancos no jamovi e compare a área inicial mediana entre quem recebeu
e quem não recebeu o tratamento, em cada um. O que a comparação revela?

--- gabarito
No ensaio randomizado, as medianas são próximas, 8,2 cm² no grupo do aspirado e
7,1 cm² no controle, com a pequena diferença que restou sendo obra do acaso da
randomização. Na coorte, são 12,2 cm² contra 6,0 cm², o dobro. Essa única
comparação já explica por que a análise bruta da coorte conclui o contrário da
verdade, e é a maneira mais rápida de diagnosticar confundimento por indicação em
qualquer estudo observacional que você venha a ler.
:::

::: exercicio 2
Rode `analises/analises-do-livro.py` e escolha três números deste livro para
conferir contra `resultados.md`.

--- gabarito
Qualquer três servem, e a experiência é o ponto: em um livro reprodutível,
conferir custa um comando. Se algum número não bater, a explicação será uma de
duas, e ambas são instrutivas: ou o banco foi regerado com parâmetros diferentes,
ou o texto ficou de uma versão anterior da análise, que é exatamente o erro mais
comum descrito no Capítulo 15.
:::

# Dicionário de variáveis — coorte-condutor.csv

Banco do caso condutor do livro *A Estatística na Pesquisa Clínica*.
**Dados simulados**, gerados por `gerar-banco.py` (semente 2026). Não são dados
de pacientes reais.

- **Unidade de observação:** um participante por linha
- **Tamanho:** 200 linhas (100 por grupo), 26 variáveis
- **Codificação:** UTF-8, separador vírgula, ponto como separador decimal
- **Ausentes:** célula vazia

---

## Identificação e alocação

| Variável | Tipo | Valores | Ausentes | Descrição |
|---|---|---|---|---|
| `id` | texto | P001 a P200 | 0 | Código do participante |
| `centro` | nominal | Centro A, Centro B, Centro C | 0 | Centro recrutador |
| `grupo` | nominal | Aspirado, Controle | 0 | Grupo de alocação. Aspirado = aspirado de medula óssea + compressão; Controle = compressão isolada |

## Características da linha de base

| Variável | Tipo | Valores | Ausentes | Descrição |
|---|---|---|---|---|
| `idade` | discreta | 40 a 88 | 0 | Idade em anos completos |
| `sexo` | nominal | Feminino, Masculino | 0 | Sexo |
| `imc` | contínua | 18,0 a 40,6 | 3 | Índice de massa corporal, kg/m². Ausente = não aferido |
| `diabetes` | nominal | Sim, Não | 0 | Diabetes melito em tratamento |
| `tabagismo` | ordinal | Nunca fumou, Ex-fumante, Fumante atual | 0 | Situação tabágica |
| `itb` | contínua | 0,80 a 1,30 | 0 | Índice tornozelo-braquial. Valores abaixo de 0,80 eram critério de exclusão |
| `dor_eva_basal` | discreta | 0 a 10 | 0 | Dor pela escala visual analógica na inclusão |

## Características da úlcera na inclusão

| Variável | Tipo | Valores | Ausentes | Descrição |
|---|---|---|---|---|
| `area_inicial_cm2` | contínua | 0,8 a 66,4 | 0 | Área da úlcera por planimetria, cm². Distribuição assimétrica à direita (mediana 7,6; quartis 4,7 e 12,7) |
| `duracao_ulcera_meses` | discreta | 2 a 72 | 0 | Tempo de existência da úlcera atual, em meses |
| `ulcera_recidivante` | nominal | Sim, Não | 0 | Úlcera recidivante no mesmo membro |
| `tcpo2_basal` | contínua | 15,0 a 55,1 | 12 | Pressão transcutânea de oxigênio periulcerosa, mmHg. Ausente = falha do equipamento. **Teste índice do capítulo de testes diagnósticos** |

## Tratamento e adesão

| Variável | Tipo | Valores | Ausentes | Descrição |
|---|---|---|---|---|
| `adesao_compressao` | nominal | Adequada, Inadequada | 0 | Adesão à terapia compressiva ao longo das 12 semanas. Adequada = uso em pelo menos 80% dos dias |

## Desfechos

| Variável | Tipo | Valores | Ausentes | Descrição |
|---|---|---|---|---|
| `cicatrizacao_12sem` | nominal | Sim, Não | 16 | **Desfecho primário.** Epitelização completa em 12 semanas, mantida por 14 dias, confirmada por avaliador cego. Ausente = perda de seguimento |
| `area_4sem_cm2` | contínua | 0,0 a 62,2 | 6 | Área da úlcera em 4 semanas, cm² |
| `reducao_area_4sem_pct` | contínua | −50,0 a 100,0 | 6 | **Desfecho secundário contínuo principal.** Redução percentual da área em 4 semanas. Valores negativos indicam piora. Sem efeito teto relevante |
| `area_12sem_cm2` | contínua | 0,0 a 55,3 | 16 | Área da úlcera em 12 semanas, cm². Zero em quem cicatrizou |
| `reducao_area_12sem_pct` | contínua | −46,8 a 100,0 | 16 | Redução percentual da área em 12 semanas. **Satura em 100%** na maioria: mediana igual a 100 nos dois grupos |
| `dor_eva_12sem` | discreta | 0 a 8 | 16 | Dor pela escala visual analógica em 12 semanas. Pareia com `dor_eva_basal` |
| `tempo_ate_cicatrizacao_dias` | contínua | 11 a 84 | 0 | **Tempo de seguimento até o evento ou até a censura**, em dias. Sempre preenchido. Deve ser lido junto com `evento_cicatrizacao` |
| `evento_cicatrizacao` | binária | 1, 0 | 0 | 1 = a úlcera cicatrizou na data acima; 0 = observação censurada (perda de seguimento ou fim das 12 semanas sem cicatrização) |

## Segurança e seguimento

| Variável | Tipo | Valores | Ausentes | Descrição |
|---|---|---|---|---|
| `perda_seguimento` | nominal | Sim, Não | 0 | Perda de seguimento antes das 12 semanas (16 casos, 8 por grupo) |
| `infeccao_ferida` | nominal | Sim, Não | 0 | Infecção da ferida durante o seguimento. Evento pouco frequente |
| `dor_sitio_puncao` | nominal | Sim, Não | 100 | Dor no sítio de punção medular. **Ausência estrutural**: a variável não existe para quem não recebeu o aspirado. Não é dado faltante e não deve ser imputada |

---

## Advertências de uso

**Tempo até evento.** `tempo_ate_cicatrizacao_dias` isolada não significa nada:
84 dias pode ser uma úlcera que não cicatrizou ou uma que cicatrizou no último
dia. É sempre lida com `evento_cicatrizacao`. Esse par é a matéria-prima do
capítulo de sobrevida e a armadilha mais comum do tema.

**Faltantes.** Existem três naturezas diferentes de ausência neste banco, e o
livro as distingue: falha de aferição (`imc`, `tcpo2_basal`), perda de
seguimento (`cicatrizacao_12sem` e os demais desfechos de 12 semanas) e ausência
estrutural (`dor_sitio_puncao`). Só a segunda ameaça a validade do resultado
principal, e é ela que motiva a análise por intenção de tratar.

**Efeito teto.** `reducao_area_12sem_pct` tem mediana 100 nos dois grupos.
Aplicar um teste t nela e concluir que "não houve diferença" é o erro que o
capítulo de estatística descritiva usa como exemplo.

**Reprodutibilidade.** Qualquer alteração no banco se faz editando
`gerar-banco.py` e regerando o arquivo, nunca editando o CSV à mão. A semente
2026 garante que o mesmo comando produz sempre o mesmo banco, e é o que permite
ao leitor conferir cada número impresso no livro.

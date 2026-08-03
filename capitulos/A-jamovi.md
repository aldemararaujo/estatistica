::: caso
Todas as análises deste livro foram feitas no jamovi. Este apêndice existe para
que quem nunca o abriu consiga chegar ao fim do Capítulo 8 sem travar na terceira
tela.
:::

## Por que jamovi

É gratuito e de código aberto. Funciona por cliques, sem programação. Roda em
Windows, macOS e Linux. Atualiza os resultados sozinho quando os dados mudam. E
guarda dados, análises e resultados em um único arquivo, o que resolve boa parte
do problema de reprodutibilidade do Capítulo 7.

Por baixo dele roda o R, o que significa que quem quiser migrar depois não estará
começando do zero, e que quem precisar de algo que o menu não oferece pode
instalar o módulo **Rj** e escrever código dentro do próprio programa.

## Instalar

1. Vá a [jamovi.org](https://www.jamovi.org/) e baixe a versão **solid**, que é a
   estável. A versão *current* traz novidades e também instabilidades.
2. Instale normalmente. Não requer licença, cadastro nem conexão permanente.
3. Anote a versão instalada. Ela precisa constar dos métodos do seu artigo, e é o
   que permite a alguém reproduzir suas telas anos depois.

## A tela, em três partes

**Aba Data.** A planilha. É aqui que se importa, se confere e se transforma.

**Aba Analyses.** Os menus de análise, agrupados por família: Exploration,
T-Tests, ANOVA, Regression, Frequencies, Factor.

**Painel de resultados**, à direita. Cada análise pedida aparece ali e permanece.
Clicar no resultado reabre as opções que o geraram, o que é a maior vantagem do
programa: nada é uma saída morta, tudo continua editável.

## As oito operações que resolvem o livro inteiro

**1. Importar.** Menu ☰, **Open**, **Browse**. Ele lê CSV, XLSX, SAV do SPSS,
RData e outros. Para o banco deste livro, escolha `coorte-condutor.csv`.

**2. Conferir os tipos.** Aba **Data**, botão **Setup**. Três ícones: régua para
contínua, barras para ordinal, círculos para nominal. Corrija o que o programa
adivinhou errado, e ele erra com frequência em variáveis codificadas 0 e 1.

**3. Ordenar categorias.** Ainda em Setup, no painel **Levels**, arraste as
categorias para a ordem que fizer sentido clínico. Isso define também a categoria
de referência das regressões, o que muda a interpretação de toda razão de
chances.

**4. Criar variáveis.** Aba **Data**, botão **Compute**. Exemplos usados no livro:

| Objetivo | Fórmula |
|---|---|
| Logaritmo da área | `LN(area_inicial_cm2)` |
| Corte de 40% em 4 semanas | `IF(reducao_area_4sem_pct >= 40, "Positivo", "Negativo")` |
| Variação da dor | `dor_eva_basal - dor_eva_12sem` |
| Número aleatório para sorteio | `UNIF(0, 1)` |

**5. Filtrar.** Aba **Data**, botão **Filters**. Escreva a condição, por exemplo
`grupo == "Aspirado"`. O filtro é **reversível**: pode ser desligado a qualquer
momento, ao contrário de apagar linhas, que é irreversível e proibido pelo
Capítulo 7.

**6. Analisar.** Aba **Analyses**. O mapa dos menus:

| O que você quer | Onde está |
|---|---|
| Descrever variáveis, histogramas, boxplots | Exploration, Descriptives |
| Tabela de contingência, qui-quadrado, Fisher | Frequencies, Independent Samples |
| McNemar | Frequencies, Paired Samples |
| Intervalo de confiança de uma proporção | Frequencies, 2 Outcomes |
| Teste t, Welch, Mann-Whitney | T-Tests, Independent Samples |
| t pareado, Wilcoxon | T-Tests, Paired Samples |
| ANOVA, Kruskal-Wallis | ANOVA, One-Way ANOVA |
| Correlação de Pearson e Spearman | Regression, Correlation Matrix |
| Regressão linear | Regression, Linear Regression |
| Regressão logística | Regression, 2 Outcomes (Binomial) |

**7. Instalar módulos.** Ícone **+**, no canto superior direito, **jamovi
library**. Três módulos são usados neste livro:

| Módulo | Para quê | Capítulo |
|---|---|---|
| jpower | cálculo do tamanho da amostra e curvas de poder | 6 |
| um módulo de ROC | curva ROC e área sob a curva | 13 |
| um módulo de sobrevida (Death Watch e similares) | Kaplan-Meier, log-rank, Cox | 14 |

A biblioteca muda com o tempo, e nomes de módulos aparecem e desaparecem.
Procure pelo assunto, e não pelo nome exato citado aqui.

**8. Salvar e exportar.** Salve sempre como **.omv**, que guarda dados, análises
e resultados. Para o manuscrito, clique com o botão direito em qualquer tabela e
escolha copiar, ou use **Export** para gerar PDF ou HTML de todos os resultados.

## Cinco armadilhas do jamovi

**Tipo errado de variável.** É a causa da maioria dos resultados absurdos. O
programa não avisa: ele calcula.

**Categoria de referência invertida.** Se a referência de `grupo` for "Aspirado",
as razões de chances virão de cabeça para baixo. Confira sempre em Reference
Levels.

**Decimais em excesso.** O padrão do programa é generoso demais para pesquisa
clínica. Ajuste em Preferences, ou arredonde ao transcrever, conforme o Capítulo
8.

**Separador decimal.** Bancos gerados em português usam vírgula, e o jamovi
espera ponto. Se uma coluna numérica for importada como texto, é quase sempre
isso. O banco deste livro já vem com ponto.

**Análise que some.** Se você apagar a análise do painel de resultados, ela se
vai. Prefira desmarcar opções a excluir a análise inteira.

## Exercícios

::: exercicio 1
Instale o jamovi, importe `coorte-condutor.csv` e corrija o tipo de
`evento_cicatrizacao`. Quantas variáveis o programa classificou errado?

--- gabarito
A mais evidente é `evento_cicatrizacao`, importada como contínua por estar
codificada em 0 e 1, e que deve ser nominal. Dependendo da versão, `dor_eva_basal`
e `dor_eva_12sem` podem vir como contínuas, e a decisão de tratá-las como ordinais
ou contínuas deve ser tomada e justificada, conforme o Capítulo 4. O exercício
importa menos pelo número exato e mais pelo hábito: conferir tipos antes de
qualquer análise.
:::

::: exercicio 2
Crie a variável `log_area` e um filtro que selecione apenas participantes com
área inicial acima de 10 cm². Quantos restam?

--- gabarito
A fórmula é `LN(area_inicial_cm2)` em Compute, e o filtro é
`area_inicial_cm2 > 10` em Filters. Restam pouco mais de sessenta participantes,
já que o terceiro quartil da área é 12,7 cm². O número exato aparece no rodapé da
planilha, que mostra quantas linhas o filtro manteve, e conferir esse rodapé é
uma boa prática antes de qualquer análise filtrada.
:::

## Recursos

- [jamovi.org](https://www.jamovi.org/) — download e documentação.
- [jamovi library](https://library.jamovi.org/) — módulos adicionais.
- [jamovi user guide](https://www.jamovi.org/user-manual.html) — manual oficial.

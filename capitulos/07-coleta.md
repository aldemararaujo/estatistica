::: caso
O estudo vai gerar 200 fichas, cada uma com dezenas de campos, preenchidas em
três centros ao longo de dois anos, por pessoas diferentes. Entre a última
consulta e a análise estatística existe uma etapa que nenhum manual de
bioestatística ensina e que determina se o estudo será analisável: transformar
papel em banco de dados.
:::

## O banco é um ativo, não um rascunho

Um banco de dados bem-feito sobrevive ao estudo. Ele permite reanálise, permite
metanálise, permite responder à pergunta do revisor três meses depois e permite
que outra pessoa confira o que você fez. Um banco malfeito obriga a refazer
digitação, gera resultados que não batem entre si e, em muitos casos, inviabiliza
qualquer conferência.

A regra que organiza tudo é uma só:

> **Uma linha por participante, uma coluna por variável, uma informação por
> célula.**

Parece óbvio e é violado o tempo inteiro.

## Os erros que destroem bancos

**Uma coluna com duas informações.** "PA: 140/90" precisa virar duas colunas,
sistólica e diastólica. "Diabetes tipo 2 há 8 anos" vira três: presença, tipo e
duração.

**Células mescladas.** O Excel permite; nenhum programa estatístico consegue ler.

**Cor como dado.** Pintar de amarelo os pacientes que abandonaram parece
prático. A cor não é exportada, e a informação desaparece na importação. Se é
informação, é coluna.

**Texto em coluna numérica.** Um único "não realizado" no meio de mil números faz
o programa importar a coluna inteira como texto, e nenhuma média será calculada.
Ausente se registra deixando a célula **vazia**.

**Códigos numéricos para ausente.** O clássico 999, ou pior, o 0. Se ninguém
recodificar antes da análise, entram na média e produzem resultados absurdos, e o
erro passa despercebido quando o valor é plausível.

**Datas.** A maior fonte de dor silenciosa. O Excel converte para o formato
regional da máquina, e 03/04 significa 3 de abril em uma e 4 de março em outra.
Grave datas no formato AAAA-MM-DD, que ordena corretamente como texto e não
admite ambiguidade.

**Nomes de coluna com espaço, acento e caractere especial.** Use minúsculas, sem
acento, com sublinhado: `area_inicial_cm2`. É feio e funciona em qualquer
programa, hoje e daqui a dez anos.

**Nome do paciente na planilha de análise.** Além de desnecessário, viola a Lei
Geral de Proteção de Dados. Identificação e dados de pesquisa vivem em arquivos
separados, ligados por um código.

::: atencao Codificar ausente com 0 é o erro mais perigoso da lista
Os demais erros estragam a análise de maneira visível: o programa recusa a
importação, a coluna não calcula, a data sai errada. O 0 no lugar de ausente
produz um resultado plausível e falso. Uma área de úlcera registrada como 0
porque não foi medida entra na média e a puxa para baixo, e ninguém percebe. Se o
dado não existe, a célula fica vazia.
:::

## O dicionário de variáveis

Todo banco precisa de um documento que descreva cada coluna: nome, tipo, unidade,
valores possíveis, o que significa ausente e como a variável foi aferida. O deste
estudo está em `dados/dicionario.md`.

Ele custa uma tarde e resolve três problemas: permite que outra pessoa use o
banco, permite que **você** o use daqui a dois anos, e obriga a tomar decisões de
codificação antes da coleta, quando ainda dá tempo de mudar a ficha.

| Elemento | Exemplo |
|---|---|
| Nome | `reducao_area_4sem_pct` |
| Tipo | contínua |
| Unidade | pontos percentuais |
| Faixa válida | −50 a 100 |
| Ausentes | célula vazia, quando houve perda antes da quarta semana |
| Aferição | planimetria fotográfica por avaliador cego |

## As três naturezas do dado ausente

O banco deste estudo tem ausências de três tipos, e o Capítulo 12 depende de
distingui-las:

**Falha de aferição.** O TcPO₂ tem 12 valores ausentes por falha do equipamento.
A ausência não tem relação com o desfecho, e o impacto é apenas perda de
precisão.

**Perda de seguimento.** Dezesseis participantes saíram antes das doze semanas, e
com eles se foram todos os desfechos finais. Esta é a ausência que ameaça a
validade, porque pode se relacionar ao próprio desfecho: quem não melhora tende a
abandonar mais.

**Ausência estrutural.** A dor no sítio de punção não existe para quem não
recebeu o aspirado. Não é dado faltante, é uma pergunta que não se aplica, e
imputá-la seria inventar dado.

A conduta padrão diante das perdas é a **análise por intenção de tratar**:
analisar cada participante no grupo em que foi alocado, independentemente do que
recebeu, e declarar explicitamente como os faltantes foram tratados. A análise
principal costuma ser acompanhada de análises de sensibilidade, como a que
considera todas as perdas como não cicatrizadas, para mostrar que a conclusão não
depende de uma suposição conveniente.

## Coleta: papel, planilha ou sistema

| Meio | Quando serve | Risco principal |
|---|---|---|
| Ficha em papel, digitada depois | estudo pequeno, sem infraestrutura | erro de digitação, ficha perdida |
| Planilha preenchida direto | estudo pequeno, um único centro | ausência de validação, versões paralelas do arquivo |
| Sistema eletrônico (REDCap e similares) | multicêntrico, ou com dados sensíveis | curva de aprendizado, exige configuração inicial |

Para um estudo multicêntrico como este, o sistema eletrônico é a escolha certa:
ele valida faixas na hora da digitação, registra quem digitou o quê e quando,
impede campos obrigatórios em branco e elimina a etapa de transcrição. O REDCap é
gratuito para instituições acadêmicas e é hoje o padrão em pesquisa clínica.

Se a coleta for em papel, a proteção clássica é a **dupla digitação**: duas
pessoas digitam o mesmo material de forma independente e um programa compara as
duas versões. É trabalhoso e detecta erros que nenhuma conferência visual pega.

## Reprodutibilidade, que é o assunto verdadeiro deste capítulo

Reprodutível é o estudo cujos resultados podem ser regerados por outra pessoa a
partir dos dados originais. Não é um ideal abstrato: é a diferença entre
conseguir e não conseguir responder ao revisor que pede uma análise adicional.

**Não altere o banco bruto.** Ele se preserva como veio, e as correções vivem em
um script ou em um registro de alterações. Corrigir a mão, no arquivo original,
apaga a história e impede a conferência.

**Registre as decisões de limpeza.** Quantos valores foram corrigidos, quais e
por quê.

**Automatize o que puder.** Este livro pratica o que prega: todos os números
impressos aqui saem de `analises/analises-do-livro.py`, que lê o banco e escreve
`analises/resultados.md`. Se o banco mudar, basta rodar de novo, e nenhum
capítulo fica desatualizado sem que se perceba.

**Use semente fixa quando houver sorteio.** O banco deste estudo é simulado, e a
semente 2026 garante que o mesmo comando produza sempre o mesmo arquivo.

**Faça cópias de segurança em três lugares**, sendo um fora do prédio. Disco
rígido único é questão de tempo.

**Publique o banco anonimizado**, sempre que a ética permitir. Além de correto, é
o que dá ao seu trabalho a chance de ser usado por outros e citado por eles.

::: nota A LGPD em três frases
Dado de pesquisa em saúde é dado pessoal sensível. Ele exige consentimento
específico, finalidade declarada e medidas de proteção proporcionais ao risco.
Na prática, isso significa três coisas: separe a identificação dos dados de
pesquisa, guarde a chave que liga os dois em local restrito e sob
responsabilidade nominal, e publique apenas o banco anonimizado, do qual não seja
possível reidentificar ninguém, o que exige atenção especial em variáveis raras,
como idade acima de noventa anos ou doenças de baixa prevalência.
:::

::: jamovi
1. Importe o CSV em **Open**, **Browse**. O jamovi lê CSV, XLSX, SAV, RData e
   outros formatos.
2. Confira **todos** os tipos em **Setup**, como visto no Capítulo 4.
3. Verifique valores absurdos antes de qualquer análise: rode **Descriptives**
   com **Minimum** e **Maximum** para todas as variáveis numéricas de uma vez.
   Idade de 180 anos, área de úlcera negativa e índice tornozelo-braquial de 12
   aparecem imediatamente.
4. Use **Filters** para excluir casos de forma **reversível**, em vez de apagar
   linhas. O filtro fica registrado no arquivo e pode ser desligado; a linha
   apagada não volta.
5. Salve o trabalho como arquivo `.omv`. Ele guarda dados, análises e resultados
   juntos, e é o que permite reabrir o estudo meses depois e ver exatamente o que
   foi feito, o que é a versão jamovi da reprodutibilidade.
:::

::: revisor
**"Não está descrito como os dados foram coletados e conferidos."** Um parágrafo
nos métodos: instrumento, quem preencheu, como foi digitado, que validações
houve.

**"Não há informação sobre dados faltantes."** Quantos, em quais variáveis, e
como foram tratados na análise.

**"Os autores excluíram participantes com dados faltantes sem discutir o
impacto."** A análise de casos completos supõe que a ausência é aleatória, o que
raramente se verifica. Apresente análise de sensibilidade.

**"O estudo não menciona aprovação ética nem consentimento."** Número do parecer
e comitê.

**"Os dados não estão disponíveis e não há justificativa."** Muitas revistas hoje
exigem declaração de disponibilidade de dados. "Disponíveis mediante solicitação
razoável" é aceito, e cobrado.

**"O número de participantes difere entre tabelas sem explicação."** Cada tabela
deve dizer sobre quantos casos foi calculada.
:::

::: quiz
? [facil] Qual a regra que organiza um banco de dados de pesquisa?
+ Uma linha por participante, uma coluna por variável, uma informação por célula. | Correto. Parece óbvia e é violada o tempo inteiro, com pressão arterial em uma célula só, cores com significado e células mescladas.
- Uma linha por variável e uma coluna por participante. | É a transposição do formato correto, e nenhum programa estatístico a lê diretamente.
- Uma planilha por participante, reunidas em uma pasta. | Inviabiliza qualquer análise e multiplica o risco de perda.
- Uma linha por consulta, com o participante repetido. | É o formato longo, útil em medidas repetidas, e ainda assim exige identificador e estrutura declarada; a regra geral do capítulo é uma linha por participante.
- Uma planilha por variável, ligadas por fórmulas. | Fragmenta o banco e torna a conferência impossível.
@ cap-7-o-banco-e-um-ativo-nao-um-rascunho

? [facil] Como se registra um dado que não foi coletado?
+ Deixando a célula vazia. | Correto. Códigos numéricos entram nos cálculos se ninguém os recodificar, e o texto no meio de uma coluna numérica faz o programa importar tudo como texto.
- Com o código 999. | É o erro clássico: 999 é um número e será tratado como tal, distorcendo médias e modelos.
- Com o valor 0. | É o mais perigoso de todos, porque produz um resultado plausível e falso, que ninguém percebe.
- Com a palavra "ausente" na célula. | Texto em coluna numérica faz o programa importar a coluna inteira como texto.
- Com um traço ou hífen. | Mesmo problema do texto: contamina o tipo da coluna.
@ cap-7-os-erros-que-destroem-bancos

? [media] O banco do caso condutor tem três naturezas diferentes de dado ausente. Qual delas ameaça a validade do resultado principal?
+ A perda de seguimento, porque pode se relacionar ao próprio desfecho. | Correto. Quem não melhora tende a abandonar mais, e é por isso que ela motiva a análise por intenção de tratar e as análises de sensibilidade.
- A falha de aferição do TcPO₂ por defeito do equipamento. | Não tem relação com o desfecho e custa apenas precisão.
- A ausência estrutural da dor no sítio de punção no grupo controle. | Não é dado faltante: é pergunta que não se aplica, e imputá-la seria inventar dado.
- A falta do índice de massa corporal em três participantes. | Falha de aferição pontual, sem relação com o desfecho.
- Todas ameaçam igualmente. | Elas têm consequências diferentes, e distingui-las é justamente o que o capítulo ensina.
@ cap-7-as-tres-naturezas-do-dado-ausente

? [media] Por que o banco bruto nunca deve ser editado à mão?
+ Porque a edição manual não deixa rastro, e meses depois ninguém sabe se o valor era assim na ficha ou se foi corrigido, por quem e por quê. | Correto. Banco bruto preservado mais script de limpeza permitem reconstruir o banco analítico e mostram a cadeia inteira de decisões. É a mesma lógica do prontuário: não se apaga, acrescenta-se.
- Porque programas estatísticos não conseguem ler arquivos editados. | Leem normalmente; o problema é de rastreabilidade, não de formato.
- Porque a edição manual sempre introduz erros de digitação. | Pode introduzir, e o argumento central é a impossibilidade de auditar depois.
- Porque a LGPD proíbe alterar dados de pesquisa. | A lei trata de proteção de dados pessoais, e não de metodologia de limpeza.
- Porque o banco bruto é propriedade do comitê de ética. | Não é, e a razão para preservá-lo é metodológica.
@ cap-7-reprodutibilidade-que-e-o-assunto-verdadeiro-deste-capitulo

? [media] Qual formato de data evita ambiguidade entre sistemas?
+ AAAA-MM-DD, que ordena corretamente como texto e não admite leitura dupla. | Correto. É a maior fonte de dor silenciosa em bancos: 03/04 significa 3 de abril em uma máquina e 4 de março em outra.
- DD/MM/AAAA, o formato usado no Brasil. | É ambíguo quando o arquivo circula entre máquinas com configurações regionais diferentes.
- MM/DD/AAAA, o formato internacional. | É o formato americano, e é justamente o que gera o conflito com o brasileiro.
- O formato que o Excel sugerir automaticamente. | O programa sugere conforme a configuração da máquina, que é exatamente o problema.
- Data por extenso, como "3 de abril de 2026". | Não ambíguo, e impossível de ordenar e calcular sem conversão.
@ cap-7-os-erros-que-destroem-bancos

? [dificil] Um estudo perdeu 16 participantes, oito em cada grupo. Por que o equilíbrio no número não basta para descartar viés?
+ Porque perdas equilibradas em número podem ser desequilibradas em natureza: os motivos de abandono podem diferir entre os grupos. | Correto. Se no grupo tratado abandonaram os que não melhoravam e no controle os que melhoraram cedo, o viés existe apesar do equilíbrio numérico. Por isso se comparam as características basais dos perdidos.
- Porque dezesseis perdas são muitas para um estudo de duzentos participantes. | Oito por cento está dentro do previsto no protocolo e não é, em si, um problema.
- Porque o cálculo do tamanho da amostra não previa perdas. | Previa 10%, e o observado ficou abaixo disso.
- Porque a análise por intenção de tratar exige que não haja perdas. | Ela existe justamente para lidar com elas, e não pressupõe ausência.
- Porque perdas sempre invalidam um ensaio clínico. | Não invalidam: exigem descrição, comparação dos perdidos e análise de sensibilidade.
@ cap-7-as-tres-naturezas-do-dado-ausente

? [dificil] O que caracteriza um estudo reprodutível, na definição deste capítulo?
+ Outra pessoa consegue regerar os resultados a partir dos dados originais. | Correto. Não é ideal abstrato: é a diferença entre conseguir e não conseguir responder ao revisor que pede uma análise adicional.
- Outro grupo consegue repetir o estudo e obter o mesmo resultado. | Isso é replicação, que é diferente e depende de um novo estudo com novos participantes.
- Os resultados são publicados em revista de acesso aberto. | Acesso aberto facilita a leitura, e não garante que alguém consiga refazer as contas.
- O banco de dados foi aprovado pelo comitê de ética. | Aprovação ética é obrigatória e não diz nada sobre reprodutibilidade.
- As análises foram conferidas por um estatístico. | Conferência ajuda, e reprodutibilidade significa que qualquer pessoa, com os dados, chega ao mesmo número.
@ cap-7-reprodutibilidade-que-e-o-assunto-verdadeiro-deste-capitulo
:::

## Exercícios

::: exercicio 1
Uma planilha traz a coluna "PA" com valores como "140/90", "150 x 100" e
"hipertenso". Descreva como reorganizá-la.

--- gabarito
Criar duas colunas numéricas, `pa_sistolica` e `pa_diastolica`, ambas em mmHg, e
converter os registros que tiverem os dois valores. "Hipertenso" não é uma
medida de pressão e não pode ser convertido: as duas células ficam vazias, e a
informação, se relevante, vai para uma terceira coluna nominal, `hipertensao`,
com Sim e Não. Convém ainda registrar quantos casos precisaram desse tratamento,
para constar do relato de limpeza.
:::

::: exercicio 2
Por que registrar ausente como 999 é perigoso, e o que fazer no lugar?

--- gabarito
Porque 999 é um número, e todo programa o tratará como tal se ninguém o
recodificar. Ele entra em médias, desvios padrão e regressões, distorcendo tudo,
e o erro é difícil de perceber quando a variável tem faixa ampla. A conduta é
deixar a célula vazia. Se for indispensável distinguir motivos de ausência, crie
uma coluna adicional com o motivo, em texto ou código, mantendo a coluna do valor
vazia.
:::

::: exercicio 3
O estudo teve 16 perdas de seguimento, 8 em cada grupo. Por que o equilíbrio
entre os grupos é tranquilizador, mas não suficiente?

--- gabarito
É tranquilizador porque perdas desiguais sugeririam que o próprio tratamento
influenciou o abandono, o que quebraria a comparabilidade obtida pela
randomização. Não é suficiente porque perdas equilibradas em número podem ser
desequilibradas em natureza: se no grupo tratado abandonaram os que não
melhoravam e no controle abandonaram os que melhoraram cedo, o viés existe apesar
do equilíbrio numérico. Por isso se comparam as características basais dos
perdidos e se fazem análises de sensibilidade.
:::

::: exercicio 4
Explique por que este livro insiste que o banco bruto nunca seja editado à mão.

--- gabarito
Porque a edição manual não deixa rastro. Seis meses depois, ninguém sabe se
aquele valor era assim na ficha ou se foi corrigido, nem por quem, nem por quê. O
banco bruto preservado mais um script de limpeza permitem reconstruir o banco
analítico a qualquer momento e mostram a cadeia inteira de decisões. É a mesma
lógica do prontuário: não se apaga, acrescenta-se.
:::

::: exercicio 5
Abra o banco no jamovi e rode Descriptives com mínimo e máximo para todas as
variáveis numéricas. Alguma delas tem valores implausíveis?

--- gabarito
Não deve haver, porque o banco foi gerado com limites fisiológicos. O que se
encontra são valores extremos legítimos, como área de úlcera de 66,4 cm² e
redução de área de −50%, que representam piora. A distinção entre valor extremo e
valor errado é clínica, não estatística: 66,4 cm² é uma úlcera enorme e possível;
uma área de 6.640 cm² seria erro de digitação. É por isso que a conferência
precisa ser feita por quem conhece a doença.
:::

::: exercicio 6
Escreva o parágrafo de métodos que descreve a coleta e o gerenciamento dos dados
deste estudo, com o que você aprendeu no capítulo.

--- gabarito
Um exemplo aceitável: "Os dados foram coletados em formulário eletrônico
padronizado, preenchido pelo pesquisador de cada centro durante a consulta, com
validação automática de faixas e campos obrigatórios. A área da úlcera foi
aferida por planimetria em fotografia digital, avaliada por pesquisador cego para
a alocação. Os dados foram armazenados em servidor institucional com acesso
restrito, e a identificação dos participantes foi mantida em arquivo separado,
ligado ao banco de pesquisa apenas por código numérico. Dados faltantes foram
mantidos como células vazias e sua distribuição está descrita nos resultados. A
análise foi conduzida por intenção de tratar, com análises de sensibilidade
descritas adiante. O banco anonimizado está disponível mediante solicitação ao
autor correspondente."
:::

::: agora
1. Escreva o dicionário de variáveis do seu estudo **antes** da primeira coleta.
   Uma tarde agora poupa semanas depois, e obriga decisões de codificação
   enquanto ainda dá tempo de mudar a ficha.
2. Defina onde ficam a identificação dos participantes e os dados de pesquisa,
   em arquivos separados, e quem guarda a chave que liga os dois.
3. Estabeleça três cópias de segurança, sendo uma fora do prédio, e teste a
   restauração de uma delas hoje.
4. Se ainda não coletou nada, avalie usar um sistema eletrônico de captura. A
   configuração custa alguns dias e elimina a etapa de digitação, que é onde os
   erros nascem.
:::

## Recursos

- [REDCap](https://projectredcap.org/) — sistema gratuito de captura de dados de
  pesquisa para instituições acadêmicas.
- [CONSORT Statement](https://www.consort-statement.org/) — itens sobre dados
  faltantes e análise por intenção de tratar.
- [jamovi](https://www.jamovi.org/) — o arquivo `.omv` guarda dados e análises
  juntos.

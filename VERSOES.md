# Histórico de versões

O livro é uma obra viva: corrige-se, amplia-se e é republicado no mesmo
endereço. Este arquivo registra o que mudou em cada versão, para que quem citou
uma versão anterior saiba o que era diferente.

## Como a numeração funciona

O número tem duas partes, no formato **maior.menor**.

- O **primeiro** número muda quando a estrutura da obra muda: capítulos novos,
  reescrita de partes inteiras, alteração do caso condutor ou da pergunta de
  pesquisa. Quem citou a versão anterior precisa conferir se ainda vale.
- O **segundo** muda com acréscimos e correções que não alteram a arquitetura:
  novas seções, exercícios, recursos de leitura, ajustes de texto, correção de
  erratas e de links.

A data de construção acompanha o número na ficha e no rodapé do sumário, porque
duas construções da mesma versão podem diferir em detalhes de data e de links.

---

## Versão 1.4 — 04/08/2026

**O quiz deixa de ser decorável**

- O bloco de perguntas de cada capítulo passa a ser um **banco**, e não uma lista
  fixa. O navegador sorteia sete a cada tentativa, respeitando a proporção de
  níveis do banco e preferindo as perguntas que aquele leitor ainda não viu.
- As cinco alternativas **trocam de lugar a cada tentativa**, e as letras são
  escritas depois do sorteio. Antes, a posição da resposta certa era fixada na
  construção, por rodízio: quem refazia o quiz decorava a letra antes de decorar
  a resposta.
- Com os sete atuais, o leitor recebe as mesmas sete em ordem sempre nova, com
  as alternativas sempre em posições diferentes. Ampliar o banco de um capítulo
  é acrescentar perguntas ao mesmo bloco, sem tocar em código: um banco de 21,
  em 6 fáceis, 9 intermediárias e 6 difíceis, entrega três rodadas inteiras sem
  repetir uma única pergunta.
- O sorteio em curso fica guardado, e recarregar a página no meio do quiz não
  troca as perguntas de quem está respondendo. Destacar um termo pela busca
  também deixou de apagar as respostas já dadas.
- "Refazer o quiz" passa a sortear rodada nova. "Refazer só as que errei"
  mantém as mesmas perguntas de propósito, e apenas reembaralha as alternativas.
- Zerar o progresso limpa também a memória do que já caiu. O arquivo de
  progresso exportado passa à versão 2 e carrega essa memória, para que trocar
  de computador não devolva as mesmas sete; arquivo da versão 1 continua sendo
  aceito.
- A identidade de cada pergunta vem do enunciado, e não da posição no bloco:
  acrescentar ou reordenar perguntas não apaga a memória das outras.

---

## Versão 1.3 — 04/08/2026

**Apêndice E, Referências comentadas**

- Apêndice novo, com quarenta e seis obras comentadas em quatorze seções,
  agrupadas pelo assunto do capítulo a que servem, e não por ordem alfabética.
- Nove livros de cabeceira: Fletcher, Hulley, Greenhalgh, Altman (dois),
  Pocock, Lwanga e Lemeshow, o manual da Cochrane e Rothman. Os três com edição
  brasileira trazem o registro da Biblioteca Virtual em Saúde ao lado do
  original.
- Seções novas de leitura para os Capítulos 1, 4 e 7, que não tinham nenhuma.
- Nota explicando que o *Cochrane Reviewers' Handbook* e o *Cochrane Handbook
  for Systematic Reviews of Interventions* são a mesma obra, com o nome que
  mudou na versão 4.2.4, de março de 2005, e a advertência de que a seção sobre
  risco de viés foi reescrita depois disso.

**Dados abertos**

- Os bancos e os scripts passam a ter link. A promessa de reprodutibilidade
  existia desde a versão 1.0, mas nenhuma página oferecia o arquivo: agora o
  Apêndice D linka os dois CSV, o dicionário, os geradores, o script de análises
  e o protocolo do estudo.
- Correção: a coorte observacional tem 14 variáveis, e não 12, como dizia o
  Apêndice D.

**Endereços**

- Dois encurtadores retirados da capa. O link do Google Acadêmico passava por
  `bit.ly` e depois por `goo.gl`, ambos em desativação, para chegar a uma página
  que nunca mudou de lugar. O Lattes passou de `http` para `https`.
- Reverificação completa: 43 DOIs contra a Crossref e 52 endereços na rede,
  nenhum quebrado e nenhum DOI inválido. A data da conferência passa a aparecer
  no quadro "O livro em números", que antes prometia data e não mostrava
  nenhuma.

**Leitura e acesso**

- Ficha `schema.org/Book` em JSON-LD, com autor, ORCID, licença, versão e os
  capítulos, para que buscadores e agregadores acadêmicos tratem a página como
  livro.
- Placar do quiz, contador de exercícios, saída das calculadoras e resultados da
  busca passam a ser anunciados por leitor de tela.
- A página respeita quem pede menos movimento no sistema, e ganha ícone próprio
  na aba do navegador, embutido e sem requisição externa.

---

## Versão 1.2 — 03/08/2026

**Figuras**

- Quatro figuras em SVG substituem a arte em caracteres: o fluxograma de escolha
  do teste e o de como descrever uma variável, no Apêndice B; o diagrama CONSORT
  do estudo, no Capítulo 15; e o esquema das três populações, no Capítulo 5.
- SVG embutido, e não imagem: as figuras herdam as cores do tema claro e escuro,
  o texto delas continua encontrável pela busca do livro e legível por leitor de
  tela, e as quatro juntas somam poucos quilobytes.

**Divulgação**

- Imagem de compartilhamento, criada no Canva e publicada como
  `compartilhar.png`, com as marcações Open Graph e Twitter Card. Quem manda o
  endereço do livro por mensagem passa a ver capa, título e descrição.

---

## Versão 1.1 — 03/08/2026

**Conteúdo**

- Capítulo 5 ampliado: amostragem por cotas e sua diferença em relação à
  estratificada, saturação teórica, marco amostral, distinção entre técnica e
  tamanho de amostra, simulador de amostragem do autor e quatro referências de
  aprofundamento.
- Todos os acrônimos em inglês passam a ser abertos na primeira aparição, com
  tabela completa no Apêndice C. Removida a variante PIRO, que não se sustenta
  como estrutura de pergunta.
- Estrangeirismos em itálico em toda a obra, com quatro exceções documentadas.
- Bloco "O que fazer agora, no seu projeto" em cada capítulo.
- O card de erros passa a se chamar "Aqui é onde o artigo é rejeitado", e a
  apresentação explica o que é revisão por pares.
- Quiz de sete perguntas em cada capítulo: 112 perguntas, 560 comentários.
- Quadro "O livro em números" na abertura.

**Correções**

- Quartil da área inicial na Tabela 1 do Capítulo 8: 14,6 cm², e não 14,7.
- Intervalo de Wilson do exercício 4 do Capítulo 9: 5,5% a 17,4%.
- Link quebrado do módulo do jamovi substituído por `library.jamovi.org`.
- Pergunta de pesquisa reformulada como pergunta de estimação, com o objetivo
  geral passando de "comparar" para "estimar" e a hipótese nula para "a
  diferença de proporção é zero".

**Leitura**

- Marcador do que já foi lido, com percentual ponderado pelo tamanho de cada
  capítulo, tempo estimado de leitura e retomada de onde parou.
- Busca no texto completo, indiferente a acentos, com destaque das ocorrências.
- Índice interno por capítulo e endereço permanente para cada seção.
- Citação pronta em ABNT e Vancouver, e link para reportar erro.
- Calculadoras nos Capítulos 6, 9 e 13.
- Progresso exportável em arquivo e exercícios marcáveis como resolvidos.
- Glossário com definição ao passar o cursor.

## Versão 1.0 — 03/08/2026

Primeira versão completa: dezesseis capítulos e quatro apêndices, com o caso
condutor, os bancos de dados simulados e o script que reproduz todos os números
impressos na obra.

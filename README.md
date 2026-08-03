# A Estatística na Pesquisa Clínica

**do problema clínico à decisão estatística**

Aldemar Araujo Castro · Maceió, AL
[Currículo Lattes](http://lattes.cnpq.br/2259022333178681)

**Leia o livro:** https://aldemararaujo.github.io/estatistica/

Livro de acesso aberto sobre estatística aplicada à pesquisa com seres humanos,
escrito para o pós-graduando, o residente e o profissional de saúde que precisa
planejar, executar e publicar um estudo próprio, e que não tem formação
matemática formal.

Dezesseis capítulos e quatro apêndices, organizados na ordem das decisões reais
de um projeto: da dúvida clínica ao artigo submetido. Todas as análises são
feitas no [jamovi](https://www.jamovi.org/), que é gratuito e funciona por
cliques.

## O que este repositório contém

O livro é **uma única página HTML**, com CSS e JavaScript embutidos: abre com
dois cliques, funciona sem internet e não depende de servidor.

| Arquivo | Conteúdo |
|---|---|
| `index.html` | **o livro**, pronto para leitura |
| `capitulos/` | a fonte, um Markdown por capítulo |
| `estrutura.json` | partes, capítulos e perguntas-guia |
| `construir.py` | gera `index.html` a partir da fonte |
| `tema/` | `tema.css` e `livro.js`, embutidos na construção |
| `dados/` | os bancos, o dicionário e os scripts que os geram |
| `analises/` | o script que calcula todos os números do livro |
| `CASO-CONDUTOR.md` | o protocolo do estudo que atravessa a obra |
| `recursos.md` | catálogo de links, com data de verificação |

## Os dados são simulados

O livro inteiro é construído sobre um estudo clínico fictício: um ensaio
randomizado de aspirado de medula óssea em úlcera venosa de membro inferior, com
200 participantes. **Os dados não são reais** e não constituem evidência sobre o
tratamento de úlceras venosas.

A escolha é deliberada, por três motivos: dados reais de pacientes não podem ser
distribuídos livremente, e um livro que promete reprodutibilidade precisa
entregar o banco; o efeito verdadeiro é conhecido, o que permite mostrar quando
um método acerta e quando erra; e um exemplo inventado apresentado como real
seria pior do que um exemplo inventado apresentado como tal.

## Reprodutibilidade

Todo número impresso no livro sai de um único script:

```bash
python analises/analises-do-livro.py
```

Ele lê os bancos e escreve `analises/resultados.md`. Qualquer resultado da obra
pode ser conferido comparando as duas coisas. Os bancos, por sua vez, se regeram
por script com semente fixa:

```bash
python dados/gerar-banco.py
python dados/gerar-coorte-observacional.py
```

## Como reconstruir o livro

```bash
python -m pip install markdown
python construir.py
```

O comando lê `estrutura.json` e os arquivos de `capitulos/`, escreve
`index.html` e imprime a contagem de palavras e de páginas por capítulo.

Para escrever ou revisar um capítulo, edite o Markdown correspondente em
`capitulos/` e reconstrua. O gabarito de escrita, com o padrão de seis blocos e
toda a sintaxe disponível, está em `capitulos/_modelo.md`.

## Correções e sugestões

Erratas, correções e sugestões são bem-vindas, pelas
[issues](https://github.com/aldemararaujo/estatistica/issues) ou pelo correio
eletrônico: aldemararaujocastro@gmail.com

## Licença

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pt-br).
Uso livre em ensino e em disciplinas de metodologia, com atribuição e sem
cobrança pelo material.

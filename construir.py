"""
Constroi index.html: pagina unica, autocontida, com CSS e JS embutidos.

Le estrutura.json e os arquivos de capitulos/, converte o Markdown e monta a
navegacao por abas. Nada de CDN, nada de arquivo externo: o livro final e um
unico HTML que abre em qualquer navegador, funciona sem internet e pode ser
enviado por anexo.

Uso:  python construir.py
Saida: index.html (+ relatorio de progresso no terminal)

O nome index.html e deliberado: e ele que o GitHub Pages serve na raiz do
endereco, sem exigir nada do leitor.

Dependencia unica: markdown (pip install markdown)
"""

import html
import json
import re
import unicodedata
from datetime import date
from pathlib import Path

import markdown

RAIZ = Path(__file__).parent
CAPITULOS = RAIZ / "capitulos"
TEMA = RAIZ / "tema"
SAIDA = RAIZ / "index.html"

EXTENSOES = ["tables", "fenced_code", "attr_list", "footnotes", "sane_lists", "abbr"]

TITULOS_PADRAO = {
    "caso": "O caso",
    "jamovi": "Mãos ao jamovi",
    "revisor": "O que o revisor devolve",
    "nota": "Nota",
    "atencao": "Atenção",
}

md = markdown.Markdown(extensions=EXTENSOES)


def para_html(texto):
    """Converte um trecho de Markdown, reiniciando o estado do conversor."""
    md.reset()
    return md.convert(texto.strip())


def envolve_tabelas(bruto):
    """Toda tabela rola sozinha: a pagina nunca rola na horizontal."""
    return re.sub(r"(<table>.*?</table>)", r'<div class="rolagem">\1</div>', bruto, flags=re.S)


def slug(texto):
    """Identificador estavel para um titulo: serve de ancora permanente."""
    limpo = unicodedata.normalize("NFKD", re.sub(r"<[^>]+>", "", texto))
    limpo = limpo.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", limpo)).strip("-")[:60]


def ancora_titulos(bruto, prefixo):
    """Da id e link permanente a cada h2 e h3, para citar uma secao em aula."""
    usados = {}

    def troca(m):
        nivel, texto = m.group(1), m.group(2)
        base = f"{prefixo}-{slug(texto)}" or prefixo
        usados[base] = usados.get(base, 0) + 1
        ident = base if usados[base] == 1 else f"{base}-{usados[base]}"
        return (f'<h{nivel} id="{ident}">{texto}'
                f'<a class="ancora" href="#{ident}" aria-label="Link para esta seção">#</a>'
                f"</h{nivel}>")

    return re.sub(r"<h([23])>(.*?)</h\1>", troca, bruto, flags=re.S)


# --------------------------------------------------------------- blocos

ABRE = re.compile(r"^:::[ \t]*(\w+)[ \t]*(.*)$")
FECHA = re.compile(r"^:::[ \t]*$")


def fatia(texto):
    """Separa o capitulo em trechos comuns e blocos ::: de primeiro nivel."""
    partes, buffer, atual = [], [], None
    for linha in texto.splitlines():
        if atual is None:
            m = ABRE.match(linha)
            if m:
                if buffer:
                    partes.append(("md", "\n".join(buffer)))
                    buffer = []
                atual = {"tipo": m.group(1), "arg": m.group(2).strip(), "linhas": []}
                continue
            buffer.append(linha)
        else:
            if FECHA.match(linha):
                partes.append(("bloco", atual))
                atual = None
                continue
            atual["linhas"].append(linha)
    if atual is not None:                       # bloco sem fechamento
        partes.append(("bloco", atual))
    if buffer:
        partes.append(("md", "\n".join(buffer)))
    return partes


def render_exercicio(bloco):
    corpo = "\n".join(bloco["linhas"])
    partes = re.split(r"^---[ \t]*gabarito[ \t]*$", corpo, maxsplit=1, flags=re.M)
    enunciado = envolve_tabelas(para_html(partes[0]))
    rotulo = f"Exercício {bloco['arg']}" if bloco["arg"] else "Exercício"
    saida = [f'<div class="exercicio"><div class="titulo">{html.escape(rotulo)}</div>', enunciado]
    if len(partes) == 2:
        saida.append("<details><summary>Ver o gabarito comentado</summary>"
                     + envolve_tabelas(para_html(partes[1])) + "</details>")
    saida.append("</div>")
    return "\n".join(saida)


def render_abas(bloco, seq):
    """Blocos '== Rotulo' viram abas. Serve para 'no jamovi' x 'a conta'."""
    corpo = "\n".join(bloco["linhas"])
    pedacos = re.split(r"^==[ \t]*(.+?)[ \t]*$", corpo, flags=re.M)[1:]
    pares = list(zip(pedacos[0::2], pedacos[1::2]))
    if not pares:
        return envolve_tabelas(para_html(corpo))
    tira, paineis = [], []
    for i, (rotulo, conteudo) in enumerate(pares):
        pid = f"aba-{seq}-{i}"
        tira.append(f'<button type="button" role="tab" aria-controls="{pid}" '
                    f'aria-selected="{str(i == 0).lower()}">{html.escape(rotulo)}</button>')
        paineis.append(f'<div class="aba-painel" id="{pid}" role="tabpanel"'
                       + ("" if i == 0 else " hidden") + ">"
                       + envolve_tabelas(para_html(conteudo)) + "</div>")
    return ('<div class="abas"><div class="abas-tira" role="tablist">'
            + "".join(tira) + "</div>" + "".join(paineis) + "</div>")


def render_caixa(bloco):
    tipo = bloco["tipo"]
    titulo = bloco["arg"] or TITULOS_PADRAO.get(tipo, tipo.capitalize())
    classe = tipo if tipo in TITULOS_PADRAO else "nota"
    return (f'<div class="caixa {classe}"><div class="titulo">{html.escape(titulo)}</div>'
            + envolve_tabelas(para_html("\n".join(bloco["linhas"]))) + "</div>")


def render(texto):
    saida, seq = [], 0
    for especie, dado in fatia(texto):
        if especie == "md":
            if dado.strip():
                saida.append(envolve_tabelas(para_html(dado)))
        elif dado["tipo"] == "exercicio":
            saida.append(render_exercicio(dado))
        elif dado["tipo"] == "abas":
            seq += 1
            saida.append(render_abas(dado, seq))
        else:
            saida.append(render_caixa(dado))
    return "\n".join(saida)


# ---------------------------------------------------------------- livro

def construir():
    livro = json.loads((RAIZ / "estrutura.json").read_text(encoding="utf-8"))
    css = (TEMA / "tema.css").read_text(encoding="utf-8")
    js = (TEMA / "livro.js").read_text(encoding="utf-8")

    sumario, paineis, sequencia, relatorio, meta = [], [], [], [], []

    # capa
    sequencia.append(("capa", "Capa"))
    sumario.append('<a href="#capa" data-id="capa" data-busca="capa rosto ficha">'
                   '<span class="num">•</span><span>Capa e apresentação</span></a>')

    for parte in livro["partes"]:
        sumario.append(f'<div class="parte">{html.escape(parte["titulo"])}</div>')
        for cap in parte["capitulos"]:
            cid = f"cap-{cap['n']}"
            arquivo = CAPITULOS / cap["arquivo"]
            existe = arquivo.exists()
            fonte = arquivo.read_text(encoding="utf-8") if existe else ""
            palavras = len(fonte.split())

            sumario.append(
                f'<a href="#{cid}" data-id="{cid}" data-palavras="{palavras}" '
                f'data-busca="{html.escape(cap["guia"])}"'
                + ("" if existe else ' class="pendente"') + ">"
                + f'<span class="num">{cap["n"]}</span>'
                + f'<span class="rotulo">{html.escape(cap["titulo"])}</span></a>')

            miolo = ancora_titulos(render(fonte), cid) if existe else (
                '<div class="aviso-vazio"><p>Capítulo em preparação.</p>'
                f'<p>Ele responderá: <em>{html.escape(cap["guia"])}</em></p></div>')

            if existe:
                meta.append({"id": cid, "n": str(cap["n"]), "titulo": cap["titulo"],
                             "palavras": palavras, "parte": parte["titulo"]})

            paineis.append(
                f'<article class="capitulo" id="{cid}" data-titulo="{html.escape(cap["titulo"])}" hidden>'
                '<header class="cabecalho-cap">'
                f'<div class="etiqueta">{html.escape(parte["titulo"])} · Capítulo {cap["n"]}</div>'
                f'<h1>{html.escape(cap["titulo"])}</h1>'
                f'<p class="guia">{html.escape(cap["guia"])}</p></header>'
                + miolo + "</article>")

            sequencia.append((cid, cap["titulo"]))
            relatorio.append((str(cap["n"]), cap["titulo"], palavras, existe))

    # navegacao anterior/proximo, injetada no fim de cada capitulo
    for i, (cid, _) in enumerate(sequencia):
        nav = ['<nav class="navega-cap">']
        if i > 0:
            nav.append(f'<a href="#{sequencia[i-1][0]}"><span>Anterior</span>'
                       f'<b>{html.escape(sequencia[i-1][1])}</b></a>')
        if i < len(sequencia) - 1:
            nav.append(f'<a class="prox" href="#{sequencia[i+1][0]}"><span>Próximo</span>'
                       f'<b>{html.escape(sequencia[i+1][1])}</b></a>')
        nav.append("</nav>")
        alvo = f'<article class="capitulo" id="{cid}"'
        for j, painel in enumerate(paineis):
            if painel.startswith(alvo):
                paineis[j] = painel[: -len("</article>")] + "".join(nav) + "</article>"

    apresentacao = CAPITULOS / "00-apresentacao.md"
    texto_capa = render(apresentacao.read_text(encoding="utf-8")) if apresentacao.exists() else ""

    capa = (
        '<article class="capitulo" id="capa" data-titulo="Capa">'
        '<header class="cabecalho-cap">'
        f'<div class="etiqueta">{html.escape(livro["autor"])}</div>'
        f'<h1>{html.escape(livro["titulo"])}</h1>'
        f'<p class="guia">{html.escape(livro["subtitulo"])}</p></header>'
        '<div id="retomar" hidden></div>'
        + texto_capa +
        '<div class="ficha">'
        f'<p>{html.escape(livro["autor"])} — <a href="{livro["lattes"]}">currículo Lattes</a></p>'
        f'<p>{html.escape(livro["local"])}, {html.escape(livro["ano"])}</p>'
        f'<p>ISBN: {html.escape(livro["isbn"])} · Licença {html.escape(livro["licenca"])}</p>'
        f'<p>Comentários, sugestões e críticas: <a href="mailto:{livro["contato"]}">{livro["contato"]}</a></p>'
        f'<p>Versão de {date.today().strftime("%d/%m/%Y")}</p>'
        "</div></article>")
    paineis.insert(0, capa)

    pagina = f"""<!DOCTYPE html>
<html lang="pt-BR" data-tema="claro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(livro["titulo"])}</title>
<meta name="author" content="{html.escape(livro["autor"])}">
<meta name="description" content="{html.escape(livro["titulo"])}: {html.escape(livro["subtitulo"])}">
<style>
{css}
</style>
</head>
<body>
<div id="barra-progresso"></div>
<a class="pular" href="#leitura">Pular para o conteúdo</a>
<button id="abre-sumario" type="button">Sumário</button>
<div id="leiaute">
<nav id="sumario">
  <div class="marca">
    <b>{html.escape(livro["titulo"])}</b>
    <span>{html.escape(livro["subtitulo"])}</span>
  </div>

  <section id="painel-progresso" aria-label="Progresso de leitura">
    <div class="trilho"><div class="preenchido" id="progresso-preenchido"></div></div>
    <p class="linha-progresso"><strong id="progresso-pct">0%</strong>
       <span id="progresso-detalhe">do livro lido</span></p>
    <p class="linha-restante" id="progresso-restante"></p>
  </section>

  <input id="busca" type="search" placeholder="Buscar no livro inteiro (tecla /)"
         aria-label="Buscar no livro inteiro" autocomplete="off">
  <div id="resultados-busca" hidden></div>

  <div id="lista-capitulos">
  {"".join(sumario)}
  </div>

  <div id="rodape-sumario">
    <div class="ferramentas">
      <button id="alterna-tema" type="button">Tema escuro</button>
      <button id="imprime-tudo" type="button">Imprimir</button>
    </div>
    <div class="ferramentas">
      <span class="rotulo-ferramenta">Texto</span>
      <button id="fonte-menor" type="button" aria-label="Diminuir o texto">A&minus;</button>
      <button id="fonte-maior" type="button" aria-label="Aumentar o texto">A+</button>
      <button id="zera-progresso" type="button">Zerar leitura</button>
    </div>
    <p>Setas ou J e K mudam de capítulo. Tecla / busca. Tecla M marca como lido.</p>
  </div>
</nav>
<main id="leitura">
{"".join(paineis)}
</main>
</div>
<button id="ao-topo" type="button" hidden aria-label="Voltar ao topo">&uarr;</button>
<script>
var LIVRO_TITULO = {json.dumps(livro["titulo"])};
var LIVRO_CAPS = {json.dumps(meta, ensure_ascii=False)};
var PALAVRAS_POR_MINUTO = 200;
{js}
</script>
</body>
</html>
"""
    SAIDA.write_text(pagina, encoding="utf-8")

    # ------------------------------------------------------- relatorio
    prontos = sum(1 for *_, existe in relatorio if existe)
    total_palavras = sum(p for _, _, p, existe in relatorio if existe)
    print(f"{SAIDA.name} gerado: {SAIDA.stat().st_size / 1024:.0f} KB\n")
    print(f"{'Cap':>3}  {'Título':38s} {'Palavras':>9}  {'Páginas':>7}")
    print("-" * 64)
    for n, titulo, palavras, existe in relatorio:
        if existe:
            print(f"{n:>3}  {titulo[:38]:38s} {palavras:>9}  {palavras/450:>7.1f}")
        else:
            print(f"{n:>3}  {titulo[:38]:38s} {'—':>9}  {'—':>7}")
    print("-" * 64)
    print(f"{prontos} de {len(relatorio)} capítulos escritos · "
          f"{total_palavras} palavras · cerca de {total_palavras/450:.0f} páginas")


if __name__ == "__main__":
    construir()

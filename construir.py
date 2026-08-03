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
    "revisor": "Aqui é onde o artigo é rejeitado",
    "agora": "O que fazer agora, no seu projeto",
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


def render_exercicio(bloco, prefixo, seq):
    corpo = "\n".join(bloco["linhas"])
    partes = re.split(r"^---[ \t]*gabarito[ \t]*$", corpo, maxsplit=1, flags=re.M)
    enunciado = envolve_tabelas(para_html(partes[0]))
    rotulo = f"Exercício {bloco['arg']}" if bloco["arg"] else "Exercício"
    ident = f"{prefixo}-ex-{bloco['arg'] or seq}"
    saida = [f'<div class="exercicio" id="{ident}" data-exercicio="{ident}">'
             f'<div class="titulo">{html.escape(rotulo)}'
             f'<button type="button" class="resolvido" aria-pressed="false">'
             f'marcar como resolvido</button></div>', enunciado]
    if len(partes) == 2:
        saida.append("<details><summary>Ver o gabarito comentado</summary>"
                     + envolve_tabelas(para_html(partes[1])) + "</details>")
    saida.append("</div>")
    return "\n".join(saida)


CALCULADORAS = {
    "amostra": """
<div class="calc" data-calc="amostra">
  <div class="calc-titulo">Calculadora: tamanho da amostra para duas proporções</div>
  <div class="calc-campos">
    <label>Proporção esperada no grupo controle (%)
      <input type="number" data-campo="p2" value="55" min="1" max="99" step="0.1"></label>
    <label>Proporção esperada no grupo intervenção (%)
      <input type="number" data-campo="p1" value="75" min="1" max="99" step="0.1"></label>
    <label>Nível de significância
      <select data-campo="alfa">
        <option value="1.959964" selected>5% bilateral</option>
        <option value="2.575829">1% bilateral</option>
        <option value="1.644854">5% unilateral</option>
      </select></label>
    <label>Poder
      <select data-campo="poder">
        <option value="0.841621" selected>80%</option>
        <option value="1.281552">90%</option>
        <option value="1.644854">95%</option>
      </select></label>
    <label>Perdas previstas (%)
      <input type="number" data-campo="perdas" value="10" min="0" max="50" step="1"></label>
  </div>
  <div class="calc-saida" data-saida></div>
</div>""",
    "intervalo": """
<div class="calc" data-calc="intervalo">
  <div class="calc-titulo">Calculadora: proporções, diferença e número necessário para tratar</div>
  <div class="calc-campos">
    <label>Eventos no grupo intervenção
      <input type="number" data-campo="a" value="65" min="0" step="1"></label>
    <label>Total no grupo intervenção
      <input type="number" data-campo="n1" value="92" min="1" step="1"></label>
    <label>Eventos no grupo controle
      <input type="number" data-campo="c" value="49" min="0" step="1"></label>
    <label>Total no grupo controle
      <input type="number" data-campo="n2" value="92" min="1" step="1"></label>
  </div>
  <div class="calc-saida" data-saida></div>
</div>""",
    "fagan": """
<div class="calc" data-calc="fagan">
  <div class="calc-titulo">Calculadora: probabilidade pós-teste</div>
  <div class="calc-campos">
    <label>Probabilidade pré-teste (%)
      <input type="number" data-campo="pre" value="62" min="0.1" max="99.9" step="0.1"></label>
    <label>Sensibilidade (%)
      <input type="number" data-campo="sens" value="71.1" min="0.1" max="100" step="0.1"></label>
    <label>Especificidade (%)
      <input type="number" data-campo="esp" value="80" min="0.1" max="99.9" step="0.1"></label>
  </div>
  <div class="calc-saida" data-saida></div>
</div>""",
}


def render_calculadora(bloco):
    return CALCULADORAS.get(bloco["arg"].strip(), "")


FIGURAS = RAIZ / "figuras"
_contador_figuras = {"n": 0}


def render_figura(bloco):
    """Embute um SVG de figuras/ dentro do texto, com legenda numerada.

    SVG inline, e nao imagem: herda as cores do tema, mantem o texto
    pesquisavel pela busca do livro e legivel por leitor de tela, e pesa
    poucos quilobytes.
    """
    nome = bloco["arg"].strip()
    arquivo = FIGURAS / f"{nome}.svg"
    if not arquivo.exists():
        return (f'<p class="aviso-vazio">Figura <code>{html.escape(nome)}</code> '
                "ainda não desenhada.</p>")

    svg = arquivo.read_text(encoding="utf-8")
    svg = re.sub(r"<\?xml.*?\?>", "", svg, flags=re.S).strip()
    _contador_figuras["n"] += 1
    legenda = " ".join(l.strip() for l in bloco["linhas"] if l.strip())

    titulo = ""
    m = re.search(r"<title>(.*?)</title>", svg, re.S)
    if m:
        titulo = m.group(1).strip()

    corpo = [f'<figure class="figura" id="fig-{_contador_figuras["n"]}"'
             f' role="img" aria-label="{html.escape(titulo or legenda)}">',
             '<div class="figura-quadro">', svg, "</div>"]
    if legenda:
        corpo.append(f'<figcaption><b>Figura {_contador_figuras["n"]}.</b> '
                     f'{para_html(legenda)[3:-4]}</figcaption>')
    corpo.append("</figure>")
    return "\n".join(corpo)


NIVEIS = {"facil": "fácil", "media": "intermediária", "dificil": "difícil"}


def render_quiz(bloco, prefixo):
    """Converte o bloco ::: quiz em um questionario recolhido.

    Sintaxe de cada pergunta:
        ? [facil] Enunciado da pergunta
        - alternativa errada | por que ela esta errada
        + alternativa certa   | por que ela esta certa
        @ ancora-da-secao-para-reler
    """
    perguntas, atual = [], None
    for linha in bloco["linhas"]:
        crua = linha.strip()
        if crua.startswith("?"):
            if atual:
                perguntas.append(atual)
            m = re.match(r"\?\s*(?:\[(\w+)\])?\s*(.+)$", crua)
            atual = {"nivel": (m.group(1) or "media"), "texto": m.group(2).strip(),
                     "alts": [], "ancora": ""}
        elif atual and crua.startswith("@"):
            atual["ancora"] = crua[1:].strip()
        elif atual and (crua.startswith("-") or crua.startswith("+")):
            corpo = crua[1:].strip()
            texto, _, retorno = corpo.partition("|")
            atual["alts"].append({"certa": crua.startswith("+"),
                                  "texto": texto.strip(),
                                  "retorno": retorno.strip()})
        elif atual and crua and atual["alts"]:
            atual["alts"][-1]["retorno"] += " " + crua
    if atual:
        perguntas.append(atual)
    if not perguntas:
        return ""

    # Deslocamento por capitulo, para que a posicao da resposta certa nao siga
    # o mesmo desenho em todos os quizzes do livro.
    desloca = sum(ord(c) for c in prefixo) % 5

    itens = []
    for i, p in enumerate(perguntas, 1):
        # A correta vai para uma posicao distribuida por rodizio, e nao sorteada:
        # sorteio com poucas perguntas produz aglomerados, e foi o que aconteceu
        # na primeira versao, com a resposta certa caindo em D ou E sete vezes.
        outras = [a for a in p["alts"] if not a["certa"]]
        certa_alt = next((a for a in p["alts"] if a["certa"]), None)
        if certa_alt is None:
            continue
        certa = (i - 1 + desloca) % len(p["alts"])
        alts = outras[:certa] + [certa_alt] + outras[certa:]

        linhas_alt = []
        for k, a in enumerate(alts):
            linhas_alt.append(
                f'<li><button type="button" class="quiz-alt" data-i="{k}">'
                f'<span class="letra">{chr(65 + k)}</span>'
                f'<span class="texto">{para_html(a["texto"])[3:-4]}</span></button>'
                f'<p class="quiz-retorno" hidden>{para_html(a["retorno"])[3:-4]}</p></li>')

        releia = (f'<p class="quiz-releia" hidden>Releia: '
                  f'<a href="#{p["ancora"]}">a seção correspondente do capítulo</a></p>'
                  if p["ancora"] else "")

        itens.append(
            f'<li class="quiz-pergunta" data-certa="{certa}">'
            f'<p class="quiz-enunciado">'
            f'<span class="nivel {p["nivel"]}">{NIVEIS.get(p["nivel"], p["nivel"])}</span>'
            f'{para_html(p["texto"])[3:-4]}</p>'
            f'<ul class="quiz-alternativas">{"".join(linhas_alt)}</ul>'
            f"{releia}</li>")

    return (f'<details class="quiz" data-quiz="{prefixo}">'
            f'<summary><b>Teste o que você entendeu</b>'
            f'<span class="quiz-resumo">{len(perguntas)} perguntas · '
            f'responda sem consultar o capítulo</span></summary>'
            f'<div class="quiz-corpo"><ol class="quiz-perguntas">{"".join(itens)}</ol>'
            f'<div class="quiz-placar" hidden></div>'
            f'<div class="quiz-acoes" hidden>'
            f'<button type="button" class="quiz-refazer">Refazer o quiz</button>'
            f'<button type="button" class="quiz-refazer-erros">Refazer só as que errei</button>'
            f"</div></div></details>")


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


def render(texto, prefixo="doc"):
    saida, seq, nex = [], 0, 0
    for especie, dado in fatia(texto):
        if especie == "md":
            if dado.strip():
                saida.append(envolve_tabelas(para_html(dado)))
        elif dado["tipo"] == "exercicio":
            nex += 1
            saida.append(render_exercicio(dado, prefixo, nex))
        elif dado["tipo"] == "abas":
            seq += 1
            saida.append(render_abas(dado, seq))
        elif dado["tipo"] == "calculadora":
            saida.append(render_calculadora(dado))
        elif dado["tipo"] == "quiz":
            saida.append(render_quiz(dado, prefixo))
        elif dado["tipo"] == "figura":
            saida.append(render_figura(dado))
        else:
            saida.append(render_caixa(dado))
    return "\n".join(saida)


def numero(n):
    """Formata com ponto de milhar, no padrao brasileiro."""
    return f"{n:,}".replace(",", ".")


def painel_numeros(paineis, meta, glossario, palavras_total):
    """Monta o quadro 'O livro em números', na abertura.

    Tudo e contado a partir do conteudo ja renderizado, para que os numeros
    nunca envelhecam: o livro cresce e o quadro acompanha sozinho.
    """
    corpo = "".join(paineis)
    minutos = round(palavras_total / 200)
    horas, resto = divmod(minutos, 60)
    tempo = f"{horas}h{resto:02d}" if horas else f"{minutos} min"

    participantes = 0
    variaveis = 0
    bancos = 0
    for arquivo in sorted((RAIZ / "dados").glob("*.csv")):
        try:
            linhas = arquivo.read_text(encoding="utf-8").splitlines()
            participantes += max(0, len(linhas) - 1)
            variaveis += len(linhas[0].split(",")) if linhas else 0
            bancos += 1
        except OSError:
            pass

    n_quizzes = corpo.count('class="quiz" data-quiz=')
    n_capitulos = sum(1 for c in meta if str(c["n"]).isdigit())
    n_apendices = len(meta) - n_capitulos

    cartoes = [
        (numero(len(meta)), "capítulos e apêndices",
         f"{n_capitulos} capítulos mais {n_apendices} apêndices"),
        (numero(palavras_total), "palavras",
         f"cerca de {numero(round(palavras_total / 450))} páginas impressas"),
        (tempo, "de leitura",
         "a 200 palavras por minuto, do começo ao fim"),
        (numero(corpo.count('class="quiz-pergunta"')), "perguntas de quiz",
         f"em {n_quizzes} questionários, com cinco alternativas cada"),
        (numero(corpo.count('class="quiz-retorno"')), "comentários de resposta",
         "um para cada alternativa, certa ou errada"),
        (numero(corpo.count('class="exercicio"')), "exercícios",
         "todos com gabarito comentado"),
        (numero(corpo.count('class="caixa revisor"')), "seções sobre rejeição",
         "os erros que os revisores de fato devolvem"),
        (numero(corpo.count("<table>")), "tabelas",
         "além de fluxogramas e listas de verificação"),
        (numero(corpo.count('class="calc"')), "calculadoras",
         "tamanho de amostra, intervalos e probabilidade pós-teste"),
        (numero(len(glossario)), "verbetes no glossário",
         "com definição ao passar o cursor sobre o termo"),
        (numero(len(set(re.findall(r'href="(https?://[^"]+)"', corpo)))), "links externos",
         "verificados um a um, com data de conferência"),
        (numero(participantes), "participantes simulados",
         f"em {bancos} bancos de dados abertos, somando {variaveis} variáveis"),
    ]

    itens = "".join(
        f'<div class="cartao"><b>{valor}</b><span class="rotulo">{rotulo}</span>'
        f'<span class="detalhe">{detalhe}</span></div>'
        for valor, rotulo, detalhe in cartoes)

    return (
        '<section id="livro-em-numeros" aria-label="O livro em números">'
        '<h2 class="titulo-numeros">O livro em números</h2>'
        f'<div class="grade-numeros">{itens}</div>'
        '<p class="rodape-numeros">Tudo em uma única página, que funciona sem '
        'internet e não depende de nenhum servidor. Os números acima são contados '
        'automaticamente a cada nova versão.</p>'
        "</section>")


def extrai_glossario(caminho):
    """Le o apendice C e devolve {termo: definicao} para as dicas de leitura."""
    if not caminho.exists():
        return {}
    verbetes = {}
    for m in re.finditer(r"^\*\*(.+?)\.\*\*\s+(.+?)(?=\n\n|\n\*\*|\Z)",
                         caminho.read_text(encoding="utf-8"), re.M | re.S):
        termo = m.group(1).strip()
        texto = re.sub(r"\s+", " ", m.group(2)).strip()
        texto = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", texto)
        # o italico dos estrangeirismos precisa sobreviver ate a dica de leitura
        texto = re.sub(r"\*(.+?)\*", r"<em>\1</em>", texto)
        # "Alfa (α)" vira "Alfa"; "Wilson, intervalo de" vira "Wilson"
        principal = re.sub(r"\s*\(.*?\)", "", termo)
        principal = re.split(r",\s*", principal)[0].strip()
        if len(principal) >= 5 and principal not in verbetes:
            verbetes[principal] = texto
    return verbetes


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

            miolo = ancora_titulos(render(fonte, cid), cid) if existe else (
                '<div class="aviso-vazio"><p>Capítulo em preparação.</p>'
                f'<p>Ele responderá: <em>{html.escape(cap["guia"])}</em></p></div>')

            if existe:
                meta.append({"id": cid, "n": str(cap["n"]), "titulo": cap["titulo"],
                             "palavras": palavras, "parte": parte["titulo"],
                             "exercicios": miolo.count('class="exercicio"')})

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
    texto_capa = render(apresentacao.read_text(encoding="utf-8"), "capa") if apresentacao.exists() else ""
    glossario = extrai_glossario(CAPITULOS / "C-glossario.md")

    capa = (
        '<article class="capitulo" id="capa" data-titulo="Capa">'
        '<header class="cabecalho-cap">'
        f'<div class="etiqueta">{html.escape(livro["autor"])}</div>'
        f'<h1>{html.escape(livro["titulo"])}</h1>'
        f'<p class="guia">{html.escape(livro["subtitulo"])}</p></header>'
        '<div id="retomar" hidden></div>'
        "<!--NUMEROS-->"
        + texto_capa +
        '<div class="ficha">'
        f'<p class="autor-ficha">{html.escape(livro["autor"])}</p>'
        '<p class="perfis">'
        f'<a href="{livro["lattes"]}" target="_blank" rel="noopener">Lattes</a>'
        '<span aria-hidden="true">|</span>'
        f'<a href="{livro["google"]}" target="_blank" rel="noopener">Google</a>'
        '<span aria-hidden="true">|</span>'
        f'<a href="{livro["orcid"]}" target="_blank" rel="noopener">ORCID</a>'
        "</p>"
        f'<p>ISBN: {html.escape(livro["isbn"])} · Licença {html.escape(livro["licenca"])}</p>'
        f'<p>Comentários, sugestões e críticas: <a href="mailto:{livro["contato"]}">{livro["contato"]}</a></p>'
        f'<p class="versao">Versão {html.escape(livro.get("versao", "1.0"))} · '
        f'{date.today().strftime("%d/%m/%Y")} · '
        f'<a href="{livro["repositorio"]}/blob/main/VERSOES.md">histórico de versões</a></p>'
        '<p class="acoes-ficha">'
        '<button type="button" id="abre-citar">Como citar este livro</button>'
        '</p>'
        "</div></article>")
    paineis.insert(0, capa)

    # O quadro de numeros e montado por ultimo, sobre o conteudo ja renderizado,
    # e substitui o marcador deixado na capa.
    total_palavras = sum(p for _, _, p, existe in relatorio if existe)
    paineis[0] = paineis[0].replace(
        "<!--NUMEROS-->", painel_numeros(paineis[1:], meta, glossario, total_palavras))

    # o que aparece quando alguem manda o endereco do livro por mensagem
    descricao = (
        f"Livro de acesso aberto sobre estatística aplicada à pesquisa com seres "
        f"humanos, de {livro['autor']}. "
        f"{sum(1 for c in meta if str(c['n']).isdigit())} capítulos na ordem das "
        f"decisões de um projeto, da dúvida clínica ao artigo submetido, com "
        f"exercícios, questionários e os dados abertos para conferir cada número.")

    pagina = f"""<!DOCTYPE html>
<html lang="pt-BR" data-tema="claro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(livro["titulo"])}</title>
<meta name="author" content="{html.escape(livro["autor"])}">
<meta name="description" content="{html.escape(descricao)}">
<link rel="canonical" href="{livro["url"]}">

<meta property="og:type" content="book">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="{html.escape(livro["titulo"])}">
<meta property="og:title" content="{html.escape(livro["titulo"])}: {html.escape(livro["subtitulo"])}">
<meta property="og:description" content="{html.escape(descricao)}">
<meta property="og:url" content="{livro["url"]}">
<meta property="og:image" content="{livro["url"]}compartilhar.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="1006">
<meta property="og:image:alt" content="Capa do livro {html.escape(livro["titulo"])}">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(livro["titulo"])}">
<meta name="twitter:description" content="{html.escape(descricao)}">
<meta name="twitter:image" content="{livro["url"]}compartilhar.png">
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
    </div>
    <div class="ferramentas">
      <span class="rotulo-ferramenta">Progresso</span>
      <button id="exporta-progresso" type="button">Exportar</button>
      <button id="importa-progresso" type="button">Importar</button>
      <button id="zera-progresso" type="button">Zerar</button>
      <input type="file" id="arquivo-progresso" accept="application/json,.json" hidden>
    </div>
    <p>Setas ou J e K mudam de capítulo. Tecla / busca. Tecla M marca como lido.</p>
    <p class="selo-versao">Versão {html.escape(livro.get("versao", "1.0"))}
       · {date.today().strftime("%d/%m/%Y")}</p>
  </div>
</nav>
<main id="leitura">
{"".join(paineis)}
</main>
</div>
<button id="ao-topo" type="button" hidden aria-label="Voltar ao topo">&uarr;</button>

<div id="dica-glossario" hidden role="tooltip"></div>

<dialog id="painel-citar">
  <h2>Como citar</h2>
  <div id="citacoes"></div>
  <button type="button" id="fecha-citar">Fechar</button>
</dialog>

<script>
var LIVRO_TITULO = {json.dumps(livro["titulo"])};
var LIVRO = {json.dumps({k: livro.get(k, "") for k in
    ["titulo", "subtitulo", "autor", "local", "ano", "url", "repositorio",
     "licenca", "isbn", "versao"]},
    ensure_ascii=False)};
var LIVRO_CAPS = {json.dumps(meta, ensure_ascii=False)};
var GLOSSARIO = {json.dumps(glossario, ensure_ascii=False)};
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

"""
Confere as referências e os endereços do livro, um a um.

Trabalha sobre **index.html**, e não sobre os arquivos de origem: o que interessa
é o endereço que o leitor de fato recebe, depois de o Markdown ter sido
convertido. Foi essa escolha que revelou, na primeira execução, que o problema
estava no verificador e não no livro.

Faz duas verificações independentes:

1. **DOI contra o registro da Crossref.** Não basta o DOI existir: o título
   registrado precisa aparecer no livro, junto do DOI. É o que impede a situação
   em que o texto promete um artigo e o endereço entrega outro.
2. **Endereço contra a rede.** Toda URL citada é acessada. Vários editores
   respondem 403, 406 ou 429 a programas e atendem navegadores normalmente;
   esses aparecem como bloqueio a robô, e não como falha, e ficam marcados para
   conferência manual. O mesmo vale para os servidores de TLS antigo, que o
   OpenSSL do Python recusa e o navegador aceita: aparecem como TLS, e não como
   endereço quebrado.

Uso:  python analises/verificar-referencias.py
Saida: relatorio no terminal; sai com codigo 1 se houver problema real.
"""

import html as _html
import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).parent.parent
LIVRO = RAIZ / "index.html"

# O console do Windows abre em cp1252, e titulo de artigo vem cheio de sinal que
# cp1252 nao conhece: o hifen tipografico da Wiley derrubava o relatorio inteiro
# no meio da conferencia.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CABECA = {"User-Agent": "livro-estatistica/1.0 (https://aldemararaujo.github.io/estatistica/)"}
NAVEGADOR = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/120 Safari/537.36",
             "Accept": "text/html,application/xhtml+xml,*/*;q=0.8"}

# editores que barram programas mas atendem navegadores
BLOQUEIO = {401, 403, 406, 429, 503, 520}


def normaliza(s):
    """Compara títulos ignorando acento, caixa, pontuação e marcação."""
    s = _html.unescape(re.sub(r"<[^>]+>", " ", s))
    s = s.replace("’", "'").replace("“", '"').replace("”", '"').lower()
    s = re.sub(r"[^a-z0-9]+", " ", s.encode("ascii", "ignore").decode())
    return " ".join(s.split())


def crossref(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/")
    with urllib.request.urlopen(urllib.request.Request(url, headers=CABECA), timeout=30) as r:
        m = json.load(r)["message"]
    return {"titulo": " ".join(m.get("title", []) + (m.get("subtitle") or [])),
            "ano": (m.get("issued", {}).get("date-parts") or [[None]])[0][0]}


def situacao(url):
    ultimo = None
    for cabecalho in (NAVEGADOR, CABECA):
        try:
            req = urllib.request.Request(url, headers=cabecalho, method="GET")
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status
        except urllib.error.HTTPError as e:
            ultimo = e.code
        except urllib.error.URLError as e:
            # Servidor de TLS antigo que o OpenSSL recusa e o navegador aceita.
            # E o caso do Lattes: Chrome e curl abrem, o Python nao. Recusar o
            # handshake aqui nao autoriza dizer que o endereco esta quebrado.
            ultimo = "TLS" if isinstance(e.reason, ssl.SSLError) else str(e)[:40]
        except Exception as e:
            ultimo = str(e)[:40]
        time.sleep(0.5)
    return ultimo


def main():
    if not LIVRO.exists():
        print("index.html não encontrado: rode primeiro python construir.py")
        return 1
    pagina = LIVRO.read_text(encoding="utf-8")
    texto_limpo = normaliza(pagina)
    problemas, avisos = [], []

    # ---------------------------------------------------------------- DOIs
    dois = sorted({urllib.parse.unquote(m.group(1))
                   for m in re.finditer(r'href="https://doi\.org/([^"]+)"', pagina)})
    print(f"Conferindo {len(dois)} DOIs contra o registro da Crossref\n")
    for doi in dois:
        try:
            reg = crossref(doi)
        except Exception as e:
            problemas.append(f"DOI não resolve na Crossref: {doi} ({str(e)[:40]})")
            print(f"  FALHA   {doi}")
            continue
        # as primeiras palavras do título registrado precisam existir no livro
        pedaco = " ".join(normaliza(reg["titulo"]).split()[:6])
        bate = bool(pedaco) and pedaco in texto_limpo
        if not bate:
            avisos.append(f"conferir o título de {doi}: o registro diz "
                          f"\"{re.sub(r'<[^>]+>', '', reg['titulo'])[:70]}\"")
        print(f"  {'OK ' if bate else 'VER'}     {doi}  ({reg['ano']}) "
              f"{re.sub(r'<[^>]+>', '', reg['titulo'])[:56]}")
        time.sleep(0.25)

    # -------------------------------------------------------------- endereços
    urls = sorted({m.group(1) for m in re.finditer(r'href="(https?://[^"]+)"', pagina)
                   if "doi.org" not in m.group(1)})
    print(f"\nConferindo {len(urls)} endereços na rede\n")
    for u in urls:
        st = situacao(_html.unescape(u))
        if st == 200:
            print(f"  OK      {u[:78]}")
        elif st == "TLS":
            print(f"  TLS     {u[:70]}")
            avisos.append(f"{u} usa TLS que o OpenSSL recusa e o navegador aceita; "
                          "conferir no navegador")
        elif st in BLOQUEIO:
            print(f"  ROBÔ    {st}  {u[:70]}")
            avisos.append(f"{u} responde {st} a programas; conferir no navegador")
        else:
            print(f"  FALHA   {st}  {u[:70]}")
            problemas.append(f"endereço quebrado: {u} ({st})")

    # ---------------------------------------------------------------- resumo
    print("\n" + "=" * 66)
    if problemas:
        print(f"{len(problemas)} PROBLEMA(S) REAL(IS):")
        for p in problemas:
            print("  -", p)
    else:
        print("Nenhum endereço quebrado e nenhum DOI inválido.")
    if avisos:
        print(f"\n{len(avisos)} ponto(s) para conferência manual:")
        for a in avisos:
            print("  -", a)
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main())

/* ------------------------------------------------------------------
   A Estatística na Pesquisa Clínica — comportamento da página do livro
   Embutido em index.html pelo construir.py. Sem dependência externa.

   O que este arquivo faz:
   - navegação por capítulo, com endereço permanente por seção
   - marcador de leitura: o que já foi lido e quanto falta do livro
   - busca no texto completo, com trecho de contexto e destaque
   - índice interno do capítulo
   - tema claro e escuro, tamanho do texto, impressão
   ------------------------------------------------------------------ */
(function () {
  "use strict";

  var capitulos = Array.prototype.slice.call(document.querySelectorAll(".capitulo"));
  var elos = Array.prototype.slice.call(document.querySelectorAll("#sumario a[data-id]"));
  var busca = document.getElementById("busca");
  var resultados = document.getElementById("resultados-busca");
  var listaCapitulos = document.getElementById("lista-capitulos");
  var progresso = document.getElementById("barra-progresso");
  var corpo = document.body;

  var CHAVE_LIDOS = "epc-lidos";
  var CHAVE_ULTIMO = "epc-ultimo";
  var CHAVE_TEMA = "epc-tema";
  var CHAVE_FONTE = "epc-fonte";

  /* ------------------------------------------------------- utilidades */

  function guarda(chave, valor) {
    try { localStorage.setItem(chave, valor); } catch (e) {}
  }
  function busca_guardado(chave) {
    try { return localStorage.getItem(chave); } catch (e) { return null; }
  }
  function semAcento(s) {
    return s.normalize ? s.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase()
                       : s.toLowerCase();
  }
  function duracao(palavras) {
    var min = Math.round(palavras / PALAVRAS_POR_MINUTO);
    if (min < 1) { return "menos de 1 min"; }
    if (min < 60) { return min + " min"; }
    var h = Math.floor(min / 60), m = min % 60;
    return h + " h" + (m ? " " + m + " min" : "");
  }

  /* --------------------------------------------------- marcador de leitura */

  var lidos = {};
  (function carregaLidos() {
    try { lidos = JSON.parse(busca_guardado(CHAVE_LIDOS) || "{}") || {}; } catch (e) { lidos = {}; }
  })();

  var totalPalavras = LIVRO_CAPS.reduce(function (s, c) { return s + c.palavras; }, 0);

  function palavrasLidas() {
    return LIVRO_CAPS.reduce(function (s, c) { return s + (lidos[c.id] ? c.palavras : 0); }, 0);
  }

  function estaLido(id) { return !!lidos[id]; }

  function marca(id, valor) {
    if (!LIVRO_CAPS.some(function (c) { return c.id === id; })) { return; }
    if (valor) { lidos[id] = 1; } else { delete lidos[id]; }
    guarda(CHAVE_LIDOS, JSON.stringify(lidos));
    pintaProgresso();
    pintaBotaoLido();
  }

  function pintaProgresso() {
    var lidasP = palavrasLidas();
    var pct = totalPalavras ? Math.round((lidasP / totalPalavras) * 100) : 0;
    var quantos = LIVRO_CAPS.filter(function (c) { return lidos[c.id]; }).length;

    var preenchido = document.getElementById("progresso-preenchido");
    if (preenchido) { preenchido.style.width = pct + "%"; }
    var elPct = document.getElementById("progresso-pct");
    if (elPct) { elPct.textContent = pct + "%"; }
    var det = document.getElementById("progresso-detalhe");
    if (det) {
      det.textContent = "do livro lido · " + quantos + " de " + LIVRO_CAPS.length + " capítulos";
    }
    var rest = document.getElementById("progresso-restante");
    if (rest) {
      var faltam = totalPalavras - lidasP;
      rest.textContent = faltam > 0 ? "Faltam cerca de " + duracao(faltam) + " de leitura"
                                    : "Você leu o livro inteiro.";
    }

    elos.forEach(function (a) {
      a.classList.toggle("lido", estaLido(a.getAttribute("data-id")));
    });
  }

  function pintaBotaoLido() {
    var cap = capitulos.find(function (c) { return !c.hidden; });
    if (!cap) { return; }
    var botao = cap.querySelector(".marcar-lido");
    if (!botao) { return; }
    var lido = estaLido(cap.id);
    botao.classList.toggle("feito", lido);
    botao.setAttribute("aria-pressed", String(lido));
    botao.textContent = lido ? "✓ Capítulo lido" : "Marcar como lido";
  }

  /* ------------------ enfeites que cada capítulo recebe uma única vez */

  function preparaCapitulo(cap) {
    if (cap.dataset.pronto === "1") { return; }
    cap.dataset.pronto = "1";

    var dados = LIVRO_CAPS.filter(function (c) { return c.id === cap.id; })[0];
    var cabecalho = cap.querySelector(".cabecalho-cap");

    // tempo de leitura, logo abaixo da pergunta-guia
    if (dados && cabecalho) {
      var t = document.createElement("p");
      t.className = "tempo-leitura";
      t.textContent = duracao(dados.palavras) + " de leitura · " +
                      dados.palavras.toLocaleString("pt-BR") + " palavras";
      cabecalho.appendChild(t);
    }

    // índice interno, quando o capítulo tem seções suficientes
    var titulos = Array.prototype.slice.call(cap.querySelectorAll("h2[id]"));
    if (titulos.length >= 3 && cabecalho) {
      var box = document.createElement("details");
      box.className = "indice-cap";
      var resumo = document.createElement("summary");
      resumo.textContent = "Neste capítulo (" + titulos.length + " seções)";
      box.appendChild(resumo);
      var ul = document.createElement("ul");
      titulos.forEach(function (h) {
        var li = document.createElement("li");
        var a = document.createElement("a");
        a.href = "#" + h.id;
        a.textContent = h.textContent.replace(/#$/, "").trim();
        li.appendChild(a);
        ul.appendChild(li);
      });
      box.appendChild(ul);
      cabecalho.parentNode.insertBefore(box, cabecalho.nextSibling);
    }

    // botão de marcar como lido, antes da navegação de rodapé
    if (dados) {
      var nav = cap.querySelector(".navega-cap");
      var caixa = document.createElement("div");
      caixa.className = "caixa-marcar";
      var botao = document.createElement("button");
      botao.type = "button";
      botao.className = "marcar-lido";
      caixa.appendChild(botao);
      if (nav) { cap.insertBefore(caixa, nav); } else { cap.appendChild(caixa); }
    }
    religa(cap);
  }

  /* Trocar o innerHTML (ao destacar e ao limpar a busca) mata os ouvintes de
     evento sem apagar os elementos. Esta função os devolve, e é por isso que
     ela não pode criar nada: quem cria é preparaCapitulo, uma única vez. */
  function religa(cap) {
    cap.querySelectorAll(".abas").forEach(function (g) { g.dataset.ligado = ""; });
    ligaAbas(cap);
    var botao = cap.querySelector(".marcar-lido");
    if (botao && botao.dataset.ligado !== "1") {
      botao.dataset.ligado = "1";
      botao.addEventListener("click", function () { marca(cap.id, !estaLido(cap.id)); });
    }
    pintaBotaoLido();
  }

  /* ------------------------------------------------ navegação por hash */

  function capituloDe(elemento) {
    while (elemento && !elemento.classList.contains("capitulo")) { elemento = elemento.parentElement; }
    return elemento;
  }

  function mostrar(id, rolarPara) {
    var alvo = document.getElementById(id);
    var cap = alvo ? capituloDe(alvo) : null;
    if (!cap) { cap = capitulos[0]; }

    capitulos.forEach(function (c) { c.hidden = c !== cap; });
    preparaCapitulo(cap);

    elos.forEach(function (a) {
      var ativo = a.getAttribute("data-id") === cap.id;
      a.classList.toggle("ativo", ativo);
      if (ativo) { a.setAttribute("aria-current", "page"); } else { a.removeAttribute("aria-current"); }
    });

    document.title = (cap.getAttribute("data-titulo") || "") + " — " + LIVRO_TITULO;
    guarda(CHAVE_ULTIMO, cap.id);
    corpo.classList.remove("sumario-aberto");

    if (rolarPara !== false) {
      if (alvo && alvo !== cap) {
        alvo.scrollIntoView({ block: "start" });
      } else {
        window.scrollTo(0, 0);
      }
    }
    pintaBotaoLido();
    atualizaProgresso();
    if (termoAtivo) { destaca(cap, termoAtivo); }
    setTimeout(verificaLeituraCompleta, 400);
  }

  window.addEventListener("hashchange", function () {
    mostrar((location.hash || "").replace(/^#/, ""));
  });

  /* --------------------- marcação automática ao terminar o capítulo */

  function verificaLeituraCompleta() {
    var cap = capitulos.find(function (c) { return !c.hidden; });
    if (!cap || estaLido(cap.id)) { return; }
    if (!LIVRO_CAPS.some(function (c) { return c.id === cap.id; })) { return; }

    var h = document.documentElement;
    var rolavel = h.scrollHeight - h.clientHeight;
    if (rolavel < 200) {
      // capítulo que cabe na tela: conta como lido após alguns segundos
      if (!cap.dataset.temporizador) {
        cap.dataset.temporizador = "1";
        setTimeout(function () { if (!cap.hidden) { marca(cap.id, true); } }, 8000);
      }
      return;
    }
    if (h.scrollTop / rolavel > 0.9) { marca(cap.id, true); }
  }

  /* ------------------------------------------- busca no texto completo */

  var indice = null;
  var termoAtivo = "";

  function montaIndice() {
    if (indice) { return indice; }
    indice = capitulos.map(function (cap) {
      var texto = cap.textContent.replace(/\s+/g, " ").trim();
      return {
        id: cap.id,
        titulo: cap.getAttribute("data-titulo") || "Capa",
        texto: texto,
        normal: semAcento(texto)
      };
    });
    return indice;
  }

  function trecho(texto, pos, termo) {
    var ini = Math.max(0, pos - 60);
    var fim = Math.min(texto.length, pos + termo.length + 90);
    return (ini > 0 ? "…" : "") + texto.slice(ini, fim).trim() + (fim < texto.length ? "…" : "");
  }

  function mostraResultados(termo) {
    var alvo = semAcento(termo);
    var achados = [];
    montaIndice().forEach(function (item) {
      var n = 0, de = 0, primeiro = -1;
      while (true) {
        var p = item.normal.indexOf(alvo, de);
        if (p === -1) { break; }
        if (primeiro === -1) { primeiro = p; }
        n++; de = p + alvo.length;
        if (n > 99) { break; }
      }
      if (n) { achados.push({ id: item.id, titulo: item.titulo, n: n, trecho: trecho(item.texto, primeiro, termo) }); }
    });

    resultados.innerHTML = "";
    if (!achados.length) {
      resultados.innerHTML = '<p class="vazio">Nada encontrado para <b>' +
        termo.replace(/[<>&]/g, "") + "</b>.</p>";
      resultados.hidden = false;
      listaCapitulos.hidden = true;
      return;
    }

    achados.sort(function (a, b) { return b.n - a.n; });
    var total = achados.reduce(function (s, a) { return s + a.n; }, 0);
    var cabeca = document.createElement("p");
    cabeca.className = "cabeca-resultados";
    cabeca.textContent = total + (total === 1 ? " ocorrência em " : " ocorrências em ") +
                         achados.length + (achados.length === 1 ? " capítulo" : " capítulos");
    resultados.appendChild(cabeca);

    achados.forEach(function (a) {
      var link = document.createElement("a");
      link.className = "resultado";
      link.href = "#" + a.id;
      link.innerHTML = "<b>" + a.titulo + "</b><span class=\"contagem\">" + a.n + "</span>" +
                       "<em>" + a.trecho.replace(/[<>&]/g, " ") + "</em>";
      link.addEventListener("click", function () {
        termoAtivo = termo;
        corpo.classList.remove("sumario-aberto");
      });
      resultados.appendChild(link);
    });

    resultados.hidden = false;
    listaCapitulos.hidden = true;
  }

  function limpaDestaque(cap) {
    if (cap.dataset.original) {
      cap.innerHTML = cap.dataset.original;
      delete cap.dataset.original;
      religa(cap);
    }
  }

  function destaca(cap, termo) {
    limpaDestaque(cap);
    if (!termo || termo.length < 2) { return; }
    cap.dataset.original = cap.innerHTML;

    var alvo = semAcento(termo);
    var caminhante = document.createTreeWalker(cap, NodeFilter.SHOW_TEXT, {
      acceptNode: function (no) {
        if (!no.nodeValue.trim()) { return NodeFilter.FILTER_REJECT; }
        var pai = no.parentNode.nodeName;
        if (pai === "SCRIPT" || pai === "STYLE" || pai === "BUTTON") { return NodeFilter.FILTER_REJECT; }
        return semAcento(no.nodeValue).indexOf(alvo) === -1
          ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT;
      }
    });

    var nos = [], no, primeiro = null;
    while ((no = caminhante.nextNode())) { nos.push(no); }

    nos.forEach(function (texto) {
      var valor = texto.nodeValue, normal = semAcento(valor);
      var frag = document.createDocumentFragment();
      var de = 0, p;
      while ((p = normal.indexOf(alvo, de)) !== -1) {
        if (p > de) { frag.appendChild(document.createTextNode(valor.slice(de, p))); }
        var m = document.createElement("mark");
        m.textContent = valor.slice(p, p + alvo.length);
        frag.appendChild(m);
        if (!primeiro) { primeiro = m; }
        de = p + alvo.length;
      }
      frag.appendChild(document.createTextNode(valor.slice(de)));
      texto.parentNode.replaceChild(frag, texto);
    });

    if (primeiro) { primeiro.scrollIntoView({ block: "center" }); }
  }

  if (busca) {
    var atraso;
    busca.addEventListener("input", function () {
      clearTimeout(atraso);
      atraso = setTimeout(function () {
        var termo = busca.value.trim();
        if (termo.length < 2) {
          resultados.hidden = true;
          listaCapitulos.hidden = false;
          termoAtivo = "";
          capitulos.forEach(limpaDestaque);
          return;
        }
        mostraResultados(termo);
      }, 180);
    });
    busca.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape") {
        busca.value = "";
        busca.dispatchEvent(new Event("input"));
        busca.blur();
      }
    });
  }

  /* ------------------------------------------------------------- abas */

  function ligaAbas(escopo) {
    (escopo || document).querySelectorAll(".abas").forEach(function (grupo) {
      if (grupo.dataset.ligado === "1") { return; }
      grupo.dataset.ligado = "1";
      var botoes = Array.prototype.slice.call(grupo.querySelectorAll(".abas-tira button"));
      var paineis = Array.prototype.slice.call(grupo.querySelectorAll(".aba-painel"));
      botoes.forEach(function (b, i) {
        b.addEventListener("click", function () {
          botoes.forEach(function (o, j) { o.setAttribute("aria-selected", String(i === j)); });
          paineis.forEach(function (p, j) { p.hidden = i !== j; });
        });
        b.addEventListener("keydown", function (ev) {
          var d = ev.key === "ArrowRight" ? 1 : ev.key === "ArrowLeft" ? -1 : 0;
          if (!d) { return; }
          ev.preventDefault();
          var alvo = botoes[(i + d + botoes.length) % botoes.length];
          alvo.focus(); alvo.click();
        });
      });
    });
  }
  ligaAbas(document);

  /* ------------------------------------------------------------- tema */

  var btnTema = document.getElementById("alterna-tema");
  function aplicaTema(t) {
    document.documentElement.setAttribute("data-tema", t);
    guarda(CHAVE_TEMA, t);
    if (btnTema) { btnTema.textContent = t === "escuro" ? "Tema claro" : "Tema escuro"; }
  }
  aplicaTema(busca_guardado(CHAVE_TEMA) ||
    (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "escuro" : "claro"));
  if (btnTema) {
    btnTema.addEventListener("click", function () {
      aplicaTema(document.documentElement.getAttribute("data-tema") === "escuro" ? "claro" : "escuro");
    });
  }

  /* -------------------------------------------------- tamanho do texto */

  var escala = parseFloat(busca_guardado(CHAVE_FONTE) || "1");
  function aplicaFonte(v) {
    escala = Math.min(1.5, Math.max(0.85, Math.round(v * 100) / 100));
    document.documentElement.style.setProperty("--escala", escala);
    guarda(CHAVE_FONTE, String(escala));
  }
  aplicaFonte(escala);
  var menor = document.getElementById("fonte-menor");
  var maior = document.getElementById("fonte-maior");
  if (menor) { menor.addEventListener("click", function () { aplicaFonte(escala - 0.08); }); }
  if (maior) { maior.addEventListener("click", function () { aplicaFonte(escala + 0.08); }); }

  /* ------------------------------------------------- zerar o progresso */

  var zerar = document.getElementById("zera-progresso");
  if (zerar) {
    zerar.addEventListener("click", function () {
      if (!window.confirm("Apagar as marcas de leitura de todos os capítulos?")) { return; }
      lidos = {};
      guarda(CHAVE_LIDOS, "{}");
      pintaProgresso();
      pintaBotaoLido();
    });
  }

  /* --------------------------------------------- retomar de onde parou */

  (function montaRetomar() {
    var alvo = document.getElementById("retomar");
    var ultimo = busca_guardado(CHAVE_ULTIMO);
    if (!alvo || !ultimo || ultimo === "capa") { return; }
    var dados = LIVRO_CAPS.filter(function (c) { return c.id === ultimo; })[0];
    if (!dados) { return; }
    alvo.innerHTML = '<a href="#' + dados.id + '"><span>Continuar de onde parou</span><b>' +
      "Capítulo " + dados.n + ". " + dados.titulo + "</b></a>";
    alvo.hidden = false;
  })();

  /* --------------------------------- barra de progresso e voltar ao topo */

  var aoTopo = document.getElementById("ao-topo");
  function atualizaProgresso() {
    var h = document.documentElement;
    var total = h.scrollHeight - h.clientHeight;
    if (progresso) { progresso.style.width = (total > 40 ? (h.scrollTop / total) * 100 : 0) + "%"; }
    if (aoTopo) { aoTopo.hidden = h.scrollTop < 600; }
  }
  window.addEventListener("scroll", function () {
    atualizaProgresso();
    verificaLeituraCompleta();
  }, { passive: true });
  if (aoTopo) {
    aoTopo.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: "smooth" }); });
  }

  var btnSumario = document.getElementById("abre-sumario");
  if (btnSumario) {
    btnSumario.addEventListener("click", function () { corpo.classList.toggle("sumario-aberto"); });
  }
  var btnImprimir = document.getElementById("imprime-tudo");
  if (btnImprimir) { btnImprimir.addEventListener("click", function () { window.print(); }); }

  /* ---------------------------------------------------------- teclado */

  document.addEventListener("keydown", function (ev) {
    if (ev.target.tagName === "INPUT" || ev.target.tagName === "TEXTAREA" ||
        ev.metaKey || ev.ctrlKey || ev.altKey) { return; }
    var atual = capitulos.findIndex(function (c) { return !c.hidden; });
    if (ev.key === "ArrowRight" || ev.key === "j") {
      if (atual < capitulos.length - 1) { location.hash = capitulos[atual + 1].id; }
    } else if (ev.key === "ArrowLeft" || ev.key === "k") {
      if (atual > 0) { location.hash = capitulos[atual - 1].id; }
    } else if (ev.key === "/") {
      ev.preventDefault();
      corpo.classList.add("sumario-aberto");
      if (busca) { busca.focus(); }
    } else if (ev.key === "m" || ev.key === "M") {
      var cap = capitulos[atual];
      if (cap) { marca(cap.id, !estaLido(cap.id)); }
    }
  });

  /* ------------------------------------------------------------ início */

  var inicial = (location.hash || "").replace(/^#/, "") || busca_guardado(CHAVE_ULTIMO) || capitulos[0].id;
  mostrar(inicial, false);
  pintaProgresso();
})();

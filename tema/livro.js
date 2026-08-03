/* ------------------------------------------------------------------
   A Estatística na Pesquisa Clínica — comportamento da página do livro
   Embutido em livro.html pelo construir.py. Sem dependência externa.
   ------------------------------------------------------------------ */
(function () {
  "use strict";

  var capitulos = Array.prototype.slice.call(document.querySelectorAll(".capitulo"));
  var elos = Array.prototype.slice.call(document.querySelectorAll("#sumario a[data-id]"));
  var busca = document.getElementById("busca");
  var progresso = document.getElementById("barra-progresso");
  var corpo = document.body;

  /* ------------------------------------------------ navegacao por hash */

  function mostrar(id, rolarAoTopo) {
    var alvo = document.getElementById(id) ? id : capitulos[0].id;
    capitulos.forEach(function (c) { c.hidden = c.id !== alvo; });
    elos.forEach(function (a) {
      var ativo = a.getAttribute("data-id") === alvo;
      a.classList.toggle("ativo", ativo);
      if (ativo) { a.setAttribute("aria-current", "page"); } else { a.removeAttribute("aria-current"); }
    });
    var cap = document.getElementById(alvo);
    document.title = (cap.getAttribute("data-titulo") || "") + " — " + LIVRO_TITULO;
    try { localStorage.setItem("epc-ultimo", alvo); } catch (e) {}
    if (rolarAoTopo !== false) { window.scrollTo(0, 0); }
    corpo.classList.remove("sumario-aberto");
    atualizaProgresso();
  }

  function daHash() {
    var id = (location.hash || "").replace(/^#/, "");
    if (!id) {
      try { id = localStorage.getItem("epc-ultimo") || ""; } catch (e) { id = ""; }
    }
    mostrar(id || capitulos[0].id, false);
  }

  window.addEventListener("hashchange", function () { mostrar((location.hash || "").replace(/^#/, "")); });

  /* ------------------------------------------------------------ busca */

  if (busca) {
    busca.addEventListener("input", function () {
      var termo = busca.value.trim().toLowerCase();
      elos.forEach(function (a) {
        var texto = (a.textContent + " " + (a.getAttribute("data-busca") || "")).toLowerCase();
        a.classList.toggle("oculto", termo.length > 1 && texto.indexOf(termo) === -1);
      });
      document.querySelectorAll("#sumario .parte").forEach(function (p) {
        var visiveis = 0, no = p.nextElementSibling;
        while (no && no.tagName === "A") {
          if (!no.classList.contains("oculto")) { visiveis++; }
          no = no.nextElementSibling;
        }
        p.style.display = visiveis ? "" : "none";
      });
    });
  }

  /* ------------------------------------------------------------- abas */

  document.querySelectorAll(".abas").forEach(function (grupo) {
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
        botoes[(i + d + botoes.length) % botoes.length].focus();
        botoes[(i + d + botoes.length) % botoes.length].click();
      });
    });
  });

  /* ------------------------------------------------------------- tema */

  var btnTema = document.getElementById("alterna-tema");
  function aplicaTema(t) {
    document.documentElement.setAttribute("data-tema", t);
    try { localStorage.setItem("epc-tema", t); } catch (e) {}
    if (btnTema) { btnTema.textContent = t === "escuro" ? "Tema claro" : "Tema escuro"; }
  }
  var temaSalvo = null;
  try { temaSalvo = localStorage.getItem("epc-tema"); } catch (e) {}
  aplicaTema(temaSalvo || (window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches ? "escuro" : "claro"));
  if (btnTema) {
    btnTema.addEventListener("click", function () {
      aplicaTema(document.documentElement.getAttribute("data-tema") === "escuro" ? "claro" : "escuro");
    });
  }

  /* -------------------------------------------------------- progresso */

  function atualizaProgresso() {
    if (!progresso) { return; }
    var h = document.documentElement;
    var total = h.scrollHeight - h.clientHeight;
    progresso.style.width = (total > 40 ? (h.scrollTop / total) * 100 : 0) + "%";
  }
  window.addEventListener("scroll", atualizaProgresso, { passive: true });

  /* ------------------------------------------------- sumario no celular */

  var btnSumario = document.getElementById("abre-sumario");
  if (btnSumario) {
    btnSumario.addEventListener("click", function () { corpo.classList.toggle("sumario-aberto"); });
  }

  /* --------------------------------------------------------- impressao */

  var btnImprimir = document.getElementById("imprime-tudo");
  if (btnImprimir) { btnImprimir.addEventListener("click", function () { window.print(); }); }

  /* ---------------------------------------------------------- teclado */

  document.addEventListener("keydown", function (ev) {
    if (ev.target.tagName === "INPUT" || ev.target.tagName === "TEXTAREA" || ev.metaKey || ev.ctrlKey) {
      if (ev.key === "Escape" && ev.target === busca) { busca.value = ""; busca.dispatchEvent(new Event("input")); busca.blur(); }
      return;
    }
    var atual = capitulos.findIndex(function (c) { return !c.hidden; });
    if (ev.key === "ArrowRight" || ev.key === "j") {
      if (atual < capitulos.length - 1) { location.hash = capitulos[atual + 1].id; }
    } else if (ev.key === "ArrowLeft" || ev.key === "k") {
      if (atual > 0) { location.hash = capitulos[atual - 1].id; }
    } else if (ev.key === "/") {
      ev.preventDefault();
      if (busca) { corpo.classList.add("sumario-aberto"); busca.focus(); }
    }
  });

  daHash();
})();

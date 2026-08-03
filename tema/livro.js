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
  var CHAVE_EXERCICIOS = "epc-exercicios";
  var CHAVE_QUIZ = "epc-quiz";

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
  var resolvidos = {};
  var quizzes = {};
  (function carregaLidos() {
    try { lidos = JSON.parse(busca_guardado(CHAVE_LIDOS) || "{}") || {}; } catch (e) { lidos = {}; }
    try { resolvidos = JSON.parse(busca_guardado(CHAVE_EXERCICIOS) || "{}") || {}; } catch (e) { resolvidos = {}; }
    try { quizzes = JSON.parse(busca_guardado(CHAVE_QUIZ) || "{}") || {}; } catch (e) { quizzes = {}; }
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
      var totalEx = LIVRO_CAPS.reduce(function (s, c) { return s + (c.exercicios || 0); }, 0);
      var feitos = Object.keys(resolvidos).length;
      var linha = faltam > 0 ? "Faltam cerca de " + duracao(faltam) + " de leitura"
                             : "Você leu o livro inteiro.";
      if (feitos) { linha += " · " + feitos + " de " + totalEx + " exercícios resolvidos"; }
      var ids = Object.keys(quizzes);
      if (ids.length) {
        var certos = 0, possiveis = 0;
        ids.forEach(function (k) { certos += quizzes[k].acertos; possiveis += quizzes[k].total; });
        linha += " · quiz: " + certos + " de " + possiveis + " em " + ids.length +
                 (ids.length === 1 ? " capítulo" : " capítulos");
      }
      rest.textContent = linha;
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

      var extras = document.createElement("p");
      extras.className = "acoes-cap";
      var citar = document.createElement("button");
      citar.type = "button";
      citar.className = "citar-cap";
      citar.textContent = "Como citar este capítulo";
      var erro = document.createElement("a");
      erro.className = "reportar";
      erro.target = "_blank";
      erro.rel = "noopener";
      erro.textContent = "Encontrei um erro aqui";
      erro.href = LIVRO.repositorio + "/issues/new?title=" +
        encodeURIComponent("Correção no capítulo " + dados.n + ": " + dados.titulo) +
        "&body=" + encodeURIComponent(
          "Capítulo " + dados.n + " — " + dados.titulo + "\n" +
          "Endereço: " + LIVRO.url + "#" + cap.id + "\n\n" +
          "Trecho com problema:\n\n\n" +
          "O que parece estar errado:\n\n");
      extras.appendChild(citar);
      extras.appendChild(erro);
      caixa.appendChild(extras);

      if (nav) { cap.insertBefore(caixa, nav); } else { cap.appendChild(caixa); }
    }
    religa(cap);
  }

  /* Trocar o innerHTML (ao destacar e ao limpar a busca) mata os ouvintes de
     evento sem apagar os elementos. Esta função os devolve, e é por isso que
     ela não pode criar nada: quem cria é preparaCapitulo, uma única vez. */
  function religa(cap) {
    /* Trocar o innerHTML preserva o atributo data-ligado no HTML restaurado, mas
       não os ouvintes. Zerar a marca de todos é o que impede componentes mudos
       depois de uma busca: abas, calculadoras e botões de exercício. */
    cap.querySelectorAll("[data-ligado]").forEach(function (e) { e.dataset.ligado = ""; });
    ligaAbas(cap);
    var botao = cap.querySelector(".marcar-lido");
    if (botao && botao.dataset.ligado !== "1") {
      botao.dataset.ligado = "1";
      botao.addEventListener("click", function () { marca(cap.id, !estaLido(cap.id)); });
    }
    ligaExercicios(cap);
    ligaCalculadoras(cap);
    ligaQuiz(cap);
    ligaTermos(cap);
    pintaBotaoLido();
  }

  /* -------------------------------------------------------------- quiz */

  function ligaQuiz(escopo) {
    escopo.querySelectorAll(".quiz").forEach(function (quiz) {
      if (quiz.dataset.ligado === "1") { return; }
      quiz.dataset.ligado = "1";

      var perguntas = Array.prototype.slice.call(quiz.querySelectorAll(".quiz-pergunta"));
      var placar = quiz.querySelector(".quiz-placar");
      var acoes = quiz.querySelector(".quiz-acoes");

      function respondidas() {
        return perguntas.filter(function (p) { return p.dataset.respondida === "1"; });
      }
      function acertos() {
        return perguntas.filter(function (p) { return p.dataset.acertou === "1"; }).length;
      }

      function mostraPlacar() {
        var feitas = respondidas().length;
        if (feitas < perguntas.length) { return; }
        var n = acertos(), total = perguntas.length;
        var recado;
        if (n === total) {
          recado = "Você acertou todas. Siga para o próximo capítulo.";
        } else if (n >= Math.ceil(total * 0.7)) {
          recado = "Bom resultado. Releia as seções indicadas nas que errou e siga adiante.";
        } else if (n >= Math.ceil(total * 0.4)) {
          recado = "Vale reler o capítulo antes de seguir: metade do conteúdo ainda não está firme.";
        } else {
          recado = "Releia o capítulo com calma. Errar aqui é barato; errar no projeto, não.";
        }
        placar.innerHTML = "<b>" + n + " de " + total + "</b> " +
          (n === 1 ? "acerto" : "acertos") + "<p>" + recado + "</p>";
        placar.hidden = false;
        acoes.hidden = false;
        guardaQuiz(quiz.getAttribute("data-quiz"), n, total);
        pintaProgresso();
      }

      perguntas.forEach(function (pergunta) {
        var certa = parseInt(pergunta.getAttribute("data-certa"), 10);
        var botoes = Array.prototype.slice.call(pergunta.querySelectorAll(".quiz-alt"));

        botoes.forEach(function (botao, i) {
          botao.addEventListener("click", function () {
            if (pergunta.dataset.respondida === "1") { return; }
            pergunta.dataset.respondida = "1";
            var acertou = i === certa;
            pergunta.dataset.acertou = acertou ? "1" : "0";

            botoes.forEach(function (b, k) {
              b.disabled = true;
              if (k === certa) { b.classList.add("certa"); }
              else if (k === i) { b.classList.add("errada"); }
              else { b.classList.add("apagada"); }
            });

            var retorno = botao.parentNode.querySelector(".quiz-retorno");
            if (retorno) {
              retorno.hidden = false;
              retorno.classList.add(acertou ? "acerto" : "erro");
            }
            if (!acertou) {
              var certaRetorno = botoes[certa].parentNode.querySelector(".quiz-retorno");
              if (certaRetorno) { certaRetorno.hidden = false; certaRetorno.classList.add("acerto"); }
              var releia = pergunta.querySelector(".quiz-releia");
              if (releia) { releia.hidden = false; }
            }
            mostraPlacar();
          });
        });
      });

      function limpa(pergunta) {
        delete pergunta.dataset.respondida;
        delete pergunta.dataset.acertou;
        pergunta.querySelectorAll(".quiz-alt").forEach(function (b) {
          b.disabled = false;
          b.classList.remove("certa", "errada", "apagada");
        });
        pergunta.querySelectorAll(".quiz-retorno").forEach(function (r) {
          r.hidden = true;
          r.classList.remove("acerto", "erro");
        });
        var releia = pergunta.querySelector(".quiz-releia");
        if (releia) { releia.hidden = true; }
      }

      var refazer = quiz.querySelector(".quiz-refazer");
      if (refazer) {
        refazer.addEventListener("click", function () {
          perguntas.forEach(limpa);
          placar.hidden = true; acoes.hidden = true;
          quiz.querySelector("summary").scrollIntoView({ block: "start" });
        });
      }
      var soErros = quiz.querySelector(".quiz-refazer-erros");
      if (soErros) {
        soErros.addEventListener("click", function () {
          var erradas = perguntas.filter(function (p) { return p.dataset.acertou === "0"; });
          if (!erradas.length) { return; }
          erradas.forEach(limpa);
          placar.hidden = true; acoes.hidden = true;
          erradas[0].scrollIntoView({ block: "center" });
        });
      }
    });
  }

  function guardaQuiz(id, acertos, total) {
    if (!id) { return; }
    quizzes[id] = { acertos: acertos, total: total };
    guarda(CHAVE_QUIZ, JSON.stringify(quizzes));
  }

  /* ---------------------------------------------- exercícios resolvidos */

  function pintaExercicio(caixa) {
    var id = caixa.getAttribute("data-exercicio");
    var botao = caixa.querySelector(".resolvido");
    if (!botao) { return; }
    var feito = !!resolvidos[id];
    caixa.classList.toggle("feito", feito);
    botao.setAttribute("aria-pressed", String(feito));
    botao.textContent = feito ? "✓ resolvido" : "marcar como resolvido";
  }

  function ligaExercicios(cap) {
    cap.querySelectorAll(".exercicio[data-exercicio]").forEach(function (caixa) {
      var botao = caixa.querySelector(".resolvido");
      if (botao && botao.dataset.ligado !== "1") {
        botao.dataset.ligado = "1";
        botao.addEventListener("click", function () {
          var id = caixa.getAttribute("data-exercicio");
          if (resolvidos[id]) { delete resolvidos[id]; } else { resolvidos[id] = 1; }
          guarda(CHAVE_EXERCICIOS, JSON.stringify(resolvidos));
          pintaExercicio(caixa);
          pintaContadorExercicios(cap);
          pintaProgresso();
        });
      }
      pintaExercicio(caixa);
    });
    pintaContadorExercicios(cap);
  }

  function pintaContadorExercicios(cap) {
    var caixas = cap.querySelectorAll(".exercicio[data-exercicio]");
    if (!caixas.length) { return; }
    var feitos = 0;
    caixas.forEach(function (c) { if (resolvidos[c.getAttribute("data-exercicio")]) { feitos++; } });
    var alvo = cap.querySelector(".contador-exercicios");
    if (!alvo) {
      var primeira = caixas[0];
      alvo = document.createElement("p");
      alvo.className = "contador-exercicios";
      primeira.parentNode.insertBefore(alvo, primeira);
    }
    alvo.textContent = feitos + " de " + caixas.length + " exercícios resolvidos neste capítulo";
    alvo.classList.toggle("completo", feitos === caixas.length);
  }

  /* ------------------------------------------------------ calculadoras */

  function fmt(v, casas) {
    if (!isFinite(v)) { return "—"; }
    return v.toFixed(casas === undefined ? 1 : casas).replace(".", ",");
  }

  function wilson(k, n) {
    if (!n) { return [0, 0]; }
    var z = 1.959964, p = k / n, d = 1 + z * z / n;
    var c = (p + z * z / (2 * n)) / d;
    var m = z * Math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d;
    return [Math.max(0, c - m), Math.min(1, c + m)];
  }

  function calculaAmostra(campos) {
    var p1 = campos.p1 / 100, p2 = campos.p2 / 100;
    var za = campos.alfa, zb = campos.poder, perdas = campos.perdas / 100;
    var delta = Math.abs(p1 - p2);
    if (!delta || p1 <= 0 || p1 >= 1 || p2 <= 0 || p2 >= 1) {
      return "<p class=\"erro\">Informe duas proporções diferentes, entre 1% e 99%.</p>";
    }
    var pb = (p1 + p2) / 2;
    var n = Math.pow(za * Math.sqrt(2 * pb * (1 - pb)) +
                     zb * Math.sqrt(p1 * (1 - p1) + p2 * (1 - p2)), 2) / (delta * delta);
    var porGrupo = Math.ceil(n);
    var comPerdas = perdas < 1 ? Math.ceil(porGrupo / (1 - perdas)) : porGrupo;
    return "<p><b>" + porGrupo + "</b> participantes por grupo, <b>" + (porGrupo * 2) +
      "</b> no total.</p><p>Prevendo " + fmt(campos.perdas, 0) + "% de perdas: <b>" + comPerdas +
      "</b> por grupo, <b>" + (comPerdas * 2) + "</b> no total.</p>" +
      "<p class=\"nota-calc\">Diferença a detectar: " + fmt(delta * 100) + " pontos percentuais.</p>";
  }

  function calculaIntervalo(campos) {
    var a = campos.a, n1 = campos.n1, c = campos.c, n2 = campos.n2;
    if (a > n1 || c > n2 || !n1 || !n2) {
      return "<p class=\"erro\">Os eventos não podem superar o total do grupo.</p>";
    }
    var p1 = a / n1, p2 = c / n2, i1 = wilson(a, n1), i2 = wilson(c, n2);
    var dif = p1 - p2;
    var ep = Math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2);
    var li = dif - 1.959964 * ep, ls = dif + 1.959964 * ep;
    var linhas = "<table><tr><td>Intervenção</td><td>" + fmt(p1 * 100) + "% (IC95% " +
      fmt(i1[0] * 100) + " a " + fmt(i1[1] * 100) + ")</td></tr>" +
      "<tr><td>Controle</td><td>" + fmt(p2 * 100) + "% (IC95% " +
      fmt(i2[0] * 100) + " a " + fmt(i2[1] * 100) + ")</td></tr>" +
      "<tr><td>Diferença absoluta</td><td>" + fmt(dif * 100) + " pp (IC95% " +
      fmt(li * 100) + " a " + fmt(ls * 100) + ")</td></tr>";
    if (p2 > 0) {
      var rr = p1 / p2;
      var eplog = Math.sqrt((1 - p1) / (p1 * n1) + (1 - p2) / (p2 * n2));
      linhas += "<tr><td>Risco relativo</td><td>" + fmt(rr, 2) + " (IC95% " +
        fmt(Math.exp(Math.log(rr) - 1.959964 * eplog), 2) + " a " +
        fmt(Math.exp(Math.log(rr) + 1.959964 * eplog), 2) + ")</td></tr>";
    }
    if (Math.abs(dif) > 0.0001) {
      var nnt = 1 / Math.abs(dif);
      var aviso = (li < 0 && ls > 0) ? " <span class=\"nota-calc\">(o intervalo da diferença " +
        "inclui o zero: o NNT perde sentido)</span>" : "";
      linhas += "<tr><td>Número necessário para tratar</td><td>" + fmt(nnt) + aviso + "</td></tr>";
    }
    return linhas + "</table>";
  }

  function calculaFagan(campos) {
    var pre = campos.pre / 100, sens = campos.sens / 100, esp = campos.esp / 100;
    if (esp >= 1 || pre <= 0 || pre >= 1) {
      return "<p class=\"erro\">Use valores entre 0,1% e 99,9%.</p>";
    }
    var rvp = sens / (1 - esp), rvn = (1 - sens) / esp;
    var odds = pre / (1 - pre);
    var pos = (odds * rvp) / (1 + odds * rvp), neg = (odds * rvn) / (1 + odds * rvn);
    return "<table><tr><td>Razão de verossimilhança positiva</td><td>" + fmt(rvp, 2) + "</td></tr>" +
      "<tr><td>Razão de verossimilhança negativa</td><td>" + fmt(rvn, 2) + "</td></tr>" +
      "<tr><td>Se o teste der <b>positivo</b></td><td><b>" + fmt(pos * 100) + "%</b> de probabilidade</td></tr>" +
      "<tr><td>Se o teste der <b>negativo</b></td><td><b>" + fmt(neg * 100) + "%</b> de probabilidade</td></tr>" +
      "</table><p class=\"nota-calc\">Probabilidade pré-teste de " + fmt(campos.pre) + "%.</p>";
  }

  var CALCULOS = { amostra: calculaAmostra, intervalo: calculaIntervalo, fagan: calculaFagan };

  function ligaCalculadoras(escopo) {
    escopo.querySelectorAll(".calc").forEach(function (calc) {
      var tipo = calc.getAttribute("data-calc");
      var saida = calc.querySelector("[data-saida]");
      var entradas = Array.prototype.slice.call(calc.querySelectorAll("[data-campo]"));
      function roda() {
        var campos = {};
        entradas.forEach(function (e) { campos[e.getAttribute("data-campo")] = parseFloat(e.value); });
        var ok = entradas.every(function (e) { return e.value !== "" && !isNaN(parseFloat(e.value)); });
        saida.innerHTML = ok ? CALCULOS[tipo](campos)
                             : "<p class=\"erro\">Preencha todos os campos.</p>";
      }
      if (calc.dataset.ligado !== "1") {
        calc.dataset.ligado = "1";
        entradas.forEach(function (e) {
          e.addEventListener("input", roda);
          e.addEventListener("change", roda);
        });
      }
      roda();
    });
  }

  /* ------------------------------------------- glossário sob o cursor */

  var termosOrdenados = Object.keys(GLOSSARIO).sort(function (a, b) { return b.length - a.length; });
  var dica = document.getElementById("dica-glossario");

  function ligaTermos(cap) {
    if (cap.id === "cap-C" || cap.dataset.termos === "1") { return; }
    cap.dataset.termos = "1";
    var restantes = {};
    termosOrdenados.forEach(function (t) { restantes[t] = true; });

    var caminhante = document.createTreeWalker(cap, NodeFilter.SHOW_TEXT, {
      acceptNode: function (no) {
        var pai = no.parentNode;
        if (!no.nodeValue.trim()) { return NodeFilter.FILTER_REJECT; }
        while (pai && pai !== cap) {
          var nome = pai.nodeName;
          if (nome === "H1" || nome === "H2" || nome === "H3" || nome === "CODE" ||
              nome === "PRE" || nome === "BUTTON" || nome === "SUMMARY" ||
              nome === "MARK" || pai.classList.contains("termo") ||
              pai.classList.contains("indice-cap") || pai.classList.contains("calc")) {
            return NodeFilter.FILTER_REJECT;
          }
          pai = pai.parentNode;
        }
        return NodeFilter.FILTER_ACCEPT;
      }
    });

    var nos = [], no;
    while ((no = caminhante.nextNode())) { nos.push(no); }

    nos.forEach(function (texto) {
      var valor = texto.nodeValue;
      for (var i = 0; i < termosOrdenados.length; i++) {
        var termo = termosOrdenados[i];
        if (!restantes[termo]) { continue; }
        var pos = semAcento(valor).indexOf(semAcento(termo));
        if (pos === -1) { continue; }
        var antes = valor.charAt(pos - 1), depois = valor.charAt(pos + termo.length);
        if (/[\wÀ-ÿ]/.test(antes) || /[\wÀ-ÿ]/.test(depois)) { continue; }

        var frag = document.createDocumentFragment();
        frag.appendChild(document.createTextNode(valor.slice(0, pos)));
        var marca_termo = document.createElement("span");
        marca_termo.className = "termo";
        marca_termo.setAttribute("tabindex", "0");
        marca_termo.setAttribute("data-termo", termo);
        marca_termo.textContent = valor.slice(pos, pos + termo.length);
        frag.appendChild(marca_termo);
        frag.appendChild(document.createTextNode(valor.slice(pos + termo.length)));
        texto.parentNode.replaceChild(frag, texto);
        restantes[termo] = false;
        return;
      }
    });
  }

  function mostraDica(alvo) {
    if (!dica) { return; }
    var termo = alvo.getAttribute("data-termo");
    dica.innerHTML = "<b>" + termo + "</b>" + GLOSSARIO[termo] +
      ' <a href="#cap-C">ver no glossário</a>';
    dica.hidden = false;
    var r = alvo.getBoundingClientRect();
    var largura = Math.min(320, window.innerWidth - 24);
    dica.style.width = largura + "px";
    var esquerda = Math.min(Math.max(8, r.left), window.innerWidth - largura - 8);
    dica.style.left = esquerda + "px";
    var acima = r.top > dica.offsetHeight + 16;
    dica.style.top = (acima ? r.top - dica.offsetHeight - 8 : r.bottom + 8) + window.scrollY + "px";
  }

  document.addEventListener("mouseover", function (ev) {
    var alvo = ev.target.closest && ev.target.closest(".termo");
    if (alvo) { mostraDica(alvo); }
  });
  document.addEventListener("mouseout", function (ev) {
    if (ev.target.closest && ev.target.closest(".termo") && dica) { dica.hidden = true; }
  });
  document.addEventListener("focusin", function (ev) {
    var alvo = ev.target.closest && ev.target.closest(".termo");
    if (alvo) { mostraDica(alvo); }
  });
  document.addEventListener("focusout", function () { if (dica) { dica.hidden = true; } });

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

  /* -------------------------------- zerar, exportar e importar progresso */

  var zerar = document.getElementById("zera-progresso");
  if (zerar) {
    zerar.addEventListener("click", function () {
      if (!window.confirm("Apagar as marcas de leitura e os exercícios resolvidos?")) { return; }
      lidos = {}; resolvidos = {}; quizzes = {};
      guarda(CHAVE_LIDOS, "{}");
      guarda(CHAVE_EXERCICIOS, "{}");
      guarda(CHAVE_QUIZ, "{}");
      capitulos.forEach(function (c) {
        c.querySelectorAll(".exercicio[data-exercicio]").forEach(pintaExercicio);
        pintaContadorExercicios(c);
      });
      pintaProgresso();
      pintaBotaoLido();
    });
  }

  var exporta = document.getElementById("exporta-progresso");
  if (exporta) {
    exporta.addEventListener("click", function () {
      var pacote = {
        formato: "epc-progresso",
        versao: 1,
        livro: LIVRO.titulo,
        data: new Date().toISOString(),
        lidos: lidos,
        exercicios: resolvidos,
        quiz: quizzes
      };
      var url = URL.createObjectURL(new Blob([JSON.stringify(pacote, null, 1)],
        { type: "application/json" }));
      var a = document.createElement("a");
      a.href = url;
      a.download = "progresso-estatistica-" + new Date().toISOString().slice(0, 10) + ".json";
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      setTimeout(function () { URL.revokeObjectURL(url); }, 2000);
    });
  }

  var importa = document.getElementById("importa-progresso");
  var arquivo = document.getElementById("arquivo-progresso");
  if (importa && arquivo) {
    importa.addEventListener("click", function () { arquivo.click(); });
    arquivo.addEventListener("change", function () {
      var f = arquivo.files && arquivo.files[0];
      if (!f) { return; }
      var leitor = new FileReader();
      leitor.onload = function () {
        try {
          var dados = JSON.parse(leitor.result);
          if (dados.formato !== "epc-progresso") { throw new Error("formato"); }
          lidos = dados.lidos || {};
          resolvidos = dados.exercicios || {};
          quizzes = dados.quiz || {};
          guarda(CHAVE_LIDOS, JSON.stringify(lidos));
          guarda(CHAVE_EXERCICIOS, JSON.stringify(resolvidos));
          guarda(CHAVE_QUIZ, JSON.stringify(quizzes));
          capitulos.forEach(function (c) {
            c.querySelectorAll(".exercicio[data-exercicio]").forEach(pintaExercicio);
            pintaContadorExercicios(c);
          });
          pintaProgresso();
          pintaBotaoLido();
          window.alert("Progresso importado: " + Object.keys(lidos).length +
                       " capítulos lidos e " + Object.keys(resolvidos).length +
                       " exercícios resolvidos.");
        } catch (e) {
          window.alert("Arquivo inválido. Use um arquivo exportado por este livro.");
        }
        arquivo.value = "";
      };
      leitor.readAsText(f);
    });
  }

  /* ------------------------------------------------------- como citar */

  function hoje() {
    var d = new Date();
    var meses = ["jan.", "fev.", "mar.", "abr.", "maio", "jun.",
                 "jul.", "ago.", "set.", "out.", "nov.", "dez."];
    return { abnt: d.getDate() + " " + meses[d.getMonth()] + " " + d.getFullYear(),
             vancouver: d.getFullYear() + " " + meses[d.getMonth()].replace(".", "") + " " + d.getDate() };
  }

  function sobrenomePrimeiro() {
    var partes = LIVRO.autor.trim().split(/\s+/);
    var sobrenome = partes.pop();
    return { abnt: sobrenome.toUpperCase() + ", " + partes.join(" "),
             vancouver: sobrenome + " " + partes.map(function (p) { return p.charAt(0); }).join("") };
  }

  function montaCitacoes(cap) {
    var a = sobrenomePrimeiro(), d = hoje();
    var obra = LIVRO.titulo + ": " + LIVRO.subtitulo;
    var cidade = LIVRO.local.split(",")[0].trim();
    var lista = [];

    lista.push({
      rotulo: "O livro, ABNT",
      texto: a.abnt + ". " + obra + ". " + cidade + ", " + LIVRO.ano +
             ". Disponível em: " + LIVRO.url + ". Acesso em: " + d.abnt + "."
    });
    lista.push({
      rotulo: "O livro, Vancouver",
      texto: a.vancouver + ". " + obra + " [Internet]. " + cidade + "; " + LIVRO.ano +
             " [citado " + d.vancouver + "]. Disponível em: " + LIVRO.url
    });

    if (cap && cap.id !== "capa") {
      var dados = LIVRO_CAPS.filter(function (c) { return c.id === cap.id; })[0];
      if (dados) {
        var endereco = LIVRO.url + "#" + cap.id;
        lista.push({
          rotulo: "Este capítulo, ABNT",
          texto: a.abnt + ". " + dados.titulo + ". In: ______. " + obra + ". " + cidade + ", " +
                 LIVRO.ano + ". cap. " + dados.n + ". Disponível em: " + endereco +
                 ". Acesso em: " + d.abnt + "."
        });
        lista.push({
          rotulo: "Este capítulo, Vancouver",
          texto: a.vancouver + ". " + dados.titulo + ". Em: " + a.vancouver + ". " + obra +
                 " [Internet]. " + cidade + "; " + LIVRO.ano + " [citado " + d.vancouver +
                 "]. cap. " + dados.n + ". Disponível em: " + endereco
        });
      }
    }
    return lista;
  }

  var painelCitar = document.getElementById("painel-citar");
  function abreCitar() {
    if (!painelCitar) { return; }
    var alvo = document.getElementById("citacoes");
    alvo.innerHTML = "";
    montaCitacoes(capitulos.find(function (c) { return !c.hidden; })).forEach(function (item) {
      var bloco = document.createElement("div");
      bloco.className = "citacao";
      var titulo = document.createElement("p");
      titulo.className = "rotulo-citacao";
      titulo.textContent = item.rotulo;
      var texto = document.createElement("p");
      texto.className = "texto-citacao";
      texto.textContent = item.texto;
      var copiar = document.createElement("button");
      copiar.type = "button";
      copiar.textContent = "Copiar";
      copiar.addEventListener("click", function () {
        if (navigator.clipboard) {
          navigator.clipboard.writeText(item.texto).then(function () {
            copiar.textContent = "Copiado";
            setTimeout(function () { copiar.textContent = "Copiar"; }, 1800);
          });
        }
      });
      bloco.appendChild(titulo);
      bloco.appendChild(texto);
      bloco.appendChild(copiar);
      alvo.appendChild(bloco);
    });
    var aviso = document.createElement("p");
    aviso.className = "nota-calc";
    aviso.textContent = "ISBN " + LIVRO.isbn + ". Licença " + LIVRO.licenca + ".";
    alvo.appendChild(aviso);
    if (painelCitar.showModal) { painelCitar.showModal(); } else { painelCitar.setAttribute("open", ""); }
  }

  document.addEventListener("click", function (ev) {
    if (ev.target.id === "abre-citar" || (ev.target.closest && ev.target.closest(".citar-cap"))) {
      ev.preventDefault();
      abreCitar();
    }
  });
  var fechaCitar = document.getElementById("fecha-citar");
  if (fechaCitar && painelCitar) {
    fechaCitar.addEventListener("click", function () {
      if (painelCitar.close) { painelCitar.close(); } else { painelCitar.removeAttribute("open"); }
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

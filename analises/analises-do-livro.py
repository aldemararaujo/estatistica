"""
Calcula TODOS os numeros citados no livro, a partir do banco condutor.

Nenhum resultado impresso no livro pode vir de outro lugar que nao seja este
script. E o que garante que o Capitulo 9 e o Capitulo 14 nao se contradigam, e
e a prova pratica da reprodutibilidade que o Capitulo 7 prega.

Uso:  python analises/analises-do-livro.py
Saida: analises/resultados.md
"""

import io
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
from statsmodels.duration.hazard_regression import PHReg
from statsmodels.duration.survfunc import SurvfuncRight, survdiff

warnings.filterwarnings("ignore")

RAIZ = Path(__file__).parent.parent
d = pd.read_csv(RAIZ / "dados" / "coorte-condutor.csv")
saida = io.StringIO()


def p(*args):
    print(*args, file=saida)


def sec(titulo):
    p(f"\n## {titulo}\n")


def fmt_p(valor):
    return "< 0,001" if valor < 0.001 else f"{valor:.3f}".replace(".", ",")


def br(x, casas=1):
    return f"{x:.{casas}f}".replace(".", ",")


p("# Resultados do caso condutor")
p("\nGerado por `analises/analises-do-livro.py`. Todo número impresso no livro")
p("sai daqui. Para conferir, rode o script e compare.\n")

comp = d.dropna(subset=["cicatrizacao_12sem"])          # com desfecho observado
asp = comp[comp.grupo == "Aspirado"]
ctl = comp[comp.grupo == "Controle"]

# ============================================================ descritiva
sec("Capítulo 8 — Descritiva")

p(f"- n randomizado: {len(d)} ({int((d.grupo=='Aspirado').sum())} aspirado, "
  f"{int((d.grupo=='Controle').sum())} controle)")
p(f"- perdas de seguimento: {int((d.perda_seguimento=='Sim').sum())} "
  f"({int(((d.perda_seguimento=='Sim') & (d.grupo=='Aspirado')).sum())} e "
  f"{int(((d.perda_seguimento=='Sim') & (d.grupo=='Controle')).sum())} por grupo)")
p(f"- área inicial: média {br(d.area_inicial_cm2.mean())} (DP {br(d.area_inicial_cm2.std())}), "
  f"mediana {br(d.area_inicial_cm2.median())} "
  f"(quartis {br(d.area_inicial_cm2.quantile(.25))} e {br(d.area_inicial_cm2.quantile(.75))})")
p(f"- participantes com área acima da média: {int((d.area_inicial_cm2 > d.area_inicial_cm2.mean()).sum())} de {len(d)}")

# ============================================== proporcoes e intervalos
sec("Capítulo 9 — Estimativa e intervalo de confiança")

a = int((asp.cicatrizacao_12sem == "Sim").sum()); na = len(asp)
c = int((ctl.cicatrizacao_12sem == "Sim").sum()); nc = len(ctl)
p1, p2 = a / na, c / nc


def wilson(k, n, z=1.96):
    ph = k / n
    den = 1 + z * z / n
    centro = (ph + z * z / (2 * n)) / den
    meio = z * np.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / den
    return centro - meio, centro + meio


li1, ls1 = wilson(a, na)
li2, ls2 = wilson(c, nc)
dif = p1 - p2
ep_dif = np.sqrt(p1 * (1 - p1) / na + p2 * (1 - p2) / nc)
rr = p1 / p2
ep_log_rr = np.sqrt((1 - p1) / (p1 * na) + (1 - p2) / (p2 * nc))
odds = (a / (na - a)) / (c / (nc - c))
ep_log_or = np.sqrt(1/a + 1/(na-a) + 1/c + 1/(nc-c))

p(f"- cicatrização aspirado: {a}/{na} = {br(100*p1)}% (IC95% Wilson {br(100*li1)} a {br(100*ls1)})")
p(f"- cicatrização controle: {c}/{nc} = {br(100*p2)}% (IC95% Wilson {br(100*li2)} a {br(100*ls2)})")
p(f"- diferença absoluta: {br(100*dif)} pontos percentuais "
  f"(IC95% {br(100*(dif-1.96*ep_dif))} a {br(100*(dif+1.96*ep_dif))})")
p(f"- número necessário para tratar: {br(1/dif)} "
  f"(IC95% {br(1/(dif+1.96*ep_dif))} a {br(1/(dif-1.96*ep_dif))})")
p(f"- risco relativo: {br(rr,2)} "
  f"(IC95% {br(np.exp(np.log(rr)-1.96*ep_log_rr),2)} a {br(np.exp(np.log(rr)+1.96*ep_log_rr),2)})")
p(f"- razão de chances: {br(odds,2)} "
  f"(IC95% {br(np.exp(np.log(odds)-1.96*ep_log_or),2)} a {br(np.exp(np.log(odds)+1.96*ep_log_or),2)})")

r4a = d.loc[d.grupo == "Aspirado", "reducao_area_4sem_pct"].dropna()
r4c = d.loc[d.grupo == "Controle", "reducao_area_4sem_pct"].dropna()
dm = r4a.mean() - r4c.mean()
ep_dm = np.sqrt(r4a.var(ddof=1)/len(r4a) + r4c.var(ddof=1)/len(r4c))
gl = (r4a.var(ddof=1)/len(r4a) + r4c.var(ddof=1)/len(r4c))**2 / (
     (r4a.var(ddof=1)/len(r4a))**2/(len(r4a)-1) + (r4c.var(ddof=1)/len(r4c))**2/(len(r4c)-1))
tcrit = stats.t.ppf(0.975, gl)
dcohen = dm / np.sqrt(((len(r4a)-1)*r4a.var(ddof=1) + (len(r4c)-1)*r4c.var(ddof=1)) /
                      (len(r4a)+len(r4c)-2))
p(f"- redução de área em 4 semanas, aspirado: média {br(r4a.mean())}% (DP {br(r4a.std())}), n = {len(r4a)}")
p(f"- redução de área em 4 semanas, controle: média {br(r4c.mean())}% (DP {br(r4c.std())}), n = {len(r4c)}")
p(f"- diferença de médias: {br(dm)} pontos percentuais "
  f"(IC95% {br(dm-tcrit*ep_dm)} a {br(dm+tcrit*ep_dm)})")
p(f"- d de Cohen: {br(dcohen,2)}")

# ==================================================== testes de hipotese
sec("Capítulo 10 — Teste de hipótese e valor de p")

tab = np.array([[a, na - a], [c, nc - c]])
qui2, pqui, _, _ = stats.chi2_contingency(tab, correction=False)
qui2c, pquic, _, _ = stats.chi2_contingency(tab, correction=True)
_, pfisher = stats.fisher_exact(tab)
p(f"- qui-quadrado de Pearson: {br(qui2,2)}, gl = 1, p = {fmt_p(pqui)}")
p(f"- com correção de continuidade: {br(qui2c,2)}, p = {fmt_p(pquic)}")
p(f"- teste exato de Fisher: p = {fmt_p(pfisher)}")

t, pt = stats.ttest_ind(r4a, r4c, equal_var=False)
u, pu = stats.mannwhitneyu(r4a, r4c, alternative="two-sided")
p(f"- teste t de Welch (redução em 4 semanas): t = {br(t,2)}, p = {fmt_p(pt)}")
p(f"- Mann-Whitney: U = {br(u,0)}, p = {fmt_p(pu)}")

# poder observado para a diferenca planejada e para a observada
def poder(p1, p2, n):
    pb = (p1 + p2) / 2
    z = (abs(p1 - p2) * np.sqrt(n) - 1.96 * np.sqrt(2 * pb * (1 - pb))) / \
        np.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return stats.norm.cdf(z)

p(f"- poder para a diferença planejada (75% x 55%, n = 89 por grupo): {br(100*poder(.75,.55,89))}%")
p(f"- poder para a diferença observada ({br(100*p1)}% x {br(100*p2)}%, n = {na} e {nc}): "
  f"{br(100*poder(p1,p2,min(na,nc)))}%")

# ==================================================== escolha do teste
sec("Capítulo 11 — Escolhendo o teste")

par = comp.dropna(subset=["dor_eva_12sem"])
tp, ptp = stats.ttest_rel(par.dor_eva_basal, par.dor_eva_12sem)
w, pw = stats.wilcoxon(par.dor_eva_basal, par.dor_eva_12sem)
p(f"- dor EVA basal: mediana {br(par.dor_eva_basal.median())}; "
  f"em 12 semanas: mediana {br(par.dor_eva_12sem.median())} (n = {len(par)})")
p(f"- t pareado: t = {br(tp,2)}, p = {fmt_p(ptp)}")
p(f"- Wilcoxon pareado: W = {br(w,0)}, p = {fmt_p(pw)}")

par2 = par.copy()
par2["dor_alta_basal"] = par2.dor_eva_basal >= 5
par2["dor_alta_12"] = par2.dor_eva_12sem >= 5
b = int(((par2.dor_alta_basal) & (~par2.dor_alta_12)).sum())
cc = int(((~par2.dor_alta_basal) & (par2.dor_alta_12)).sum())
mcnemar = (abs(b - cc) - 1) ** 2 / (b + cc)
p(f"- McNemar (dor ≥ 5 antes x depois): discordantes {b} e {cc}, "
  f"qui² = {br(mcnemar,2)}, p = {fmt_p(stats.chi2.sf(mcnemar,1))}")

grupos_centro = [g.reducao_area_4sem_pct.dropna() for _, g in comp.groupby("centro")]
f_anova, pf = stats.f_oneway(*grupos_centro)
h, ph = stats.kruskal(*grupos_centro)
p(f"- ANOVA da redução em 4 semanas por centro: F = {br(f_anova,2)}, p = {fmt_p(pf)}")
p(f"- Kruskal-Wallis por centro: H = {br(h,2)}, p = {fmt_p(ph)}")

evt = d[d.evento_cicatrizacao == 1]
rho, prho = stats.spearmanr(evt.area_inicial_cm2, evt.tempo_ate_cicatrizacao_dias)
rp, prp = stats.pearsonr(evt.area_inicial_cm2, evt.tempo_ate_cicatrizacao_dias)
p(f"- correlação entre área inicial e tempo até cicatrizar (n = {len(evt)}): "
  f"Pearson r = {br(rp,2)} (p = {fmt_p(prp)}), Spearman rô = {br(rho,2)} (p = {fmt_p(prho)})")

# ============================================================= regressao
sec("Capítulo 12 — Regressão e confundimento")

m = comp.dropna(subset=["cicatrizacao_12sem"]).copy()
m["y"] = (m.cicatrizacao_12sem == "Sim").astype(int)
m["asp"] = (m.grupo == "Aspirado").astype(int)
m["dm"] = (m.diabetes == "Sim").astype(int)
m["log_area"] = np.log(m.area_inicial_cm2)
m["log_dur"] = np.log(m.duracao_ulcera_meses)
m["adesao_ok"] = (m.adesao_compressao == "Adequada").astype(int)

bruto = sm.Logit(m.y, sm.add_constant(m[["asp"]])).fit(disp=0)
ajust = sm.Logit(m.y, sm.add_constant(m[["asp", "log_area", "log_dur", "dm", "adesao_ok"]])).fit(disp=0)


def linha_or(mod, var, rotulo):
    b_, se = mod.params[var], mod.bse[var]
    p(f"  - {rotulo}: OR {br(np.exp(b_),2)} "
      f"(IC95% {br(np.exp(b_-1.96*se),2)} a {br(np.exp(b_+1.96*se),2)}), p = {fmt_p(mod.pvalues[var])}")


p(f"- modelo bruto (n = {int(bruto.nobs)}):")
linha_or(bruto, "asp", "aspirado")
p(f"- modelo ajustado (n = {int(ajust.nobs)}), pseudo-R² de McFadden {br(ajust.prsquared,3)}:")
for var, rot in [("asp", "aspirado"), ("log_area", "log da área inicial"),
                 ("log_dur", "log da duração"), ("dm", "diabetes"),
                 ("adesao_ok", "adesão adequada")]:
    linha_or(ajust, var, rot)

lin = sm.OLS(m.reducao_area_4sem_pct, sm.add_constant(
    m[["asp", "log_area", "log_dur", "dm", "adesao_ok"]]), missing="drop").fit()
p(f"- regressão linear da redução em 4 semanas (n = {int(lin.nobs)}, R² = {br(lin.rsquared,3)}):")
for var, rot in [("asp", "aspirado"), ("log_area", "log da área inicial"),
                 ("dm", "diabetes"), ("adesao_ok", "adesão adequada")]:
    b_, se = lin.params[var], lin.bse[var]
    p(f"  - {rot}: coeficiente {br(b_)} pontos percentuais "
      f"(IC95% {br(b_-1.96*se)} a {br(b_+1.96*se)}), p = {fmt_p(lin.pvalues[var])}")

# a mesma pergunta, respondida por uma coorte: confundimento por indicacao
obs = pd.read_csv(RAIZ / "dados" / "coorte-observacional.csv")
obs["y"] = (obs.cicatrizacao_12sem == "Sim").astype(int)
obs["t"] = (obs.recebeu_aspirado == "Sim").astype(int)
obs["log_area"] = np.log(obs.area_inicial_cm2)
obs["log_dur"] = np.log(obs.duracao_ulcera_meses)
obs["dm"] = (obs.diabetes == "Sim").astype(int)
obs["adesao_ok"] = (obs.adesao_compressao == "Adequada").astype(int)

p(f"\n### A mesma pergunta em uma coorte (n = {len(obs)})\n")
tratados = obs[obs.t == 1]; naotratados = obs[obs.t == 0]
p(f"- receberam o aspirado: {len(tratados)} ({br(100*len(tratados)/len(obs),0)}%)")
p(f"- área inicial mediana: {br(tratados.area_inicial_cm2.median())} cm² em quem recebeu, "
  f"{br(naotratados.area_inicial_cm2.median())} cm² em quem não recebeu")
p(f"- duração mediana: {br(tratados.duracao_ulcera_meses.median(),0)} meses em quem recebeu, "
  f"{br(naotratados.duracao_ulcera_meses.median(),0)} meses em quem não recebeu")
p(f"- diabetes: {br(100*(tratados.diabetes=='Sim').mean())}% em quem recebeu, "
  f"{br(100*(naotratados.diabetes=='Sim').mean())}% em quem não recebeu")
p(f"- cicatrização bruta: {br(100*tratados.y.mean())}% em quem recebeu, "
  f"{br(100*naotratados.y.mean())}% em quem não recebeu")
ob = sm.Logit(obs.y, sm.add_constant(obs[["t"]])).fit(disp=0)
oa = sm.Logit(obs.y, sm.add_constant(obs[["t", "log_area", "log_dur", "dm", "adesao_ok"]])).fit(disp=0)
linha_or(ob, "t", "aspirado, bruto")
linha_or(oa, "t", "aspirado, ajustado por área, duração, diabetes e adesão")
p("- efeito verdadeiro embutido na simulação: o mesmo do ensaio randomizado")
p(f"- para comparação, o ensaio randomizado deu OR bruto {br(np.exp(bruto.params['asp']),2)} "
  f"e ajustado {br(np.exp(ajust.params['asp']),2)}")

# ==================================================== testes diagnosticos
sec("Capítulo 13 — Testes diagnósticos")


def desempenho(df, var, corte, maior_e_positivo=True):
    q = df.dropna(subset=[var])
    pos = q[var] >= corte if maior_e_positivo else q[var] <= corte
    doente = q.cicatrizacao_12sem == "Sim"      # "doente" = desfecho de interesse
    vp = int((pos & doente).sum()); fp = int((pos & ~doente).sum())
    fn = int((~pos & doente).sum()); vn = int((~pos & ~doente).sum())
    sens, esp = vp / (vp + fn), vn / (vn + fp)
    return dict(vp=vp, fp=fp, fn=fn, vn=vn, sens=sens, esp=esp,
                vpp=vp / (vp + fp) if vp + fp else float("nan"),
                vpn=vn / (vn + fn) if vn + fn else float("nan"),
                rvp=sens / (1 - esp) if esp < 1 else float("inf"),
                rvn=(1 - sens) / esp)


def auc_ic(df, var):
    q = df.dropna(subset=[var])
    x = q.loc[q.cicatrizacao_12sem == "Sim", var]
    y = q.loc[q.cicatrizacao_12sem == "Não", var]
    u_, _ = stats.mannwhitneyu(x, y, alternative="two-sided")
    a_ = u_ / (len(x) * len(y))
    q1 = a_ / (2 - a_); q2 = 2 * a_ ** 2 / (1 + a_)
    se = np.sqrt((a_*(1-a_) + (len(x)-1)*(q1-a_**2) + (len(y)-1)*(q2-a_**2)) / (len(x)*len(y)))
    return a_, a_ - 1.96 * se, a_ + 1.96 * se, len(x), len(y)


for var, rotulo, cortes in [("tcpo2_basal", "TcPO₂ basal (mmHg)", [30, 35, 40]),
                            ("reducao_area_4sem_pct", "redução de área em 4 semanas (%)", [30, 40, 50])]:
    a_, li, ls, nx, ny = auc_ic(comp, var)
    p(f"- {rotulo}: AUC {br(a_,3)} (IC95% {br(li,3)} a {br(ls,3)}); "
      f"{nx} cicatrizaram, {ny} não")
    for corte in cortes:
        r = desempenho(comp, var, corte)
        p(f"  - corte ≥ {corte}: sensibilidade {br(100*r['sens'])}%, "
          f"especificidade {br(100*r['esp'])}%, VPP {br(100*r['vpp'])}%, "
          f"VPN {br(100*r['vpn'])}%, RV+ {br(r['rvp'],2)}, RV− {br(r['rvn'],2)} "
          f"(VP {r['vp']}, FP {r['fp']}, FN {r['fn']}, VN {r['vn']})")

pre = (comp.cicatrizacao_12sem == "Sim").mean()
p(f"- prevalência do desfecho (probabilidade pré-teste): {br(100*pre)}%")

# ============================================================= sobrevida
sec("Capítulo 14 — Análise de sobrevida")

for nome, sub in [("Aspirado", d[d.grupo == "Aspirado"]), ("Controle", d[d.grupo == "Controle"])]:
    sf = SurvfuncRight(sub.tempo_ate_cicatrizacao_dias, sub.evento_cicatrizacao)
    tempos, surv = np.asarray(sf.surv_times), np.asarray(sf.surv_prob)
    mediana = tempos[surv <= 0.5][0] if (surv <= 0.5).any() else None
    def cum(t):
        idx = tempos <= t
        return 1 - (surv[idx][-1] if idx.any() else 1.0)
    p(f"- {nome}: eventos {int(sub.evento_cicatrizacao.sum())}/{len(sub)}; "
      f"tempo mediano até cicatrizar {mediana if mediana else 'não atingido'} dias; "
      f"incidência acumulada 28 d {br(100*cum(28))}%, 56 d {br(100*cum(56))}%, "
      f"84 d {br(100*cum(84))}%")

chi_lr, p_lr = survdiff(d.tempo_ate_cicatrizacao_dias, d.evento_cicatrizacao, d.grupo)
p(f"- log-rank: qui² = {br(chi_lr,2)}, gl = 1, p = {fmt_p(p_lr)}")

cox_b = PHReg(d.tempo_ate_cicatrizacao_dias, sm.add_constant(
    pd.DataFrame({"asp": (d.grupo == "Aspirado").astype(int)}))[["asp"]],
    status=d.evento_cicatrizacao).fit()
X = pd.DataFrame({
    "asp": (d.grupo == "Aspirado").astype(int),
    "log_area": np.log(d.area_inicial_cm2),
    "log_dur": np.log(d.duracao_ulcera_meses),
    "dm": (d.diabetes == "Sim").astype(int),
    "adesao_ok": (d.adesao_compressao == "Adequada").astype(int)})
cox_a = PHReg(d.tempo_ate_cicatrizacao_dias, X, status=d.evento_cicatrizacao).fit()


def linha_hr(mod, X_, var, rotulo):
    i = list(X_.columns).index(var)
    b_, se = mod.params[i], mod.bse[i]
    p(f"  - {rotulo}: HR {br(np.exp(b_),2)} "
      f"(IC95% {br(np.exp(b_-1.96*se),2)} a {br(np.exp(b_+1.96*se),2)}), p = {fmt_p(mod.pvalues[i])}")


p("- Cox bruto:")
linha_hr(cox_b, pd.DataFrame({"asp": []}).reindex(columns=["asp"]), "asp", "aspirado")
p("- Cox ajustado:")
for var, rot in [("asp", "aspirado"), ("log_area", "log da área inicial"),
                 ("log_dur", "log da duração"), ("dm", "diabetes"),
                 ("adesao_ok", "adesão adequada")]:
    linha_hr(cox_a, X, var, rot)

# ============================================== tamanho de amostra e CONSORT
sec("Capítulo 6 — Tamanho da amostra (conferência da conta)")

pa, pc_ = 0.75, 0.55
pbar = (pa + pc_) / 2
n_grupo = ((1.96 * np.sqrt(2 * pbar * (1 - pbar)) +
            0.8416 * np.sqrt(pa * (1 - pa) + pc_ * (1 - pc_))) ** 2) / (pa - pc_) ** 2
p(f"- 55% x 75%, α = 5% bilateral, poder 80%: n = {np.ceil(n_grupo):.0f} por grupo")
p(f"- com 10% de perdas previstas: {np.ceil(np.ceil(n_grupo)/0.9):.0f} por grupo, "
  f"arredondado para 100")
for delta in [0.10, 0.15, 0.20, 0.25]:
    pa_ = pc_ + delta
    pb_ = (pa_ + pc_) / 2
    n_ = ((1.96 * np.sqrt(2*pb_*(1-pb_)) + 0.8416*np.sqrt(pa_*(1-pa_) + pc_*(1-pc_)))**2) / delta**2
    p(f"  - para detectar {br(100*delta,0)} pontos percentuais: {np.ceil(n_):.0f} por grupo")

sec("Capítulo 15 — Números do diagrama CONSORT")

p(f"- randomizados: {len(d)}, 100 por grupo")
p("- receberam o alocado: 100 e 100")
p(f"- perdas de seguimento: {int(((d.perda_seguimento=='Sim') & (d.grupo=='Aspirado')).sum())} "
  f"e {int(((d.perda_seguimento=='Sim') & (d.grupo=='Controle')).sum())}")
p(f"- analisados para o desfecho primário: {na} e {nc}")
p(f"- infecção da ferida: {int(((d.infeccao_ferida=='Sim') & (d.grupo=='Aspirado')).sum())} "
  f"e {int(((d.infeccao_ferida=='Sim') & (d.grupo=='Controle')).sum())}")
p(f"- dor no sítio de punção (só no grupo aspirado): "
  f"{int((d.dor_sitio_puncao=='Sim').sum())} de 100")

texto = saida.getvalue()
destino = RAIZ / "analises" / "resultados.md"
destino.write_text(texto, encoding="utf-8")
print(f"resultados escritos em {destino} ({len(texto.splitlines())} linhas)")

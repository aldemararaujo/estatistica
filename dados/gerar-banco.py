"""
Gera o banco de dados sintetico do caso condutor do livro
"A Estatistica na Pesquisa Clinica".

Estudo: ensaio clinico randomizado, aspirado de medula ossea + terapia
compressiva versus terapia compressiva isolada, em ulceras venosas de
membros inferiores. Desfecho primario: cicatrizacao completa em 12 semanas.

Os dados NAO sao reais. Sao simulados a partir de um modelo de riscos
proporcionais de Weibull, calibrado para reproduzir magnitudes de efeito
compativeis com a literatura de ulcera venosa. O objetivo e didatico:
todos os desfechos do livro (binario, continuo, tempo ate evento) nascem
do mesmo processo gerador e, por isso, conversam entre si.

Uso:  python gerar-banco.py
Saida: coorte-condutor.csv
"""

from pathlib import Path

import numpy as np
import pandas as pd

SEMENTE = 2026
N_POR_GRUPO = 100
FIM_SEGUIMENTO_DIAS = 84  # 12 semanas

rng = np.random.default_rng(SEMENTE)
n = N_POR_GRUPO * 2

# ---------------------------------------------------------------- alocacao
# Randomizacao 1:1 em blocos de 4, estratificada por centro.
centro = rng.choice(["Centro A", "Centro B", "Centro C"], size=n, p=[0.40, 0.35, 0.25])
grupo = np.empty(n, dtype=object)
for c in np.unique(centro):
    idx = np.where(centro == c)[0]
    rng.shuffle(idx)
    aloc = []
    for _ in range(int(np.ceil(len(idx) / 4))):
        bloco = ["Aspirado", "Aspirado", "Controle", "Controle"]
        rng.shuffle(bloco)
        aloc.extend(bloco)
    grupo[idx] = aloc[: len(idx)]
aspirado = (grupo == "Aspirado").astype(int)

# ------------------------------------------------------- variaveis basais
idade = np.clip(rng.normal(62, 11, n), 40, 88).round(0)
sexo = rng.choice(["Feminino", "Masculino"], size=n, p=[0.58, 0.42])
imc = np.clip(rng.normal(29.4, 4.6, n), 18, 48).round(1)
diabetes = rng.binomial(1, 0.24, n)
tabagismo = rng.choice(["Nunca fumou", "Ex-fumante", "Fumante atual"], size=n,
                       p=[0.45, 0.34, 0.21])

# Indice tornozelo-braquial: criterio de inclusao exige >= 0,80
itb = np.clip(rng.normal(1.02, 0.09, n), 0.80, 1.35).round(2)

# Area e duracao da ulcera: assimetricas a direita (log-normais)
area_inicial = np.exp(rng.normal(np.log(8.0), 0.75, n)).round(1)
duracao_meses = np.exp(rng.normal(np.log(14.0), 0.70, n)).round(0)
recidivante = rng.binomial(1, 0.55, n)

# Adesao a terapia compressiva (aferida em 12 semanas, mas ligada ao perfil basal)
p_adesao = 1 / (1 + np.exp(-(1.1 - 0.35 * diabetes - 0.020 * (imc - 29.4))))
adesao = np.where(rng.random(n) < p_adesao, "Adequada", "Inadequada")
adesao_ok = (adesao == "Adequada").astype(int)

# Pressao transcutanea de oxigenio: teste indice do capitulo de diagnostico
tcpo2 = (38 + 22 * (itb - 1.02) - 4.5 * diabetes - 2.5 * (tabagismo == "Fumante atual")
         + rng.normal(0, 6.5, n)).round(1)

# ------------------------------------- tempo ate cicatrizacao (Weibull PH)
FORMA = 1.5          # hazard crescente no tempo
ESCALA = 0.00120     # calibrado para ~55% de cicatrizacao no controle
LATENCIA = 10        # nenhuma ulcera venosa cicatriza antes de 10 dias

lp = (0.75 * aspirado
      - 0.55 * np.log(area_inicial / 8.0)
      - 0.30 * np.log(duracao_meses / 14.0)
      - 0.45 * diabetes
      - 0.20 * recidivante
      + 0.40 * adesao_ok
      + 0.055 * (tcpo2 - 38)
      - 0.25 * (tabagismo == "Fumante atual"))
lp = lp - 0.02  # centraliza o perfil medio do grupo controle

u = rng.random(n)
tempo_evento = LATENCIA + (-np.log(u) / (ESCALA * np.exp(lp))) ** (1 / FORMA)

# ------------------------------------------------- perdas de seguimento
perdeu = rng.random(n) < 0.105
tempo_perda = rng.uniform(14, FIM_SEGUIMENTO_DIAS, n)
perdeu = perdeu & (tempo_perda < np.minimum(tempo_evento, FIM_SEGUIMENTO_DIAS))

tempo_obs = np.minimum(np.minimum(tempo_evento, FIM_SEGUIMENTO_DIAS),
                       np.where(perdeu, tempo_perda, np.inf))
evento = ((tempo_evento <= FIM_SEGUIMENTO_DIAS) & ~perdeu).astype(int)

cicatrizacao = np.where(perdeu, np.nan, evento.astype(float))

# ------------------------------------------------------ desfechos continuos
# Area residual: zero se ja cicatrizou; caso contrario, o que resta do caminho
# ate a cicatrizacao prevista para aquele participante.
def area_residual(dia, ruido):
    """O ruido representa a variabilidade da evolucao e o erro de medida da
    planimetria. O teto de 1,5 vez a area inicial impede pioras implausiveis."""
    fracao = np.clip(dia / tempo_evento, 0, 1) ** 1.25
    resid = area_inicial * np.clip(1 - fracao, 0, 1) * np.exp(rng.normal(0, ruido, n))
    resid = np.minimum(resid, 1.5 * area_inicial)
    return np.where(tempo_evento <= dia, 0.0, resid).round(1)

# Aos 28 dias quase ninguem cicatrizou ainda: e a afericao continua util, sem
# o efeito teto que a area de 12 semanas tem. A reducao >= 40% da area em 4
# semanas e, alem disso, marcador prognostico consagrado na ulcera venosa.
area_04 = area_residual(28, 0.45)
area_04 = np.where(perdeu & (tempo_perda < 28), np.nan, area_04)

area_12 = area_residual(FIM_SEGUIMENTO_DIAS, 0.35)
area_12 = np.where(perdeu, np.nan, area_12)

dor_basal = np.clip(rng.normal(5.4, 1.8, n), 0, 10).round(0)
alivio = np.where(evento == 1, 3.4, 1.3) + rng.normal(0, 1.1, n)
dor_12 = np.where(perdeu, np.nan, np.clip(dor_basal - alivio, 0, 10).round(0))

# ------------------------------------------------------- eventos adversos
infeccao = rng.binomial(1, np.where(aspirado == 1, 0.07, 0.09), n)
# Dor no sitio de puncao so existe em quem recebeu o aspirado: ausencia
# estrutural, nao dado faltante.
dor_puncao = np.where(aspirado == 1, rng.binomial(1, 0.31, n), np.nan)

# ------------------------------------- faltantes deliberados (didaticos)
tcpo2 = np.where(rng.random(n) < 0.05, np.nan, tcpo2)   # falha do equipamento
imc = np.where(rng.random(n) < 0.02, np.nan, imc)       # nao aferido

def sim_nao(v):
    """1 -> 'Sim', 0 -> 'Não', NaN -> ausente (mantido como faltante)."""
    return pd.Series(v).map({1.0: "Sim", 0.0: "Não"})

dados = pd.DataFrame({
    "id": [f"P{i:03d}" for i in range(1, n + 1)],
    "centro": centro,
    "grupo": grupo,
    "idade": idade.astype(int),
    "sexo": sexo,
    "imc": imc,
    "diabetes": sim_nao(diabetes.astype(float)),
    "tabagismo": tabagismo,
    "itb": itb,
    "area_inicial_cm2": area_inicial,
    "duracao_ulcera_meses": duracao_meses.astype(int),
    "ulcera_recidivante": sim_nao(recidivante.astype(float)),
    "adesao_compressao": adesao,
    "tcpo2_basal": tcpo2,
    "dor_eva_basal": dor_basal.astype(int),
    "area_4sem_cm2": area_04,
    "reducao_area_4sem_pct": np.where(np.isnan(area_04), np.nan,
                                      (100 * (area_inicial - area_04) / area_inicial).round(1)),
    "area_12sem_cm2": area_12,
    "reducao_area_12sem_pct": np.where(np.isnan(area_12), np.nan,
                                       (100 * (area_inicial - area_12) / area_inicial).round(1)),
    "dor_eva_12sem": dor_12,
    "cicatrizacao_12sem": sim_nao(cicatrizacao),
    "tempo_ate_cicatrizacao_dias": np.round(tempo_obs, 0).astype(int),
    "evento_cicatrizacao": evento,
    "perda_seguimento": sim_nao(perdeu.astype(float)),
    "infeccao_ferida": sim_nao(infeccao.astype(float)),
    "dor_sitio_puncao": sim_nao(dor_puncao),
})

dados.to_csv(Path(__file__).parent / "coorte-condutor.csv", index=False, encoding="utf-8")

# ------------------------------------------------------------- conferencia
print(f"n = {len(dados)}")
tab = pd.crosstab(dados.grupo, dados.cicatrizacao_12sem, normalize="index")
print("\nCicatrizacao em 12 semanas (proporcao, entre os seguidos):")
print(tab.round(3))
print("\nPerdas por grupo:")
print(pd.crosstab(dados.grupo, dados.perda_seguimento))
print("\nTempo mediano ate cicatrizacao (dias, entre quem cicatrizou):")
print(dados[dados.evento_cicatrizacao == 1].groupby("grupo")
      ["tempo_ate_cicatrizacao_dias"].median())
print("\nReducao da area em 4 semanas (%), por grupo:")
print(dados.groupby("grupo").reducao_area_4sem_pct.agg(["mean", "std", "median"]).round(1))
print("\nArea inicial (mediana e quartis):")
print(dados.area_inicial_cm2.describe()[["25%", "50%", "75%"]].round(1).to_dict())
print("\nFaltantes por variavel:")
print(dados.isna().sum()[lambda s: s > 0])

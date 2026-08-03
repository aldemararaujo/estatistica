"""
Gera a versao OBSERVACIONAL do caso condutor, para o Capitulo 12.

Mesmo tratamento, mesmo desfecho, mesmo efeito verdadeiro. Muda uma coisa so:
ninguem sorteou nada. Aqui o cirurgiao indica o aspirado de medula ossea para
quem ele julga precisar mais, ou seja, para a ulcera grande, antiga e do
paciente diabetico. E o confundimento por indicacao, e o objetivo do banco e
mostrar que ele inverte o resultado.

O efeito verdadeiro do tratamento e IDENTICO ao do ensaio randomizado
(log-hazard de 0,75). Qualquer diferenca entre o que se ve aqui e o que se ve
la e obra do delineamento, nao do tratamento.

Uso:  python dados/gerar-coorte-observacional.py
Saida: coorte-observacional.csv
"""

import numpy as np
import pandas as pd
from pathlib import Path

SEMENTE = 512
N = 300
FIM = 84
FORMA, ESCALA, LATENCIA = 1.5, 0.00120, 10
EFEITO_VERDADEIRO = 0.75          # o mesmo do ensaio randomizado

rng = np.random.default_rng(SEMENTE)

# --------------------------------------------------------- caracteristicas
idade = np.clip(rng.normal(62, 11, N), 40, 88).round(0)
sexo = rng.choice(["Feminino", "Masculino"], size=N, p=[0.58, 0.42])
diabetes = rng.binomial(1, 0.24, N)
tabagismo = rng.choice(["Nunca fumou", "Ex-fumante", "Fumante atual"], size=N, p=[0.45, 0.34, 0.21])
area = np.exp(rng.normal(np.log(8.0), 0.75, N)).round(1)
duracao = np.exp(rng.normal(np.log(14.0), 0.70, N)).round(0)
p_adesao = 1 / (1 + np.exp(-(1.1 - 0.35 * diabetes)))
adesao_ok = (rng.random(N) < p_adesao).astype(int)
recidivante = rng.binomial(1, 0.55, N)
tcpo2 = (38 - 4.5 * diabetes - 2.5 * (tabagismo == "Fumante atual")
         + rng.normal(0, 6.5, N)).round(1)

# ------------------------------------------- alocacao POR INDICACAO clinica
# Quanto pior a ulcera, maior a chance de receber a terapia celular. E a
# indicacao que todo cirurgiao faria, e e exatamente ela que destroi a
# comparabilidade dos grupos.
logito = -0.4 + 1.85 * np.log(area / 8.0) + 0.95 * np.log(duracao / 14.0) + 0.95 * diabetes
recebeu = (rng.random(N) < 1 / (1 + np.exp(-logito))).astype(int)

# --------------------------------------- desfecho: mesmo modelo do ensaio
lp = (EFEITO_VERDADEIRO * recebeu
      - 0.55 * np.log(area / 8.0)
      - 0.30 * np.log(duracao / 14.0)
      - 0.45 * diabetes
      - 0.20 * recidivante
      + 0.40 * adesao_ok
      + 0.055 * (tcpo2 - 38)
      - 0.25 * (tabagismo == "Fumante atual")
      - 0.02)

tempo = LATENCIA + (-np.log(rng.random(N)) / (ESCALA * np.exp(lp))) ** (1 / FORMA)
evento = (tempo <= FIM).astype(int)

dados = pd.DataFrame({
    "id": [f"O{i:03d}" for i in range(1, N + 1)],
    "recebeu_aspirado": np.where(recebeu == 1, "Sim", "Não"),
    "idade": idade.astype(int),
    "sexo": sexo,
    "diabetes": np.where(diabetes == 1, "Sim", "Não"),
    "tabagismo": tabagismo,
    "area_inicial_cm2": area,
    "duracao_ulcera_meses": duracao.astype(int),
    "ulcera_recidivante": np.where(recidivante == 1, "Sim", "Não"),
    "tcpo2_basal": tcpo2,
    "adesao_compressao": np.where(adesao_ok == 1, "Adequada", "Inadequada"),
    "cicatrizacao_12sem": np.where(evento == 1, "Sim", "Não"),
    "tempo_ate_cicatrizacao_dias": np.minimum(tempo, FIM).round(0).astype(int),
    "evento_cicatrizacao": evento,
})

destino = Path(__file__).parent / "coorte-observacional.csv"
dados.to_csv(destino, index=False, encoding="utf-8")

print(f"n = {N}, gravado em {destino.name}")
print(f"\nReceberam o aspirado: {int(recebeu.sum())} ({100*recebeu.mean():.0f}%)")
print("\nQuem recebeu era mais grave? (mediana)")
print(dados.groupby("recebeu_aspirado")[["area_inicial_cm2", "duracao_ulcera_meses"]].median())
print("\nDiabetes por grupo (%):")
print(pd.crosstab(dados.recebeu_aspirado, dados.diabetes, normalize="index").round(3) * 100)
print("\nCicatrizacao em 12 semanas (%) — o resultado BRUTO:")
print(pd.crosstab(dados.recebeu_aspirado, dados.cicatrizacao_12sem, normalize="index").round(3) * 100)

# Resultados do caso condutor

Gerado por `analises/analises-do-livro.py`. Todo número impresso no livro
sai daqui. Para conferir, rode o script e compare.


## Capítulo 8 — Descritiva

- n randomizado: 200 (100 aspirado, 100 controle)
- perdas de seguimento: 16 (8 e 8 por grupo)
- área inicial: média 10,5 (DP 9,4), mediana 7,7 (quartis 4,7 e 12,7)
- participantes com área acima da média: 67 de 200

## Capítulo 9 — Estimativa e intervalo de confiança

- cicatrização aspirado: 65/92 = 70,7% (IC95% Wilson 60,7 a 79,0)
- cicatrização controle: 49/92 = 53,3% (IC95% Wilson 43,1 a 63,1)
- diferença absoluta: 17,4 pontos percentuais (IC95% 3,6 a 31,2)
- número necessário para tratar: 5,8 (IC95% 3,2 a 27,9)
- risco relativo: 1,33 (IC95% 1,05 a 1,67)
- razão de chances: 2,11 (IC95% 1,15 a 3,88)
- redução de área em 4 semanas, aspirado: média 45,4% (DP 45,0), n = 95
- redução de área em 4 semanas, controle: média 30,6% (DP 42,6), n = 99
- diferença de médias: 14,8 pontos percentuais (IC95% 2,4 a 27,2)
- d de Cohen: 0,34

## Capítulo 10 — Teste de hipótese e valor de p

- qui-quadrado de Pearson: 5,90, gl = 1, p = 0,015
- com correção de continuidade: 5,19, p = 0,023
- teste exato de Fisher: p = 0,022
- teste t de Welch (redução em 4 semanas): t = 2,35, p = 0,020
- Mann-Whitney: U = 5584, p = 0,024
- poder para a diferença planejada (75% x 55%, n = 89 por grupo): 80,4%
- poder para a diferença observada (70,7% x 53,3%, n = 92 e 92): 68,3%

## Capítulo 11 — Escolhendo o teste

- dor EVA basal: mediana 5,0; em 12 semanas: mediana 3,0 (n = 184)
- t pareado: t = 23,48, p = < 0,001
- Wilcoxon pareado: W = 72, p = < 0,001
- McNemar (dor ≥ 5 antes x depois): discordantes 84 e 1, qui² = 79,11, p = < 0,001
- ANOVA da redução em 4 semanas por centro: F = 0,52, p = 0,595
- Kruskal-Wallis por centro: H = 1,09, p = 0,581
- correlação entre área inicial e tempo até cicatrizar (n = 114): Pearson r = 0,19 (p = 0,038), Spearman rô = 0,28 (p = 0,002)

## Capítulo 12 — Regressão e confundimento

- modelo bruto (n = 184):
  - aspirado: OR 2,11 (IC95% 1,15 a 3,88), p = 0,016
- modelo ajustado (n = 184), pseudo-R² de McFadden 0,162:
  - aspirado: OR 2,25 (IC95% 1,13 a 4,45), p = 0,020
  - log da área inicial: OR 0,49 (IC95% 0,31 a 0,78), p = 0,002
  - log da duração: OR 0,48 (IC95% 0,28 a 0,83), p = 0,008
  - diabetes: OR 0,33 (IC95% 0,15 a 0,74), p = 0,007
  - adesão adequada: OR 2,90 (IC95% 1,36 a 6,19), p = 0,006
- regressão linear da redução em 4 semanas (n = 184, R² = 0,115):
  - aspirado: coeficiente 12,0 pontos percentuais (IC95% -0,4 a 24,4), p = 0,059
  - log da área inicial: coeficiente -9,6 pontos percentuais (IC95% -17,4 a -1,8), p = 0,016
  - diabetes: coeficiente -20,5 pontos percentuais (IC95% -35,6 a -5,5), p = 0,008
  - adesão adequada: coeficiente 12,9 pontos percentuais (IC95% -1,4 a 27,1), p = 0,079

### A mesma pergunta em uma coorte (n = 300)

- receberam o aspirado: 144 (48%)
- área inicial mediana: 12,2 cm² em quem recebeu, 6,0 cm² em quem não recebeu
- duração mediana: 18 meses em quem recebeu, 10 meses em quem não recebeu
- diabetes: 35,4% em quem recebeu, 21,2% em quem não recebeu
- cicatrização bruta: 59,0% em quem recebeu, 66,7% em quem não recebeu
  - aspirado, bruto: OR 0,72 (IC95% 0,45 a 1,15), p = 0,172
  - aspirado, ajustado por área, duração, diabetes e adesão: OR 1,87 (IC95% 0,98 a 3,56), p = 0,058
- efeito verdadeiro embutido na simulação: o mesmo do ensaio randomizado
- para comparação, o ensaio randomizado deu OR bruto 2,11 e ajustado 2,25

## Capítulo 13 — Testes diagnósticos

- TcPO₂ basal (mmHg): AUC 0,656 (IC95% 0,574 a 0,737); 109 cicatrizaram, 65 não
  - corte ≥ 30: sensibilidade 85,3%, especificidade 26,2%, VPP 66,0%, VPN 51,5%, RV+ 1,16, RV− 0,56 (VP 93, FP 48, FN 16, VN 17)
  - corte ≥ 35: sensibilidade 63,3%, especificidade 60,0%, VPP 72,6%, VPN 49,4%, RV+ 1,58, RV− 0,61 (VP 69, FP 26, FN 40, VN 39)
  - corte ≥ 40: sensibilidade 38,5%, especificidade 84,6%, VPP 80,8%, VPN 45,1%, RV+ 2,50, RV− 0,73 (VP 42, FP 10, FN 67, VN 55)
- redução de área em 4 semanas (%): AUC 0,824 (IC95% 0,766 a 0,883); 114 cicatrizaram, 70 não
  - corte ≥ 30: sensibilidade 76,3%, especificidade 65,7%, VPP 78,4%, VPN 63,0%, RV+ 2,23, RV− 0,36 (VP 87, FP 24, FN 27, VN 46)
  - corte ≥ 40: sensibilidade 71,1%, especificidade 80,0%, VPP 85,3%, VPN 62,9%, RV+ 3,55, RV− 0,36 (VP 81, FP 14, FN 33, VN 56)
  - corte ≥ 50: sensibilidade 63,2%, especificidade 92,9%, VPP 93,5%, VPN 60,7%, RV+ 8,84, RV− 0,40 (VP 72, FP 5, FN 42, VN 65)
- prevalência do desfecho (probabilidade pré-teste): 62,0%

## Capítulo 14 — Análise de sobrevida

- Aspirado: eventos 65/100; tempo mediano até cicatrizar 50 dias; incidência acumulada 28 d 23,4%, 56 d 53,9%, 84 d 69,3%
- Controle: eventos 49/100; tempo mediano até cicatrizar 82 dias; incidência acumulada 28 d 7,0%, 56 d 35,0%, 84 d 51,3%
- log-rank: qui² = 9,26, gl = 1, p = 0,002
- Cox bruto:
  - aspirado: HR 1,76 (IC95% 1,21 a 2,55), p = 0,003
- Cox ajustado:
  - aspirado: HR 2,10 (IC95% 1,43 a 3,08), p = < 0,001
  - log da área inicial: HR 0,59 (IC95% 0,46 a 0,76), p = < 0,001
  - log da duração: HR 0,74 (IC95% 0,55 a 0,99), p = 0,044
  - diabetes: HR 0,50 (IC95% 0,29 a 0,85), p = 0,011
  - adesão adequada: HR 2,22 (IC95% 1,36 a 3,62), p = 0,001

## Capítulo 6 — Tamanho da amostra (conferência da conta)

- 55% x 75%, α = 5% bilateral, poder 80%: n = 89 por grupo
- com 10% de perdas previstas: 99 por grupo, arredondado para 100
  - para detectar 10 pontos percentuais: 376 por grupo
  - para detectar 15 pontos percentuais: 163 por grupo
  - para detectar 20 pontos percentuais: 89 por grupo
  - para detectar 25 pontos percentuais: 54 por grupo

## Capítulo 15 — Números do diagrama CONSORT

- randomizados: 200, 100 por grupo
- receberam o alocado: 100 e 100
- perdas de seguimento: 8 e 8
- analisados para o desfecho primário: 92 e 92
- infecção da ferida: 6 e 10
- dor no sítio de punção (só no grupo aspirado): 34 de 100

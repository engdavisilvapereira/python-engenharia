# calc_bacia_hidrografica.py
# Biblioteca de caracterização de bacia hidrográfica
# Referência: Silveira (2005), RBRH v.10 n.1
import math
import csv
def ler_perfil_csv(caminho):
    # Lê CSV com colunas distancia_m e cota_m
    # Retorna lista de dicionários
    perfil = []
    with open(caminho, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            perfil.append(linha)
    return perfil
def calcular_forma_bacia(area_km2, perimetro_km, comprimento_talvegue_km):
    # Kf: fator de forma
    kf = area_km2 / comprimento_talvegue_km ** 2
    # Kc: coeficiente de compacidade
    kc = 0.28 * perimetro_km / math.sqrt(area_km2)
    return {"kf": kf, "kc": kc}
def calcular_declividades(perfil):
    # S1: método direto | S2: área equivalente | S3: média harmônica
    distancias = [float(p["distancia_m"]) for p in perfil]
    cotas = [float(p["cota_m"]) for p in perfil]
    l = distancias[-1]
    h_max = cotas[0]
    h_min = cotas[-1]
    s1 = (h_max - h_min) / l
    area_sob_curva = 0
    for i in range(len(distancias) - 1):
        dl = distancias[i + 1] - distancias[i]
        area_sob_curva += dl * (cotas[i] + cotas[i + 1]) / 2
    s2 = 2 * (area_sob_curva - h_min * l) / l ** 2
    somador = 0
    for i in range(len(distancias) - 1):
        li = distancias[i + 1] - distancias[i]
        delta_h = abs(cotas[i] - cotas[i + 1])
        if li > 0 and delta_h > 0:
            ii = delta_h / li
            somador += li / math.sqrt(ii)
    s3 = (l / somador) ** 2
    return {"s1": s1, "s2": s2, "s3": s3}
def calcular_tempo_concentracao(l_km, s):
    # Equações empíricas — Tc em horas, L em km, S em m/m
    # Fonte: Silveira (2005), Tabela 1
    tc_kirpich = 0.0663 * (l_km ** 0.77) * (s ** -0.385)
    tc_ven_te_chow = 0.160 * (l_km ** 0.64) * (s ** -0.32)
    tc_johnstone = 0.462 * (l_km ** 0.5) * (s ** -0.25)
    tc_corps_engineers = 0.191 * (l_km ** 0.76) * (s ** -0.19)
    tc_picking = 0.0883 * (l_km ** 0.667) * (s ** -0.333)
    tc_carter = 0.0977 * (l_km ** 0.6) * (s ** -0.3)
    return {
        "kirpich": tc_kirpich,
        "ven_te_chow": tc_ven_te_chow,
        "johnstone": tc_johnstone,
        "corps_engineers": tc_corps_engineers,
        "picking": tc_picking,
        "carter": tc_carter
    }
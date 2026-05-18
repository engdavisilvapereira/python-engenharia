# calc_bacia_hidrografica.py
# Caracterização de bacia hidrográfica
# Calcula: Kf, Kc, declividades (S1, S2, S3) e tempo de concentração
# Referência: Silveira (2005), RBRH, v.10, n.1

import math
import csv


# --- Funções de cálculo ---

def calcular_forma_bacia(area_km2, perimetro_km, comprimento_talvegue_km):
    """Calcula fator de forma (Kf) e coeficiente de compacidade (Kc)."""
    # Kf = A / Lc²  — quanto menor, menos sujeita a cheias
    kf = area_km2 / comprimento_talvegue_km ** 2
    # Kc = 0,28 * P / √A  — quanto mais próximo de 1, mais circular e mais sujeita a cheias
    kc = 0.28 * perimetro_km / math.sqrt(area_km2)
    return {"kf": kf, "kc": kc}


def calcular_declividades(perfil):
    """Calcula três métodos de declividade a partir do perfil longitudinal do talvegue.
    S1: método direto (extremos)
    S2: área equivalente (trapézios)
    S3: média harmônica (recomendada por Silveira, 2005)
    """
    distancias = [float(p["distancia_m"]) for p in perfil]
    cotas = [float(p["cota_m"]) for p in perfil]

    L = distancias[-1]   # comprimento total do talvegue (m)
    H_max = cotas[0]     # cota da nascente (ponto mais alto)
    H_min = cotas[-1]    # cota do exutório (ponto mais baixo)

    # S1 — Método direto: desnível total dividido pelo comprimento
    s1 = (H_max - H_min) / L

    # S2 — Área equivalente: área sob a curva do perfil pelo método dos trapézios
    area_sob_curva = 0
    for i in range(len(distancias) - 1):
        dl = distancias[i + 1] - distancias[i]
        area_sob_curva += dl * (cotas[i] + cotas[i + 1]) / 2
    s2 = 2 * (area_sob_curva - H_min * L) / L ** 2

    # S3 — Média harmônica: leva em conta o tempo de percurso em cada trecho
    somador = 0
    for i in range(len(distancias) - 1):
        Li = distancias[i + 1] - distancias[i]
        delta_hi = abs(cotas[i] - cotas[i + 1])
        if Li > 0 and delta_hi > 0:
            Ii = delta_hi / Li
            somador += Li / math.sqrt(Ii)
    s3 = (L / somador) ** 2

    return {"s1": s1, "s2": s2, "s3": s3}


def calcular_tempo_concentracao(L_km, S):
    """Calcula o tempo de concentração (horas) por cinco equações empíricas.
    Fonte: Silveira (2005), Tabela 1.
    L em km, S em m/m, Tc em horas.
    """
    # Kirpich (1940) — calibrada com 7 bacias rurais pequenas (EUA)
    TcK = 0.0663 * (L_km ** 0.77) * (S ** -0.385)
    # Ven te Chow (1962) — adaptada de fórmula de tempo de pico, fator 1,67
    TcV = 0.160 * (L_km ** 0.64) * (S ** -0.32)
    # Johnstone (1949) — 19 bacias rurais americanas
    TcJ = 0.462 * (L_km ** 0.5) * (S ** -0.25)
    # Corps of Engineers (1946) — maior base de dados rurais, recomendada para grandes bacias
    TcC = 0.191 * (L_km ** 0.76) * (S ** -0.19)
    # Picking — origem incerta, bom desempenho em bacias urbanas (Silveira, 2005)
    TcP = 0.0883 * (L_km ** 0.667) * (S ** -0.333)

    return {
        "kirpich": TcK,
        "ven_te_chow": TcV,
        "johnstone": TcJ,
        "corps_engineers": TcC,
        "picking": TcP
    }


# --- Programa principal ---

if __name__ == "__main__":

    # Leitura do perfil longitudinal do talvegue
    perfil = []
    with open("perfil_talvegue.csv", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            perfil.append(linha)

    print("Calculadora de Parâmetros da Bacia Hidrográfica")
    print("-" * 50)
    print("Digite em valores com ponto decimal. Exemplo: 0.54")
    print()

    # Entrada de dados pelo usuário
    try:
        area_km2 = float(input("Área da bacia (km²): "))
        perimetro_km = float(input("Perímetro da bacia (km): "))
        lc_km = float(input("Comprimento do talvegue principal (km): "))
    except ValueError:
        print("Valor inválido. Use ponto como separador decimal.")
        exit()

    # --- Item 1: Forma da bacia ---
    forma = calcular_forma_bacia(area_km2, perimetro_km, lc_km)

    print()
    print("=" * 50)
    print("ITEM 1 — FORMA DA BACIA")
    print("=" * 50)
    print(f"  Fator de forma        Kf = {forma['kf']:.4f}")
    print(f"  Coef. de compacidade  Kc = {forma['kc']:.4f}")

    # Classificação Kf
    if forma["kf"] >= 0.75:
        classe_kf = "Alta propensão a grandes enchentes"
    elif forma["kf"] >= 0.50:
        classe_kf = "Tendência mediana a grandes enchentes"
    else:
        classe_kf = "Não sujeita a grandes enchentes"

    # Classificação Kc
    if forma["kc"] <= 1.25:
        classe_kc = "Alta propensão a grandes enchentes"
    elif forma["kc"] <= 1.50:
        classe_kc = "Tendência mediana a grandes enchentes"
    else:
        classe_kc = "Não sujeita a grandes enchentes"

    print(f"  Classificação Kf: {classe_kf}")
    print(f"  Classificação Kc: {classe_kc}")

    # --- Item 3: Declividades e Kirpich ---
    decliv = calcular_declividades(perfil)

    print()
    print("=" * 50)
    print("ITEM 3 — DECLIVIDADES DO TALVEGUE")
    print("=" * 50)
    print(f"  S1 (método direto)        = {decliv['s1']:.6f} m/m")
    print(f"  S2 (área equivalente)     = {decliv['s2']:.6f} m/m")
    print(f"  S3 (média harmônica)      = {decliv['s3']:.6f} m/m")

    print()
    print("KIRPICH COM OS TRÊS MÉTODOS DE DECLIVIDADE")
    print("-" * 50)
    tc_s1 = calcular_tempo_concentracao(lc_km, decliv["s1"])["kirpich"]
    tc_s2 = calcular_tempo_concentracao(lc_km, decliv["s2"])["kirpich"]
    tc_s3 = calcular_tempo_concentracao(lc_km, decliv["s3"])["kirpich"]
    print(f"  Tc Kirpich com S1 = {tc_s1:.4f} h  ({tc_s1*60:.2f} min)")
    print(f"  Tc Kirpich com S2 = {tc_s2:.4f} h  ({tc_s2*60:.2f} min)")
    print(f"  Tc Kirpich com S3 = {tc_s3:.4f} h  ({tc_s3*60:.2f} min)")

    # --- Item 4: Todas as equações com S3 ---
    tc = calcular_tempo_concentracao(lc_km, decliv["s3"])

    print()
    print("=" * 50)
    print("ITEM 4 — TEMPO DE CONCENTRAÇÃO (S3 — média harmônica)")
    print("=" * 50)
    print(f"  Kirpich          = {tc['kirpich']:.4f} h  ({tc['kirpich']*60:.2f} min)")
    print(f"  Ven te Chow      = {tc['ven_te_chow']:.4f} h  ({tc['ven_te_chow']*60:.2f} min)")
    print(f"  Johnstone        = {tc['johnstone']:.4f} h  ({tc['johnstone']*60:.2f} min)")
    print(f"  Corps Engineers  = {tc['corps_engineers']:.4f} h  ({tc['corps_engineers']*60:.2f} min)")
    print(f"  Picking          = {tc['picking']:.4f} h  ({tc['picking']*60:.2f} min)")
    print()
    print("Referência: Silveira, A.L.L. (2005). Desempenho de Fórmulas de")
    print("Tempo de Concentração em Bacias Urbanas e Rurais.")
    print("RBRH, v.10, n.1, pp.5-23.")

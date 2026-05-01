# calc_secao_canal.py
# Calculadora de propriedades geométricas de seções de canais
# Propriedades: área molhada, perímetro molhado, raio hidráulico, largura superficial
import math
# --- Funções de cálculo por seção ---
def calcular_retangular(profundidade, largura_fundo):
    # Fórmulas — seção retangular (z = 0)
    area_molhada = largura_fundo * profundidade
    perimetro_molhado = largura_fundo + 2 * profundidade
    raio_hidraulico = area_molhada / perimetro_molhado
    largura_superficial = largura_fundo  # paredes verticais: B = b
    return {
        "area_molhada": area_molhada,
        "perimetro_molhado": perimetro_molhado,
        "raio_hidraulico": raio_hidraulico,
        "largura_superficial": largura_superficial
    }
def calcular_triangular(profundidade, inclinacao):
    # Fórmulas — seção triangular (b = 0)
    area_molhada = inclinacao * profundidade ** 2
    perimetro_molhado = 2 * profundidade * math.sqrt(inclinacao ** 2 + 1)
    raio_hidraulico = area_molhada / perimetro_molhado
    largura_superficial = 2 * inclinacao * profundidade  # B = 2*z*yn
    return {
        "area_molhada": area_molhada,
        "perimetro_molhado": perimetro_molhado,
        "raio_hidraulico": raio_hidraulico,
        "largura_superficial": largura_superficial
    }
def calcular_trapezoidal(profundidade, largura_fundo, inclinacao):
    # Fórmulas — seção trapezoidal (caso geral)
    area_molhada = profundidade * (largura_fundo + inclinacao * profundidade)
    perimetro_molhado = largura_fundo + 2 * profundidade * math.sqrt(inclinacao ** 2 + 1)
    raio_hidraulico = area_molhada / perimetro_molhado
    largura_superficial = largura_fundo + 2 * inclinacao * profundidade  # B = b + 2*z*yn
    return {
        "area_molhada": area_molhada,
        "perimetro_molhado": perimetro_molhado,
        "raio_hidraulico": raio_hidraulico,
        "largura_superficial": largura_superficial
    }
def calcular_circular(profundidade, diametro):
    # Ângulo central em radianos — θ = 2 * arccos(1 - 2*yn/D)
    angulo = 2 * math.acos(1 - 2 * profundidade / diametro)
    area_molhada = (diametro ** 2 / 8) * (angulo - math.sin(angulo))
    perimetro_molhado = angulo * diametro / 2
    raio_hidraulico = area_molhada / perimetro_molhado
    largura_superficial = diametro * math.sin(angulo / 2)  # B = D*sen(θ/2)
    return {
        "area_molhada": area_molhada,
        "perimetro_molhado": perimetro_molhado,
        "raio_hidraulico": raio_hidraulico,
        "largura_superficial": largura_superficial
    }
def selecionar_secao():
    "Exibe menu de seções, coleta dimensões e retorna propriedades geométricas."
    print("Escolha o tipo de seção:")
    print("1 — Retangular")
    print("2 — Triangular")
    print("3 — Trapezoidal")
    print("4 — Circular")
    try:
        secao = int(input("Número da seção: "))
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")
        exit()
    if secao == 1:
        try:
            yn = float(input("Profundidade (yn): "))
            b = float(input("Largura de fundo (b): "))
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            exit()
        return calcular_retangular(yn, b)
    elif secao == 2:
        try:
            yn = float(input("Profundidade (yn): "))
            z = float(input("Inclinação do talude (z): "))
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            exit()
        return calcular_triangular(yn, z)
    elif secao == 3:
        try:
            yn = float(input("Profundidade (yn): "))
            b = float(input("Largura de fundo (b): "))
            z = float(input("Inclinação do talude (z): "))
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            exit()
        return calcular_trapezoidal(yn, b, z)
    elif secao == 4:
        try:
            yn = float(input("Profundidade (yn): "))
            d = float(input("Diâmetro (D): "))
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            exit()
        if yn >= d:
            print("Profundidade deve ser menor que o diâmetro (seção não pode estar plena).")
            exit()
        return calcular_circular(yn, d)
    else:
        print("Opção inválida.")
        exit()
# --- Programa principal ---
if __name__ == "__main__":
    print("Calculadora de Seção de Canal")
    print("-" * 30)
    resultado = selecionar_secao()
    print(f"Área molhada:        {resultado['area_molhada']:.3f} m²")
    print(f"Perímetro molhado:   {resultado['perimetro_molhado']:.3f} m")
    print(f"Raio hidráulico:     {resultado['raio_hidraulico']:.3f} m")
    print(f"Largura superficial: {resultado['largura_superficial']:.3f} m")
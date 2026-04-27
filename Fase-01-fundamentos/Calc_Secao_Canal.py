# calc_secao_canal.py
# Calculadora de propriedades geométricas de seções de canais
# Propriedades: área molhada, perímetro molhado, raio hidráulico

import math
#definindo as funções
def calcular_retangular(profundidade, largura_fundo):
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
    area_molhada = inclinacao * profundidade ** 2
    perimetro_molhado = 2 * profundidade * math.sqrt(inclinacao ** 2 + 1)
    raio_hidraulico = area_molhada / perimetro_molhado
    largura_superficial = 2*inclinacao*profundidade # paredes verticais: B = b

    return {
        "area_molhada": area_molhada,
        "perimetro_molhado": perimetro_molhado,
        "raio_hidraulico": raio_hidraulico,
        "largura_superficial": largura_superficial
    }
def calcular_trapezoidal(profundidade,largura_fundo , inclinacao):
    area_molhada = profundidade * (largura_fundo + inclinacao * profundidade)
    perimetro_molhado = largura_fundo + 2 * profundidade * math.sqrt(inclinacao ** 2 + 1)
    raio_hidraulico = area_molhada / perimetro_molhado
    largura_superficial = largura_fundo + 2*inclinacao*profundidade

    return {
        "area_molhada": area_molhada,
        "perimetro_molhado": perimetro_molhado,
        "raio_hidraulico": raio_hidraulico,
        "largura_superficial": largura_superficial
    }
def calcular_circular(profundidade, diametro):
    angulo = 2 * math.acos(1 - 2 * profundidade / diametro)
    area_molhada = (diametro ** 2 / 8) * (angulo - math.sin(angulo))
    perimetro_molhado = angulo * diametro / 2
    raio_hidraulico = area_molhada / perimetro_molhado
    largura_superficial = diametro * math.sin(angulo/2)

    return {
        "area_molhada": area_molhada,
        "perimetro_molhado": perimetro_molhado,
        "raio_hidraulico": raio_hidraulico,
        "largura_superficial": largura_superficial
    }
# Exibe o menu de seções
print("Calculadora de Seção de Canal")
print("-" * 30)
print("1 — Seção Retangular")
print("2 — Seção Triangular")
print("3 — Seção Trapezoidal")
print("4 — Seção Circular")
print()
# Solicita a opção do usuário com tratamento de erro
try:
    secao_escolhida = int(input("Escolha o número da seção que deseja calcular: "))
except ValueError:
    print("Entrada inválida. Digite apenas números inteiros.")
    exit()
# Verifica se a opção está no intervalo válido (1 a 4)
if not (1 <= secao_escolhida <= 4):
    print("Opção fora do intervalo. Digite um número de 1 a 4.")
    exit()
# Seção Retangular
if secao_escolhida == 1:
    try:
        profundidade = float(input("Profundidade (yn): "))
        largura_fundo = float(input("Largura de fundo (b): "))
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        exit()
    resultado = calcular_retangular(profundidade, largura_fundo)
    print(f"Área molhada: {resultado['area_molhada']:.3f} m²")
    print(f"Perímetro molhado: {resultado['perimetro_molhado']:.3f} m")
    print(f"Raio hidráulico: {resultado['raio_hidraulico']:.3f} m")
    print(f"Largura superficial: {resultado['largura_superficial']:.3f} m")
elif secao_escolhida == 2:
    try:
        profundidade = float(input("Profundidade (yn): "))
        inclinacao = float(input("inclinação do talude (z): "))
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        exit()
    resultado = calcular_triangular(profundidade, inclinacao)
    print(f"Área molhada: {resultado['area_molhada']:.3f} m²")
    print(f"Perímetro molhado: {resultado['perimetro_molhado']:.3f} m")
    print(f"Raio hidráulico: {resultado['raio_hidraulico']:.3f} m")
    print(f"Largura superficial: {resultado['largura_superficial']:.3f} m")
# Seção Trapezoidal
elif secao_escolhida == 3:
    try:
        profundidade = float(input("Profundidade (yn): "))
        largura_fundo = float(input("Largura de fundo (b): "))
        inclinacao = float(input("inclinação do talude (z): "))
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        exit()
    resultado = calcular_trapezoidal(profundidade, largura_fundo, inclinacao)
    print(f"Área molhada: {resultado['area_molhada']:.3f} m²")
    print(f"Perímetro molhado: {resultado['perimetro_molhado']:.3f} m")
    print(f"Raio hidráulico: {resultado['raio_hidraulico']:.3f} m")
    print(f"Largura superficial: {resultado['largura_superficial']:.3f} m")
# Seção Circular
elif secao_escolhida == 4:
    try:
        profundidade = float(input("Profundidade (yn): "))
        diametro = float(input("Diâmetro (D): "))
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        exit()
    # Validação: profundidade não pode exceder o diâmetro
    if profundidade > diametro:
        print("Profundidade não pode ser maior que o diâmetro.")
        exit()
    resultado = calcular_circular(profundidade, diametro)
    print(f"Área molhada: {resultado['area_molhada']:.3f} m²")
    print(f"Perímetro molhado: {resultado['perimetro_molhado']:.3f} m")
    print(f"Raio hidráulico: {resultado['raio_hidraulico']:.3f} m")
    print(f"Largura superficial: {resultado['largura_superficial']:.3f} m")
else:
    print("Opção inválida.")

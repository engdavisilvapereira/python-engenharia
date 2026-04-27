# calc_secao_canal.py
# Calculadora de propriedades geométricas de seções de canais
# Propriedades: área molhada, perímetro molhado, raio hidráulico

import math

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
    print("Digite os valores em metros.")
    try:
        profundidade = float(input("Profundidade (yn): "))
        largura_fundo = float(input("Largura de fundo (b): "))
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        exit()

    # Fórmulas — seção retangular (caso particular: z = 0)
    area_molhada = largura_fundo * profundidade
    perimetro_molhado = largura_fundo + 2 * profundidade
    raio_hidraulico = area_molhada / perimetro_molhado

    print(f"Área molhada retangular: {area_molhada:.3f} m²")
    print(f"Perímetro molhado retangular: {perimetro_molhado:.3f} m")
    print(f"Raio hidráulico retangular: {raio_hidraulico:.3f} m")

# Seção Triangular
elif secao_escolhida == 2:
    print("Digite os valores em metros.")
    try:
        profundidade = float(input("Profundidade (yn): "))
        inclinacao = float(input("Inclinação do talude (z): "))
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        exit()

    # Fórmulas — seção triangular (caso particular: b = 0)
    area_molhada = inclinacao * profundidade ** 2
    perimetro_molhado = 2 * profundidade * math.sqrt(inclinacao ** 2 + 1)
    raio_hidraulico = area_molhada / perimetro_molhado

    print(f"Área molhada triangular: {area_molhada:.3f} m²")
    print(f"Perímetro molhado triangular: {perimetro_molhado:.3f} m")
    print(f"Raio hidráulico triangular: {raio_hidraulico:.3f} m")

# Seção Trapezoidal
elif secao_escolhida == 3:
    print("Digite os valores em metros.")
    try:
        profundidade = float(input("Profundidade (yn): "))
        largura_fundo = float(input("Largura de fundo (b): "))
        inclinacao = float(input("Inclinação do talude (z): "))
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        exit()

    # Fórmulas — seção trapezoidal (caso geral)
    area_molhada = profundidade * (largura_fundo + inclinacao * profundidade)
    perimetro_molhado = largura_fundo + 2 * profundidade * math.sqrt(inclinacao ** 2 + 1)
    raio_hidraulico = area_molhada / perimetro_molhado

    print(f"Área molhada trapezoidal: {area_molhada:.3f} m²")
    print(f"Perímetro molhado trapezoidal: {perimetro_molhado:.3f} m")
    print(f"Raio hidráulico trapezoidal: {raio_hidraulico:.3f} m")

# Seção Circular
elif secao_escolhida == 4:
    print("Digite os valores em metros.")
    try:
        profundidade = float(input("Profundidade da lâmina (yn): "))
        diametro = float(input("Diâmetro (D): "))
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        exit()

    # Validação: profundidade não pode exceder o diâmetro
    if profundidade > diametro:
        print("Profundidade não pode ser maior que o diâmetro.")
        exit()

    # Ângulo central em radianos — θ = 2 × arccos(1 - 2yn/D)
    angulo = 2 * math.acos(1 - 2 * profundidade / diametro)

    # Fórmulas — seção circular
    area_molhada = (diametro ** 2 / 8) * (angulo - math.sin(angulo))
    perimetro_molhado = angulo * diametro / 2
    raio_hidraulico = area_molhada / perimetro_molhado

    print(f"Ângulo central (θ): {angulo:.3f} rad")
    print(f"Área molhada circular: {area_molhada:.3f} m²")
    print(f"Perímetro molhado circular: {perimetro_molhado:.3f} m")
    print(f"Raio hidráulico circular: {raio_hidraulico:.3f} m")

else:
    print("Opção inválida.")
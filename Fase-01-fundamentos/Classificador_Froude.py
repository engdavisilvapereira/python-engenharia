# Classificador_Froude.py
import math
g = 9.81
# Exibe o menu de seções
print("Calculadora de Regime de escoamento segundo Froude: ")
print("-" * 30)
print("Você tem a area molhada e a Largura superficial ? ")
print("1 - Sim ")
print("2 - Não ")
# confirma a necessidade de calcular os parametros
try:
    modo = int(input("valor numerico de sim ou não:"))
except ValueError:
    print("Entrada inválida. Digite apenas números inteiros.")
    exit()
# Texte do que fazer
if modo == 1:
    try:
        area_molhada = float(input("Área molhada (m²): "))
        largura_superficial = float(input("Largura superficial (m): "))
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        exit()
elif modo == 2:
    from Calc_Secao_Canal import selecionar_secao
    resultado = selecionar_secao()
    area_molhada = resultado["area_molhada"]
    largura_superficial = resultado["largura_superficial"]
else:
    print("Valor inválido.")
    exit()
# A partir daqui, area_molhada e largura_superficial existem
# independente do modo escolhido — o código abaixo roda para os dois casos
try:
    velocidade = float(input("Velocidade média do escoamento (m/s): "))
except ValueError:
    print("Entrada inválida. Digite apenas números.")
    exit()
profundidade_hidraulica = area_molhada / largura_superficial
fr = velocidade / math.sqrt(g * profundidade_hidraulica)
if fr < 0.95:
    print(f"Regime Subcrítico ou Fluvial — Fr = {fr:.3f}")
elif fr <= 1.05:
    print(f"Regime Crítico — Fr = {fr:.3f}")
else:
    print(f"Regime Supercrítico — Fr = {fr:.3f}")
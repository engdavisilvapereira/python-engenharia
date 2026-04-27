# Classificador_Froude.py
import math
g = 9.81
def calcular_froude(velocidade, area_molhada, largura_superficial):
    profundidade_hidraulica = area_molhada / largura_superficial
    fr = velocidade / math.sqrt(g * profundidade_hidraulica)
    return fr
def secao_froude():
    #Exibe menu de opções
    print("Calculadora de Regime de escoamento segundo Froude: ")
    print("-" * 30)
    print("Você tem a area molhada e a Largura superficial ? ")
    print("1 - Sim ")
    print("2 - Não ")
    # confirma a necessidade de calcular os parametros
    try:
        modo = int(input("valor numerico de sim ou não: "))
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")
        exit()
    # Texte do que fazer
    if modo == 1:
        try:
            area_molhada = float(input("Area molhada (m²): "))
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
    try:
        velocidade = float(input("Velocidade média do escoamento (m/s): "))
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        exit()
    return calcular_froude(velocidade, area_molhada, largura_superficial)
#apresenta os resultados
if __name__ == "__main__":
    fr = secao_froude()
    if fr < 0.95:
        print(f"Regime Subcrítico ou Fluvial — Fr = {fr:.3f}")
    elif fr <= 1.05:
        print(f"Regime Crítico — Fr = {fr:.3f}")
    else:
        print(f"Regime Supercrítico — Fr = {fr:.3f}")
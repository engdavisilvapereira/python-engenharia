import csv
import math
def carregar_materiais():
    #Armazena os dados CSV
    materiais = []
    with open("tabela_hazen_williams.csv", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            material = {
                "categoria": linha["categoria"],
                "material": linha["material"],
                "c_min": float(linha["c_min"]),
                "c_tipico": float(linha["c_tipico"]),
                "c_max": float(linha["c_max"]),
                "condicao": linha["condicao"],
                "fonte": linha["fonte"]
            }
            materiais.append(material)
    return materiais
def selecionar_c():
    materiais = carregar_materiais()

    # passo 1: categorias únicas
    categorias = []
    for m in materiais:
        if m["categoria"] not in categorias:
            categorias.append(m["categoria"])

    # passo 2: exibir e coletar categoria
    print("Escolha a categoria:")
    print("-" * 30)
    for i, cat in enumerate(categorias, start=1):
        print(f"{i} — {cat}")
    try:
        opcao_cat = int(input("Número da categoria: "))
    except ValueError:
        print("Entrada inválida.")
        exit()
    if not (1 <= opcao_cat <= len(categorias)):
        print("Opção inválida.")
        exit()
    categoria_escolhida = categorias[opcao_cat - 1]  

    # passo 3: filtrar materiais da categoria
    materiais_filtrados = []
    for m in materiais:
        if m["categoria"] == categoria_escolhida:  # agora compara string com string
            materiais_filtrados.append(m)

    # passo 4: exibir e coletar material
    print()
    print(f"Materiais — {categoria_escolhida}:")
    print("-" * 30)
    for i, mat in enumerate(materiais_filtrados, start=1):
        print(f"{i} — {mat['material']}")
        print(f"    Condição: {mat['condicao']}")
        print(f"    Faixa C:  {mat['c_min']:.0f} a {mat['c_max']:.0f}")
        print(f"    Fonte:    {mat['fonte']}")
        print()
    try:
        opcao_mat = int(input("Número do material: "))
    except ValueError:
        print("Entrada inválida.")
        exit()
    if not (1 <= opcao_mat <= len(materiais_filtrados)):
        print("Opção inválida.")
        exit()
    mat = materiais_filtrados[opcao_mat - 1]

    # passo 5: confirmar n
    print(f"c tipico (mais utilizado): {mat['c_tipico']:.4f}")
    print(f"Faixa: {mat['c_min']:.4f} a {mat['c_max']:.4f}")
    confirma = input("Confirma esse valor? (s/n): ")
    if confirma.lower() == "s":
        c = mat["c_tipico"]
    else:
        try:
            c = float(input("Digite o valor de c: "))
        except ValueError:
            print("Entrada inválida.")
            exit()

    return c
def calcular_hazen_williams(c, diametro, perda_de_carga_unitaria):
    raio_hidraulico  = diametro/4
    area_molhada = math.pi * (diametro**2) / 4.
    velocidade = 0.8492 * c * (raio_hidraulico**0.63) * (perda_de_carga_unitaria**0.54)
    vazao = velocidade*area_molhada
    return vazao, velocidade
def calcular_reynolds(velocidade, diametro, viscosidade_cinematica):
    # D e v devem estar em m e m/s
    re = (velocidade * diametro) / viscosidade_cinematica
    return re
if __name__ == "__main__":
    print("Calculadora de Vazão por Hazen Williams")
    print("-" * 30)
    c = selecionar_c()
    try:
        diametro = float(input("escreva o diametrô do conduto (m): "))
    except ValueError:
        print(" Valor invalido.")
        exit()
    try:
        perda_de_carga_unitaria = float(input("escreva a perda de carga unitária hf/L (m/m): "))
    except ValueError:
        print(" Valor invalido.")
        exit()
    try:
        viscosidade_cinematica = float(input("escreva a a viscosidade cinemática (m²/s): "))
    except ValueError:
        print(" Valor invalido.")
        exit()
    vazao, velocidade = calcular_hazen_williams(c, diametro, perda_de_carga_unitaria)
    re = calcular_reynolds(velocidade, diametro, viscosidade_cinematica)
    print(f"Vazão de Hazen Williams igual a : {vazao:.3f} m³/s")
    print(f"velocidade igual a : {velocidade:.3f} m/s")
    print(f"O número de Reynolds é: {re:.2f}")
    if re < 2000:
        print("O Regime é laminar")
    elif re <= 4000:
        print("O Regime é de transição")
    else:
        print("O Regime é Turbulento")
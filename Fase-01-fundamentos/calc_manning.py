import csv
from calc_secao_canal import selecionar_secao
from classificador_froude import calcular_froude
def carregar_materiais():
    #Armazena os dados CSV
    materiais = []
    with open("tabela_manning_n.csv", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            material = {
                "categoria": linha["categoria"],
                "material": linha["material"],
                "n_min": float(linha["n_min"]),
                "n_max": float(linha["n_max"]),
                "n_medio": (float(linha["n_min"]) + float(linha["n_max"])) / 2
            }
            materiais.append(material)
    return materiais
def selecionar_n():
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
    categoria_escolhida = categorias[opcao_cat - 1]  # converte número para nome

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
        print(f"{i} — {mat['material']} (n = {mat['n_min']:.4f} a {mat['n_max']:.4f})")
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
    print(f"n sugerido (média): {mat['n_medio']:.4f}")
    print(f"Faixa: {mat['n_min']:.4f} a {mat['n_max']:.4f}")
    confirma = input("Confirma esse valor? (s/n): ")
    if confirma.lower() == "s":
        n = mat["n_medio"]
    else:
        try:
            n = float(input("Digite o valor de n: "))
        except ValueError:
            print("Entrada inválida.")
            exit()

    return n
def calcular_manning(n, area_molhada, raio_hidraulico, declividade):
    vazao = (1/n) * area_molhada * (raio_hidraulico**(2/3)) * (declividade**(1/2))
    velocidade = vazao/area_molhada
    return vazao, velocidade
if __name__ == "__main__":
    print("Calculadora de Vazão por Manning")
    print("-" * 30)
    n = selecionar_n()
    resultado = selecionar_secao()
    area_molhada = resultado["area_molhada"]
    raio_hidraulico = resultado["raio_hidraulico"]
    largura_superficial = resultado["largura_superficial"]
    try:
        declividade = float(input("Defina a declividade: "))
    except ValueError:
        print(" Valor invalido.")
        exit()
    vazao, velocidade = calcular_manning(n, area_molhada, raio_hidraulico, declividade)
    fr = calcular_froude(velocidade, area_molhada, largura_superficial)
    print(f"Vazão de Manning igual a : {vazao:.3f} m³/s")
    print(f"velocidade igual a : {velocidade:.3f} m/s")
    print(f"Número de Froude: {fr:.3f} (adimensional)")
    if fr < 0.95:
        regime = "Subcrítico (Fluvial)"
    elif fr <= 1.05:
        regime = "Crítico"
    else:
        regime = "Supercrítico (Torrencial)"
    print(f"Regime: {regime}")

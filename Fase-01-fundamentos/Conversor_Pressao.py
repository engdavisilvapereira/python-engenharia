# Conversor_Pressao.py
# Conversor de unidades de Pressão — 8 unidades, matriz completa 8×8

# Definições exatas em Pa (unidade SI):
# 1 kPa  = 1000 Pa
# 1 MPa  = 1000000 Pa
# 1 bar  = 100000 Pa
# 1 atm  = 101325 Pa
# 1 mca  = 9806.65 Pa  (convenção padrão, g = 9.80665 m/s²)
# 1 psi  = 6894.757293168 Pa
# 1 mmHg = 133.322387415 Pa

fatores = {
    "Pa": {
        "Pa": 1.0, "kPa": 0.001, "MPa": 0.000001,
        "bar": 0.00001, "atm": 0.0000098692,
        "mca": 0.0001019744, "psi": 0.0001450377,
        "mmHg": 0.0075006158
    },
    "kPa": {
        "Pa": 1000.0, "kPa": 1.0, "MPa": 0.001,
        "bar": 0.01, "atm": 0.0098692327,
        "mca": 0.1019744289, "psi": 0.1450377377,
        "mmHg": 7.5006157585
    },
    "MPa": {
        "Pa": 1000000.0, "kPa": 1000.0, "MPa": 1.0,
        "bar": 10.0, "atm": 9.8692326672,
        "mca": 101.9744289, "psi": 145.0377377,
        "mmHg": 7500.6157585
    },
    "bar": {
        "Pa": 100000.0, "kPa": 100.0, "MPa": 0.1,
        "bar": 1.0, "atm": 0.9869232667,
        "mca": 10.19744289, "psi": 14.50377377,
        "mmHg": 750.0615758
    },
    "atm": {
        "Pa": 101325.0, "kPa": 101.325, "MPa": 0.101325,
        "bar": 1.01325, "atm": 1.0,
        "mca": 10.3322745962, "psi": 14.6959487755,
        "mmHg": 760.0
    },
    "mca": {
        "Pa": 9806.65, "kPa": 9.80665, "MPa": 0.00980665,
        "bar": 0.0980665, "atm": 0.0967841105,
        "mca": 1.0, "psi": 1.4223343307,
        "mmHg": 73.5559240069
    },
    "psi": {
        "Pa": 6894.7572932, "kPa": 6.8947572932, "MPa": 0.0068947573,
        "bar": 0.0689475729, "atm": 0.0680459639,
        "mca": 0.7030696455, "psi": 1.0,
        "mmHg": 51.7149325541
    },
    "mmHg": {
        "Pa": 133.3223874, "kPa": 0.1333223874, "MPa": 0.0001333224,
        "bar": 0.0013332239, "atm": 0.0013157895,
        "mca": 0.0135951002, "psi": 0.0193368,
        "mmHg": 1.0
    }
}

# Nomes legíveis para exibição no terminal
nomes = {
    "Pa": "Pa (pascal)",
    "kPa": "kPa (quilopascal)",
    "MPa": "MPa (megapascal)",
    "bar": "bar",
    "atm": "atm (atmosfera)",
    "mca": "mca (metros de coluna d'água)",
    "psi": "psi (libra por pol²)",
    "mmHg": "mmHg (milímetros de mercúrio)"
}

# Lista ordenada das chaves para montar o menu
unidades = list(nomes.keys())

# Exibe o menu de unidades
print("Conversor de Pressão")
print("-" * 30)
for i, chave in enumerate(unidades, start=1):
    print(f"{i} — {nomes[chave]}")

print()

# Solicita as opções do usuário com tratamento de erro
try:
    opcao_origem = int(input("Unidade de origem (número): "))
    opcao_destino = int(input("Unidade de destino (número): "))
except ValueError:
    print("Entrada inválida. Digite apenas números inteiros.")
    exit()

# Converte para índice da lista (subtrai 1 porque listas começam em 0)
indice_origem = opcao_origem - 1
indice_destino = opcao_destino - 1

# Verifica se os índices estão no intervalo válido (0 a 7)
if not (0 <= indice_origem < len(unidades) and 0 <= indice_destino < len(unidades)):
    print("Opção fora do intervalo. Digite um número de 1 a 8.")
    exit()

chave_origem = unidades[indice_origem]
chave_destino = unidades[indice_destino]

# Solicita o valor da pressão com tratamento de erro
try:
    valor = float(input("Digite o valor da pressão: "))
except ValueError:
    print("Valor inválido. Digite um número (use ponto para decimais).")
    exit()

# Busca o fator na matriz e aplica a conversão
fator = fatores[chave_origem][chave_destino]
resultado = valor * fator

print(f"{valor:.3f} {nomes[chave_origem]} = {resultado:.3f} {nomes[chave_destino]}")
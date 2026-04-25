# conversor_vazao.py
# Conversor de unidades de vazão — 7 unidades, matriz completa 7×7

# Dicionário com os fatores de conversão
# Leitura: fatores[origem][destino] = fator multiplicador
fatores = {
    "m3_s": {
        "m3_s": 1.0, "m3_h": 3600.0, "l_s": 1000.0,
        "l_min": 60000.0, "l_h": 3600000.0,
        "pcm": 2118.8804605799, "gpm": 15850.3231414890
    },
    "m3_h": {
        "m3_s": 0.0002777778, "m3_h": 1.0, "l_s": 0.2777777778,
        "l_min": 16.6666666667, "l_h": 1000.0,
        "pcm": 0.5885779057, "gpm": 4.4028675393
    },
    "l_s": {
        "m3_s": 0.001, "m3_h": 3.6, "l_s": 1.0,
        "l_min": 60.0, "l_h": 3600.0,
        "pcm": 2.1188804606, "gpm": 15.8503231415
    },
    "l_min": {
        "m3_s": 0.0000166667, "m3_h": 0.06, "l_s": 0.0166666667,
        "l_min": 1.0, "l_h": 60.0,
        "pcm": 0.0353146743, "gpm": 0.2641720524
    },
    "l_h": {
        "m3_s": 0.0000002778, "m3_h": 0.001, "l_s": 0.0002777778,
        "l_min": 0.0166666667, "l_h": 1.0,
        "pcm": 0.0005885779, "gpm": 0.0044028675
    },
    "pcm": {
        "m3_s": 0.0004719475, "m3_h": 1.6990111331, "l_s": 0.4719475114,
        "l_min": 28.3168506850, "l_h": 1699.0110410990,
        "pcm": 1.0, "gpm": 7.4805194805
    },
    "gpm": {
        "m3_s": 0.0000630902, "m3_h": 0.2271247074, "l_s": 0.0630901964,
        "l_min": 3.7854117840, "l_h": 227.1247070400,
        "pcm": 0.1336805556, "gpm": 1.0
    }
}

# Nomes legíveis para exibição no terminal
nomes = {
    "m3_s": "m³/s",
    "m3_h": "m³/h",
    "l_s": "L/s",
    "l_min": "L/min",
    "l_h": "L/h",
    "pcm": "pcm (pé³/min)",
    "gpm": "GPM (gal/min US)"
}

# Lista ordenada das chaves para montar o menu
unidades = list(nomes.keys())

# Exibe o menu de unidades
print("Conversor de Vazão")
print("-" * 30)
for i, chave in enumerate(unidades, start=1):
    print(f"{i} — {nomes[chave]}")

print()

# Solicita as opções do usuário com tratamento de erro
try:
    opcao_origem = int(input("Unidade de origem (número): "))
    opcao_destino = int(input("Unidade de destino (número): "))
except ValueError:
    # O usuário digitou texto em vez de número
    print("Entrada inválida. Digite apenas números inteiros.")
    exit()  # Encerra o programa — sem isso, o código continuaria e daria outro erro

# Converte para índice da lista (subtrai 1 porque listas começam em 0)
indice_origem = opcao_origem - 1
indice_destino = opcao_destino - 1

# Verifica se os índices estão no intervalo válido (0 a 6)
if not (0 <= indice_origem < len(unidades) and 0 <= indice_destino < len(unidades)):
    print("Opção fora do intervalo. Digite um número de 1 a 7.")
    exit()

chave_origem = unidades[indice_origem]
chave_destino = unidades[indice_destino]

# Solicita o valor da vazão com tratamento de erro
try:
    valor = float(input("Digite o valor da vazão: "))
except ValueError:
    print("Valor inválido. Digite um número (use ponto para decimais).")
    exit()

# Rejeita valores negativos — vazão negativa não tem sentido físico
if valor < 0:
    print("Vazão não pode ser negativa.")
    exit()

# Busca o fator na matriz e aplica a conversão
fator = fatores[chave_origem][chave_destino]
resultado = valor * fator

print(f"{valor:.3f} {nomes[chave_origem]} = {resultado:.3f} {nomes[chave_destino]}")
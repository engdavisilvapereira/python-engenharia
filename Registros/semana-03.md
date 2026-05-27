# Semana 03 — 18/05 a 26/05/2026
# Fase 1 — Fundamentos de Python (aplicação a atividade do mestrado)

---

## Sessão 1 — 18/05/2026

**Horas dedicadas:** ~4h

**Tópicos estudados:**

- Separação entre biblioteca de funções e programa principal (padrão biblioteca + relatório)
- Função ler_perfil_csv(caminho): leitura parametrizada de CSV, caminho como argumento
- List comprehension para conversão de tipos ao ler CSV
- Acesso a elementos de lista por índice negativo (lista[-1] para último elemento)
- Cálculo de declividade por três métodos: direto (S1), área equivalente por trapézios (S2), média harmônica (S3)
- Implementação de seis equações empíricas de tempo de concentração (Kirpich, Ven te Chow, Johnstone, Corps of Engineers, Picking, Carter)
- Referência bibliográfica: Silveira (2005), RBRH v.10 n.1
- Geração de relatório formatado em .xlsx com openpyxl (cores, bordas, mesclagem de células, linhas alternadas)
- Constantes globais em maiúsculas (EQUACOES, DECLIVIDADES) para controle centralizado de listas
- Laço for sobre dicionários aninhados para gerar matriz de resultados (6 equações × 3 declividades)
- Módulo os.path.exists para validação de arquivo antes de leitura

**Entregáveis:**

- calc_bacia_hidrografica.py — biblioteca pura (zero prints, zero inputs) com quatro funções importáveis: ler_perfil_csv(), calcular_forma_bacia(), calcular_declividades(), calcular_tempo_concentracao()
- relatorio_bacia.py — programa principal que importa a biblioteca, recebe dados do usuário, calcula todos os parâmetros e exporta relatório .xlsx formatado com seções: dados de entrada, forma da bacia, declividades, duas tabelas de Tc (horas e minutos)
- perfil_talvegue.csv — perfil longitudinal com 20 pontos extraído do QGIS
- relatorio_Jardim_Bela_Vista.xlsx — relatório gerado pelo programa

Integração com disciplina do mestrado: atividade de caracterização de bacia hidrográfica da disciplina MPEH18 (Applied Hydrology, Prof. Benedito C. Silva, UNIFEI). Bacia do loteamento Jardim Bela Vista, Itajubá-MG.

**Geoprocessamento (QGIS):**

- Delimitação automática de bacia via algoritmo Watershed (SAGA/QGIS)
- MDE em SIRGAS 2000 UTM 23S
- Extração de área (539.901 m²), perímetro (3.827 m) e comprimento do talvegue (650 m) via calculadora de campo
- Traçado do talvegue sobre rede de drenagem gerada por acumulação de fluxo
- Extração do perfil longitudinal via ferramenta Elevation Profile
- Visualização 3D do terreno via Mapa 3D nativo

**Resultados validados (bacia Jardim Bela Vista):**

- Kf = 1,2779 → Alta propensão a grandes enchentes
- Kc = 1,4583 → Tendência mediana a grandes enchentes
- S1 = 0,047694 m/m | S2 = 0,028932 m/m | S3 = 0,172441 m/m
- Tc Kirpich (S3) = 5,62 min | Ven te Chow (S3) = 12,79 min | Johnstone (S3) = 34,68 min

**Dificuldades encontradas:**

- Confusão entre os argumentos de entrada e saída das funções ao chamar (passar variáveis de saída como entrada)
- Tentativa de gerar CSV para Excel com formatação visual — CSV é texto puro e não suporta formatação; solução: migrar para .xlsx via openpyxl
- Problema de separador decimal (ponto vs vírgula) ao importar CSV no Excel com configuração brasileira
- Tabela de Tc inicialmente em formato único (horas e minutos lado a lado); separada em duas tabelas por clareza

**Avaliação da semana:**

O foco desta semana migrou de exercícios isolados de Python para integração direta com atividade do mestrado. Isso é positivo — o programa resolve um problema real e foi usado de fato para entregar uma atividade acadêmica. A decisão de usar QGIS em vez do Google Earth e Python em vez de Excel mostra evolução na autonomia técnica.

O conceito de biblioteca pura (funções sem prints nem inputs) ficou consolidado. A geração de relatório .xlsx com formatação profissional é uma competência nova que vai ser reutilizada em outros programas.

Ponto de atenção: o programa foi parcialmente escrito pelo mentor por restrição de tempo. Nas próximas semanas, mesmo com o ritmo do mestrado, é importante que Davi tente escrever as funções antes de pedir ajuda — mesmo que erre. O aprendizado consolidado vem do erro corrigido, não do código copiado.

---

**Próxima meta:**

Continuar integrando atividades do mestrado com programação em Python. Programa de medição de vazão por molinete permanece reservado para Fase 2. Próxima atividade do MPEH18 será tratada na semana 4.

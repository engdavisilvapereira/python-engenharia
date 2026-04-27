# Semana 01 — 21/04 a 27/04/2026

## Sessão 1 — 25/04/2026 (sábado)

**Horas dedicadas:** 2h

**Tópicos estudados:**

- Variáveis, tipos (str, int, float), entrada/saída com input() e print()
- Condicionais (if/elif/else)
- F-strings com formatação (.3f)
- Dicionários aninhados (matriz de fatores de conversão 7×7)
- Funções enumerate(), list(), .keys()
- Tratamento de erros com try/except e exit()
- Instalação e configuração do Git 2.54.0
- Primeiro commit e push para GitHub

**Entregável:**

Conversor de vazão com matriz 7×7 completa (m³/s, m³/h, L/s, L/min, L/h, pcm, GPM), validação de entrada e tratamento de erros. Repositório público em github.com/engdavisilvapereira/python-engenharia.

**Dificuldades encontradas:**

- Confusão inicial entre a pasta .venv (ambiente virtual) e a pasta de trabalho dos scripts. Tentativa de criar arquivos dentro do .venv antes de entender que ela é infraestrutura, não local de trabalho.
- Conceito de ambiente virtual pouco claro no início; necessidade de analogia (rede hidráulica independente por empreendimento) para fixar a ideia de isolamento de dependências.
- Unidades trocadas nos prints das opções 3 e 4 do conversor (m³/h e L/s invertidos na saída); erro corrigido antes da execução.
- Mensagem do else desatualizada após adicionar novas opções (ainda dizia "Digite 1 ou 2" com 4 opções disponíveis).
- Git não instalado na máquina; necessidade de instalar o Git 2.54.0 antes de prosseguir com versionamento.
- Arquivo .gitignore da raiz confundido com o .gitignore interno da .venv; resolvido abrindo o arquivo correto via terminal com notepad.
- Esquecimento de salvar o arquivo antes de executar (SyntaxError resolvido com Ctrl+S).

**Próxima meta:**

Atividade extra da semana 1 a ser definida (a semana ficou curta para o volume de conteúdo previsto). Possibilidades: conversor de unidades de pressão ou comprimento com a mesma arquitetura de dicionários, ou script de cálculo de propriedades geométricas de seções de canais (retangular, trapezoidal, circular).

---

## Sessão 2 — 26/04/2026 (domingo)

**Horas dedicadas:** 4h

**Tópicos estudados:**

- Reaplicação da arquitetura de dicionários aninhados em domínio diferente (pressão)
- Construção de matriz 8×8 com unidade-ponte (Pa) para garantir consistência dos fatores
- Importação e uso da biblioteca math (math.sqrt, math.acos, math.sin, math.pi)
- Operador de potenciação (**) e distinção entre raiz quadrada e quadrado
- Cálculo de propriedades geométricas hidráulicas (área molhada, perímetro molhado, raio hidráulico)
- Casos particulares de seções (triangular como trapezoidal com b=0, retangular como trapezoidal com z=0)
- Cálculo de ângulo central em seções circulares a partir de yn e D
- Validação de restrições físicas (profundidade ≤ diâmetro em seção circular)
- Convenção PEP 8 para nomes de variáveis (snake_case)
- Fluxo completo de versionamento (git add, commit, push) aplicado em três commits independentes

**Entregável:**

Dois novos programas adicionados ao repositório. (1) Conversor de pressão com matriz 8×8 completa (Pa, kPa, MPa, bar, atm, mca, psi, mmHg) e tratamento de erros. (2) Calculadora de propriedades geométricas de seções de canais (retangular, triangular, trapezoidal e circular), retornando área molhada, perímetro molhado e raio hidráulico. Validação dimensional e tratamento de erros em todas as opções.

**Dificuldades encontradas:**

- Inconsistência entre os dicionários fatores e nomes na primeira versão do conversor de pressão (chave "MPa" no fatores mas "mmHg" no nomes); resolvida com revisão sistemática das chaves e expansão da matriz para 8×8.
- Erro de ordem de grandeza em alguns fatores derivados manualmente (ex.: kPa → atm com fator 9,87 em vez de 0,009869); corrigido com recálculo a partir da unidade SI.
- Confusão na aplicação das fórmulas trigonométricas da seção circular: uso de math.sqrt onde deveria ser potenciação (D²), e operação de multiplicação onde deveria ser subtração entre θ e sen(θ).
- Cópia de mensagens dos prints sem atualizar o tipo de seção (todas as seções imprimiam "retangular" inicialmente).
- Tentativa de digitar valores decimais com vírgula (formato brasileiro) em vez de ponto (formato Python); erro tratado pelo try/except mas requer atenção do usuário.
- Dúvida sobre a sintaxe correta do encadeamento de condicionais (if seguido de elif, não outro if).

**Próxima meta:**

Iniciar a semana 2 do plano: script de classificação de regimes de escoamento pelo número de Froude. Avaliar refatoração dos três programas atuais para uso de funções (prevista na semana 3) com vista à reutilização cruzada — por exemplo, o conversor de unidades poder ser chamado pelo cálculo de seção quando o usuário fornecer dados em unidades não padrão.

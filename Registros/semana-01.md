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

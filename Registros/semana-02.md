# Semana 02 — 28/04 a 03/05/2026
# Fase 1 — Fundamentos de Python (continuação antecipada de Fase 2)

---

## Sessão 1 — 03/05/2026 (sábado)

**Horas dedicadas:** ~6h

**Tópicos estudados:**

- Definição de funções com def, parâmetros e return
- Dicionário como tipo de retorno de função (retorno estruturado)
- Modularização: separação entre funções de cálculo e programa principal
- if __name__ == "__main__": proteção de módulos para importação
- Importação entre módulos com from modulo import funcao
- Princípio da responsabilidade única: cada função faz uma coisa só
- Arquitetura em blocos reutilizáveis — padrão aplicado a todos os programas
- Classificação de regime de escoamento pelo número de Froude
- Profundidade hidráulica (Dh = A/B) como parâmetro do Froude em canais abertos
- Faixa de regime crítico (0,95 ≤ Fr ≤ 1,05) como tolerância numérica adequada
- Cálculo de vazão por Manning: Q = (1/n) × A × Rh^(2/3) × S^(1/2)
- Leitura de arquivo CSV com módulo nativo csv e csv.DictReader
- Conversão de tipos ao ler CSV (str → float) e cálculo de n_medio
- Filtragem dinâmica de lista por categoria com for e if
- Equação de Hazen-Williams: V = 0,8492 × C × Rh^0,63 × S^0,54
- Número de Reynolds em condutos forçados e classificação de regime (laminar/transição/turbulento)
- Rastreabilidade bibliográfica em tabelas de dados de engenharia

**Entregáveis:**

Sete programas na pasta Fase-01-fundamentos, todos modularizados com funções importáveis e if __name__ == "__main__":

1. **conversor_vazao.py** — refatorado com converter_vazao() e secao_vazao() importáveis
2. **Conversor_Pressao.py** — refatorado com converter_pressao() e secao_pressao() importáveis
3. **Calc_Secao_Canal.py** — refatorado com calcular_retangular(), calcular_triangular(), calcular_trapezoidal(), calcular_circular() e selecionar_secao() importáveis
4. **Classificador_Froude.py** — calcular_froude() e secao_froude() importáveis, integrado ao Calc_Secao_Canal.py
5. **calc_manning.py** — integrado ao Calc_Secao_Canal.py e ao Classificador_Froude.py, com seleção de n por tabela CSV
6. **calc_hazen_williams.py** — seleção de C por tabela CSV com condição e fonte bibliográfica, cálculo de Reynolds, classificação de regime
7. **tabela_manning_n.csv** — 36 materiais, fonte: Bentley/Engman 1986
8. **tabela_hazen_williams.csv** — 53 entradas por material e condição, fontes: Azevedo Netto et al. (1998), Porto (2006), AWWA (M11, M23, M55, M41), DIPRA (2006), PPI Handbook, Lamont (1981), Williams & Hazen (1933), entre outras

Repositório: github.com/engdavisilvapereira/python-engenharia — 9 commits acumulados.

**Dificuldades encontradas:**

- Tendência recorrente de avançar sem reler o código antes de enviar, gerando erros evitáveis (dois pontos faltando em def, código após return nunca executado, variáveis mal referenciadas).
- Confusão entre referenciar uma função (nome_funcao) e executá-la (nome_funcao()) — erro sutil com consequência silenciosa.
- CSV com formatação incorreta (aspas duplas envolvendo linhas inteiras) impedindo leitura correta pelo DictReader; resolvido com regeação do arquivo com delimitação padrão.
- Tendência de repetir blocos de código que poderiam ser centralizados em uma função — identificado e corrigido com a criação de selecionar_secao() compartilhada.
- Indentação inconsistente dentro de funções (8 espaços em vez de 4 em um trecho).
- Dificuldade inicial em entender o fluxo de importação entre módulos e por que if __name__ == "__main__" é necessário.

**Avaliação da semana:**

Volume muito acima do previsto. O plano da semana 2 previa classificador de Froude e consolidação de condicionais; foram entregues adicionalmente Manning, Hazen-Williams, refatoração completa de todos os programas anteriores para arquitetura modular, e duas tabelas CSV com rastreabilidade bibliográfica. Funções e modularização — conteúdo previsto para a semana 3 — foram antecipados e aplicados com clareza.

O padrão de erros de atenção (reler antes de executar) persiste e precisa ser corrigido ativamente. A compreensão conceitual está sólida.

---

**Próxima meta:**

Semana 3 do plano: revisão formal de funções, introdução a laços aninhados (for dentro de for) e listas de listas. Base necessária para o programa de medição de vazão por molinete (método das seções/verticais), reservado para a Fase 2 após análise dos documentos da ANA e planilha de campo do Rio Bicas (Wenceslau Braz, MG, novembro de 2023).

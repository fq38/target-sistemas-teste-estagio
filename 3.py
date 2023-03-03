"""
 Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

"""

import json

# Lê o arquivo de dados em formato json
with open('faturamento.json') as file:
    data = json.load(file)

# Obtém os valores de faturamento diário
faturamento_diario = data['faturamento']

# Calcula o menor e o maior valor de faturamento diário
menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)

# Calcula a média mensal de faturamento
dias_no_mes = len(faturamento_diario)
soma_faturamento = sum(faturamento_diario)
media_mensal = soma_faturamento / dias_no_mes

# Calcula o número de dias em que o faturamento foi superior à média mensal
dias_acima_da_media = sum(1 for f in faturamento_diario if f > media_mensal)

# Imprime os resultados
print("Menor faturamento diário:", menor_faturamento)
print("Maior faturamento diário:", maior_faturamento)
print("Número de dias com faturamento acima da média mensal:", dias_acima_da_media)

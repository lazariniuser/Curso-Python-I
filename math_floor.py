from os import system
import math

system('cls')

# Um caminhão transporta ?? toneladas de carga máxima.
# Quantas viagens ele precisa fazer somente com capacidade máxima

capacidade_total = int(input('Carga total do caminhão (em toneladas): '))
carga_viagem = float(input('Carga para viagem (em toneladas): '))

qtde_viagens = math.floor(carga_viagem / capacidade_total)
carga_restante = carga_viagem - (capacidade_total * qtde_viagens)

print(f'Qtde de viagens carga máxima: {qtde_viagens}')
print(f'Carga restante: {carga_restante:.2f} toneladas')

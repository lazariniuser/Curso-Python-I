from os import system
system('cls')
import math
capacidade_total = int(input('capacidade em toneladas \n'))
carga_viagem = float(input('qts toneladas? \n'))
qtd = math.floor(carga_viagem/capacidade_total)
qtd2 = math.ceil(carga_viagem/capacidade_total)
qtd3 = round(carga_viagem/capacidade_total)
carga_restante = carga_viagem - (capacidade_total * qtd)
print(f'Comando floor: {qtd}')
print(f'Comando ceil: {qtd2}')
print(f'Comando round: {qtd3}')
print(f'Carga restante: {carga_restante}')
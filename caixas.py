from os import system
system('cls')
import math


#armazene alguns produtos e diga em quantas caixas será preciso armazenas

num_produtos = int(input('informe o número de produtos'))
produtos_caixa = int(input('qts caixas'))
qtd = math.ceil(num_produtos/produtos_caixa)
print(f'caixas necessárias: {qtd}')
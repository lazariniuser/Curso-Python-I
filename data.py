from os import system
system('cls')
from datetime import datetime

def calculaidade(datainput):
    dia = datetime.now()
    datainput = input('Digite uma data \n')
    datacerta = datetime.strptime(datainput, '%d/%m/%Y')
    res = dia.year-datacerta.year
    print(f'Esta pesssoa tem {res} anos em {dia.year}')
    decide = input(f'Deseja saber mais uma idade?')
    if decide == 'sim':
        calculaidade(datainput)
    else:
        print('parei')

    return res
ano = ""
calculaidade(ano)



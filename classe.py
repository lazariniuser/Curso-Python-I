from os import system
from datetime import datetime 
system('cls')

class Servico:
    #inicializador, para que a variável não fique nula ou vazia 
    def __init__(self, descricao, preco, datah):
        self.descricao = descricao
        self.preco = preco
        self.datah = datah # Usa a data que foi passada como argumento

    def exibir_dados(self):
        print(f'Descrição: {self.descricao}')
        print(f'Preço: R${self.preco:.2f}')
        print(f'Data e horário: {self.datah.strftime("%d/%m/%Y %H:%M")}') # Chaves adicionadas e data formatada

    def salvahist(self):
         # O 'with' garante o fechamento seguro do arquivo após a escrita acabar.
         with open('historico_servicos.txt', "a", encoding='utf-8') as f:
              f.write(f'Descrição : {self.descricao}\n')
              f.write(f'Preço : R${self.preco:.2f}\n')
              f.write(f'Data/Hora : {self.datah}\n') # Chaves adicionadas aqui
              f.write('-' * 40 + '\n')

continuar = 'S'

print(' == CADASTRO DE SERVIÇOS ==')
while continuar.upper() != 'X':
        descricao = input('Informe a descrição do serviço: ')
        preco = input('Informe o preço do serviço: ')
        datah = datetime.now() # Captura o momento exato do cadastro

        # Validação do preço
        try:
            preco = float(preco)
        except ValueError:
             print('Valor inválido! Digite um número.')
             print('-' * 40)
             continue
             
        # Criando a instância e executando as ações
        servico = Servico(descricao, preco, datah)
        servico.exibir_dados() 
        servico.salvahist()
        
        print('-' * 40)   
        continuar = input('Tecle "Enter" para continuar ou "X" para sair: ')

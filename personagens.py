from os import system
import os  

class Personagem:
    def __init__(self, nome, energia, dano):
        self.nome = nome
        self.energia = energia
        self.dano = dano
    def atacar(self, inimigo):
        inimigo.energia -= self.dano
        inimigo.energia = max(inimigo.energia, 0)  # Garantir que a energia não fique negativa
        print(f'{self.nome} atacou {inimigo.nome} causando {self.dano} de dano.')
        print(f'{inimigo.nome} agora tem {inimigo.energia} de vida restante.')

        if inimigo.energia <= 0:
            print(f'{inimigo.nome} foi derrotado! por {self.nome}')
            return True  # Retorna True se o inimigo foi derrotado   
        
print('Boas vindas à arena de batalhas!')
print('='*50)
nome_jogador = input('Digite o nome do seu personagem: \n')

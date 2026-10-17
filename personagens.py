from os import system
import os  
import random
import time
class Personagem:
    def __init__(self, nome, energia, dano):
        self.nome = nome
        self.energia = energia
        self.dano = dano
    def atacar(self, inimigo):
        while inimigo.energia > 0 and self.energia > 0:
            inimigo.energia -= self.dano
            inimigo.energia = max(inimigo.energia, 0)  # Garantir que a energia não fique negativa
            print(f'{self.nome} atacou {inimigo.nome} causando {self.dano} de dano.')
            print('-'*50)
            time.sleep(1)
            print('-'*50)
            print(f'{inimigo.nome} agora tem {inimigo.energia} de vida restante.')

            if inimigo.energia <= 0:
                print(f'{inimigo.nome} foi derrotado! por {self.nome}')
                return True  # Retorna True se o inimigo foi derrotado   
        
print('Boas vindas à arena de batalhas!')
print('='*50)

mago = Personagem('Mago', 100, random.randint(1, 100))
guerreiro = Personagem('Guerreiro', 150, random.randint(1, 100) )
npc = Personagem('NPC', 100, random.randint(1, 100))
decide = random.randint(1, 3)

if decide == 1:
    print('O Mago atacará o Guerreiro!')
    mago.atacar(guerreiro)
elif decide == 2:
    print('O Guerreiro atacará o Mago!')
    guerreiro.atacar(npc)
else:
    print('O NPC atacará o Mago!')
    npc.atacar(mago)
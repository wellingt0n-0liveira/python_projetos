#Segue um snippet bem simples em Python para gerar 50
#resultados aleatórios de pedra, papel e tesoura, um por linha:

import random

opcoes = ["pedra", "papel", "tesoura"]

for i in range(50):
    jogada = random.choice(opcoes)
    print(f"{i+1}. {jogada}")
    
#Se quiser sem numeração, é só trocar o print por:
# print(jogada)
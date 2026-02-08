import random

opcoes = ["pedra", "papel", "tesoura"]

for i in range(50):
    jogada = random.choice(opcoes)
    print(f"{i+1}. {jogada}")
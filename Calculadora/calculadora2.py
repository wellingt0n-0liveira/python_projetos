
# calculadora.py - versão 2

print("Calculadora Simples")
print("Operações disponíveis: + - * / ")

operador = input("Escolha a operação:  ")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if operador == '+':
    resultado = numero1 + numero2
elif operador == '-':
    resultado = numero1 - numero2
elif operador == '*':
    resultado = numero1 * numero2
#elif operador == '/':
 #   resultado = numero1 / numero2
elif operador == "/":
    if numero2 == 0:
        print("Erro: divisão por zero não é permitida.")
        resultado = None
    else:
        resultado = numero1 / numero2
else:
    print("Operador inválido!")
    
    
if resultado is not None:
    print("O resultado:", resultado)
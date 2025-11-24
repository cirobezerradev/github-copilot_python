# Receber do usuário dois numeros inteiros e realizar as quatro operações matemáticas básicas (adição, subtração, multiplicação e divisão), chamando funções para cada operação.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero não é permitida."

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Realizando as operações e exibindo os resultados, exemplo retorno: "Adição -> 5 + 3 = 8"
print(f"Adição -> {num1} + {num2} = {add(num1, num2)}")
print(f"Subtração -> {num1} - {num2} = {subtract(num1, num2)}")
print(f"Multiplicação -> {num1} * {num2} = {multiply(num1, num2)}")
print(f"Divisão -> {num1} / {num2} = {divide(num1, num2)}")
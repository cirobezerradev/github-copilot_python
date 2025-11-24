# receber do usuário uma string e um numero inteiro, e repetir a string o número de vezes indicado com quebra de linha, chamando uma função.

def repeat_text(text, times):
    return (text + "\n") * times

text = input("Digite uma string: ")
times = int(input("Digite um número inteiro: "))

result = repeat_text(text, times)
print("Texto repetido:", result)
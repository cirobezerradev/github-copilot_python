# O Usuário recebe um número inteiro e a função deve retornar se o número é par ou ímpar e fazer a validação se o valor é realmente um número inteiro. Usando a conveção das type annotations.

def is_even_or_odd(number: int) -> str:
    '''
    O copilot sugeriu essa validação, mas como já o mesmo já fez a conversão
    para int na chamada da função, e já trata a exceção, achei desnecessário pois
    é uma redundância no código, e o erro nunca será atingido, na validação abaixo.
    '''
    # if not isinstance(number, int):
    #     return "Erro: o valor fornecido não é um número inteiro."
    if number % 2 == 0:
        return "O número é par."
    else:
        return "O número é ímpar."

user_input = input("Digite um número inteiro: ")
try:
    int_input = int(user_input)
    result = is_even_or_odd(int_input)
except ValueError:
    result = "Erro: o valor fornecido não é um número inteiro."

print(result)
'''
Receber do usuário uma string e verificar se é um palíndromo, chamando uma função. 
Utilizar type annotations. e também a inversão de strings para comparar.'''
def is_palindrome(text: str) -> bool:
    reversed_text = text[::-1]
    return text == reversed_text

user_input = input("Digite uma string: ")
if is_palindrome(user_input):
    print("A string é um palíndromo.")
else:
    print("A string não é um palíndromo.") 

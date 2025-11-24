'''
Decidi usar a lib numpy para testar o copilot, pois é uma lib
muito utilizada em cálculos matemáticos e estatísticos em Python.
'''
'''receba três notas de um aluno, e calcule a média,
chamando uma função para o cálculo da média e utilizando 
a lib numpy para realizar o calculo. o retorno final será com duas casas decimais'''
import numpy as np

def calculate_average(grades):
    return np.mean(grades) 

grades = []
for i in range(3):
    grade = float(input(f"Digite a nota {i+1}: "))
    grades.append(grade)

average = calculate_average(grades)
print(f"A média do aluno é: {average:.2f}")
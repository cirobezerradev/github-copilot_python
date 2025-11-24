# Receber do usuário dois dados distintos e contaná-los, chamando uma função
def concat_data(data1, data2):
    return str(data1) + str(data2)

data1 = input("Digite o primeiro dado: ")
data2 = input("Digite o segundo dado: ")

result = concat_data(data1, data2) 
print("Dados concatenados:", result)


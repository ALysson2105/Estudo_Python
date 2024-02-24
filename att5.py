
numeros = []

for x in range(5):
    numero = float(input("Digite números para ver sua média:"))
    numeros.append(numero)
    print(numero)

def media():
    soma = sum(numeros)
    tamanho = len(numeros)
    resultado = soma/tamanho
    return print(resultado)

media()
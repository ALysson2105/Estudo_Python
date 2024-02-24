numeros = []

for x in range(5):
    numero = float(input("Digite números para ver seu quadrado:"))
    numero = numero ** 2
    numeros.append(numero)
    print(numero)
print(numeros[2])

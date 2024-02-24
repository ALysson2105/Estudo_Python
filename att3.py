celcius = int(input("Digite a temperatura em celsius:"))
def fahrenheit(celcius):
    f = celcius * (9/5) + 32
    return f
resposta = fahrenheit(celcius)
print(f"A temperatura em Fahrenheit é {resposta}")

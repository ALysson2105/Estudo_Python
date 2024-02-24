# ( OBJETO = CLASSE ) ( FUNÇÃO = MÉTODO )
class Carro:
    def __init__(self,marca,modelo,ano,cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
    def descrever_carro(self):
        descricao = f"{self.marca}{self.modelo}{self.ano}{self.cor}"
        print(descricao)

    def acelerar(self,incremento):
        self.velocidade += incremento
        print(f"A velocidade do {self.modelo} agora é {self.velocidade} km/h.")
    def freiar(self,descremento):
        self.velocidade = max(0,self.velocidade-descremento)


uno = Carro("Fiat" , " uno ", 2000, " vermelho ") 
civic = Carro("Honda ","Civic ",2022," preto ")

#uno.descrever_carro()
civic.descrever_carro()

civic.acelerar(50)






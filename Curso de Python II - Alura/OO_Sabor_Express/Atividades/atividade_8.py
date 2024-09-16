# Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano.
# Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro_1 = Carro("Sport", "Preta", "2024")

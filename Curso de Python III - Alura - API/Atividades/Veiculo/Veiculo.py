class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

# 2 - Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada com a marca,
# modelo e o estado de ligado/desligado do veículo.

    def __str__(self):
        return f'Marca: {self._marca}, Modelo: {self._modelo}, Estado: {self._ligado}'
# 5 - Em um arquivo chamado main.py, importe a classe Carro.
# 6 - No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.

from Carro import Carro

veiculo_1 = Carro("Marca 1", "Modelo 1", "Cor 1")
veiculo_2 = Carro("Marca 2", "Modelo 2", "Cor 2")
veiculo_3 = Carro("Marca 3", "Modelo 3", "Cor 3")

def main():
    print(f"Marca: {veiculo_1._marca}, Modelo: {veiculo_1._modelo}, Cor: {veiculo_1.cor}")
    print(f"Marca: {veiculo_2._marca}, Modelo: {veiculo_2._modelo}, Cor: {veiculo_2.cor}")
    print(f"Marca: {veiculo_3._marca}, Modelo: {veiculo_3._modelo}, Cor: {veiculo_3.cor}")

if __name__ == "__main__":
    main()
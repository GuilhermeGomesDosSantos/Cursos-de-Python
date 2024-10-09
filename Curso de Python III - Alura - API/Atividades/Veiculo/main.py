# 7 - Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

# 8 - Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto.
# Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.

from Carro import Carro
from Moto import Moto
carro_1 = Carro("Marca 1", "Modelo 1", 4)
carro_2 = Carro("Marca 2", "Modelo 2", 2)
carro_3 = Carro("Marca 3", "Modelo 3", 6)

moto_1 = Moto("Marca 4", "Modelo 4", "Esportiva")
moto_2 = Moto("Marca 5", "Modelo 5", "Casual")
moto_3 = Moto("Marca 6", "Modelo 6", "Esportiva")

# Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.

def main():
    print(carro_1)
    print(carro_2)
    print(carro_3)
    print(moto_1)
    print(moto_2)
    print(moto_3)

if __name__ == "__main__":
    main()
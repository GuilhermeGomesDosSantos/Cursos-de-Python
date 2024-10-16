from abc import ABC, abstractmethod # é utilizado para trabalhar com classes e metodos abstrados
# ABC é usado para dizer que uma classe é abstrata
# abstractmethod, é usado para dizer que um metodo de uma classe é abstrado

class ItemCardapio(ABC): # estoud dizendo que a classe ItemCardapio é abstrata
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        
    @abstractmethod # estou dizendo que o metodo abstractmethod é abstrato
    def aplicar_desconto(self):
        pass
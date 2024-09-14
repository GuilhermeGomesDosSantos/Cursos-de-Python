class Restaurante: # classe é uma abstração de um objeto do mundo em codigo
    def __init__(self, nome, categoria): # o def __init__ é um construtor que define quais parametros o objeto terá
    # o self, refere-se á instância atual da classe, ele aponta para a instância específica
    # atributos, são as caracteristicas do objeto
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

# instanciar um objeto/criando um restaurante
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

restaurantes = [restaurante_pizza, restaurante_praca]

print(restaurantes)
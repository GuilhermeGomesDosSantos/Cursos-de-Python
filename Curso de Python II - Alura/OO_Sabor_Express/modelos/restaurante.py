class Restaurante(): # classe é uma abstração de um objeto do mundo em codigo
    # atributos, são as caracteristicas do objeto
    nome = ''
    categoria = ''
    ativo = False

# instanciar um objeto/criando um restaurante
restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()

restaurantes = [restaurante_pizza, restaurante_praca]

print(restaurantes)
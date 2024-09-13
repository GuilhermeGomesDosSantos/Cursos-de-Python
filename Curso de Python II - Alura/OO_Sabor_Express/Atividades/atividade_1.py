# Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.

class Restaurante():
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()

restaurante_praca.categoria = 'Italiana'

print(f"Categoria do Restaurante da Praça é: {restaurante_praca.categoria}")
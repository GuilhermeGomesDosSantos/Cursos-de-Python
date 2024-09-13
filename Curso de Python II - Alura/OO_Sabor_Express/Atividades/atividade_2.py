# Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.

class Restaurante():
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
nome_do_restaurante = restaurante_praca.nome
print(f"Nome: {nome_do_restaurante}")
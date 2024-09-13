# Altere o valor do atributo nome para 'Bistrô'.

class Restaurante():
    nome = ""
    categoria = ""
    ativo = False

restaurante_praca = Restaurante()

nome_new = restaurante_praca.nome = "Bistrô"

print(nome_new)
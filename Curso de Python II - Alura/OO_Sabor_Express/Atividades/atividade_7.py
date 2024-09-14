# Imprima no console o nome e a categoria da instância restaurante_praca.

class Restaurante:
    nome = ""
    categoria = ""
    ativo = False

restaurante_praca = Restaurante()

restaurante_praca.nome = "Bistrô"
restaurante_praca.categoria = "Italiana"

print(f"Nome do restaurante '{restaurante_praca.nome}'\nCategoria '{restaurante_praca.categoria}'")
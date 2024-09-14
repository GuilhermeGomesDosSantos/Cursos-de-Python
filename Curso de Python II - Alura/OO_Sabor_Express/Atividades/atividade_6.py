# Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
# Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
# Mude o estado da instância restaurante_pizza para ativo.

class Restaurante():
    nome = ""
    categoria = ""
    ativo = False


'''Criando uma instância chamada restaurante_pizza'''
restaurante_pizza = Restaurante()

restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "Fast Food"

if restaurante_pizza.categoria == "Fast Food":
    print(f"A categoria do restaurante {restaurante_pizza.nome} é {restaurante_pizza.categoria}")

else:
    print(f"A categoria do restaurante {restaurante_pizza.nome} não é Fast Food")

restaurante_pizza.ativo = True

print(f"Status do restaurante {restaurante_pizza.nome}\n")
print(f"""Nome: {restaurante_pizza.nome}
Categoria: {restaurante_pizza.categoria}
Situação: {restaurante_pizza.ativo}""")
# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria.
# Exiba essa mensagem para uma instância de restaurante.

class Restaurante:
    def __init__(self, nome, categoria, e_mail, telefone, ativo = False):
        self.nome = nome
        self.categoria = categoria
        self.e_mail = e_mail
        self.telefone = telefone
        self.ativo = ativo

    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria}'

restaurante_1 = Restaurante("Teste Restaurante", "Testes", "restauranteteste@gmail.com", "123456789")

print(restaurante_1)
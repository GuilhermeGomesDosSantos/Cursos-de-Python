# Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

class Restaurante:
    def __init__(self, nome, categoria, e_mail, telefone, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.e_email = e_mail
        self.telefone = telefone
        self.ativo = ativo

restaurante_1 = Restaurante("Restaurante 1", "Teste", "RestauranteTeste@gmail.com", "123321123")
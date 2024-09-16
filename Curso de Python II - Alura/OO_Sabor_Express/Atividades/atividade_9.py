# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos.
# Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    def __init__(self, nome, categoria, e_mail, telefone, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.e_mail = e_mail
        self.telefone = telefone
        self.ativo = ativo

restaurante_1 = Restaurante("Restaurante teste", "Somente teste", "restaurante123321@gmail.com", "123456789", True)
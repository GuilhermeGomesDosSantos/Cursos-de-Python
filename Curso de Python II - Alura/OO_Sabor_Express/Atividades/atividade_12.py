# Crie uma classe chamada Cliente e pense em 4 atributos.
# Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(this, nome, e_mail, telefone, idade):
        this.nome = nome
        this.e_mail = e_mail
        this.telefone = telefone
        this.idade = idade
    
cliente_1 = Cliente("Cliente 1", "cliente1@gmail.com", "123456789", "40")
cliente_2 = Cliente("Cliente 2", "cliente2@gmail.com", "123456789", "33")
cliente_3 = Cliente("Cliente 3", "cliente3@gmail.com", "987654321", "22")
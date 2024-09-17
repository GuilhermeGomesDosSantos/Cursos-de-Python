# Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos.
# Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

# Crie um método de classe para a conta ClienteBanco.

class ClienteBanco:

    def __init__(self, nome = '', cpf = '', rg = '', dataNasc = '', ativo = False):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.dataNasc = dataNasc
        self.ativo = ativo


    @classmethod
    def listar_informacoes_cliente(cls):
        return ('Parabens, conta Criada com sucesso !!!')

cliente_banco = ClienteBanco("Gui")
print(cliente_banco.listar_informacoes_cliente())
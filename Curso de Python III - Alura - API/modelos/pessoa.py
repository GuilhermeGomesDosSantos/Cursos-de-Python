# Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão.
# Adicione um método especial __str__ para imprimir uma representação em string da pessoa.
# Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano.
# Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

class Pessoa:
    def __init__(self, nome = None, idade = None, profissao = None):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'Nome: {self.nome} | Idade: {self.idade} | Profissão: {self.profissao}'
    
    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        if self.profissao:
            return f"Olá sou o(a) {self.nome}, tenho {self.idade} e sou um(a) {self.profissao}"
        else:
            return f"Olá sou o(a) {self.nome}"
    
pessoa_1 = Pessoa("Guilherme", 21, "Programador")
pessoa_2 = Pessoa('', 22)

print(pessoa_1)
print(pessoa_2)

pessoa_1.aniversario()

print(pessoa_1.saudacao)
print(pessoa_2.saudacao)
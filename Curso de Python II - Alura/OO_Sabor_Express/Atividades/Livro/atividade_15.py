# 1 - Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao.
# Inicie um atributo chamado disponivel como True por padrão.

# 2 - Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro.
# Crie duas instâncias da classe Livro e imprima essas instâncias.

# 3 - Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False.
# Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.


class Livro:
    lista_livros = []

    def __init__(self,titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.lista_livros.append(self)

    def __str__(self):
        return f'Livro: {self._titulo}, feito por {self._autor}", no ano de {self._ano_publicacao}'
    

    def emprestar_livro(self):
        self._disponivel = False

# 4 - Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

# - 5 Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
# - 6 No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
# - 7 No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
# - 8 Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis_ano = [livro._titulo for livro in Livro.lista_livros if livro._ano_publicacao == str(ano) and livro._disponivel]
        return livros_disponiveis_ano
livro_1 = Livro("Livro 1", "Autor abc", "2222")
livro_2 = Livro("Liveo 2", "Autor cba", "2222")

# print(livro_1)
# print(livro_2)

# print(f'Livros disponíveis: {Livro.verificar_disponibilidade("2222")}')

# print(f'Livro: {livro_1._titulo}, antes de emprestar: Livro disponível {livro_1._disponivel}')

# livro_1.emprestar_livro()
# print(f'Livro: {livro_1._titulo}, depois de emprestar: Livro disponível? {livro_1._disponivel}')

    
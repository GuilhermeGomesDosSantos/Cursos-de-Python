# 5 Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

from atividade_15 import Livro

# - 6 No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

livro_test = Livro("Livro test", "Fulano", "2010")
livro_abc = Livro("Livro ABC", "Fulano", "2010")

# livro_test.emprestar_livro()

print(f'O Livro "{livro_test._titulo}", pode ser imprestado no momento? {livro_test._disponivel}')

# - 7 No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.


print(f"Livros disponiveis: {Livro.verificar_disponibilidade(2010)}")
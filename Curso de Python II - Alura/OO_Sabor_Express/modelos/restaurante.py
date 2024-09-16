class Restaurante: # classe é uma abstração de um objeto do mundo em codigo

    restaurantes = []
    
    def __init__(self, nome, categoria): # o def __init__ é um construtor que define quais parametros o objeto terá
    # o self, refere-se á instância atual da classe, ele aponta para a instância específica
    # atributos, são as caracteristicas do objeto
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self) #Como restaurantes é um atributo da classe, você precisa acessar a lista usando a classe e não o self (que se refere à instância)
    
    def __str__(self) -> str: #converte um valor qualquer em string
        #lembrando novamente o self, é a referencia da instancia do obj que está sendo usado naquele momento
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():# para criar sua propria função apenas utilize a palavra def
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    @property #property em python é um decorartor, o property permite transformar um método(função) de uma classe em um atributo de leitura e vice versa
    # permite modificar o comportamento de outra funlção ou método de forma simples e reutilizável
    def ativo(self):
        return f"☑" if self._ativo else "☒"
    
# instanciar um objeto/criando um restaurante
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()
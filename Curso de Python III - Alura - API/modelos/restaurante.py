from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante:  # classe é uma abstração de um objeto do mundo em codigo

    restaurantes = []

    def __init__(
        self, nome, categoria
    ):  # o def __init__ é um construtor que define quais parametros o objeto terá
        # o self, refere-se á instância atual da classe, ele aponta para a instância específica
        # atributos, são as caracteristicas do objeto
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(
            self
        )  # Como restaurantes é um atributo da classe, você precisa acessar a lista usando a classe e não o self (que se refere à instância)
        self._cardapio = []

    def __str__(self) -> str:  # converte um valor qualquer em string
        # lembrando novamente o self, é a referencia da instancia do obj que está sendo usado naquele momento
        return f"{self._nome} | {self.categoria}"

    @classmethod
    def listar_restaurantes(cls):  # metodo da classe Restaurante
        print(
            f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} |{"Status"}'
        )
        # for restaurante in Restaurante.restaurantes:
        for (
            restaurante
        ) in (
            cls.restaurantes
        ):  # acessa por meio do cls o atributo da classe que é a lista resutante
            print(
                f"{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}"
            )

    @property  # property em python é um decorartor, o property permite transformar um método(função) de uma classe em um atributo de leitura e vice versa
    # permite modificar o comportamento de outra funlção ou método de forma simples e reutilizável
    def ativo(self):
        return f"☑" if self._ativo else "☐"

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "-"

        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        # avaliacao._nota, é o atributo de cada obj Avalição que contém a nota
        # self._avalicao, é uma lista de objetos
        # avalicao, é uma variavel temporária que representa cada obj Avaliacao na lista self._avaliacao durante a iteração
        # for avaliacao in self.avaliacao, faz a iteração sobre cada objeto Avalicao presente na lista self._avalicao

        quantidade_de_notas = len(self._avaliacao)

        media = round(soma_das_notas / quantidade_de_notas, 1)

        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(
            item, ItemCardapio
        ):  # irá verificar se o item é um objeto da calsse ItemCardapio
            self._cardapio.append(item)

    def exibir_cardapio(self):
        print(f"Cardapio do restaurante {self._nome}\n")

        for i, item in enumerate(self._cardapio, start=1):
            
            if hasattr(item, "descricao"):
                mensagem_prato = f"{i}. Nome: {item._nome} | Preço R$: {item._preco} | Descrição: {item.descricao}"
                print(mensagem_prato)
            else:
                mensagem_bebida = f"{i}. Nome: {item._nome} | Preço R$: {item._preco} | Tamanho: {item.tamanho}"
                print(mensagem_bebida)

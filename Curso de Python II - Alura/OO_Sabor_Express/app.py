from modelos.restaurante import Restaurante
# na pasta modelos, acesse o arquivo restaurante e importe a classe Restaurante

def main():
    pass

if __name__ == "__main__":
    main()

restaurante_praca = Restaurante("praça", "gourmet")
restaurante_praca.receber_avaliacao("Gui", 4)
restaurante_praca.receber_avaliacao("Fulano", 3)
restaurante_praca.receber_avaliacao("Tester", 7)

Restaurante.listar_restaurantes()
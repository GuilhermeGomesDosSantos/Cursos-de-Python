from modelos.restaurante import Restaurante
# na pasta modelos, acesse o arquivo restaurante e importe a classe Restaurante

def main():
    pass

if __name__ == "__main__":
    main()

restaurante_praca = Restaurante("praça", "gourmet")
restaurante_mexicana = Restaurante("Mexican Food", "Mexicana")
restaurante_japonesa = Restaurante("Japa", "Japonesa")

restaurante_mexicana.alternar_estado()

Restaurante.listar_restaurantes()
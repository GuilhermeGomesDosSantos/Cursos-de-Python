# Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.

class Restaurante():
    nome = ""
    categoria = ""
    ativo = False

restaurante_praca = Restaurante()

restaurante_status = restaurante_praca.ativo

# if restaurante_praca.ativo:
#     print("Restaurante ativo")
# else:
#     print("Restaurante desativado")

ativo = 'ativado' if restaurante_status else 'desativado'

print(f"Restaurante está: {ativo}")
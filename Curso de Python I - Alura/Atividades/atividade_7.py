#Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

user_default = str("GDS")
key_default = str("abc123")

nome = str(input("Olá, qual é o seu nome? "))
user = str(input(f"{nome}, informe o nome do usuário: "))
key = str(input(f"{nome}, agora informe a senha: "))

if key == key_default and user == user_default:
    print("Credenciais OK!")

else:
    print("ERROR, Credenciais incorretas!")
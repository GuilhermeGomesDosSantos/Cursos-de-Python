#Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10

num = int(input("Informe um número: "))

contador = 0

while (contador <= 10):
    print(f"{contador} X {num} = {contador * num}")
    contador += 1

#Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10

num = int(input("Informe um número: "))

contador = 0

for i in range(1, 11):
    print(f"{num} X {i} = {i * num}")
#Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

num = [1, 2, 3, 4, 5, 6, 7,8 , 9, 10]

num_soma = 0

for n in num:
    if n % 2 != 0:
        num_soma += n

print('Total: ', num_soma)


#soma_impares = 0
#for i in range(1, 11, 2):
#    soma_impares += i
#print(soma_impares)

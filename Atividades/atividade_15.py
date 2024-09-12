# Construa um código que calcule a média dos valores em uma lista.
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0

try:
    for n in lista_numeros:
        total += n
    
    media = total / len(lista_numeros)
    print(f"A média da lista é: {media}")

except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
#Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos.
# Utilize um bloco try-except para lidar com possíveis exceções.

nums = [1, 2, 'abc', 4, 5, 6, 7, 8, 9, 10]
total = 0
for n in nums:
    try:
        total += n
    except:
        total +=0
print(f"Total é: {total}")
##Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

idade = int(input('Olá, qual é a sua idade? '))

if 0 < idade <= 12:
    # 1° verifica se idade é maior que 0, e em seguida verifica se idade é maior ou igual a 12
    print(f'Idade de Criança, Idade: {idade}')

elif 11 < idade <= 18:
    print(f'Idade de Adolescente, Idade: {idade}')

elif idade >= 18:
    print(f'Idade de Adulto, Idade: {idade}')
    
else:
    print("Valor inválido!")
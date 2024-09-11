##Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

numero = int(input('Informe um número: '))

if numero % 2 == 0:
    print(f'O número "{numero}" é PAR')
else:
    print(f'O número "{numero} é IMPAR')
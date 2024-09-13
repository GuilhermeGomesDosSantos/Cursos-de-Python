#Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

#    Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#    Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#    Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#    Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#    Caso contrário: o ponto está localizado no eixo ou origem.

num_x = float(input("Informe um valor para a coordenada 'X': "))
num_y = float(input("Informe um valor para a coordenada 'Y': "))

if num_x > 0 and num_y > 0:
    print("Primeiro Quadrante")

elif num_x < 0 and num_y > 0:
    print("Segundo Quadrante")

elif num_x < 0 and num_y < 0:
    print("Terceiro Quadrante")

elif num_x > 0 and num_y < 0:
    print("Quarto Quadrante")
    
else:
    print("o ponto está localizado no eixo ou origem")
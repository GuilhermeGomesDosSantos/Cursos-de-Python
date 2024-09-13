# Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frase = "frase de exemplo de frase para ser contada a frequência"

palavras = frase.split()

lista_palavras = {}

for palavra in palavras:
    if palavra in lista_palavras:
        lista_palavras[palavra] += 1

    else:
        lista_palavras[palavra] = 1

for palavra, contagem in lista_palavras.items():
    print(f"A palavra '{palavra}' tem {contagem} quantidade")
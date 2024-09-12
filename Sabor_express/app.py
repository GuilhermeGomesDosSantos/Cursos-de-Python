import os

restaurantes = [
{'nome':'Praça', 'categoria': 'Japonesa', 'ativo': False},
{'nome':'Pizza Suprema', 'categoria':'Pizza','ativo':True},
{'nome':'Cantina', 'categoria':'Italiano', 'ativo': False}
]

def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal")
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def exibir_nome_do_programa():
    print(
        """

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
"""
    )


def finalizar_app():
    os.system("cls")
    exibir_subtitulo("Finalizando o app")


def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")


def opcao_invalida():
    print("Opção invalida!\n")
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    os.system("cls")
    exibir_subtitulo("Cadastro de novos restaurantes!\n")

    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria_do_restaurante = input(f"Digite a categoria do restaurante {nome_do_restaurante}: ")
    ativo_do_restaurante = False

    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria_do_restaurante, "ativo":ativo_do_restaurante}
    restaurantes.append(dados_do_restaurante)

    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")

    voltar_ao_menu_principal()


def listar_restaurantes():
    os.system('cls')
    exibir_subtitulo('Listando restaurantes\n')

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"] #atribuindo o valor da chave nome a variavel nome_restaurante
        categoria = restaurante["categoria"]
        ativo = restaurante["ativo"]
        print(f'- {nome_restaurante} | {categoria} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo("Alterando o estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")

    restaurante_encontrado = False
    
    for restaurante in restaurantes: #vai procurar pelo nome do restaurante, vai percorrer o dicionario pela chave 'nome'
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True

            restaurante["ativo"] = not restaurante["ativo"]# irá ativar ou desativar
            
            mensagem = f"O restaurante {nome_restaurante}, foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"

            print(mensagem)

        if not restaurante_encontrado:
            print(f"O restaurante {nome_restaurante} não foi encontrado")

        voltar_ao_menu_principal()

def escolher_opcao():

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alternar_estado_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()

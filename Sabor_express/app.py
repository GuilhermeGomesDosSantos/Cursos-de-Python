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
    '''Exibe o subtitulo de uma das opções do menu principal'''
    os.system('cls')
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def exibir_nome_do_programa():
    print(
        '''Exibe o nome estilizado do programa na tela'''
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
    '''Finaliza a interação com o app'''
    os.system("cls")
    exibir_subtitulo("Finalizando o app")


def exibir_opcoes():
    '''Exibe as opções do menu'''
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")


def opcao_invalida():
    '''Exibe mensagem de opção inválida e retorna para o menu principal'''
    print("Opção invalida!\n")
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    '''

    os.system("cls")
    exibir_subtitulo("Cadastro de novos restaurantes!")

    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria_do_restaurante = input(f"Digite a categoria do restaurante {nome_do_restaurante}: ")
    ativo_do_restaurante = False

    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria_do_restaurante, "ativo":ativo_do_restaurante}
    restaurantes.append(dados_do_restaurante)

    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")

    voltar_ao_menu_principal()


def listar_restaurantes():
    '''Essa função é responsavel por listar todos os restaurantes que estão cadastrados'''
    os.system('cls')
    exibir_subtitulo('Listando restaurantes')

    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"] #atribuindo o valor da chave nome a variavel nome_restaurante
        categoria = restaurante["categoria"]
        ativo = 'ativado' if restaurante["ativo"] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função é responsavel por permitir que um restaurante esteja ativo ou desativado'''

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
    '''Essa função permite selecionar uma opção do menu principal'''
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
    '''Função principal que inicia o programa;'''
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()

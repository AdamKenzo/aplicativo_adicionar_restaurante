import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema','categoria':'Pizza','ativo':True},
                {'nome':'Cantina', 'categoria':'Italiana', 'ativo':False}]

def exibir_nome_do_programa():
    ''' Essa função é responsável por exibir o nome do programa estilizado na tela'''
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░     
''')

def exibir_opcoes():
    '''Essa função é responsável por exibir as opções disponíveis do menu principal'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Exibe mensagem de finalização do aplicativo'''
    exibir_subtitulo('Finalizando o app') 

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()


def opcao_invalida():
    '''Exibe mensagem de opção inválida e retorna ao menu'''
    exibir_subtitulo('Opção inválida!')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função limpa a tela e exibe o subtítulo desejado com estilização
    
    Inputs:
    -texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante

    Input:
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurantes = input('Digiite o nome do restaurante que deseja cadastrar:')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurantes}: ')
    dados_do_restaurante = {'nome':nome_do_restaurantes,'categoria':categoria, 'ativo':False}

    restaurantes.append(dados_do_restaurante)
    print(f' O restaurante {nome_do_restaurantes} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()


def listar_restaurantes():
    '''Essa função exibe os restaurantes presente na lista
    
    Output:
    - Exibe a lista, que possue o nome dos restaurantes e sua categoria e se é ativo ou não
    '''
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def  aleterar_estado_restaurante():
    '''Essa função altera o estado de um restaurantes, tanto para ativo quanto para desativado
    
    Input:
    - texto: str - O nome do restaurante, que é usado para ver se esta na lista de restaurantes

    Output:
    - verdadeiro ou falso: boolean - O estado do restaurante, ativo ou desativado
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alteramdo estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcoes():
    '''Essa função solicita e direciona para o caminho disponível desejado, dependo do que o usuário digita
    
    Input:
    - número: number - número digitado pelo usuário

    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            aleterar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função principal do aplicativo responsável por inicia-lo'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()



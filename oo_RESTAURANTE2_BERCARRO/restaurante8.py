import os
from app import Restaurante8

restaurantes = [
    Restaurante8('Bife-sujo', 'prato-feito', True),
    Restaurante8('Saco do feijão', 'feijoada', False),
    Restaurante8('Doces da Bernadete', 'doceria', True)
]

def mostrar_subtitulo(texto):
    os.system('clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    mostrar_subtitulo('Finalizando o Aplicativo')

def chamar_nome_do_app():
    print('''
    
    ℜ𝔢𝔰𝔱𝔞𝔲𝔯𝔞𝔫𝔱𝔢 𝔈𝔵𝔭𝔯𝔢𝔰𝔰𝔬
    
    ''')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def exibir_opcoes():
    print("1 Cadastrar Restaurante")
    print("2 Listar Restaurantes")
    print("3 Ativar/Desativar Restaurante")
    print("4 Sair\n")

def cadastrar_novo_restaurante():
    os.system('clear')
    nome_do_restaurante = input('Digite o nome do novo restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    restaurante = Restaurante8(nome_do_restaurante, categoria, False)
    restaurantes.append(restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    mostrar_subtitulo('Listando os Restaurantes')
    print(f'{"Nome do Restaurante":<20} | {"Categoria":<20} | {"Estado":<10}')
    for restaurante in restaurantes:
        print(f'{restaurante.nome:<20} | {restaurante.categoria:<20} | {"Ativo" if restaurante.ativo else "Desativado"}')
    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    mostrar_subtitulo('Alternando o Estado do Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante.nome:
            restaurante.ativar_desativar()
            restaurante_encontrado = True
            print(f'O estado do restaurante {restaurante.nome} foi alterado com sucesso.')
    if not restaurante_encontrado:
        print('Restaurante não encontrado.')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_digitada = int(input("Escolha uma opção: "))
        print("Você selecionou:", opcao_digitada, "\n")
        if opcao_digitada == 1:
            cadastrar_novo_restaurante()
            finalizar_app()
        elif opcao_digitada == 2:
            listar_restaurantes()
            finalizar_app()
        elif opcao_digitada == 3:
            alterar_estado_restaurante()
            finalizar_app()
        elif opcao_digitada == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    os.system('clear')
    chamar_nome_do_app()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
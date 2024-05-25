from anytree import RenderTree

from ui import Ui
from entidades import Rede

usuario_quer_sair = False
rede = Rede()

while not usuario_quer_sair:
    Ui.mostrar_opcoes_inicias()
    opcao = Ui.escolher_opcao_inicial()
    match opcao:
        case 0:
            rede.renderizar()
            Ui.pausa()
        case 1:
            print('\nEscolha o nome do novo usuário')
            usuario = input('> ')
            while len(usuario) < 1:
                print("\nNome Inválido")
                usuario = input('> ')
            if usuario in rede.buscar_todos_usuarios():
                print("Usuário já existe na árvore.")
                Ui.pausa()
            rede.adicionar_usuario(usuario)
        case 2:
            print("Digite o nome do usuário")
            usuario = input("> ")
            while usuario not in rede.buscar_todos_usuarios():
                print("\nUsuário não existe na árvore")
                usuario = input('> ')
            rede.remover_usuario(usuario)
        case 3:
            print("Digite o nome do usuário")
            usuario = input("> ")
            while len(usuario) < 1 or usuario not in rede.buscar_todos_usuarios():
                if len(usuario) < 1:
                    print("Nome inválido")
                elif usuario not in rede.buscar_todos_usuarios():
                    print(f"{usuario} não está presente na rede social")
                usuario = input("> ")
            node = rede.encontrar_usuario(usuario)
            for pre, fill, node in RenderTree(node):
                print(f"{pre}{node.name}")
            Ui.pausa()
        case 4:
            print('\nEscolha o nome do primeiro usuário')
            usuario1 = input('> ')
            while usuario1 not in rede.buscar_todos_usuarios():
                print("\nUsuário não existe na árvore")
                usuario1 = input('> ')
            print('\nEscolha o nome do segundo usuário')
            usuario2 = input('> ')
            while usuario2 not in rede.buscar_todos_usuarios():
                print("\nUsuário não existe na árvore")
                usuario2 = input('> ')
            if rede.usuarios_tem_relacao(
                usuario1=usuario1, usuario2=usuario2
            ):
                print("Estes usuários já tem uma relação")
                Ui.pausa()
                continue
            rede.criar_relacionamento(
                usuario1=usuario1,
                usuario2=usuario2
            )
        case 5:
            print('\nEscolha o nome do primeiro usuário')
            usuario1 = input('> ')
            while usuario1 not in rede.buscar_todos_usuarios():
                print("\nUsuário não existe na árvore")
                usuario1 = input('> ')
            print('\nEscolha o nome do segundo usuário')
            usuario2 = input('> ')
            while usuario2 not in rede.buscar_todos_usuarios():
                print("\nUsuário não existe na árvore")
                usuario2 = input('> ')
            if not rede.usuarios_tem_relacao(
                    usuario1=usuario1, usuario2=usuario2
            ):
                print("Estes usuários não tem uma relação")
                Ui.pausa()
                continue
            rede.remover_relacionamento(
                usuario1=usuario1,
                usuario2=usuario2
            )
        case 6:
            usuario_quer_sair = True

print("Desligando...")
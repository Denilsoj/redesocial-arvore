class Ui:

    @staticmethod
    def mostrar_opcoes_inicias():
        Ui.clear()
        print("[0] Mostrar Rede")
        print("[1] Adicionar Usuário")
        print("[2] Remover Usuário")
        print("[3] Visualizar Usuário")
        print("[4] Criar Relacionamento")
        print("[5] Remover Relacionamento")
        print("[6] Sair\n")


    @staticmethod
    def clear():
        for i in range(100):
            print("")

    @staticmethod
    def escolher_opcao_inicial():
        possiveis_opcoes = ["0","1","2","3","4","5","6"]
        input_usuario = input("> ").strip()
        while input_usuario not in possiveis_opcoes:
            print("Opção inválida.")
            input_usuario = input("> ")
        return int(input_usuario)

    @staticmethod
    def pausa():
        input("Enter para continuar...")
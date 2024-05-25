from lib2to3.pytree import Node
from anytree import Node, RenderTree

usuarios = [
    "Jorge",
    "Maria",
    "Claudio",
    "Jones",
    "Gabriel"
]

class Rede:
    def __init__(self):
        self.node = Node("Rede", )
        for user in usuarios:
            Node(user, parent=self.node)

    def renderizar(self):
        for pre, fill, node in RenderTree(self.node):
            print(f"{pre}{node.name}")

    def adicionar_usuario(self, usuario: str):
        Node(usuario, parent=self.node)

    def remover_usuario(self, usuario: str):
        for node in self.node.descendants:
            if node.name == usuario:
                node.parent = None


    def criar_relacionamento(self, usuario1: str, usuario2: str):
        for node in self.node.descendants:
            if node.name == usuario1:
                Node(usuario2, parent=node)
            if node.name == usuario2:
                Node(usuario1, parent=node)

    def remover_relacionamento(self, usuario1: str, usuario2: str):
        for node in self.node.descendants:
            if node.name == usuario1 and node.parent.name == usuario2:
                node.parent = None
            if node.name == usuario2 and node.parent.name == usuario1:
                node.parent = None

    def encontrar_usuario(self, usuario: str) -> Node | None:
        for node in self.node.children:
            if node.name == usuario:
                return node
        return None

    def buscar_todos_usuarios(self):
        return [node.name for node in self.node.children]

    def usuarios_tem_relacao(self, usuario1: str, usuario2: str) -> bool:
        for node in self.node.children:
            if node.name == usuario1:
                for child_node in node.children:
                    if child_node.name == usuario2:
                        return True
        return False
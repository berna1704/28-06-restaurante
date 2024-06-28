class Restaurante8:
    def __init__(self, nome, categoria, ativo=True):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

    def ativar_desativar(self):
        self.ativo = not self.ativo

    def __str__(self):
        estado = "Ativo" if self.ativo else "Desativado"
        return f"Nome: {self.nome}, Categoria: {self.categoria}, Estado: {estado}"
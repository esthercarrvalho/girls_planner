class Usuario:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def verificar_login(self, usuario, senha):
        return self.usuario == usuario and self.senha == senha
class Atividade:
    def __init__(self, titulo, categoria, data, prioridade):
        self.titulo = titulo
        self.categoria = categoria
        self.data = data
        self.prioridade = prioridade
        self.concluida = False

    def concluir(self):
        self.concluida = True

    def editar(self, titulo, categoria, data, prioridade):
        self.titulo = titulo
        self.categoria = categoria
        self.data = data
        self.prioridade = prioridade
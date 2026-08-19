def salvar_atividade(atividade):
    with open("dados/atividades.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(atividade + "\n")


def ler_atividades():
    with open("dados/atividades.txt", "r", encoding="utf-8") as arquivo:
        return arquivo.readlines()
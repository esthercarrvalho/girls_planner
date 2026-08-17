import tkinter as tk
from tkinter import messagebox
from usuario import Usuario
from telas.principal import TelaPrincipal


class TelaLogin:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Girl's Planner - Login")
        self.janela.geometry("400x300")

        self.usuario_cadastrado = Usuario("esther", "1234")

        self.criar_widgets()

        self.janela.mainloop()

    def criar_widgets(self):
        tk.Label(
            self.janela,
            text="🎀 GIRL'S PLANNER",
            font=("Arial", 20)
        ).grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(
            self.janela,
            text="Usuário:"
        ).grid(row=1, column=0, padx=10, pady=10)

        self.campo_usuario = tk.Entry(self.janela)
        self.campo_usuario.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(
            self.janela,
            text="Senha:"
        ).grid(row=2, column=0, padx=10, pady=10)

        self.campo_senha = tk.Entry(
            self.janela,
            show="*"
        )
        self.campo_senha.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(
            self.janela,
            text="ENTRAR",
            command=self.entrar
        ).grid(row=3, column=0, columnspan=2, pady=10)

        tk.Button(
            self.janela,
            text="SAIR",
            command=self.sair
        ).grid(row=4, column=0, columnspan=2)

    def entrar(self):
        usuario = self.campo_usuario.get()
        senha = self.campo_senha.get()

        if self.usuario_cadastrado.verificar_login(usuario, senha):
            self.janela.destroy()
            TelaPrincipal()
        else:
            messagebox.showerror(
                "Erro",
                "Usuário ou senha incorretos!"
            )

    def sair(self):
        resposta = messagebox.askyesno(
            "Sair",
            "Deseja realmente sair?"
        )

        if resposta:
            self.janela.destroy()
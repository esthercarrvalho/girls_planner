import tkinter as tk
from tkinter import messagebox
from atividade import Atividade


class TelaCadastro:
    def __init__(self, janela, atividades):
        self.janela = tk.Toplevel(janela)
        self.janela.title("Nova Atividade")
        self.janela.geometry("350x400")
        self.janela.configure(bg="#FCE4EC")

        self.atividades = atividades

        tk.Label(
            self.janela,
            text="🎀 NOVA ATIVIDADE",
            font=("Arial", 18, "bold"),
            bg="#FCE4EC",
            fg="#8E4A70"
        ).pack(pady=20)

        tk.Label(
            self.janela,
            text="Título",
            bg="#FCE4EC"
        ).pack()

        self.titulo = tk.Entry(self.janela, width=35)
        self.titulo.pack(pady=5)

        tk.Label(
            self.janela,
            text="Categoria",
            bg="#FCE4EC"
        ).pack()

        self.categoria = tk.Entry(self.janela, width=35)
        self.categoria.pack(pady=5)

        tk.Label(
            self.janela,
            text="Data",
            bg="#FCE4EC"
        ).pack()

        self.data = tk.Entry(self.janela, width=35)
        self.data.pack(pady=5)

        tk.Label(
            self.janela,
            text="Prioridade",
            bg="#FCE4EC"
        ).pack()

        self.prioridade = tk.Entry(self.janela, width=35)
        self.prioridade.pack(pady=5)

        tk.Button(
            self.janela,
            text="Cadastrar",
            width=20,
            command=self.cadastrar,
            bg="#C76B9B",
            fg="white",
            relief="flat"
        ).pack(pady=20)

    def cadastrar(self):
        titulo = self.titulo.get().strip()
        categoria = self.categoria.get().strip()
        data = self.data.get().strip()
        prioridade = self.prioridade.get().strip()

        if not titulo or not categoria or not data or not prioridade:
            messagebox.showerror(
                "Erro",
                "Preencha todos os campos!"
            )
            return

        atividade = Atividade(
            titulo,
            categoria,
            data,
            prioridade
        )

        self.atividades.append(atividade)

        messagebox.showinfo(
            "Sucesso",
            "Atividade cadastrada!"
        )

        self.janela.destroy()
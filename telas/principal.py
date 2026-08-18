import tkinter as tk
from tkinter import messagebox

from telas.atividades import TelaAtividades
from telas.cadastro import TelaCadastro


class TelaPrincipal:

    ROSA_CLARO = "#FCE4EC"
    ROSA = "#E8A8C7"
    ROSA_ESCURO = "#C76B9B"
    ROSA_MUITO_ESCURO = "#8E4A70"
    CREME = "#FFF8FB"
    BRANCO = "#FFFFFF"
    TEXTO = "#4A3540"

    def __init__(self):

        self.janela = tk.Tk()

        self.janela.title("Girl's Planner")
        self.janela.geometry("600x550")
        self.janela.resizable(False, False)
        self.janela.configure(bg=self.ROSA_CLARO)

        self.atividades = []

        self.criar_widgets()

        self.janela.mainloop()

    def criar_widgets(self):

        tk.Label(
            self.janela,
            text="🎀",
            font=("Arial", 35),
            bg=self.ROSA_CLARO,
            fg=self.ROSA_ESCURO
        ).pack(pady=(30, 0))

        tk.Label(
            self.janela,
            text="GIRL'S PLANNER",
            font=("Arial", 25, "bold"),
            bg=self.ROSA_CLARO,
            fg=self.ROSA_MUITO_ESCURO
        ).pack()

        tk.Label(
            self.janela,
            text="Olá! Vamos organizar seu dia? ♡",
            font=("Arial", 12),
            bg=self.ROSA_CLARO,
            fg=self.TEXTO
        ).pack(pady=(5, 25))

        quadro = tk.Frame(
            self.janela,
            bg=self.BRANCO,
            padx=40,
            pady=25
        )

        quadro.pack(
            padx=70,
            fill="x"
        )

        tk.Label(
            quadro,
            text="O que você deseja fazer?",
            font=("Arial", 13, "bold"),
            bg=self.BRANCO,
            fg=self.TEXTO
        ).pack(pady=(0, 20))

        tk.Button(
            quadro,
            text="📝  Minhas atividades",
            font=("Arial", 11, "bold"),
            bg=self.ROSA_ESCURO,
            fg=self.BRANCO,
            activebackground=self.ROSA_MUITO_ESCURO,
            activeforeground=self.BRANCO,
            relief="flat",
            cursor="hand2",
            command=self.abrir_atividades
        ).pack(
            fill="x",
            ipady=10,
            pady=7
        )

        tk.Button(
            quadro,
            text="📊  Meu resumo",
            font=("Arial", 11, "bold"),
            bg=self.ROSA,
            fg=self.TEXTO,
            activebackground=self.ROSA_ESCURO,
            activeforeground=self.BRANCO,
            relief="flat",
            cursor="hand2",
            command=self.abrir_resumo
        ).pack(
            fill="x",
            ipady=10,
            pady=7
        )

        tk.Button(
            quadro,
            text="🚪  Sair",
            font=("Arial", 10),
            bg=self.BRANCO,
            fg=self.ROSA_MUITO_ESCURO,
            activebackground=self.ROSA_CLARO,
            relief="flat",
            cursor="hand2",
            command=self.sair
        ).pack(
            pady=(15, 0)
        )

        tk.Label(
            self.janela,
            text="Planeje ✦ Organize ✦ Realize",
            font=("Arial", 9),
            bg=self.ROSA_CLARO,
            fg=self.ROSA_MUITO_ESCURO
        ).pack(pady=25)

    def abrir_atividades(self):

        tela = TelaAtividades(
            self.janela,
            self.atividades
        )

        tk.Button(
            tela.janela,
            text="+ Nova atividade",
            font=("Arial", 10, "bold"),
            bg=self.ROSA_ESCURO,
            fg=self.BRANCO,
            activebackground=self.ROSA_MUITO_ESCURO,
            activeforeground=self.BRANCO,
            relief="flat",
            cursor="hand2",
            command=lambda: self.abrir_cadastro(tela)
        ).pack(pady=5)

    def abrir_cadastro(self, tela_atividades):

        TelaCadastro(
            tela_atividades.janela,
            self.atividades
        )

    def abrir_resumo(self):

        total = len(self.atividades)
        concluidas = sum(
            1 for atividade in self.atividades
            if atividade.concluida
        )
        pendentes = total - concluidas

        messagebox.showinfo(
            "Meu resumo 📊",
            f"Total: {total}\n"
            f"Concluídas: {concluidas}\n"
            f"Pendentes: {pendentes}"
        )

    def sair(self):

        resposta = messagebox.askyesno(
            "Sair",
            "Deseja realmente sair do Girl's Planner?"
        )

        if resposta:
            self.janela.destroy()
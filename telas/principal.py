import tkinter as tk
from tkinter import messagebox


class TelaPrincipal:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Girl's Planner")
        self.janela.geometry("500x400")

        self.criar_widgets()

        self.janela.mainloop()

    def criar_widgets(self):
        tk.Label(
            self.janela,
            text="🎀 GIRL'S PLANNER",
            font=("Arial", 22)
        ).pack(pady=30)

        tk.Label(
            self.janela,
            text="Organize suas atividades!",
            font=("Arial", 12)
        ).pack(pady=5)

        tk.Button(
            self.janela,
            text="📝 Minhas atividades",
            width=25,
            command=self.abrir_atividades
        ).pack(pady=15)

        tk.Button(
            self.janela,
            text="📊 Meu resumo",
            width=25,
            command=self.abrir_resumo
        ).pack(pady=15)

        tk.Button(
            self.janela,
            text="🚪 Sair",
            width=25,
            command=self.sair
        ).pack(pady=15)

    def abrir_atividades(self):
        messagebox.showinfo(
            "Minhas atividades",
            "Tela de atividades será aberta aqui."
        )

    def abrir_resumo(self):
        messagebox.showinfo(
            "Meu resumo",
            "Tela de resumo será aberta aqui."
        )

    def sair(self):
        resposta = messagebox.askyesno(
            "Sair",
            "Deseja realmente sair?"
        )

        if resposta:
            self.janela.destroy()
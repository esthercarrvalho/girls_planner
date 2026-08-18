import tkinter as tk
from tkinter import messagebox

from telas.principal import TelaPrincipal


class TelaLogin:

    # Cores do Girls Planner
    ROSA_CLARO = "#FCE4EC"
    ROSA = "#E8A8C7"
    ROSA_ESCURO = "#C76B9B"
    ROSA_MUITO_ESCURO = "#8E4A70"
    CREME = "#FFF8FB"
    BRANCO = "#FFFFFF"
    TEXTO = "#4A3540"

    def __init__(self):
        self.janela = tk.Tk()

        self.janela.title("Girl's Planner - Login")
        self.janela.geometry("500x500")
        self.janela.resizable(False, False)
        self.janela.configure(bg=self.ROSA_CLARO)

        self.criar_widgets()

        self.janela.mainloop()

    def criar_widgets(self):

        # =========================
        # TÍTULO
        # =========================

        tk.Label(
            self.janela,
            text="🎀",
            font=("Arial", 35),
            bg=self.ROSA_CLARO,
            fg=self.ROSA_ESCURO
        ).pack(pady=(35, 0))

        tk.Label(
            self.janela,
            text="GIRL'S PLANNER",
            font=("Arial", 24, "bold"),
            bg=self.ROSA_CLARO,
            fg=self.ROSA_MUITO_ESCURO
        ).pack()

        tk.Label(
            self.janela,
            text="Organize sua rotina do seu jeitinho ♡",
            font=("Arial", 11),
            bg=self.ROSA_CLARO,
            fg=self.TEXTO
        ).pack(pady=(5, 25))

        # =========================
        # ÁREA DO LOGIN
        # =========================

        quadro = tk.Frame(
            self.janela,
            bg=self.BRANCO,
            padx=35,
            pady=25
        )

        quadro.pack(
            padx=50,
            fill="x"
        )

        # Usuário
        tk.Label(
            quadro,
            text="Usuário",
            font=("Arial", 11, "bold"),
            bg=self.BRANCO,
            fg=self.TEXTO
        ).pack(anchor="w")

        self.campo_usuario = tk.Entry(
            quadro,
            font=("Arial", 11),
            bg=self.CREME,
            fg=self.TEXTO,
            relief="solid",
            bd=1
        )

        self.campo_usuario.pack(
            fill="x",
            ipady=7,
            pady=(5, 15)
        )

        # Senha
        tk.Label(
            quadro,
            text="Senha",
            font=("Arial", 11, "bold"),
            bg=self.BRANCO,
            fg=self.TEXTO
        ).pack(anchor="w")

        self.campo_senha = tk.Entry(
            quadro,
            font=("Arial", 11),
            bg=self.CREME,
            fg=self.TEXTO,
            show="*",
            relief="solid",
            bd=1
        )

        self.campo_senha.pack(
            fill="x",
            ipady=7,
            pady=(5, 20)
        )

        # =========================
        # BOTÃO ENTRAR
        # =========================

        tk.Button(
            quadro,
            text="ENTRAR  ♡",
            font=("Arial", 11, "bold"),
            bg=self.ROSA_ESCURO,
            fg=self.BRANCO,
            activebackground=self.ROSA_MUITO_ESCURO,
            activeforeground=self.BRANCO,
            relief="flat",
            cursor="hand2",
            command=self.entrar
        ).pack(
            fill="x",
            ipady=8,
            pady=(0, 10)
        )

        # =========================
        # BOTÃO SAIR
        # =========================

        tk.Button(
            quadro,
            text="SAIR",
            font=("Arial", 10),
            bg=self.BRANCO,
            fg=self.ROSA_MUITO_ESCURO,
            activebackground=self.ROSA_CLARO,
            relief="flat",
            cursor="hand2",
            command=self.sair
        ).pack()

        # Rodapé
        tk.Label(
            self.janela,
            text="Seu espaço para organizar, planejar e conquistar ✨",
            font=("Arial", 9),
            bg=self.ROSA_CLARO,
            fg=self.ROSA_MUITO_ESCURO
        ).pack(pady=25)

    def entrar(self):

        usuario = self.campo_usuario.get().strip()
        senha = self.campo_senha.get().strip()

        # Verifica se os campos estão preenchidos
        if usuario == "" or senha == "":
            messagebox.showerror(
                "Ops! 💗",
                "Preencha o usuário e a senha."
            )
            return

        # Login provisório
        # Depois será conectado ao cadastro da Kauany.
        self.janela.destroy()

        TelaPrincipal()

    def sair(self):

        resposta = messagebox.askyesno(
            "Sair",
            "Deseja realmente sair do Girl's Planner?"
        )

        if resposta:
            self.janela.destroy()
import tkinter as tk
from tkinter import messagebox, simpledialog


class TelaAtividades:

    def __init__(self, janela, atividades):
        self.janela = tk.Toplevel(janela)
        self.janela.title("Minhas atividades")
        self.janela.geometry("750x550")
        self.janela.configure(bg="#FCE4EC")

        self.atividades = atividades

        self.criar_widgets()
        self.atualizar_lista()

    def criar_widgets(self):

        tk.Label(
            self.janela,
            text="🎀 MINHAS ATIVIDADES",
            font=("Arial", 20, "bold"),
            bg="#FCE4EC",
            fg="#8E4A70"
        ).pack(pady=20)

        self.lista = tk.Listbox(
            self.janela,
            width=90,
            height=16,
            font=("Arial", 10),
            bg="white",
            fg="#4A3540"
        )
        self.lista.pack(pady=10)

        botoes = tk.Frame(
            self.janela,
            bg="#FCE4EC"
        )
        botoes.pack(pady=15)

        tk.Button(
            botoes,
            text="✓ Concluir",
            width=13,
            command=self.concluir,
            bg="#E8A8C7",
            fg="#4A3540",
            relief="flat"
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            botoes,
            text="✎ Editar",
            width=13,
            command=self.editar,
            bg="#E8A8C7",
            fg="#4A3540",
            relief="flat"
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            botoes,
            text="✕ Excluir",
            width=13,
            command=self.excluir,
            bg="#C76B9B",
            fg="white",
            relief="flat"
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            botoes,
            text="↻ Atualizar",
            width=13,
            command=self.atualizar_lista,
            bg="#E8A8C7",
            fg="#4A3540",
            relief="flat"
        ).grid(row=0, column=3, padx=5)

    def atualizar_lista(self):

        self.lista.delete(0, tk.END)

        if not self.atividades:
            self.lista.insert(
                tk.END,
                "Nenhuma atividade cadastrada."
            )
            return

        for atividade in self.atividades:

            if atividade.concluida:
                status = "✓ Concluída"
            else:
                status = "○ Pendente"

            texto = (
                f"{atividade.titulo} | "
                f"{atividade.categoria} | "
                f"{atividade.data} | "
                f"{atividade.prioridade} | "
                f"{status}"
            )

            self.lista.insert(
                tk.END,
                texto
            )

    def selecionar(self):

        selecionado = self.lista.curselection()

        if not selecionado:
            messagebox.showwarning(
                "Atenção",
                "Selecione uma atividade."
            )
            return None

        if not self.atividades:
            return None

        indice = selecionado[0]

        if indice >= len(self.atividades):
            return None

        return indice

    def concluir(self):

        indice = self.selecionar()

        if indice is None:
            return

        atividade = self.atividades[indice]

        if atividade.concluida:
            messagebox.showinfo(
                "Aviso",
                "Essa atividade já está concluída."
            )
            return

        atividade.concluir()

        self.atualizar_lista()

        messagebox.showinfo(
            "Sucesso",
            "Atividade concluída!"
        )

    def editar(self):

        indice = self.selecionar()

        if indice is None:
            return

        atividade = self.atividades[indice]

        titulo = simpledialog.askstring(
            "Editar atividade",
            "Novo título:",
            initialvalue=atividade.titulo
        )

        if titulo is None:
            return

        titulo = titulo.strip()

        if not titulo:
            messagebox.showerror(
                "Erro",
                "O título não pode ficar vazio."
            )
            return

        categoria = simpledialog.askstring(
            "Editar atividade",
            "Nova categoria:",
            initialvalue=atividade.categoria
        )

        if categoria is None:
            return

        categoria = categoria.strip()

        if not categoria:
            messagebox.showerror(
                "Erro",
                "A categoria não pode ficar vazia."
            )
            return

        data = simpledialog.askstring(
            "Editar atividade",
            "Nova data:",
            initialvalue=atividade.data
        )

        if data is None:
            return

        data = data.strip()

        if not data:
            messagebox.showerror(
                "Erro",
                "A data não pode ficar vazia."
            )
            return

        prioridade = simpledialog.askstring(
            "Editar atividade",
            "Nova prioridade:",
            initialvalue=atividade.prioridade
        )

        if prioridade is None:
            return

        prioridade = prioridade.strip()

        if not prioridade:
            messagebox.showerror(
                "Erro",
                "A prioridade não pode ficar vazia."
            )
            return

        atividade.editar(
            titulo,
            categoria,
            data,
            prioridade
        )

        self.atualizar_lista()

        messagebox.showinfo(
            "Sucesso",
            "Atividade editada!"
        )

    def excluir(self):

        indice = self.selecionar()

        if indice is None:
            return

        atividade = self.atividades[indice]

        resposta = messagebox.askyesno(
            "Excluir atividade",
            f'Deseja excluir "{atividade.titulo}"?'
        )

        if resposta:

            self.atividades.pop(indice)

            self.atualizar_lista()

            messagebox.showinfo(
                "Sucesso",
                "Atividade excluída!"
            )
from tkinter import *
from controller.c_inserir import Inserir_categoria
from sqlalchemy.exc import IntegrityError, PendingRollbackError


class AppCategoria:
    def __init__(self, master: Tk):
        self.master = master
        self.master.geometry("400x100")
        self.master.title("Categorias")

        self.container_entry = Frame(self.master)
        self.container_botton = Frame(self.master)

        self.lbl_nome_ctg = Label(self.container_entry, text="Nome: ").pack(side=LEFT)
        self.txt_nome_ctg = Entry(self.container_entry)
        self.txt_nome_ctg.pack()
        self.container_entry.pack(pady=10)

        self.btn_criar_ctg = Button(self.container_botton, text="Criar Categoria")
        self.btn_criar_ctg.pack(side=LEFT)
        self.btn_criar_ctg.bind('<Button-1>', self.get)

        self.btn_cancelar = Button(self.container_botton, text="Cancelar", command=self.master.destroy)
        self.btn_cancelar.pack(side=LEFT, padx=5)
        self.container_botton.pack()

        self.statusbar = Label(self.master, text="Status bar", bd=1, relief=SUNKEN, anchor=W, pady=2)
        self.statusbar.pack(side=BOTTOM, fill=X)

    def get(self, *args):
        nome = self.txt_nome_ctg.get()

        if not nome:
            self.statusbar["text"] = "Não é possivel cadastras um valor em branco."
            return
        ctg = Inserir_categoria(nome)

        try:
            result = ctg.inserir()
            if result == 'ok':
                self.statusbar["text"] = 'Categoria cadastrada com SUCESSO.'
            elif result == 'duplicado':
                self.statusbar["text"] = 'Categoria já esta cadastrada.'

        except Exception as err:
            if 'UNIQUE' in str(err):
                ctg.session_flush()
                self.statusbar["text"] = 'Categoria já esta cadastrada.'
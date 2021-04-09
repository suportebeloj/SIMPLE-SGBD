from tkinter import *
from views.v_categoria import AppCategoria
from controller.start_db import Inteface


class AppMain:
    def __init__(self, master: Tk):
        # Initial settings
        self.master = master
        self.master.geometry('600x350')
        self.master.title('Controle de Gastos')
        # Initial settings

        # Frame Top
        self.frame_top = Frame(self.master)
        self.frame_top.pack(fill=X)

        self.frame_top_container = Frame(self.frame_top)
        self.frame_top_container.pack(padx=100, pady=5)

        self.btn_categoria = Button(self.frame_top_container, text="Categorias", width=8, height=8,
                                    command=self.screen_category)
        self.btn_categoria.pack(side=LEFT)

        self.btn_entrada = Button(self.frame_top_container, text="Entradas", width=8, height=8)
        self.btn_entrada.pack(side=LEFT)

        self.btn_saidas = Button(self.frame_top_container, text="Saidas", width=8, height=8)
        self.btn_saidas.pack(side=LEFT)

        self.btn_relatorio = Button(self.frame_top_container, text="Relatorio", width=8, height=8)
        self.btn_relatorio.pack(side=LEFT)

    def screen_category(self):
        top = Toplevel()
        AppCategoria(top)

    def screen_in(self):
        pass

    def screen_out(self):
        pass

    def screen_report(self):
        pass


def main():
    Inteface()
    root = Tk()
    AppMain(root)
    root.mainloop()

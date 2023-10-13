from tkinter import *
from tkinter import ttk

#root = TTKThemes(theme="arc")
root = Tk()

class Application:
    def __init__(self) -> None:
        self.root = root
        self.tela()
        self.frames()
        self.whidgets_frame1()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background='#f2f2f2')
        self.root.geometry("700x600")
        self.root.resizable(TRUE, TRUE)
        self.root.minsize(width=400, height=200)
        self.root.maxsize(width=800, height=600)

    def frames(self):
        # Place, Pack, Grid.
        self.frame_1 = Frame(self.root, bd=4, bg="#ffffff", highlightbackground="#737373", highlightthickness=1)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg="#ffffff", highlightbackground="#737373", highlightthickness=1)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def whidgets_frame1(self):
        self.bt_limpar = Button(self.frame_1, text="Limpar")
        self.bt_limpar.place(relx=0.2, rely=0.15, relwidth=0.08, relheight=0.1)

        self.bt_buscar = Button(self.frame_1, text="Buscar")
        self.bt_buscar.place(relx=0.3, rely=0.15, relwidth=0.08, relheight=0.1)

        self.bt_novo = Button(self.frame_1, text="Novo")
        self.bt_novo.place(relx=0.7, rely=0.15, relwidth=0.08, relheight=0.1)

        self.bt_alterar = Button(self.frame_1, text="Alterar")
        self.bt_alterar.place(relx=0.8, rely=0.15, relwidth=0.08, relheight=0.1)
        
        self.bt_apagar = Button(self.frame_1, text="Apagar")
        self.bt_apagar.place(relx=0.9, rely=0.15, relwidth=0.08, relheight=0.1)

        self.lb_codigo = Label(self.frame_1, text="Código")
        self.lb_codigo.place(relx=0.05, rely=0.05, relheight=0.1, relwidth=0.1) 

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relheight=0.1, relwidth=0.1)

Application()




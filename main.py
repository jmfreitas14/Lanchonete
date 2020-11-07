from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database

jan = Tk()
jan.title("Atividade Prática")
jan.geometry("500x600")
jan.configure(background="white")
jan.resizable(width=False, height=False)

logo = PhotoImage(file="images/cardapio.png")

TopFrame = Frame(jan, width=500, height=290, bg="white", relief="raise")
TopFrame.pack(side=TOP)

BotFrame = Frame(jan, width=500, height=310, bg="white", relief="raise")
BotFrame.pack(side=BOTTOM)

LogoLabel = Label(TopFrame, image=logo, bg="white")
LogoLabel.place(x=50, y=50)

NomeLabel = Label(BotFrame, text="Nome do Cliente: ", font=("Century Gothic", 20), bg="white", fg="black")
NomeLabel.place(x=5, y=20)

NomeEntry = ttk.Entry(BotFrame, width=30)
NomeEntry.place(x=260, y=33)

CodigoLabel = Label(BotFrame, text="Código: ", font=("Century Gothic", 20), bg="white", fg="black")
CodigoLabel.place(x=5, y=60)

CodigoEntry = ttk.Entry(BotFrame, width=30)
CodigoEntry.place(x=135, y=73)

QuantLabel = Label(BotFrame, text="Quantidade: ", font=("Century Gothic", 20), bg="white", fg="black")
QuantLabel.place(x=5, y=100)

QuantEntry = ttk.Entry(BotFrame, width=30)
QuantEntry.place(x=195, y=113)


def realizarpedido():
    nome = NomeEntry.get()
    cod = CodigoEntry.get()
    quant = QuantEntry.get()

    if (nome == "" or cod == "" or quant == ""):
        messagebox.showerror(title="Register Error", message="Preencha todos os campos.")

    else:
        database.cursor.execute("""
                            INSERT INTO pedido(nome, codigo, quant) VALUES (?, ?, ?)
                        """, (nome, cod, quant))

        database.conn.commit()

        messagebox.showinfo(title="Register Info", message="Pedido realizado.")


PedirButton = ttk.Button(BotFrame, text="Pedir", width=35, command=realizarpedido)
PedirButton.place(x=150, y=150)


def encerrar():
    CodigoLabel.place(x=99999)
    CodigoEntry.place(x=99999)
    QuantLabel.place(x=99999)
    QuantEntry.place(x=99999)
    PedirButton.place(x=99999)
    EncerrarButton.place(x=99999)

    def consultar():
        Nome = NomeEntry.get()

        if (Nome == ""):
            messagebox.showerror(title="Register Error", message="Preencha o nome do cliente.")

        else:
            database.cursor.execute("""
                            select ((select preco from cardapio where codigo = (select codigo from pedido where nome = ?)) * quant) as valor from pedido where nome = ?;
                            """, ((Nome), Nome))

            total = database.cursor.fetchone()
            valor = 'Valor Total:\n R$', total
            messagebox.showinfo(title="Preço Total", message=valor)

    ConsultarButton = ttk.Button(BotFrame, text="Consultar preço", width=45, command=consultar)
    ConsultarButton.place(x=120, y=100)


EncerrarButton = ttk.Button(BotFrame, text="Encerrar pedido", width=45, command=encerrar)
EncerrarButton.place(x=120, y=180)

jan.mainloop()

from tkinter import *



window = Tk()
window.geometry("800x500")
window.title("Gestor de Filmes&Séries")
window.configure(bg='black')


janela_inicial = window # guarda a designação da janela anterior

# nova janela de login

def apagar_janela_login(window):
    window.janela_login.destroy()

def login():
    janela_inicial.withdraw()  # fecha a janela do menu
    janela_login = Toplevel()
    janela_login.geometry("800x500")
    janela_login.title("Página de Login")
    janela_login.config(bg="black")
    janela_login.focus()
    janela_login.grab_set()

    #Login
    lbl_login = Label(janela_login,text="Entra na App", fg="white", bg="black",font=("Helvetica",25))
    lbl_login.place(x=250, y=50)

    #nome
    nome_utilizador = Entry(janela_login, width=31,font=("Helvetica",10))
    nome_utilizador.insert(0, "nome")
    nome_utilizador.place(x=250, y=110)

    #password
    pass_utilizador = Entry(janela_login, width=31, font=("Helvetica",10))
    pass_utilizador.insert(0,"password")
    pass_utilizador.place(x=250, y=150)

    #button registar
    btn_registar = Button(janela_login, text="Entrar", width=10, height=2, font=("Helvetica",10))
    btn_registar.place(x=310, y=190)

    #ir para o registar
    btn_conta = Button(janela_login, text="Ir para o registo", width=26, height=2, font=("Helvetica", 10), command=janela_inicial)
    btn_conta.place(x=250, y= 250)

    

#Registo
lbl_registo = Label(window, text="Registe na App", fg="white", bg="black",font=("Helvetica",25))
lbl_registo.place(x=250, y=50)

#nome
nome_utilizador = Entry(window, width=31,font=("Helvetica",10))
nome_utilizador.insert(0, "nome")
nome_utilizador.place(x=250, y=110)

#email
email_utilizador = Entry(window, width=31, font=("Helvetica",10))
email_utilizador.insert(0,"email")
email_utilizador.place(x=250, y=150)

#password
pass_utilizador = Entry(window, width=31, font=("Helvetica",10))
pass_utilizador.insert(0,"password")
pass_utilizador.place(x=250, y=190)

#button registar
btn_registar = Button(window, text="Registar", width=10, height=2, font=("Helvetica",10))
btn_registar.place(x=310, y=230)

#button no caso de tiver conta
btn_conta = Button(window, text="Já tenho conta!", width=26, height=2, font=("Helvetica", 10), command=login)
btn_conta.place(x=250, y= 310)

window.mainloop()
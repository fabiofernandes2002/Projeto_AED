from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import re



window = Tk()
# window.geometry("800x500")
# window.title("Gestor de Filmes&Séries")

#Get the current screen width and height
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 800                             # tamanho (pixeis) da window a criar
appHeight = 500
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))



janela_inicial = window # guarda a designação da janela anterior

#ficheiros: estrutura "username;email;password;tipo_utilizador"
ficheiro_utilizadores = "./ficheiros/utilizadores.txt"


# verificar os dados de login
def dados_registo(nome_registo, email_registo, pass_registo):
    nome = nome_registo.get()
    email = email_registo.get()
    password = pass_registo.get()

    if email and nome and password:
        email_valido = re.search(".*@*", email)
   #     if email.find("@") = -1:
    #    mensagem e erro e return
        if email_valido:
            f = open(ficheiro_utilizadores, "r", encoding="utf-8")
            lista_utilizadores = []
            for linha in f:
                texto = linha[0:len(linha)-1].split(";")
                lista_utilizadores.append({"nome": texto[0], "email": texto[1], "password": texto[2]})
            f.close()

            # verificar se já tem utilizadores com o mesmo nome ou email:
            dados_iguais = False
            for utilizador in lista_utilizadores:
                if utilizador["email"] == email or utilizador["nome"] == nome:
                    dados_iguais = True
                

                # se tiver algum problema, manda um aviso
            if dados_iguais:
                    messagebox.showerror(
                        title="Valores iguais", message="O email ou nome de utilizador já está a ser usado")
                # se não tiver, adiciona no ficheiro
            else:
                    f = open(ficheiro_utilizadores, "a", encoding="utf-8")
                    linha = nome + ";" + email + ";" + password + ";user\n"
                    f.write(linha)
                    f.close()
                
                    nome_registo.delete(0, "end")
                    email_registo.delete(0, "end")
                    pass_registo.delete(0, "end")
                  


def dados_login(nome_login, pass_login):

    nome = nome_login.get()
    password = pass_login.get()

    if nome and password:
            f = open(ficheiro_utilizadores, "r", encoding="utf-8")
            lista_utilizadores = []
            for linha in f:
                texto = linha[0:len(linha)-1].split(";")
                lista_utilizadores.append(
                    {"nome": texto[0], "password": texto[2], "type": texto[3]})
            f.close()
            # Verifica pelo username e depois a password
            # aparece a window principal se o username e password forem corretos
            tentativa_admin = {"nome": nome,
                               "password": password, "type": "admin"}
            tentativa_user = {"nome": nome,
                              "password": password, "type": "user"}

            if tentativa_admin in lista_utilizadores:
                nome_login.delete(0, "end")
                pass_login.delete(0, "end")
                #abrir_window_inicial("admin") #pagina do administrador
            elif tentativa_user in lista_utilizadores:
                nome_login.delete(0, "end")
                pass_login.delete(0, "end")
                pagina_user() #pagina do user normal
            else:
                messagebox.showerror(
                    title="Erro", message="Nome de utilizador ou password errados")
                

def pagina_user():
    global janela_login
    janela_login.withdraw()  # fecha a janela do menu
    janela_user = Toplevel()
    janela_user.geometry("800x500")
    janela_user.title("Gestor Filmes&Séries")
    janela_user.config(bg="black")
    janela_user.focus()
    janela_user.grab_set()

# def fechar_janelaLogin2(janela_login):
#     janela_login.destroy()
#     #janela_user.update()
#     #janela_user.deiconify()        
                

# nova janela de login

def fechar(janela_login):
    janela_login.destroy()
    janela_inicial.update()
    janela_inicial.deiconify()

    

def apagar_janela_login(window):
    window.janela_login.destroy() 

def login():
    janela_inicial.withdraw()  # fecha a janela do menu
    global janela_login
    janela_login = Toplevel()
    #janela_login.geometry("800x500")
    janela_login.title("Página de Login")
    janela_login.config(bg="black")
    janela_login.focus()
    janela_login.grab_set()

    #Get the current screen width and height
    screenWidth = janela_login.winfo_screenwidth()
    screenHeight = janela_login.winfo_screenheight()
    appWidth = 800                             # tamanho (pixeis) da window a criar
    appHeight = 500
    x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
    y = (screenHeight/2) - (appHeight/2)
    janela_login.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))

    #Login

    # img2 = ImageTk.PhotoImage(Image.open("imagens/login_capa.jpg"))

    # lbl_imagem_fundo2 = Label(window, image=img2, width=800, height=500)
    # lbl_imagem_fundo2.place(x=0, y = 0)

    # lbl_login = Label(janela_login,text="Entra na App", fg="white", bg="black",font=("Helvetica",25))
    # lbl_login.place(x=250, y=50)

    #nome
    nome_utilizador = Entry(janela_login, width=31,font=("Helvetica",10))
    nome_utilizador.insert(0, "nome")
    nome_utilizador.place(x=250, y=110)

    #password
    pass_utilizador = Entry(janela_login, width=31, font=("Helvetica",10), show="*")
    pass_utilizador.insert(0,"password")
    pass_utilizador.place(x=250, y=150)

    #button registar
    btn_registar = Button(janela_login, text="Entrar", width=10, height=2, font=("Helvetica",10), command= lambda: dados_login(nome_utilizador, pass_utilizador))
    btn_registar.place(x=310, y=190)

    #ir para o registar
    btn_conta = Button(janela_login, text="Ir para o registo", width=26, height=2, font=("Helvetica", 10), command= lambda: fechar(janela_login))
    btn_conta.place(x=250, y= 250)

    

#Registo

#Label de imagem do fundo
img = ImageTk.PhotoImage(Image.open("./imagens/capa_inicial.jpg"))

lbl_imagem_fundo = Label(window, image=img, width=800, height=500)
lbl_imagem_fundo.place(x=0, y = 0)

lbl_registo = Label(window, text="Registe na App", fg="black",font=("Helvetica",25))
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
pass_utilizador = Entry(window, width=31, font=("Helvetica",10), show="*")
pass_utilizador.insert(0,"password")
pass_utilizador.place(x=250, y=190)

#button registar
btn_registar = Button(window, text="Registar", width=10, height=2, font=("Helvetica",10), command= lambda: dados_registo(nome_utilizador, email_utilizador,pass_utilizador))
btn_registar.place(x=310, y=230)

#button no caso de tiver conta
btn_conta = Button(window, text="Já tenho conta!", width=26, height=2, font=("Helvetica", 10), command=login)
btn_conta.place(x=250, y= 310)

window.mainloop()
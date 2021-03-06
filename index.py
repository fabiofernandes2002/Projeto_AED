from dataclasses import InitVar
from email import message
from tkinter import *
from tkinter import filedialog   # filedialog boxe
from tkinter import ttk

from PIL import ImageTk, Image
#from tkVideoPlayer import TkinterVideo
# importa users.py, ficheiro onde estão definidas algumas funções
from users import *

ficheiro_categorias = "./ficheiros/categorias.txt"
ficheiro_utilizadores = "./ficheiros/utilizadores.txt"
ficheiro_utilizadores_removidos = "./ficheiros/removidos.txt"
filmes_series = "./ficheiros/filmes&series.txt"
fichero_fav = "./ficheiros/favoritos.txt"
ficheiro_descrição = "./ficheiros/descrição.txt"

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

#função que lê as categorias na listbox
def ler_categorias():
    f= open(ficheiro_categorias, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()
    for  linha in lista:
        lstbox.insert("end", linha)

def categorias_admin():
    f= open(ficheiro_categorias, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()
    for  linha in lista:
        listbox_categorias.insert("end", linha)
        
def gestao_categorias():
    f= open(ficheiro_categorias, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()
    for  linha in lista:
        listbox_gerir_categorias.insert("end", linha)

def adicionar_categoria(linha):
    linha = linha.get()
    if linha:
        linha += "\n"
        f = open(ficheiro_categorias, "a", encoding="utf-8")
        f.write(linha)
        f.close()
    
    

    janela_gestao_categorias.withdraw()
    janela_gestao_categorias.after(0, gerir_categorias)

def remover_categoria():
    # category = listbox_gerir_categorias.get(listbox_gerir_categorias.curselection()[0])
    # f = open(ficheiro_categorias, "r", encoding="utf-8")
    # lista_categorias = f.readlines()
    # f.close()
    # line = category + "\n"
    # nova_lista = ""
    # for item in lista_categorias:
    #     if item != line:
    #         nova_lista += item
    # f = open(ficheiro_categorias, "w", encoding="utf-8")
    # f.write(nova_lista)
    # f.close()
    category = listbox_gerir_categorias.get(listbox_gerir_categorias.curselection())
    f = open(ficheiro_categorias, "r", encoding="utf-8")
    lista_categorias = f.readlines()
    f.close()
    line = category
    nova_lista = ""
    for item in lista_categorias:
        if item != line:
            nova_lista += item
    f = open(ficheiro_categorias, "w", encoding="utf-8")
    f.write(nova_lista)
    f.close()
    # item_selecionado = listbox_gerir_categorias.curselection()
    # listbox_gerir_categorias.delete(item_selecionado[0])

    janela_gestao_categorias.withdraw()
    janela_gestao_categorias.after(0, gerir_categorias)

def gestao_utilizadores():
    f = open(ficheiro_utilizadores, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()
    utilizadores = []
    for item in lista:
        informacao = item.split(";")
        utilizadores.append(informacao[0])
    return utilizadores

def ler_filmes_series():
    tree_filmes_series.delete(*tree_filmes_series.get_children())  # remove o conteudo da treeview
    pos = lstbox.curselection()     # Item selecionado na Listbox
    categoria = lstbox.get(pos)     # categoria selecionada
    f = open("ficheiros\\filmes&series.txt", "r", encoding="utf-8")
    lista = f.readlines()
    f.close()

    global cont
    global filme_maximo
    global tipo
    cont=0
    maximo =0
    filme_maximo=""
    for  linha in lista:
        campos = linha.split(";")
        if categoria == campos[3]:
            tree_filmes_series.insert("","end", values = (campos[0], campos[1], campos[2]))
            cont+=1
            if int(campos[2]) > maximo:
                maximo = int(campos[2])
                tipo = campos[1]
                filme_maximo = campos[0]
    if cont ==0:
        messagebox.showwarning("receitas", "Não existem Filmes&Séries registados de momento")

#treeview leitura dos dados dos filmes
def ler_filmes_series2():
    tree_filmes_series2.delete(*tree_filmes_series2.get_children())  # remove o conteudo da treeview
    pos = listbox_categorias.curselection()     # Item selecionado na Listbox
    categoria = listbox_categorias.get(pos)     # categoria selecionada
    f = open("ficheiros\\filmes&series.txt", "r", encoding="utf-8")
    lista = f.readlines()
    f.close()

    global cont
    global filme_maximo
    global tipo
    cont=0
    maximo =0
    filme_maximo=""
    for  linha in lista:
        campos = linha.split(";")
        if categoria == campos[3]:
            tree_filmes_series2.insert("","end", values = (campos[0], campos[1], campos[2]))
            cont+=1
            if int(campos[2]) > maximo:
                maximo = int(campos[2])
                tipo = campos[1]
                filme_maximo = campos[0]
    if cont ==0:
        messagebox.showwarning("receitas", "Não existem Filmes&Séries registados de momento")

""" def ver_mais():
    global cont
    global receita_maximo
    # num_visualizacoes.set(str(cont))
    # tipologia.set(tipo)
    # titulo.set(receita_maximo)

"""
def listar_favoritos():
    f = open(fichero_fav, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()

    for  linha in lista:
        list_fav.insert("end", linha)


def obter_conteodo(): 
    try:
        # Obter dados da linha selecionada da TreeView
        row_id = tree_filmes_series.focus()  # obter o id da linha ativa / selecionada
        lista = tree_filmes_series.item(row_id)
        # dados obtidos da treeView sáo atribuidos às variáveis associadas às Entrys
        titulo.set(lista["values"][0])
        tipologia.set(lista["values"][1])
        num_visualizacoes.set(lista["values"][2])
    except:
        messagebox.showinfo(title="ERRO", message="Seleciona o elemento a ser monstrado" )

def obter_conteodo2():
    try:
        # Obter dados da linha selecionada da TreeView
        row_id = tree_filmes_series2.focus()  # obter o id da linha ativa / selecionada
        lista = tree_filmes_series2.item(row_id)
        # dados obtidos da treeView sáo atribuidos às variáveis associadas às Entrys
        titulo.set(lista["values"][0])
        tipologia.set(lista["values"][1])
        num_visualizacoes.set(lista["values"][2])
    except:
        messagebox.showinfo(title="ERRO", message="Seleciona o elemento a ser monstrado" )

def procurar_por_categoria(*args):
    search_item = search_categorias.get()

    f = open(ficheiro_categorias, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()

    lstbox.delete(0, END)

    for item in lista:
        if search_item.lower() in item.lower():
            lstbox.insert(END, item)

def procurar_por_titulo():
    search_t = search_titulo.get()

    f= open(ficheiro_categorias, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()

    tree_filmes_series.delete(*tree_filmes_series.get_children())


    for item in lista:
        if search_t.lower() in item.lower():
            tree_filmes_series.insert(END, item)



def iniciarSessao(userName, userPass):
    userAutenticado.set(validaConta(userName, userPass))
    admin = "admin" 
    pass_admin = "admin"
    if userName == admin and userPass == pass_admin:
       pagina_inicial_admin()
    else:
        pagina_user()
    
    
#fecho de janelas login
def fechar(janela_login):
    janela_login.destroy()
    janela_inicial.update()
    janela_inicial.deiconify()

    
def apagar_janela_login(window):
    window.janela_login.destroy()

# validar a validação dos utilizadores
# def validar_text(avaliação):
#     try:
#         int(avaliação.get())
#         messagebox.showinfo(title="obrigado", message="obrigado pela sua avaliação ")
#     except ValueError:
#         messagebox.showinfo(title="erro", message="tem que intuduzir um numero ")

# pagina do user normal
def pagina_user():
    global janela_login
    global janela_user
    janela_login.withdraw()  # fecha a janela do menu
    janela_user = Toplevel()
    #janela_user.geometry("800x800")
    janela_user.title("Gestor Filmes&Séries")
    janela_user.config(bg="black")
    janela_user.focus()
    janela_user.grab_set()

    #Get the current screen width and height
    screenWidth = janela_user.winfo_screenwidth()
    screenHeight = janela_user.winfo_screenheight()
    appWidth = 800                             # tamanho (pixeis) da window a criar
    appHeight = 800
    x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
    y = (screenHeight/2) - (appHeight/2)
    janela_user.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))

    #label categorias
    lbl_cat = Label(janela_user , text= "CATEGORIAS"  , fg= "white", bg="black",  font=('Helvetica', 25))
    lbl_cat.place(x=30,y=30)

    #listbox
    global lstbox
    lstbox = Listbox(janela_user, width=25, height=20 , bg="white", relief="sunken")
    lstbox.place(x=30, y= 80)

    ler_categorias()

    btn_ver = Button(janela_user,activebackground="blue", bd=0, anchor="w" , bg="white", text="Visualizar" , fg="black", font=('Helvetica', 10 ), command=ler_filmes_series) 
    btn_ver.place(x=300, y=200)

    btn_favoritos = Button(janela_user,activebackground="grey", bd=0, anchor="w" , bg="white", text="Meus favoritos" , fg="black", font=('Helvetica', 20), command=favoritos) 
    btn_favoritos.place(x=450,y=30)

    # panel_filmes_series = PanedWindow(janela_user, width=350, height=250 , bg="white", relief="sunken")
    # panel_filmes_series.place(x=450, y= 110)
    global tree_filmes_series
    tree_filmes_series = ttk.Treeview(janela_user, selectmode="browse", columns=("Filmes e Séries" ,"Tipologia","Visualizações") , show="headings")
    tree_filmes_series.place(x=450,y=110)

    tree_filmes_series.column("Filmes e Séries", anchor="w" , width=250)
    tree_filmes_series.column("Tipologia", anchor="c" , width=150)
    tree_filmes_series.column("Visualizações", anchor="c" , width=120)

    tree_filmes_series.heading("Filmes e Séries", text="Filmes e Séries")
    tree_filmes_series.heading("Tipologia", text="Tipologia")
    tree_filmes_series.heading("Visualizações", text="Visualizações")

    frame_filtro =  LabelFrame(janela_user, text="Filtros" ,width=380, height=150, relief="sunken",fg="white", bg="black")
    frame_filtro.place(x=30,y=500) 

    lbl_categorias_filtro = Label(frame_filtro, text="Categorias:", fg="white", bg="black",font=("Helvetica",10))
    lbl_categorias_filtro.place(x=25,y=25)

    global search_categorias
    search_categorias = StringVar()
    search_categorias.trace("w", procurar_por_categoria)
    entry_categorias_filtro = Entry(frame_filtro, width=25, textvariable=search_categorias)
    entry_categorias_filtro.place(x=100, y=25)
   
    lbl_titulo_filtro = Label(frame_filtro, text="Título:", fg="white", bg="black",font=("Helvetica",10))
    lbl_titulo_filtro.place(x=25,y=55)

    global search_titulo
    search_categorias.trace("w", procurar_por_titulo)
    search_titulo = StringVar()
    entry_titulo_filtro = Entry(frame_filtro, width=25, textvariable=search_titulo)
    entry_titulo_filtro.place(x=100, y=55)

    btn_categorias_filtro = Button(frame_filtro, text="Filtrar", fg="black", bg="white",font=("Helvetica",10), command=procurar_por_categoria)
    btn_categorias_filtro.place(x=280,y=25)
  
    btn_titulo_filtro = Button(frame_filtro, text="Filtrar", fg="black", bg="white",font=("Helvetica",10), command=procurar_por_titulo)
    btn_titulo_filtro.place(x=280,y=55)

    panel_vermais = PanedWindow(janela_user ,width=480, height=150,  bg="white", relief="sunken")
    panel_vermais.place(x=450, y= 500)

    btn_obter = Button(panel_vermais, text="Obter", fg="black", bg="white", font=("Helvetica", 10), command=obter_conteodo)
    btn_obter.place(x=25, y=35)

    btn_vermais = Button(panel_vermais, text="Ver +", fg="black", bg="white",font=("Helvetica",10), command=ver_conteodo)
    btn_vermais.place(x=25,y=75)

    lbl_titulo = Label(panel_vermais, text="Título:", fg="black" ,font=("Helvetica",10))
    lbl_titulo.place(x=100,y=35)

    global titulo
    titulo = StringVar()
    txt_titulo = Entry(panel_vermais, width=34, state="readonly", text="titulo", textvariable=titulo)
    txt_titulo.place(x=240,y=35)

    lbl_tipologia = Label(panel_vermais, text="Tipologia:", fg="black",font=("Helvetica",10))
    lbl_tipologia.place(x=100,y=65)
    
    global tipologia
    tipologia = StringVar()
    txt_tipologia = Entry(panel_vermais, width=34 , state="readonly", text="tipologia", textvariable=tipologia)
    txt_tipologia.place(x=240,y=65)
    
    lbl_vizualizaçoes = Label(panel_vermais, text="Nº de Vizualizaçoes:", fg="black",font=("Helvetica",10))
    lbl_vizualizaçoes.place(x=100,y=95)

    global num_visualizacoes
    num_visualizacoes = StringVar()
    txt_vizualizaçoes =Entry(panel_vermais, width=34 , state="readonly", text="Nº de vizualizaçoes", textvariable=num_visualizacoes)
    txt_vizualizaçoes.place(x=240,y=95)

    btn_sair = Button(janela_user, font=("Helvetica",10), bg="white", fg="black",relief="groove", text="Sair", width=10, command=sair2)
    btn_sair.place(x=980, y=600)

def sair():
    janela_logada_admin.destroy()
    janela_inicial.deiconify()

def sair2():
    janela_user.destroy()
    janela_inicial.deiconify()


#pagina de administrador
def pagina_inicial_admin():
    janela_inicial.withdraw()  # fecha a janela do menu
    global janela_logada_admin
    janela_logada_admin = Toplevel()
    #janela_logada_admin.geometry("800x800")
    janela_logada_admin.title("Página admin")
    janela_logada_admin.config(bg="black")
    janela_logada_admin.focus()
    janela_logada_admin.grab_set()

    #Get the current screen width and height
    screenWidth = janela_logada_admin.winfo_screenwidth()
    screenHeight = janela_logada_admin.winfo_screenheight()
    appWidth = 800                             # tamanho (pixeis) da window a criar
    appHeight = 800
    x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
    y = (screenHeight/2) - (appHeight/2)
    janela_logada_admin.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))

    lbl_cat = Label(janela_logada_admin , text= "CATEGORIAS"  , fg= "white", bg="black",  font=('Helvetica', 25))
    lbl_cat.place(x=30,y=30)

    global listbox_categorias
    listbox_categorias = Listbox(janela_logada_admin, width=25, height=20 , bg="white", relief="sunken")
    listbox_categorias.place(x=30, y= 80)

    categorias_admin()

    btn_ver = Button(janela_logada_admin,activebackground="blue", bd=0, anchor="w" , bg="white", text="Visualizar" , fg="black", font=('Helvetica', 10 ), command=lambda: ler_filmes_series2()) 
    btn_ver.place(x=300, y=200)

    btn_favoritos = Button(janela_logada_admin,activebackground="grey", bd=0, anchor="w" , bg="white", text="Meus favoritos" , fg="black", font=('Helvetica', 20)) 
    btn_favoritos.place(x=450,y=30)

    # panel_filmes_series = PanedWindow(janela_user, width=350, height=250 , bg="white", relief="sunken")
    # panel_filmes_series.place(x=450, y= 110)
    global tree_filmes_series2
    tree_filmes_series2 = ttk.Treeview(janela_logada_admin, selectmode="browse", columns=("Filmes e Séries" ,"Tipologia","Visualizações") , show="headings")
    tree_filmes_series2.place(x=450,y=110)

    tree_filmes_series2.column("Filmes e Séries", anchor="w" , width=250)
    tree_filmes_series2.column("Tipologia", anchor="c" , width=150)
    tree_filmes_series2.column("Visualizações", anchor="c" , width=120)

    tree_filmes_series2.heading("Filmes e Séries", text="Filmes e Séries")
    tree_filmes_series2.heading("Tipologia", text="Tipologia")
    tree_filmes_series2.heading("Visualizações", text="Visualizações")

    btn_gestao_cat = Button(janela_logada_admin, text="Gerir categorias", bg="white" ,width=20 ,height=2 , command=gerir_categorias)
    btn_gestao_cat.place(x=30,y=500) 

    btn_gestao_catalogo = Button(janela_logada_admin, text="Gerir catalogo", bg="white", width=20,height=2 , command= gerir_catalogo)
    btn_gestao_catalogo.place(x=30,y=555) 

    btn_gestao_utilizadores = Button(janela_logada_admin, text="Gerir utilizadores" ,bg="white", width=20,height=2 , command=gerir_utilizadores)
    btn_gestao_utilizadores.place(x=30,y=610) 


    # frame_filtro =  LabelFrame(janela_logada_admin, text="Filtros" ,width=380, height=150, relief="sunken",fg="white", bg="black")
    # frame_filtro.place(x=30,y=500) 

    # lbl_categorias_filtro = Label(frame_filtro, text="Categorias:", fg="white", bg="black",font=("Helvetica",10))
    # lbl_categorias_filtro.place(x=25,y=25)

    # entry_categorias_filtro = Entry(frame_filtro, width=25)
    # entry_categorias_filtro.place(x=100, y=25)
   
    # lbl_titulo_filtro = Label(frame_filtro, text="Título:", fg="white", bg="black",font=("Helvetica",10))
    # lbl_titulo_filtro.place(x=25,y=55)

    # entry_titulo_filtro = Entry(frame_filtro, width=25)
    # entry_titulo_filtro.place(x=100, y=55)

    # btn_categorias_filtro = Button(frame_filtro, text="Filtrar", fg="black", bg="white",font=("Helvetica",10))
    # btn_categorias_filtro.place(x=280,y=25)
  
    # btn_titulo_filtro = Button(frame_filtro, text="Filtrar", fg="black", bg="white",font=("Helvetica",10))
    # btn_titulo_filtro.place(x=280,y=55)

    panel_vermais = PanedWindow(janela_logada_admin ,width=480, height=150,  bg="white", relief="sunken")
    panel_vermais.place(x=450, y= 500)

    btn_obter = Button(panel_vermais, text="Obter", fg="black", bg="white", font=("Helvetica", 10), command=obter_conteodo2)
    btn_obter.place(x=25, y=35)

    btn_vermais = Button(panel_vermais, text="Ver +", fg="black", bg="white",font=("Helvetica",10), command=ver_conteodo)
    btn_vermais.place(x=25,y=75)

    lbl_titulo = Label(panel_vermais, text="Título:", fg="black" ,font=("Helvetica",10))
    lbl_titulo.place(x=100,y=35)

    global titulo
    titulo = StringVar()
    txt_titulo = Entry(panel_vermais, width=34, state="readonly", text="titulo", textvariable=titulo)
    txt_titulo.place(x=240,y=35)

    lbl_tipologia = Label(panel_vermais, text="Tipologia:", fg="black",font=("Helvetica",10))
    lbl_tipologia.place(x=100,y=65)
    
    global tipologia
    tipologia = StringVar()
    txt_tipologia = Entry(panel_vermais, width=34 , state="readonly", text="tipologia", textvariable=tipologia)
    txt_tipologia.place(x=240,y=65)
    
    lbl_vizualizaçoes = Label(panel_vermais, text="Nº de Vizualizaçoes:", fg="black",font=("Helvetica",10))
    lbl_vizualizaçoes.place(x=100,y=95)

    global num_visualizacoes
    num_visualizacoes = StringVar()
    txt_vizualizaçoes =Entry(panel_vermais, width=34 , state="readonly", text="Nº de vizualizaçoes", textvariable=num_visualizacoes)
    txt_vizualizaçoes.place(x=240,y=95)

    btn_sair = Button(janela_logada_admin, font=("Helvetica",10), bg="white", fg="black",relief="groove", text="Sair", width=10, command=sair)
    btn_sair.place(x=980, y=600)

#pagina depois de selecionar o conteodo da treeview
def ver_conteodo():
    janela_inicial.withdraw()  # fecha a janela do menu
    janela_logada_conteodo = Toplevel()
    janela_logada_conteodo.geometry("800x500")
    janela_logada_conteodo.title("Página inicial")
    janela_logada_conteodo.config(bg="black")
    janela_logada_conteodo.focus()
    janela_logada_conteodo.grab_set()

    obter_conteodo()

    lbl_titulo = Label( janela_logada_conteodo , text= "Título"  , fg= "white", bg="black",  font=('Helvetica', 15))
    lbl_titulo.place(x=30,y=30)

    titulo_ver_mais = StringVar
    titulo_ver_mais = titulo
    entry_titulo = Entry( janela_logada_conteodo , width=20 , 
    font=('Helvetica', 15) , textvariable=titulo_ver_mais , state="readonly")
    entry_titulo.place(x=115,y=30)
        

    lbl_tipologia = Label( janela_logada_conteodo , text= "Tipologia"  , fg= "white", bg="black" ,  font=('Helvetica', 15))
    lbl_tipologia.place(x=30,y=80)

    
    tipologia_ver_mais = tipologia
    entry_tipologia = Entry( janela_logada_conteodo , width=20 , 
     textvariable=tipologia_ver_mais ,font=('Helvetica', 15), state="readonly" )
    entry_tipologia.place(x=120,y=80)
        
        
    lbl_cat = Label( janela_logada_conteodo , text= "Categorias"  , fg= "white", bg="black",  font=('Helvetica', 15))
    lbl_cat.place(x=30,y=130)
    
    categoria = StringVar
    file = open(filmes_series , "r" , encoding="utf-8")
    linhas = file.readlines()
    for line in linhas:
        line.split(";")
        if line[0] == titulo_ver_mais.get():

            print("entra na condição")
            categoria = line[3]
    file.close()

    cat_entry = Entry( janela_logada_conteodo, width=20, relief="sunken"
     , textvariable=categoria ,  font=('Helvetica', 15) , state="readonly")
    cat_entry.place(x=145,y=130)

    img_canvas = Canvas( janela_logada_conteodo, width=300, height=210 , bg="white", relief="sunken")    
    img_canvas.place(x=400,y=30)

    lbl_descrição = Label( janela_logada_conteodo, text="Descrição", fg="white", bg="black", font=('Helvetica', 15))
    lbl_descrição.place(x=30, y=250)

    lbl_descrição = Label( janela_logada_conteodo, text="De 0 a 10 quanto avalias este Filme&Série", fg="white", bg="black", font=('Helvetica', 15))
    lbl_descrição.place(x=400, y=250)

    
    #descriçao_txt = StringVar                                            abrir ficheiro da descrição 
    #file_descriçao = open(ficheiro_descrição , "r" , encoding="utf-8")   tentar procurar o titulo selecionado da treeview 
    #desc_linha = file_descriçao.readlines()                              e igualar a Text ao 2 posição da lina
    #for linha in desc_linha:
    #         desc_linha.split(";")
    #    if linha[0] == titulo_ver_mais:
    #        descriçao_txt = linha[1] 

    text_descrição = Text( janela_logada_conteodo, width=25, height=5 , font=('Helvetica', 15), state="disable") #, textvariable=descriçao_txt)
    text_descrição.place(x=30, y=300)

    #lbl_avaliacao = Label(janela_logada_conteodo, text="De 0 a 10 quanto avaliavas este Filme&Série", font=('Helvetica', 10))
    #lbl_avaliacao.place(500, 50)

    avaliação = Spinbox( janela_logada_conteodo , width=5,from_=1, to=10 )
    avaliação.place(x=500, y=300)

    # valor = InitVar()
    # valor.set(1)
    # spin = Spinbox(janela_logada_conteodo, width=5, from_=1, to=10)
    # spin.place(x=500, y=300)


    btn_enviar = Button( janela_logada_conteodo, text="Enviar")# , command="validar_text(avaliação)")
    btn_enviar.place(x=550, y=300)

    btn_adicionar_fav = Button( janela_logada_conteodo, text="Adicionar aos favoritos" , command= adicionar_favoritos(titulo_ver_mais))
    btn_adicionar_fav.place(x=500, y=350)

def adicionar_favoritos(titulo_ver_mais):
    #nome_user = userName.get()
    nome_fav = titulo_ver_mais.get()
    file_fav = open(fichero_fav, "a", encoding="utf-8")
    linha = nome_fav + "\n"
    file_fav.write(linha)
    file_fav.close
    #print("esta a entrar na função")


#gerir utilizadores
def gerir_utilizadores():
    janela_inicial.withdraw()  # fecha a janela do menu
    global janela_gerir_utilizadores
    janela_gerir_utilizadores = Toplevel()
    #janela_gerir_utilizadores.geometry("800x500")
    janela_gerir_utilizadores.title("gerir utilizadores")
    janela_gerir_utilizadores.config(bg="black")
    janela_gerir_utilizadores.focus()
    janela_gerir_utilizadores.grab_set()

    #Get the current screen width and height
    screenWidth = janela_gerir_utilizadores.winfo_screenwidth()
    screenHeight = janela_gerir_utilizadores.winfo_screenheight()
    appWidth = 800                             # tamanho (pixeis) da window a criar
    appHeight = 800
    x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
    y = (screenHeight/2) - (appHeight/2)
    janela_gerir_utilizadores.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))

    lbl_utilizadores = Label(janela_gerir_utilizadores, text= "Utilizadores"  , fg= "white", bg="black",  font=('Helvetica', 25))
    lbl_utilizadores.place(x=30,y=30)

    global listbox_utilizadores
    utilizadores = gestao_utilizadores()
    listbox_utilizadores = Listbox(janela_gerir_utilizadores, width=25, height=20 , bg="white", relief="sunken")
    for user in utilizadores:
        if user != "admin":
            listbox_utilizadores.insert(END, user)
    listbox_utilizadores.place(x=30, y= 80)

    
    btn_detalhes =Button(janela_gerir_utilizadores, text="Mais detalhes", bg="white" , height=4 , width=15, command=mais_detalhes_utilizadores)
    btn_detalhes.place(x=250,y=150)


    # frame_utilzadores =  LabelFrame(janela_gerir_utilizadores, text="utilzadores" ,width=350, height=250, relief="sunken",fg="white", bg="black")
    # frame_utilzadores.place(x=400,y=90) 

    # lbl_username = Label(frame_utilzadores, text="nome:", fg="black" ,font=("Helvetica",10))
    # lbl_username.place(x=20,y=35)

    # global utilizador
    # utilizador = StringVar()
    # txt_username = Entry(frame_utilzadores, width=25, state="readonly", text="titulo", textvariable=utilizador)
    # txt_username.place(x=80,y=35)

    # lbl_email = Label(frame_utilzadores, text="email:", fg="black",font=("Helvetica",10))
    # lbl_email.place(x=20,y=65)
    
    # txt_email = Entry(frame_utilzadores, width=25 , state="readonly", text="email")
    # txt_email.place(x=80,y=65)
    
    # lbl_tipo = Label(frame_utilzadores, text="tipo de utilzador:", fg="black",font=("Helvetica",10))
    # lbl_tipo.place(x=20,y=95)

    # txt_tipo =Entry(frame_utilzadores, width=25 , state="readonly", text="Nº de vizualizaçoes")
    # txt_tipo.place(x=140,y=95)

    # btn_remover = Button(frame_utilzadores, text="remover utilizador", fg="black" , bg="white" )
    # btn_remover.place(x=100 , y=130 )

#gerir categorias
def gerir_categorias():
    global janela_gestao_categorias
    janela_inicial.withdraw()  # fecha a janela do menu
    janela_gestao_categorias= Toplevel()
    #janela_gestao_categorias.geometry("800x500")
    janela_gestao_categorias.title("gerir categorias")
    janela_gestao_categorias.config(bg="black")
    janela_gestao_categorias.focus()
    janela_gestao_categorias.grab_set()

    #Get the current screen width and height
    screenWidth = janela_gestao_categorias.winfo_screenwidth()
    screenHeight = janela_gestao_categorias.winfo_screenheight()
    appWidth = 800                             # tamanho (pixeis) da window a criar
    appHeight = 800
    x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
    y = (screenHeight/2) - (appHeight/2)
    janela_gestao_categorias.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))

    lbl_cat = Label(janela_gestao_categorias , text= "CATEGORIAS"  , fg= "white", bg="black",  font=('Helvetica', 25))
    lbl_cat.place(x=30,y=30)

    global listbox_gerir_categorias
    listbox_gerir_categorias = Listbox(janela_gestao_categorias, width=25, height=20 , bg="white", relief="sunken")
    listbox_gerir_categorias.place(x=30, y= 80)

    gestao_categorias()

    # btn_adicionar = Button(janela_gestao_categorias, text="adiconar" , width=20 , height=2)
    # btn_adicionar.place(x=200, y=130)

    btn_remover = Button(janela_gestao_categorias , text="Remover" , width=20 , height=2, command=remover_categoria)
    btn_remover.place(x=200, y=180)

    frame_categorias =  LabelFrame(janela_gestao_categorias, text="Categoria" ,width=350, height=250, relief="sunken",fg="white", bg="black")
    frame_categorias.place(x=400,y=90)

    lbl_cat = Label(frame_categorias, text="Categoria:", )
    lbl_cat.place(x=50,y=50)

    txt_cat = Entry(frame_categorias, width=25, text="Nº de vizualizaçoes")
    txt_cat.place(x=150, y=50)

    btn_adicionar_cat = Button(frame_categorias, text="Adiconar" , width=15 , height=2, command=lambda:adicionar_categoria(txt_cat))
    btn_adicionar_cat.place(x=150, y=100)

def gerir_catalogo():
    janela_inicial.withdraw()  # fecha a janela do menu
    janela_gerir_catalogo = Toplevel()
    #janela_logada_fav.geometry("800x500")
    janela_gerir_catalogo.title("gerir catalogo")
    janela_gerir_catalogo.config(bg="black")
    janela_gerir_catalogo.focus()
    janela_gerir_catalogo.grab_set()

    #Get the current screen width and height
    screenWidth = janela_gerir_catalogo.winfo_screenwidth()
    screenHeight = janela_gerir_catalogo.winfo_screenheight()
    appWidth = 800                             # tamanho (pixeis) da window a criar
    appHeight = 500
    x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
    y = (screenHeight/2) - (appHeight/2)
    janela_gerir_catalogo.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))

    lbl_titulo = Label(janela_gerir_catalogo , text= "Título:"  , fg= "white", bg="black",  font=('Helvetica', 15))
    lbl_titulo.place(x=30,y=30)

    global entry_titulo 
    entry_titulo = Entry(janela_gerir_catalogo , width=20 , font=('Helvetica', 15) )
    entry_titulo.place(x=115,y=30)
       
    
    lbl_tipologia = Label(janela_gerir_catalogo , text= "Tipologia:"  , fg= "white", bg="black",  font=('Helvetica', 15))
    lbl_tipologia.place(x=30,y=80)

    entry_tipologia = Entry(janela_gerir_catalogo , width=20 , font=('Helvetica', 15) )
    entry_tipologia.place(x=120,y=80)
       
       
    lbl_cat = Label(janela_gerir_catalogo , text= "Categoria:"  , fg= "white", bg="black",  font=('Helvetica', 15))
    lbl_cat.place(x=30,y=130)

    file = open(ficheiro_categorias, "r" , encoding="utf-8")
    linhas = file.readlines()
    lista_cat = []
    file.close()
    for linha in linhas:
        lista_cat.append(linha)

    #lista_cat = ['acao', 'romance' , 'comedia' ]
    txt_categorias = Entry(janela_gerir_catalogo, width=20 , bg="white", relief="sunken" ,  font=('Helvetica', 15))
    txt_categorias.place(x=170,y=130)

    img_canvas = Canvas(janela_gerir_catalogo, width=300, height=210 , bg="white", relief="sunken")    
    img_canvas.pack(expand= YES, fill= BOTH)
    img_canvas.place(x=420,y=30)

    btn_img = Button(janela_gerir_catalogo, text="Escolher uma imagem" , bg="white" , fg="black" , command=lambda: open_folder_img(janela_gerir_catalogo, img_canvas))
    btn_img.place(x=490,y=260)

    lbl_descrição = Label(janela_gerir_catalogo, text="Descrição:", fg="white", bg="black", font=('Helvetica', 15))
    lbl_descrição.place(x=30, y=250)
    global text_descrição 
    text_descrição = Text(janela_gerir_catalogo, width=25, height=5)
    text_descrição.place(x=30, y=300)

    btn_adicionar = Button(janela_gerir_catalogo, text="Adicionar",
     command=lambda: adicionar_filme_serie(txt_categorias , entry_titulo , entry_tipologia ,text_descrição ))
    btn_adicionar.place(x=400,y=320)

def adicionar_filme_serie(txt_categorias, entry_tipologia, entry_titulo  ,text_descrição ):
    descrição_serie_filme(text_descrição,entry_titulo)
    file = open(filmes_series , "a" , encoding="utf-8" )
    file_cat = open(ficheiro_categorias, "r" , encoding="utf-8")
    lista_cat = []
    linhas_cat = file_cat.readlines()
    for categoria in linhas_cat:
        lista_cat.append(categoria)
    
    titulo = entry_titulo.get()
    categorias = txt_categorias.get()
    tipologia = entry_tipologia.get()


    linha = tipologia + ";" + titulo + ";" + "0" + ";" + categorias
    try:

        file.write(linha) == True
        messagebox.showinfo(title="SUCESSO", message="Contéudo adicionado")
    except ValueError:
        pass


    file.close()
    file_cat.close()

    #if file.write(linha) :
    #    messagebox.showinfo(title="adicionado" , message="filme/serie adicionada com sucesso")


#guardar num ficheiro a parte o titulo juntamente com a descrição
def descrição_serie_filme(text_descrição,entry_titulo):
    file = open(ficheiro_descrição , "a" , encoding="utf-8")
    descrição_elemento =text_descrição.get("1.0" , "end-1c")
    titulo = entry_titulo.get()
    linha = titulo + ";" + descrição_elemento

    file.write(linha)
    file.close()

    #if file.write(linha) :
    #    messagebox.showinfo(title="adicionado" , message="descrição adicionada com sucesso")

#abrir uma imagem e adicionar ao canvas 
def open_folder_img(janela_gerir_catalogo,img_canvas):

    janela_gerir_catalogo.folder = filedialog.askopenfilename(initialdir=("/"), title="imagens", filetypes=(("jpg files", "*.jpg"), ("png files", "*.png")))
    img_filme = ImageTk.PhotoImage(Image.open(janela_gerir_catalogo.folder))
    img_canvas.create_image(1,1, image = img_filme , anchor="nw" )
    img_label = Label(image = img_filme).pack()
    
   
#favoritos
def favoritos():
    #adicionar_favoritos(titulo_ver_mais)
    global list_fav
    janela_inicial.withdraw()  # fecha a janela do menu
    janela_logada_fav = Toplevel()
    #janela_logada_fav.geometry("800x500")
    janela_logada_fav.title("favoritos")
    janela_logada_fav.config(bg="black")
    janela_logada_fav.focus()
    janela_logada_fav.grab_set()

    #Get the current screen width and height
    screenWidth = janela_logada_fav.winfo_screenwidth()
    screenHeight = janela_logada_fav.winfo_screenheight()
    appWidth = 800                             # tamanho (pixeis) da window a criar
    appHeight = 500
    x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
    y = (screenHeight/2) - (appHeight/2)
    janela_logada_fav.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))

    lbl_fav = Label(janela_logada_fav , text= "Favoritos"  , fg= "white", bg="black",  font=('Helvetica', 25))
    lbl_fav.place(x=30,y=30)

    #file_fav = open(fichero_fav, "r" , encoding="utf-8")  
    #linhas = file_fav.readlines()
    #lista_fav = []
    # for line in linhas:
    #       line.spli(";")
    #     if     

    list_fav = Listbox(janela_logada_fav, width=15, height=12 , bg="white", relief="sunken",  font=('Helvetica', 15))
    list_fav.place(x=30, y= 80)
    listar_favoritos()

    btn_remover = Button(janela_logada_fav , text="Remover", width=10, height=2, font=("Helvetica",10), command=remover_favoritos)
    btn_remover.place(x=220 , y=180)

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

    # img2 = ImageTk.PhotoImage(Image.open("./imagens/login_capa.jpg"))

    # lbl_imagem_fundo2 = Label(window, image=img2, width=800, height=500)
    # lbl_imagem_fundo2.place(x=0, y = 0)

    lbl_login = Label(janela_login,text="Entra na App", fg="white", bg="black",font=("Helvetica",25))
    lbl_login.place(x=250, y=50)

    #nome
    global userName
    userName = StringVar()
    nome_utilizador = Entry(janela_login, width=31,font=("Helvetica",10), textvariable= userName)
    nome_utilizador.insert(0, "nome")
    nome_utilizador.place(x=250, y=110)

    #password
    global userPass
    userPass = StringVar()
    pass_utilizador = Entry(janela_login, width=31, font=("Helvetica",10), show="*", textvariable= userPass)
    pass_utilizador.insert(0,"password")
    pass_utilizador.place(x=250, y=150)

    #button entrar
    btn_registar = Button(janela_login, text="Entrar", width=10, height=2, font=("Helvetica",10),
                    command = lambda: iniciarSessao(userName.get(), userPass.get()))
    btn_registar.place(x=310, y=190)

    #ir para o registar
    btn_conta = Button(janela_login, text="Ir para o registo", width=26, height=2, font=("Helvetica", 10), command= lambda: fechar(janela_login))
    btn_conta.place(x=250, y= 250)


#---- Label com o user autenticado num dado momento
global userAutenticado
userAutenticado = StringVar()
lblUserAutenticado = Label(window, textvariable= userAutenticado)
lblUserAutenticado.place(x=25, y=10)

#Registo

#Label de imagem do fundo
img = ImageTk.PhotoImage(Image.open("./imagens/capa_inicial.jpg"))

lbl_imagem_fundo = Label(window, image=img, width=800, height=500)
lbl_imagem_fundo.place(x=0, y = 0)

lbl_registo = Label(window, text="Registe na App", fg="black",font=("Helvetica",25))
lbl_registo.place(x=250, y=50)

#nome
userName = StringVar()
nome_utilizador = Entry(window, width=31,font=("Helvetica",10), textvariable= userName)
nome_utilizador.insert(0, "nome")
nome_utilizador.place(x=250, y=110)

#email
userEmail = StringVar()
email_utilizador = Entry(window, width=31, font=("Helvetica",10), textvariable=userEmail)
email_utilizador.insert(0,"email")
email_utilizador.place(x=250, y=150)

#password
userPass = StringVar()
pass_utilizador = Entry(window, width=31, font=("Helvetica",10), show="*", textvariable= userPass)
pass_utilizador.insert(0,"password")
pass_utilizador.place(x=250, y=190)

#button registar
btn_registar = Button(window, text="Registar", width=10, height=2, font=("Helvetica",10),
                command= lambda:[criaConta(userName.get(), userEmail.get() ,userPass.get())])
btn_registar.place(x=310, y=230)

#button no caso de tiver conta
btn_conta = Button(window, text="Já tenho conta!", width=26, height=2, font=("Helvetica", 10), command=login)
btn_conta.place(x=250, y= 310)

def mais_detalhes_utilizadores():
    id_user = listbox_utilizadores.curselection()[0] + 1
    f = open(ficheiro_utilizadores, "r", encoding="utf-8")
    linha_users = f.readlines()[id_user]
    f.close()

    linha_utilizador = linha_users[0:len(linha_users)-1].split(";")

    utilizador = {}
    for i in range(len(linha_utilizador)):
        if i == 0:
            utilizador["userName"] = linha_utilizador[0]
        if i == 1:
            utilizador["userEmail"] = linha_utilizador[1]
        if i == 3:
            utilizador["tipo_user"] = linha_utilizador[3]

    frame_utilizador = LabelFrame(janela_gerir_utilizadores, text="Utilizador",width=400, height=340, font=("Helvetica",10), bg="white")
    frame_utilizador.place(x=500, y=100)

    label_utilizador = Label(frame_utilizador, text="Nome de utilizador",font=("Helvetica",10), bg="white", fg="black")
    label_utilizador.place(x=20, y=30)

    nome_utilizador = Label(frame_utilizador, text=utilizador.get("userName"), font=("Helvetica",10), bg="white", fg="black")
    nome_utilizador.place(x=200, y=30)

    label_email = Label(frame_utilizador, text="Email",font=("Helvetica",10), bg="white", fg="black")
    label_email.place(x=20, y=80)
    
    email = Label(frame_utilizador, text=utilizador.get("userEmail"), font=("Helvetica",10), bg="white", fg="black")
    email.place(x=200, y=80)
    
    label_tipo_user = Label(frame_utilizador, text="Tipo de utilizador",font=("Helvetica",10), bg="white", fg="black")
    label_tipo_user.place(x=20, y=130)
    
    tipo_user = Label(frame_utilizador, text=utilizador.get("tipo_user"), font=("Helvetica",10), bg="white", fg="black")
    tipo_user.place(x=200, y=130)

    btn_remover_user = Button(frame_utilizador, text="Remover utilizador",width=15, height=2, bg="black", relief="groove",fg="white", font=("Helvetica",10),command=remover_utilizador)
    btn_remover_user.place(x=150, y=230)

def remover_utilizador():
    id_user = listbox_utilizadores.curselection()[0] + 1
    f = open(ficheiro_utilizadores, "r", encoding="utf-8")
    lista_utilizadores = f.readlines()
    f.close()

    utilizador = lista_utilizadores[id_user]
    nova_lista = ""

    for user in lista_utilizadores:
        if user != utilizador:
            nova_lista += user

    f = open(ficheiro_utilizadores, "w", encoding="utf-8")
    f.write(nova_lista)
    f.close()

    # adicionar a lista de emails removidos
    email = utilizador.split(";")[1] + "\n"
    f = open(ficheiro_utilizadores_removidos, "w")
    f.write(email)
    f.close()

    janela_gerir_utilizadores.withdraw()
    janela_gerir_utilizadores.after(100, gerir_utilizadores)

def remover_favoritos():
    id_user = list_fav.curselection()[0] + 1
    f = open(fichero_fav, "r", encoding="utf-8")
    lista_favoritos = f.readlines()
    f.close()

    utilizador = lista_favoritos[id_user]
    nova_lista = ""

    for user in lista_favoritos:
        if user != utilizador:
            nova_lista += user

    f = open(fichero_fav, "w", encoding="utf-8")
    f.write(nova_lista)
    f.close()
    


window.mainloop()
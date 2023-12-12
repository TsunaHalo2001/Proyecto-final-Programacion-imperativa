import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import numpy as np
import hashlib

#Tema mamalon Sun Valley
import sv_ttk

#Variables globales
#Variable del estado del programa
#0 = Menu principal
#1 = Login y registro
#2 = Bienvenido
pstate = 0

#Variables de ruta de archivos
#Variable de ruta de la base de datos de usuarios y contraseñas
uplist = "txt/registro_inicio.txt"
cplist = "txt/password.txt"

#Variables de fuente y color
ftitle = "MS Sans Serif"
fctitle = "#505050"
bgcolor = "#DCDCDC"

#Variables de texto
mrtitle = "My restaurant"
mydescription = "\nYa sea que busques un almuerzo casual con\namigos, una cena romántica o un evento\nespecial, nuestro restaurante\npromete una experiencia que cautivará tu\npaladar y creará recuerdos duraderos.\n"
usuario = "."

#Variables de tamaño
logoar = 567 / 487
bwregist = 37 / 1366

#Descifrar lista de usuarios y contraseñas
txtloginlist = open(uplist, "r")
loginlist = txtloginlist.read()
txtloginlist.close()
loginlist = loginlist.replace("']", "").replace("['", "")
lloginlist = loginlist.split("', '")

#Descifrar lista de contraseñas cifradas
txtcpassword = open(cplist, "r")
cpassword = txtcpassword.read()
txtcpassword.close()
cpassword = cpassword.replace("']", "").replace("['", "")
lcpassword = cpassword.split("', '")

#Base de datos de correos
emaildb = ["@correounivalle.edu.co","@gmail.com", "@hotmail.com", "@outlook.com", "@yahoo.com", "@icloud.com", "@live.com", "@msn.com", "@aol.com", "@yandex.com", "@protonmail.com", "@zoho.com", "@gmx.com", "@mail.com", "@yopmail.com", "@tutanota.com", "@mail.ru", "@gmx.us", "@gmx.de", "@gmx.fr", "@gmx.at", "@gmx.ch", "@gmx.net", "@gmx.co.uk", "@gmx.com.mx", "@gmx.es", "@gmx.eu", "@gmx.it", "@gmx.com.br", "@gmx.com.ar", "@gmx.com.co", "@gmx.com.ve", "@gmx.com.pe", "@gmx.com.ec", "@gmx.com.bo", "@gmx.com.py", "@gmx.com.uy", "@gmx.com.pa", "@gmx.com.do", "@gmx.com.gt", "@gmx.com.sv", "@gmx.com.hn", "@gmx.com.ni", "@gmx.com.cr", "@gmx.com.cu", "@gmx.com.pr", "@gmx.com.jm", "@gmx.com.bb", "@gmx.com.ag", "@gmx.com.dm", "@gmx.com.vc", "@gmx.com.lc", "@gmx.com.gy", "@gmx.com.sr", "@gmx.com.bo", "@gmx.com.py", "@gmx.com.uy", "@gmx.com.ar", "@gmx.com.co", "@gmx.com.ve", "@gmx.com.pe", "@gmx.com.ec", "@gmx.com.bo", "@gmx.com.py", "@gmx.com.uy", "@gmx.com.pa", "@gmx.com.do", "@gmx.com.gt", "@gmx.com.sv", "@gmx.com.hn", "@gmx.com.ni", "@gmx.com.cr", "@gmx.com.cu", "@gmx.com.pr", "@gmx.com.jm", "@gmx.com.bb", "@gmx.com.ag", "@gmx.com.dm", "@gmx.com.vc", "@gmx.com.lc", "@gmx.com.gy", "@gmx.com.sr", "@gmx.com.bo", "@gmx.com.py", "@gmx.com.uy"]

#Funciones
#Funcion para volver a la pantalla anterior
def back():
    #Variables globales
    #Variable del estado del programa
    global main, fmainmenu, finicio, flogin, fregist, pstate

    #Entry de login
    global eluser, elpassword

    #Entry de registro
    global eruser, erpassword, ercpassword

    #Condicional para volver a la pantalla principal
    if pstate == 1:
        #Variable del estado del programa en el valor de la pantalla principal
        pstate = 0
    
        #Se reinician los entrys
        eluser.delete(0, END)
        elpassword.delete(0, END)
        eruser.delete(0, END)
        erpassword.delete(0, END)
        ercpassword.delete(0, END)

        #Se remueve la pantalla de funcionamiento
        main.grid_remove()

        #Se agrega la pantalla principal
        fmainmenu.grid(row = 0, column = 0)

    elif pstate == 2:
        pstate = 1

#Funcion para la pantalla de registro
def regist():
    #Variables globales
    global main, fmainmenu, finicio, flogin, fregist, fwelcome, pstate

    #Variable del estado del programa en el valor de 1era pantalla
    pstate = 1

    #Se remueve la pantalla principal
    fmainmenu.grid_remove()

    #Se agrega la pantalla de funcionamiento
    main.grid(row = 0, column = 0)

    #Se agregan las pestañas
    main.add(finicio, text = "Inicio")
    main.add(fregist, text = "Registrarse")
    main.add(flogin, text = "Iniciar sesion")
    main.add(fwelcome, text = "Menu principal")

    #Se selecciona la pestaña de registro
    main.select(fregist)

    #Se asigna la funcion de volver a la pantalla anterior
    main.bind("<<NotebookTabChanged>>", lambda event: back())

    #Se remueve la pestaña de login
    main.forget(flogin)

    #Se remueve la pestaña de menu principal
    main.forget(fwelcome)

#Funcion para la pantalla de login
def login():
    #Variables globales
    global main, fmainmenu, finicio, flogin ,fregist, pstate

    #Variable del estado del programa en el valor de 1era pantalla
    pstate = 1

    #Se remueve la pantalla principal
    fmainmenu.grid_remove()

    #Se agrega la pantalla de funcionamiento
    main.grid(row = 0, column = 0)

    #Se agregan las pestañas
    main.add(finicio, text = "Inicio")
    main.add(flogin, text = "Iniciar sesion")
    main.add(fregist, text = "Registrarse")
    main.add(fwelcome, text = "Menu principal")

    #Se selecciona la pestaña de login
    main.select(flogin)

    #Se asigna la funcion de volver a la pantalla anterior
    main.bind("<<NotebookTabChanged>>", lambda event: back())

    #Se remueve la pestaña de registro
    main.forget(fregist)

    #Se remueve la pestaña de menu principal
    main.forget(fwelcome)

#Funcion para la pantalla de menu principal
def welcome():
    #Variables globales
    global main, fwelcome, pstate, lwelcomemessage, usuario

    #Se agrega la pestaña del menu principal
    main.add(fwelcome, text = "Menu principal")

    #Se selecciona la pestaña del menu principal
    main.select(fwelcome)

    #Se asigna la funcion de volver a la pantalla anterior
    main.bind("<<NotebookTabChanged>>", lambda event: back())

    #Se remueve la pestaña de login
    main.forget(flogin)

    lwelcomemessage.config(text = "Bienvenido " + usuario)

    #Variable del estado del programa en el valor de 2da pantalla
    pstate = 2

#Funcion para la pantalla de gestion de platos
def gestionplatos():
    pass

#Funcion para la pantalla de gestion de mesas
def gestionmesas():
    pass

#Funcion para la pantalla de gestion de pedidos
def gestionpedidos():
    pass

#Funcion para iniciar sesion
def slogin():
    #Variables globales
    global main, finicio, flogin, pstate, lloginlist, eluser, elpassword, usuario

    #Lista temporal de login
    tloginlist = ""

    #Condicional para verificar si los campos estan vacios
    if elpassword.get() == "" or eluser.get() == "":
        messagebox.showerror("Error", "No se pueden dejar campos vacios")

    else:
        #Condicional para verificar si el usuario y la contraseña son correctos
        try:
            #Se obtiene el usuario que inicio sesion
            usuario = usuario.replace(usuario, eluser.get())

            #Se concatenan el usuario y la contraseña
            tloginlist += eluser.get().lower()
            tloginlist += ", " + elpassword.get()

            print(tloginlist)

            #Se verifica si el usuario y la contraseña estan en la base de datos
            lloginlist.index(tloginlist)

            messagebox.showinfo("Iniciado", "Sesion iniciada con exito")

            #Se accede al menu principal
            welcome()

        #Excepcion para cuando el usuario o la contraseña son incorrectos
        except ValueError:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

#Funcion para registrar usuario
def sregist():
    #Variables globales
    global main, finicio, fregist, pstate, lloginlist, lcpassword, eruser, erpassword, ercpassword

    #Lista temporal de login
    tloginlist = ""

    #Condicional para verificar si los campos estan vacios
    if erpassword.get() == "" or eruser.get() == "" or ercpassword.get() == "":
        messagebox.showerror("Error", "No se pueden dejar campos vacios")

    #Condicional para verificar si el correo es valido
    elif eruser.get().count("@") != 1 or eruser.get()[eruser.get().index("@"):] not in emaildb:
        messagebox.showerror("Error", "Correo invalido")

    #Condicional para verificar si las contraseñas coinciden
    elif erpassword.get() == ercpassword.get():
        #Condicional para verificar si el usuario y la contraseña tienen espacios
        try:
            erpassword.get().index(" ")
            ercpassword.get().index(" ")
            eruser.get().index(" ")
            messagebox.showerror("Error", "No se pueden usar espacios en los campos")

        #Excepcion para cuando el usuario y la contraseña no tienen espacios
        except ValueError:
            #Condicional para verificar si la contraseña contiene al menos 1 letra minuscula, 1 letra mayuscula, 1 numero, 1 caracter especial y solo 10 caracteres
            if erpassword.get().isalnum() == False and any(chr.islower() for chr in erpassword.get()) == True and any(chr.isupper() for chr in erpassword.get()) == True and any(chr.isdigit() for chr in erpassword.get()) == True and len(erpassword.get()) == 10:
                #Se concatenan el usuario y la contraseña
                tloginlist += eruser.get().lower()
                tloginlist += ", " + erpassword.get()

                #Condicional para verificar si el usuario ya existe
                try:
                    lloginlist.index(tloginlist)
                    messagebox.showerror("Error", "El usuario ya existe")

                #Excepcion para cuando el usuario no existe
                except ValueError:
                    #Se agrega el usuario y la contraseña a la base de datos
                    lloginlist.append(tloginlist)

                    #Se cifra la contraseña
                    lcpassword.append(hashlib.sha256(erpassword.get().encode()).hexdigest())

                    #Se guarda la base de datos
                    txtloginlist = open(uplist, "w")
                    txtloginlist.write(str(lloginlist))
                    txtloginlist.close()

                    #Se guarda la base de datos de contraseñas
                    txtcpassword = open(cplist, "w")
                    txtcpassword.write(str(lcpassword))
                    txtcpassword.close()

                    messagebox.showinfo("Registrado", "Usuario registrado con exito")
                    back()

            #Excepcion para cuando la contraseña no contiene al menos 1 letra minuscula, 1 letra mayuscula, 1 numero, 1 caracter especial y solo 10 caracteres
            else:
                messagebox.showerror("Error", "La contraseña debe tener al menos 1 letra minuscula, 1 letra mayuscula, 1 numero, 1 caracter especial y solo 10 caracteres")

    else:
        messagebox.showerror("Error", "Las contraseñas no coinciden")

#Funcion principal
def run():
    #Variables globales
    global ssize, fsize, root, ico
    global main, fmainmenu, finicio, flogin, fregist, fwelcome
    global eluser, elpassword, usuario
    global eruser, erpassword, ercpassword
    global lwelcomemessage

    #Se crea la ventana
    root = tkinter.Tk()
    
    #Se crea el tema
    sv_ttk.set_theme("light")

    #Se obtiene el tamaño de la pantalla
    ssize = (root.winfo_screenwidth(), root.winfo_screenheight())

    #Se asignan los tamaños de fuente
    fsize = int((35 / 1366) * ssize[0])

    #Se asigna el tamaño de 1 tercio de la pantalla
    trissize = int((455 / 1366) * ssize[0])

    #Se maximiza la ventana
    root.state("zoomed")

    #Se asigna el titulo y el color de fondo
    root.title(mrtitle)
    root.config(bg = bgcolor)

    #Se asigna el icono
    ico = Image.open("img/logo.png")
    root.wm_iconphoto(False, ImageTk.PhotoImage(ico))

    #Se crea la pantalla de funcionamiento
    main = ttk.Notebook(root)

    #MENU PRINCIPAL
    #Se crea la pantalla principal
    fmainmenu = Frame(root, bg = bgcolor)

    #Se crea el frame de espacio superior izquierdo de la pantalla principal
    ftlmspace = Frame(fmainmenu, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el titulo de la pantalla principal
    lmaintitle = Label(fmainmenu, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    #Se crea el logo de la pantalla principal
    logo = ImageTk.PhotoImage(ico.resize((int(ssize[0] * 0.1), int(ssize[0] * 0.1 * logoar))))
    limaintitle = tkinter.Label(fmainmenu, image = logo, bg = bgcolor)
    
    #Se crea el frame de espacio medio izquierdo de la pantalla principal
    fmlmspace = Frame(fmainmenu, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea la descripcion de la pantalla principal
    lmaindesc = Label(fmainmenu, text = mydescription, font = (ftitle, int(fsize / 2), "bold"), relief = "raised", padx = int(ssize[0] * 0.03), pady = int(ssize[1] * 0.01))

    #Se crea el frame de espacio superior central de la pantalla principal
    ftcmspace = Frame(fmainmenu, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el boton de registro de la pantalla principal
    bregist = Button(fmainmenu, text = "Registrarse", font = (ftitle, int(fsize / 2), "bold"), command = regist, height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

    #Se crea el boton de login de la pantalla principal
    blogin = Button(fmainmenu, text = "Iniciar sesion", font = (ftitle, int(fsize / 2), "bold"), command = login, height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

    #Se crea el frame de espacio superior derecho de la pantalla principal
    ftrmspace = Frame(fmainmenu, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de espacio inferior izquierdo de la pantalla principal
    fblmspace = Frame(fmainmenu, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    #INICIO
    #Se crea la pantalla de inicio
    finicio = Frame(main, bg = bgcolor)

    #LOGIN
    #Se crea la pantalla de login
    flogin = Frame(main, bg = bgcolor)

    #Se crea el frame de espacio superior izquierdo de la pantalla de login
    ftllspace = Frame(flogin, width = ssize[0] * 0.39, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el titulo de la pantalla de login
    llogintitle = Label(flogin, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    #Se crea el logo de la pantalla de login
    lilogintitle = tkinter.Label(flogin, image = logo, bg = bgcolor)

    #Se crea el frame de ubicacion de los elementos de la pantalla de login
    fltext = Frame(flogin, bg = bgcolor)

    #Se crea el label de usuario de la pantalla de login
    lluser = Label(fltext, text = "Email", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de usuario de la pantalla de login
    eluser = Entry(fltext, font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.02))

    #Se crea el label de contraseña de la pantalla de login
    llpassword = Label(fltext, text = "Contraseña", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de contraseña de la pantalla de login
    elpassword = Entry(fltext, show = "*",font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.02))

    #Se crea el label de espacio vacio de la pantalla de login
    ltlogin = Label(fltext, text = " ", font = (ftitle, int(fsize / 5), "bold"), bg = bgcolor)

    #Se crea el boton de iniciar sesion de la pantalla de login
    bslogin = Button(fltext, text = "Iniciar sesion", command = slogin, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.002), width = int(ssize[0] * 0.009))

    #Se crea el frame de espacio superior derecho de la pantalla de login
    ftrlspace = Frame(flogin, width = ssize[0] * 0.39, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de espacio central izquierdo de la pantalla de login
    fcllspace = Frame(flogin, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de espacio inferior izquierdo de la pantalla de login
    fbllspace = Frame(flogin, width = ssize[0] * 0.05, height = ssize[0] * 0.08, bg = bgcolor)

    #REGISTRO  
    #Se crea la pantalla de registro
    fregist = Frame(main, bg = bgcolor)

    #Se crea el frame de espacio superior izquierdo de la pantalla de registro
    ftlrspace = Frame(fregist, width = ssize[0] * 0.39, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el titulo de la pantalla de registro
    lregisttitle = Label(fregist, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    #Se crea el logo de la pantalla de registro
    liregisttitle = tkinter.Label(fregist, image = logo, bg = bgcolor)

    #Se crea el frame de ubicacion de los elementos de la pantalla de registro
    frtext = Frame(fregist, bg = bgcolor)

    #Se crea el label de usuario de la pantalla de registro
    lruser = Label(frtext, text = "Email", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de usuario de la pantalla de registro
    eruser = Entry(frtext, font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.02))

    #Se crea el label de contraseña de la pantalla de registro
    lrpassword = Label(frtext, text = "Contraseña", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de contraseña de la pantalla de registro
    erpassword = Entry(frtext, show = "*",font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.02))

    #Se crea el label de confirmar contraseña de la pantalla de registro
    lrcpassword = Label(frtext, text = "Confirmar contraseña", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de confirmar contraseña de la pantalla de registro
    ercpassword = Entry(frtext, show = "*",font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.02))

    #Se crea el label de espacio vacio de la pantalla de registro
    ltregist = Label(frtext, text = " ", font = (ftitle, int(fsize / 5), "bold"), bg = bgcolor)

    #Se crea el boton de registrarse de la pantalla de registro
    bsregist = Button(frtext, text = "Registrarse", command = sregist, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.002), width = int(ssize[0] * 0.009))

    #Se crea el frame de espacio superior derecho de la pantalla de registro
    ftrrspace = Frame(fregist, width = ssize[0] * 0.39, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de espacio central izquierdo de la pantalla de registro
    fclrspace = Frame(fregist, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de espacio inferior izquierdo de la pantalla de registro
    fblrspace = Frame(fregist, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    #BIENVENIDO
    #Se crea la pantalla de menu principal
    fwelcome = Frame(main, bg = bgcolor)

    #Se crea el frame de espacio superior izquierdo de la pantalla de menu principal
    ftlwspace = Frame(fwelcome, width = ssize[0] * 0.11, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el titulo de la pantalla de menu principal
    lwelcometitle = Label(fwelcome, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    #Se crea el logo de la pantalla de menu principal
    liwelcometitle = tkinter.Label(fwelcome, image = logo, bg = bgcolor)

    #Se crea el frame de espacio superior central de la pantalla de menu principal
    ftcwspace = Frame(fwelcome, width = ssize[0] * 0.11, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de espacio superior derecho de la pantalla de menu principal
    ftrwspace = Frame(fwelcome, width = ssize[0] * 0.16, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de ubicacion de los elementos de la pantalla de menu principal
    fwtext = Frame(fwelcome, bg = bgcolor)

    #Se crea el label de mensaje de bienvenida de la pantalla de menu principal
    lwelcomemessage = Label(fwtext, font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el boton de gestion de platos
    bwgestionplatos = Button(fwtext, text = "Gestion de platos", command = gestionplatos, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

    #Se crea el boton de gestion de mesas
    bwgestionmesas = Button(fwtext, text = "Gestion de mesas", command = gestionmesas, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))
    
    #Se crea el boton de gestion de pedidos
    bwgestionpedidos = Button(fwtext, text = "Gestion de pedidos", command = gestionpedidos, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

    #Se crea el boton de cerrar sesion
    bwcsesion = Button(fwtext, text = "Cerrar sesion", command = back, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

    #Posicionamiento de Frames
    #Posicionamiento de la pantalla principal
    fmainmenu.grid(row = 0, column = 0)

    #Posicionamiento del frame de espacio superior izquierdo de la pantalla principal
    ftlmspace.grid(row = 0, column = 0)

    #Posicionamiento del frame de espacio medio izquierdo de la pantalla principal
    fmlmspace.grid(row = 3, column = 0)

    #Posicionamiento del frame de espacio inferior izquierdo de la pantalla principal
    fblmspace.grid(row = 5, column = 0)

    #Posicionamiento del titulo de la pantalla principal
    lmaintitle.grid(row = 1, column = 1)

    #Posicionamiento del logo de la pantalla principal
    limaintitle.grid(row = 2, column = 1)

    #Posicionamiento de la descripcion de la pantalla principal
    lmaindesc.grid(row = 4, column = 1)

    #Posicionamiento del frame de espacio superior central de la pantalla principal
    ftcmspace.grid(row = 0, column = 2)

    #Posicionamiento del boton de registro de la pantalla principal
    bregist.grid(row = 1, column = 4)

    #Redunda la funcion de registro
    bregist.bind("<Button-1>", lambda event: regist())

    #Posicionamiento del boton de login de la pantalla principal
    blogin.grid(row = 2, column = 4)

    #Redunda la funcion de login
    blogin.bind("<Button-1>", lambda event: login())

    #Posicionamiento del frame de espacio superior derecho de la pantalla principal
    ftrmspace.grid(row = 0, column = 5)

    #Posicionamiento del login
    #Posicionamiento del frame de espacio superior izquierdo de la pantalla de login
    ftllspace.grid(row = 0, column = 0)

    #Posicionamiento del frame de espacio central izquierdo de la pantalla de login
    fcllspace.grid(row = 3, column = 0)

    #Posicionamiento del frame de espacio inferior izquierdo de la pantalla de login
    fbllspace.grid(row = 5, column = 0)

    #Posicionamiento del titulo de la pantalla de login
    llogintitle.grid(row = 1, column = 1)

    #Posicionamiento del logo de la pantalla de login
    lilogintitle.grid(row = 2, column = 1)

    #Posicionamiento del frame de ubicacion de los elementos de la pantalla de login
    fltext.grid(row = 4, column = 1)

    #Posicionamiento del label de usuario de la pantalla de login
    lluser.grid(row = 0, column = 0)

    #Posicionamiento del entry de usuario de la pantalla de login
    eluser.grid(row = 1, column = 0)

    #Posicionamiento del label de contraseña de la pantalla de login
    llpassword.grid(row = 2, column = 0)

    #Posicionamiento del entry de contraseña de la pantalla de login
    elpassword.grid(row = 3, column = 0)

    #Posicionamiento del label de espacio vacio de la pantalla de login
    ltlogin.grid(row = 4, column = 0)

    #Posicionamiento del boton de iniciar sesion de la pantalla de login
    bslogin.grid(row = 5, column = 0)

    #Posicionamiento del frame de espacio superior derecho de la pantalla de login
    ftrlspace.grid(row = 0, column = 2)

    #Posicionamiento del registro
    #Posicionamiento del frame de espacio superior izquierdo de la pantalla de registro
    ftlrspace.grid(row = 0, column = 0)

    #Posicionamiento del frame de espacio central izquierdo de la pantalla de registro
    fclrspace.grid(row = 3, column = 0)

    #Posicionamiento del frame de espacio inferior izquierdo de la pantalla de registro
    fblrspace.grid(row = 5, column = 0)

    #Posicionamiento del titulo de la pantalla de registro
    lregisttitle.grid(row = 1, column = 1)

    #Posicionamiento del logo de la pantalla de registro
    liregisttitle.grid(row = 2, column = 1)

    #Posicionamiento del frame de ubicacion de los elementos de la pantalla de registro
    frtext.grid(row = 4, column = 1)

    #Posicionamiento del label de usuario de la pantalla de registro
    lruser.grid(row = 0, column = 0)

    #Posicionamiento del entry de usuario de la pantalla de registro
    eruser.grid(row = 1, column = 0)

    #Posicionamiento del label de contraseña de la pantalla de registro
    lrpassword.grid(row = 2, column = 0)

    #Posicionamiento del entry de contraseña de la pantalla de registro
    erpassword.grid(row = 3, column = 0)

    #Posicionamiento del label de confirmar contraseña de la pantalla de registro
    lrcpassword.grid(row = 4, column = 0)

    #Posicionamiento del entry de confirmar contraseña de la pantalla de registro
    ercpassword.grid(row = 5, column = 0)

    #Posicionamiento del label de espacio vacio de la pantalla de registro
    ltregist.grid(row = 6, column = 0)

    #Posicionamiento del boton de registrarse de la pantalla de registro
    bsregist.grid(row = 7, column = 0)

    #Posicionamiento del frame de espacio superior derecho de la pantalla de registro
    ftrrspace.grid(row = 0, column = 2)

    #Posicionamiento del menu principal
    #Posicionamiento del frame de espacio superior izquierdo de la pantalla de menu principal
    ftlwspace.grid(row = 0, column = 0)
    
    #Posicionamiento del titulo de la pantalla de menu principal
    lwelcometitle.grid(row = 1, column = 1)

    #Posicionamiento del logo de la pantalla de menu principal
    liwelcometitle.grid(row = 2, column = 1)

    #Posicionamiento del frame de espacio superior central de la pantalla de menu principal
    ftcwspace.grid(row = 0, column = 2)

    #Posicionamiento del frame de ubicacion de los elementos de la pantalla de menu principal
    fwtext.grid(row = 2, column = 3)

    #Posicionamiento del label de mensaje de bienvenida de la pantalla de menu principal
    lwelcomemessage.grid(row = 0, column = 0)

    #Posicionamiento del boton de gestion de platos
    bwgestionplatos.grid(row = 1, column = 0)

    #Posicionamiento del boton de gestion de mesas
    bwgestionmesas.grid(row = 2, column = 0)

    #Posicionamiento del boton de gestion de pedidos
    bwgestionpedidos.grid(row = 3, column = 0)

    #Posicionamiento del boton de cerrar sesion
    bwcsesion.grid(row = 4, column = 0)

    #Posicionamiento del frame de espacio superior derecho de la pantalla de menu principal
    ftrwspace.grid(row = 0, column = 4)

    #Bucle de la ventana
    root.mainloop()

#Ejecucion del programa
if __name__ == "__main__":
    run()
from configfile import *

#Funciones
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

    #Se selecciona la pestaña de registro
    main.select(fregist)

    #Se asigna la funcion de volver a la pantalla anterior
    main.bind("<<NotebookTabChanged>>", lambda event: back())

    #Se remueve la pestaña de login
    main.hide(flogin)

    #Se remueve la pestaña de menu principal
    main.hide(fwelcome)
    main.hide(fgestionplatos)

#Funcion para la pantalla de login
def login():
    #Variables globales
    global main, fmainmenu, finicio, flogin ,fregist, fwelcome, fgestionplatos, fgestionmesas, fgestionpedidos, pstate

    #Variable del estado del programa en el valor de 1era pantalla
    pstate = 1

    #Se remueve la pantalla principal
    fmainmenu.grid_remove()

    #Se agrega la pantalla de funcionamiento
    main.grid(row = 0, column = 0)

    #Se agregan las pestañas
    main.add(finicio, text = "Inicio")
    main.add(flogin, text = "Iniciar sesion")

    #Se selecciona la pestaña de login
    main.select(flogin)

    #Se asigna la funcion de volver a la pantalla anterior
    main.bind("<<NotebookTabChanged>>", lambda event: back())

    #Se remueve la pestaña de registro
    main.hide(fregist)

    #Se remueve la pestaña de menu principal
    main.hide(fwelcome)
    main.hide(fgestionplatos)

#Funcion para la pantalla de menu principal
def welcome():
    #Variables globales
    global main, finicio, fwelcome, fgestionplatos, fgestionmesas, fgestionpedidos, pstate, lwelcomemessage, usuario

    #Variable del estado del programa en el valor de 2da pantalla
    pstate = 2

    #Se agrega la pestaña del menu principal
    main.add(finicio, text = "Inicio")
    main.add(fwelcome, text = "Menu principal")

    #Se remueven las pestañas
    main.hide(fgestionplatos)
    #main.forget(fgestionmesas)
    #main.forget(fgestionpedidos)

    #Se selecciona la pestaña del menu principal
    main.select(fwelcome)

    #Se asigna la funcion de volver a la pantalla anterior
    main.bind("<<NotebookTabChanged>>", lambda event: back())

    #Se remueve la pestaña de login
    main.hide(flogin)

    #Se asigna el texto del mensaje de bienvenida
    lwelcomemessage.config(text = "Bienvenido " + usuario)

#Funcion para la pantalla de gestion de platos
def gestionplatos():
    #Variables globales
    global main, finicio, fgestionplatos, pstate

    #Variable del estado del programa en el valor de 3era pantalla
    pstate = 4

    #Se agrega la pestaña de gestion de platos
    main.add(fgestionplatos, text = "Gestion de platos")

    #Se selecciona la pestaña de gestion de platos
    main.select(fgestionplatos)

    #Se asigna la funcion de volver a la pantalla anterior
    main.bind("<<NotebookTabChanged>>", lambda event: back())

    #Se remueve la pestaña de inicio
    main.hide(finicio)

#Funcion para la pantalla de gestion de mesas
def gestionmesas():
    pass

#Funcion para la pantalla de gestion de pedidos
def gestionpedidos():
    pass

def agregarplato():
    pass

def eliminarplato():
    pass

def actualizarplato():
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
            tloginlist += eluser.get().lower() + ", " + elpassword.get()

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
                tloginlist += eruser.get().lower() + ", " + erpassword.get()

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

                    #Se guarda la base de datos de usuarios y contraseñas
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
        #Variable del estado del programa en el valor de la pagina principal
        pstate = 0
    
        #Se reinician los entrys
        eluser.delete(0, END)
        elpassword.delete(0, END)
        eruser.delete(0, END)
        erpassword.delete(0, END)
        ercpassword.delete(0, END)

        #Se remueve la pantalla de funcionamiento
        main.hide(finicio)
        main.hide(fgestionplatos)
        main.grid_remove()

        #Se agrega la pantalla principal
        fmainmenu.grid(row = 0, column = 0)

    #Condicional para volver a la pantalla del menu principal
    elif pstate == 2:
        #Variable del estado del programa en el valor de gestion de platos, mesas y pedidos
        pstate = 1

    elif pstate == 3:

        welcome()
        pstate = 1

    elif pstate == 4:
        #Variable del estado del programa en el valor de gestion de platos
        pstate = 3

#Funcion principal
def run():
    #Variables globales
    global ssize, fsize, root, ico
    global main, fmainmenu, finicio, flogin, fregist, fwelcome, fgestionplatos, fgestionmesas, fgestionpedidos
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

    #GESTION DE PLATOS
    #Se crea la pantalla de gestion de platos
    fgestionplatos = Frame(main, bg = bgcolor)

    #Se crea el frame de espacio superior izquierdo de la pantalla de gestion de platos
    ftlgpspace = Frame(fgestionplatos, width = ssize[0] * 0.11, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el titulo de la pantalla de gestion de platos
    lgestionplatostitle = Label(fgestionplatos, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    #Se crea el logo de la pantalla de gestion de platos
    ligestionplatostitle = tkinter.Label(fgestionplatos, image = logo, bg = bgcolor)

    #Se crea el frame de espacio superior central de la pantalla de gestion de platos
    ftcgpspace = Frame(fgestionplatos, width = ssize[0] * 0.11, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de espacio superior derecho de la pantalla de gestion de platos
    ftrgpspace = Frame(fgestionplatos, width = ssize[0] * 0.16, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de ubicacion de los elementos de la pantalla de gestion de platos
    fgpstext = Frame(fgestionplatos, bg = bgcolor)

    #Se crea el label de gestion de platos
    lgestionplatos = Label(fgpstext, text = "Gestion de platos", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el boton de agregar plato
    bgpagregarplato = Button(fgpstext, text = "Agregar plato", command = agregarplato, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

    #Se crea el boton de eliminar plato
    bgpeliminarplato = Button(fgpstext, text = "Eliminar plato", command = eliminarplato, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

    #Se crea el boton de actualizar plato
    bgpactualizarplato = Button(fgpstext, text = "Actualizar plato", command = actualizarplato, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

    #Se agregan las pestañas
    main.add(finicio, text = "Inicio")
    main.add(flogin, text = "Iniciar sesion")
    main.add(fregist, text = "Registrarse")
    main.add(fwelcome, text = "Menu principal")
    main.add(fgestionplatos, text = "Gestion de platos")
    #main.add(fgestionmesas, text = "Gestion de mesas")
    #main.add(fgestionpedidos, text = "Gestion de pedidos")

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

    #Posicionamiento de la pantalla de gestion de platos
    #Posicionamiento del frame de espacio superior izquierdo de la pantalla de gestion de platos
    ftlgpspace.grid(row = 0, column = 0)

    #Posicionamiento del titulo de la pantalla de gestion de platos
    lgestionplatostitle.grid(row = 1, column = 1)

    #Posicionamiento del logo de la pantalla de gestion de platos
    ligestionplatostitle.grid(row = 2, column = 1)

    #Posicionamiento del frame de espacio superior central de la pantalla de gestion de platos
    ftcgpspace.grid(row = 0, column = 2)

    #Posicionamiento del frame de ubicacion de los elementos de la pantalla de gestion de platos
    fgpstext.grid(row = 2, column = 3)

    #Posicionamiento del label de gestion de platos
    lgestionplatos.grid(row = 0, column = 0)

    #Posicionamiento del boton de agregar plato
    bgpagregarplato.grid(row = 1, column = 0)

    #Posicionamiento del boton de eliminar plato
    bgpeliminarplato.grid(row = 2, column = 0)

    #Posicionamiento del boton de actualizar plato
    bgpactualizarplato.grid(row = 3, column = 0)

    #Posicionamiento del frame de espacio superior derecho de la pantalla de gestion de platos
    ftrgpspace.grid(row = 0, column = 4)

    #Bucle de la ventana
    root.mainloop()

#Ejecucion del programa
if __name__ == "__main__":
    run()
from configfile import *

#Funciones
#Funcion para la pantalla de registro
def regist():
    global pstate

    #Variable del estado del programa en el valor de login y registro
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

    #Se remueven las pestañas
    main.hide(flogin)
    main.hide(fwelcome)
    main.hide(fgestionplatos)

#Funcion para la pantalla de login
def login():
    global pstate

    #Variable del estado del programa en el valor de login y registro
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

    #Se remueven las pestañas
    main.hide(fregist)
    main.hide(fwelcome)
    main.hide(fgestionplatos)

#Funcion para la pantalla de menu principal
def welcome():
    global pstate, usuario

    #Variable del estado del programa en el valor de menu principal
    pstate = 2

    #Se agrega la pestaña del menu principal
    main.add(finicio, text = "Inicio")
    main.add(fwelcome, text = "Menu principal")

    #Se remueven las pestañas
    main.hide(flogin)
    main.hide(fgestionplatos)
    #main.forget(fgestionmesas)
    #main.forget(fgestionpedidos)

    #Se selecciona la pestaña del menu principal
    main.select(fwelcome)

    #Se asigna la funcion de volver a la pantalla anterior
    main.bind("<<NotebookTabChanged>>", lambda event: back())

    #Se asigna el texto del mensaje de bienvenida
    lwelcomemessage.config(text = "Bienvenido " + usuario)

#Funcion para la pantalla de gestion de platos
def gestionplatos():
    global pstate

    #Variable del estado del programa en el valor de gestion de platos
    pstate = 4

    #Se agrega la pestaña de gestion de platos
    main.add(fwelcome, text = "Menu principal")
    main.add(fgestionplatos, text = "Gestion de platos")

    #Se selecciona la pestaña de gestion de platos
    main.select(fgestionplatos)

    #Se asigna la funcion de volver a la pantalla anterior
    main.bind("<<NotebookTabChanged>>", lambda event: back())

    #Se remueven las pestañas
    main.hide(finicio)
    main.hide(fagregarplato)
    main.hide(feliminaractualizarplato)

#Funcion para la pantalla de agregar plato
def agregarplato():
    global pstate

    #Variable del estado del programa en el valor de agregar plato
    pstate = 5

    #Se agrega la pestaña de agregar plato
    main.add(fagregarplato, text = "Agregar plato")

    #Se selecciona la pestaña de agregar plato
    main.select(fagregarplato)

    #Se asigna la funcion de volver a la pantalla anterior
    main.bind("<<NotebookTabChanged>>", lambda event: back())

    #Se muestra la pestaña de menu principal
    main.hide(fwelcome)

#Funcion para la pantalla de eliminar o actualizar plato
def eliminaractualizarplato():
    global pstate

    #Variable del estado del programa en el valor de eliminar o actualizar plato
    pstate = 6

    #Variables de listas de platos
    snplatos = []
    spplatos = []
    sdesplatos = []
    sdplatos = []

    #Se agrega la pestaña de agregar plato
    main.add(fgestionplatos, text = "Gestion de platos")
    main.add(feliminaractualizarplato, text = "Eliminar o actualizar plato")

    #Se selecciona la pestaña de agregar plato
    main.select(feliminaractualizarplato)

    #Se asigna la funcion de volver a la pantalla anterior
    main.bind("<<NotebookTabChanged>>", lambda event: back())

    #Se asigna la funcion de seleccionar lineas de listbox
    lbnplatos.bind("<ButtonRelease-1>", lambda event: selneliminarplato())
    lbpplatos.bind("<ButtonRelease-1>", lambda event: selpeliminarplato())
    lbdesplatos.bind("<ButtonRelease-1>", lambda event: seldeseliminarplato())
    lbdplatos.bind("<ButtonRelease-1>", lambda event: seldeliminarplato())

    #Se muestra la pestaña de menu principal
    main.hide(fwelcome)
    main.hide(factualizarplato)

    #Se organiza la lista de nombres de platos
    for i in range(len(lplatos)):
        snplatos.append(lplatos[i][0].capitalize())

    #Se organiza la lista de precios de platos
    for i in range(len(lplatos)):
        spplatos.append(lplatos[i][1])

    #Se organiza la lista de descripciones de platos
    for i in range(len(lplatos)):
        sdesplatos.append(lplatos[i][2])

    #Se organiza la lista de disponibilidades de platos
    for i in range(len(lplatos)):
        sdplatos.append(lplatos[i][3])

    #Se asigna el listado de nombres de platos
    lbnplatos.delete(0, END)
    lbnplatos.insert(0, *snplatos)

    #Se asigna el listado de precios de platos
    lbpplatos.delete(0, END)
    lbpplatos.insert(0, *spplatos)

    #Se asigna el listado de descripciones de platos
    lbdesplatos.delete(0, END)
    lbdesplatos.insert(0, *sdesplatos)

    #Se asigna el listado de disponibilidades de platos
    lbdplatos.delete(0, END)
    lbdplatos.insert(0, *sdplatos)

#Funcion para la pantalla de actualizar plato
def actualizarplato():
    global pstate

    #Condicional para verificar si se selecciono un plato
    if lbnplatos.curselection() != ():
        #Variable del estado del programa en el valor de actualizar plato
        pstate = 7

        #Se agrega la pestaña de agregar plato
        main.add(factualizarplato, text = "Actualizar plato")

        #Se selecciona la pestaña de agregar plato
        main.select(factualizarplato)
        
        #Se limpian los entrys
        eanombreplato.delete(0, END)
        eaprecioplato.delete(0, END)
        eadescripcionplato.delete(0, END)
        eadisponibilidadplato.delete(0, END)

        #Se asignan los entrys con los valores del plato seleccionado
        eanombreplato.insert(0, lbnplatos.get(lbnplatos.curselection()))
        eaprecioplato.insert(0, lbpplatos.get(lbpplatos.curselection()))
        eadescripcionplato.insert(0, lbdesplatos.get(lbdesplatos.curselection()))
        eadisponibilidadplato.insert(0, lbdplatos.get(lbdplatos.curselection()))

        #Se asigna la funcion de volver a la pantalla anterior
        main.bind("<<NotebookTabChanged>>", lambda event: back())

        #Se muestra la pestaña de menu principal
        main.hide(fgestionplatos)

#Funcion para la pantalla de gestion de mesas
def gestionmesas():
    pass

#Funcion para la pantalla de gestion de pedidos
def gestionpedidos():
    pass

#Funcion para iniciar sesion
def slogin():
    global usuario

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
    global lloginlist, lcpassword

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

#Funcion para agregar plato
def sagregarplato():
    global lplatos

    #Lista temporal de platos
    tlplatos = []
    
    #Condicional para verificar si los campos estan vacios
    if enombreplato.get() == "" or eprecioplato.get() == "" or edescripcionplato.get() == "" or edisponibilidadplato.get() == "":
        messagebox.showerror("Error", "No se pueden dejar campos vacios")

    #Condicional para verificar si la disponibilidad del plato es si o no
    elif edisponibilidadplato.get().lower() != "si" and edisponibilidadplato.get().lower() != "no":
        messagebox.showerror("Error", "La disponibilidad del plato solo puede ser si o no")

    #Condicional para verificar si el precio del plato es un numero
    elif eprecioplato.get().isdigit() == False:
        messagebox.showerror("Error", "El precio del plato solo puede ser un numero y no puede ser negativo")

    else:
        #Condicional para verificar si el plato ya existe
        try:
            for i in range(len(lplatos)):
                lplatos[i].index(enombreplato.get().lower())
            messagebox.showerror("Error", "El plato ya existe")

        #Excepcion para cuando el plato no existe
        except ValueError:
            #Se agrega el plato a la base de datos
            tlplatos.append(enombreplato.get().lower())
            tlplatos.append(eprecioplato.get())
            tlplatos.append(edescripcionplato.get())
            tlplatos.append(edisponibilidadplato.get().lower())

            lplatos.append(tlplatos)

            #Se guarda la base de datos de platos
            txtplatos = open(plist, "w")
            txtplatos.write(str(lplatos))
            txtplatos.close()

            messagebox.showinfo("Agregado", "Plato agregado con exito")

#Funcion para eliminar plato
def seliminarplato():
    #Condicional para verificar si se selecciono un plato
    if lbnplatos.curselection() != ():
        #Se elimina el plato de la base de datos
        lplatos.pop(lbnplatos.curselection()[0])

        #Se eliminan los platos de los listbox
        lbnplatos.delete(lbnplatos.curselection())
        lbpplatos.delete(lbpplatos.curselection())
        lbdesplatos.delete(lbdesplatos.curselection())
        lbdplatos.delete(lbdplatos.curselection())

        #Se guarda la base de datos de platos
        txtplatos = open(plist, "w")
        txtplatos.write(str(lplatos))
        txtplatos.close()

        messagebox.showinfo("Eliminado", "Plato eliminado con exito")

#Funcion para actualizar plato
def sactualizarplato():
    global lplatos

    #Lista temporal de platos
    tlplatos = []

    #Condicional para verificar si los campos estan vacios
    if eanombreplato.get() == "" or eaprecioplato.get() == "" or eadescripcionplato.get() == "" or eadisponibilidadplato.get() == "":
        messagebox.showerror("Error", "No se pueden dejar campos vacios")

    #Condicional para verificar si la disponibilidad del plato es si o no
    elif eadisponibilidadplato.get().lower() != "si" and eadisponibilidadplato.get().lower() != "no":
        messagebox.showerror("Error", "La disponibilidad del plato solo puede ser si o no")

    #Condicional para verificar si el precio del plato es un numero
    elif eaprecioplato.get().isdigit() == False:
        messagebox.showerror("Error", "El precio del plato solo puede ser un numero y no puede ser negativo")

    else:
        #Condicional para verificar si el plato ya existe
        try:
            for i in range(len(lplatos)):
                lplatos[i].index(eanombreplato.get().lower())
            messagebox.showerror("Error", "El plato ya existe")

        #Excepcion para cuando el plato no existe
        except ValueError:
            #Se agrega el plato a la base de datos
            tlplatos.append(eanombreplato.get().lower())
            tlplatos.append(eaprecioplato.get())
            tlplatos.append(eadescripcionplato.get())
            tlplatos.append(eadisponibilidadplato.get().lower())

            lplatos.pop(lbnplatos.curselection()[0])
            lplatos.insert(lbnplatos.curselection()[0], tlplatos)

            #Se guarda la base de datos de platos
            txtplatos = open(plist, "w")
            txtplatos.write(str(lplatos))
            txtplatos.close()

            messagebox.showinfo("Actualizado", "Plato actualizado con exito")

#Funciones para seleccionar lineas de listbox 
def selneliminarplato():
    lbpplatos.selection_clear(0, END)
    lbdesplatos.selection_clear(0, END)
    lbdplatos.selection_clear(0, END)

    lbpplatos.selection_set(lbnplatos.curselection())
    lbdesplatos.selection_set(lbnplatos.curselection())
    lbdplatos.selection_set(lbnplatos.curselection())

def selpeliminarplato():
    lbnplatos.selection_clear(0, END)
    lbdesplatos.selection_clear(0, END)
    lbdplatos.selection_clear(0, END)

    lbnplatos.selection_set(lbpplatos.curselection())
    lbdesplatos.selection_set(lbpplatos.curselection())
    lbdplatos.selection_set(lbpplatos.curselection())

def seldeseliminarplato():
    lbpplatos.selection_clear(0, END)
    lbnplatos.selection_clear(0, END)
    lbdplatos.selection_clear(0, END)

    lbpplatos.selection_set(lbdesplatos.curselection())
    lbnplatos.selection_set(lbdesplatos.curselection())
    lbdplatos.selection_set(lbdesplatos.curselection())

def seldeliminarplato():
    lbpplatos.selection_clear(0, END)
    lbdesplatos.selection_clear(0, END)
    lbnplatos.selection_clear(0, END)

    lbpplatos.selection_set(lbdplatos.curselection())
    lbdesplatos.selection_set(lbdplatos.curselection())
    lbnplatos.selection_set(lbdplatos.curselection())

#Funcion para volver a la pantalla anterior
def back():
    global pstate

    #Condicional para volver a la pantalla principal
    if pstate == 1:
        #Variable del estado del programa en el valor de pagina principal
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
        main.hide(fagregarplato)
        main.hide(feliminaractualizarplato)
        main.hide(factualizarplato)
        main.grid_remove()

        #Se agrega la pantalla principal
        fmainmenu.grid(row = 0, column = 0)

    #Condicional para volver a la pantalla principal
    elif pstate == 2:
        pstate = 1

    elif pstate == 3:
        #Se vuelve a la pantalla de menu principal
        welcome()
        pstate = 1

    elif pstate == 4:
        #Se reinician los entrys
        enombreplato.delete(0, END)
        eprecioplato.delete(0, END)
        edescripcionplato.delete(0, END)
        edisponibilidadplato.delete(0, END)

        #Se vuelve a la pantalla de gestion de platos
        gestionplatos()
        pstate = 3

    #Condicional para volver a la pantalla de gestion de platos
    elif pstate == 5:
        pstate = 4

    elif pstate == 6:
        #Se vuelve a la pantalla de eliminar o actualizar platos
        eliminaractualizarplato()
        pstate = 4

    #Condicional para volver a la pantalla de eliminar o actualizar platos
    elif pstate == 7:
        pstate = 6

#Funcion para definir la pantalla principal
def pmainmenu():
    #Variables globales
    global fmainmenu, ftlmspace, fmlmspace, fblmspace, lmaintitle, logo, limaintitle, lmaindesc, ftcmspace, bregist, blogin, ftrmspace
    
    #Se crea la pantalla principal
    fmainmenu = Frame(root, bg = bgcolor)

    #Se crea el frame de espacio superior izquierdo de la pantalla principal
    ftlmspace = Frame(fmainmenu, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el titulo de la pantalla principal
    lmaintitle = Label(fmainmenu, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    #Se crea el logo de la pantalla principal
    logo = ImageTk.PhotoImage(ico.resize((int(ssize[0] * 0.1), int(ssize[0] * 0.1 * logoar))))
    limaintitle = Label(fmainmenu, image = logo, bg = bgcolor)
    
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

#Funcion para definir la pantalla de login
def plogin():
    global flogin, ftllspace, fcllspace, fbllspace, ftrlspace, llogintitle, lilogintitle, fltext, eluser, elpassword, lluser, llpassword, ltlogin, bslogin

    #Se crea la pantalla de login
    flogin = Frame(main, bg = bgcolor)

    #Se crea el frame de espacio superior izquierdo de la pantalla de login
    ftllspace = Frame(flogin, width = ssize[0] * 0.39, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el titulo de la pantalla de login
    llogintitle = Label(flogin, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    #Se crea el logo de la pantalla de login
    lilogintitle = Label(flogin, image = logo, bg = bgcolor)

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

#Funcion para definir la pantalla de registro
def pregist():
    global fregist, ftlrspace, fblrspace, fclrspace, ftrrspace, lregisttitle, liregisttitle, frtext, eruser, erpassword, ercpassword, lruser, lrpassword, lrcpassword, ltregist, bsregist

    #Se crea la pantalla de registro
    fregist = Frame(main, bg = bgcolor)

    #Se crea el frame de espacio superior izquierdo de la pantalla de registro
    ftlrspace = Frame(fregist, width = ssize[0] * 0.39, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el titulo de la pantalla de registro
    lregisttitle = Label(fregist, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    #Se crea el logo de la pantalla de registro
    liregisttitle = Label(fregist, image = logo, bg = bgcolor)

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

#Funcion para definir la pantalla de menu principal
def pwelcome():
    global fwelcome, ftlwspace, ftcwspace, ftrwspace, lwelcometitle, liwelcometitle, fwtext, lwelcomemessage, bwgestionplatos, bwgestionmesas, bwgestionpedidos, bwcsesion

    #Se crea la pantalla de menu principal
    fwelcome = Frame(main, bg = bgcolor)

    #Se crea el frame de espacio superior izquierdo de la pantalla de menu principal
    ftlwspace = Frame(fwelcome, width = ssize[0] * 0.11, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el titulo de la pantalla de menu principal
    lwelcometitle = Label(fwelcome, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    #Se crea el logo de la pantalla de menu principal
    liwelcometitle = Label(fwelcome, image = logo, bg = bgcolor)

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

#Funcion para definir la pantalla de gestion de platos
def pgestionplatos():
    global fgestionplatos, ftlgpspace, ftcgpspace, ftrgpspace, lgestionplatostitle, ligestionplatostitle, fgptext, lgestionplatos, bgpagregarplato, bgpeliminaractualizarplato

    #Se crea la pantalla de gestion de platos
    fgestionplatos = Frame(main, bg = bgcolor)

    #Se crea el frame de espacio superior izquierdo de la pantalla de gestion de platos
    ftlgpspace = Frame(fgestionplatos, width = ssize[0] * 0.11, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el titulo de la pantalla de gestion de platos
    lgestionplatostitle = Label(fgestionplatos, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    #Se crea el logo de la pantalla de gestion de platos
    ligestionplatostitle = Label(fgestionplatos, image = logo, bg = bgcolor)

    #Se crea el frame de espacio superior central de la pantalla de gestion de platos
    ftcgpspace = Frame(fgestionplatos, width = ssize[0] * 0.11, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de espacio superior derecho de la pantalla de gestion de platos
    ftrgpspace = Frame(fgestionplatos, width = ssize[0] * 0.16, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de ubicacion de los elementos de la pantalla de gestion de platos
    fgptext = Frame(fgestionplatos, bg = bgcolor)

    #Se crea el label de gestion de platos
    lgestionplatos = Label(fgptext, text = "Gestion de platos", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el boton de agregar plato
    bgpagregarplato = Button(fgptext, text = "Agregar plato", command = agregarplato, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

    #Se crea el boton de eliminar plato
    bgpeliminaractualizarplato = Button(fgptext, text = "Eliminar o actualizar plato", command = eliminaractualizarplato, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

#Funcion para definir la pantalla de agregar plato
def pagregarplato():
    global fagregarplato, ftlapspace, lagregarplatotitle, liagregarplatotitle, ftcapspace, ftrapspace, faptext, lagregarplato, lnombreplato, enombreplato, lprecioplato, eprecioplato, ldescripcionplato, edescripcionplato, ldisponibilidadplato, edisponibilidadplato, bagregarplato

    #Se crea la pantalla de agregar plato
    fagregarplato = Frame(main, bg = bgcolor)

    #Se crea el frame de espacio superior izquierdo de la pantalla de agregar plato
    ftlapspace = Frame(fagregarplato, width = ssize[0] * 0.11, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el titulo de la pantalla de agregar plato
    lagregarplatotitle = Label(fagregarplato, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    #Se crea el logo de la pantalla de agregar plato
    liagregarplatotitle = Label(fagregarplato, image = logo, bg = bgcolor)

    #Se crea el frame de espacio superior central de la pantalla de agregar plato
    ftcapspace = Frame(fagregarplato, width = ssize[0] * 0.11, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de espacio superior derecho de la pantalla de agregar plato
    ftrapspace = Frame(fagregarplato, width = ssize[0] * 0.16, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de ubicacion de los elementos de la pantalla de agregar plato
    faptext = Frame(fagregarplato, bg = bgcolor)

    #Se crea el label de agregar plato
    lagregarplato = Label(faptext, text = "Agregar plato", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea label de nombre de plato
    lnombreplato = Label(faptext, text = "Nombre del plato", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de nombre de plato
    enombreplato = Entry(faptext, font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.04))

    #Se crea label de precio de plato
    lprecioplato = Label(faptext, text = "Precio del plato", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de precio de plato
    eprecioplato = Entry(faptext, font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.04))

    #Se crea label de descripcion de plato
    ldescripcionplato = Label(faptext, text = "Descripcion del plato", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de descripcion de plato
    edescripcionplato = Entry(faptext, font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.04))

    #Se crea label de disponibilidad de plato
    ldisponibilidadplato = Label(faptext, text = "Disponibilidad del plato", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de disponibilidad de plato
    edisponibilidadplato = Entry(faptext, font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.04))

    #Se crea el boton de agregar plato
    bagregarplato = Button(faptext, text = "Agregar plato", command = sagregarplato, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.001), width = int(ssize[0] * 0.01))

#Funcion para definir la pantalla de eliminar o actualizar plato
def peliminaractualizarplato():
    global logosmall, feliminaractualizarplato, lieliminaractualizarplatotitle, leliminaractualizarplatotitle, featext, leliminaractualizarplato, beliminarplato, bactualizarplato, lbnplatos, lbpplatos, lbdesplatos, lbdplatos, lnplatos, lpplatos, ldesplatos, ldplatos

    #Se crea la pantalla de eliminar o actualizar plato
    feliminaractualizarplato = Frame(main, bg = bgcolor)

    #Se crea el logo de la pantalla de eliminar o actualizar plato
    logosmall = ImageTk.PhotoImage(ico.resize((int(ssize[0] * 0.05), int(ssize[0] * 0.05 * logoar))))
    lieliminaractualizarplatotitle = Label(feliminaractualizarplato, image = logosmall, bg = bgcolor)

    #Se crea el frame de espacio superior izquierdo de la pantalla de eliminar o actualizar plato
    leliminaractualizarplatotitle = Label(feliminaractualizarplato, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    #Se crea el boton de eliminar plato
    beliminarplato = Button(feliminaractualizarplato, bg = "red", text = "Eliminar plato", command = seliminarplato, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.001), width = int(ssize[0] * 0.01))

    #Se crea el boton de actualizar plato
    bactualizarplato = Button(feliminaractualizarplato, text = "Actualizar plato", command = actualizarplato, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.001), width = int(ssize[0] * 0.01))

    #Se crea el frame de ubicacion de los elementos de la pantalla de eliminar o actualizar plato
    featext = Frame(feliminaractualizarplato, bg = bgcolor)

    #Se crea el label de eliminar o actualizar plato
    leliminaractualizarplato = Label(featext, text = "Platos", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea label del listbox de nombre de platos
    lnplatos = Label(featext, text = "Nombre", font = (ftitle, int(fsize / 3), "bold"), relief = "raised")

    #Se crea el listbox del nombre de los platos
    lbnplatos = Listbox(featext, exportselection = 0,font = (ftitle, int(fsize / 3), "bold"))

    #Se crea label del listbox de precio de platos
    lpplatos = Label(featext, text = "Precio", font = (ftitle, int(fsize / 3), "bold"), relief = "raised")

    #Se crea el listbox del precio de los platos
    lbpplatos = Listbox(featext, exportselection = 0, font = (ftitle, int(fsize / 3), "bold"))

    #Se crea label del listbox de descripcion de platos
    ldesplatos = Label(featext, text = "Descripcion", font = (ftitle, int(fsize / 3), "bold"), relief = "raised")

    #Se crea el listbox de la descripcion de los platos
    lbdesplatos = Listbox(featext, exportselection = 0, font = (ftitle, int(fsize / 3), "bold"))

    #Se crea label del listbox de disponibilidad de platos
    ldplatos = Label(featext, text = "Disponibilidad", font = (ftitle, int(fsize / 3), "bold"), relief = "raised")

    #Se crea el listbox de la disponibilidad de los platos
    lbdplatos = Listbox(featext, exportselection = 0, font = (ftitle, int(fsize / 3), "bold"))

#Funcion para definir la pantalla de actualizar plato
def pactualizarplato():
    global factualizarplato, ftlacpspace, lactualizarplatotitle, liactualizarplatotitle, ftcacpspace, ftracpspace, facptext, lactualizarplato, lanombreplato, eanombreplato, laprecioplato, eaprecioplato, ladescripcionplato, eadescripcionplato, ladisponibilidadplato, eadisponibilidadplato, baactualizarplato

    #Se crea la pantalla de actualizar plato
    factualizarplato = Frame(main, bg = bgcolor)

    #Se crea el frame de espacio superior izquierdo de la pantalla de actualizar plato
    ftlacpspace = Frame(factualizarplato, width = ssize[0] * 0.11, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el titulo de la pantalla de actualizar plato
    lactualizarplatotitle = Label(factualizarplato, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    #Se crea el logo de la pantalla de actualizar plato
    liactualizarplatotitle = Label(factualizarplato, image = logo, bg = bgcolor)

    #Se crea el frame de espacio superior central de la pantalla de actualizar plato
    ftcacpspace = Frame(factualizarplato, width = ssize[0] * 0.11, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de espacio superior derecho de la pantalla de actualizar plato
    ftracpspace = Frame(factualizarplato, width = ssize[0] * 0.16, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de ubicacion de los elementos de la pantalla de actualizar plato
    facptext = Frame(factualizarplato, bg = bgcolor)

    #Se crea el label de actualizar plato
    lactualizarplato = Label(facptext, text = "Actualizar plato", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea label de nombre de plato
    lanombreplato = Label(facptext, text = "Nombre del plato", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de nombre de plato
    eanombreplato = Entry(facptext, font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.04))

    #Se crea label de precio de plato
    laprecioplato = Label(facptext, text = "Precio del plato", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de precio de plato
    eaprecioplato = Entry(facptext, font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.04))

    #Se crea label de descripcion de plato
    ladescripcionplato = Label(facptext, text = "Descripcion del plato", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de descripcion de plato
    eadescripcionplato = Entry(facptext, font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.04))

    #Se crea label de disponibilidad de plato
    ladisponibilidadplato = Label(facptext, text = "Disponibilidad del plato", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de disponibilidad de plato
    eadisponibilidadplato = Entry(facptext, font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.04))

    #Se crea el boton de actualizar plato
    baactualizarplato = Button(facptext, text = "Actualizar plato", command = sactualizarplato, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.001), width = int(ssize[0] * 0.01))

#Funcion para posicionar la pantalla principal
def pospprincipal():
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

#Funcion para posicionar la pantalla de login
def poslogin():
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

#Funcion para posicionar la pantalla de registro
def posregist():
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

#Funcion para posicionar la pantalla de menu principal
def poswelcome():
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

#Funcion para posicionar la pantalla de gestion de platos
def posgestionplatos():
    #Posicionamiento del frame de espacio superior izquierdo de la pantalla de gestion de platos
    ftlgpspace.grid(row = 0, column = 0)

    #Posicionamiento del titulo de la pantalla de gestion de platos
    lgestionplatostitle.grid(row = 1, column = 1)

    #Posicionamiento del logo de la pantalla de gestion de platos
    ligestionplatostitle.grid(row = 2, column = 1)

    #Posicionamiento del frame de espacio superior central de la pantalla de gestion de platos
    ftcgpspace.grid(row = 0, column = 2)

    #Posicionamiento del frame de ubicacion de los elementos de la pantalla de gestion de platos
    fgptext.grid(row = 2, column = 3)

    #Posicionamiento del label de gestion de platos
    lgestionplatos.grid(row = 0, column = 0)

    #Posicionamiento del boton de agregar plato
    bgpagregarplato.grid(row = 1, column = 0)

    #Posicionamiento del boton de eliminar plato
    bgpeliminaractualizarplato.grid(row = 2, column = 0)

    #Posicionamiento del frame de espacio superior derecho de la pantalla de gestion de platos
    ftrgpspace.grid(row = 0, column = 4)

#Funcion para posicionar la pantalla de agregar plato
def posagregarplato():
    #Posicionamiento del frame de espacio superior izquierdo de la pantalla de agregar plato
    ftlapspace.grid(row = 0, column = 0)

    #Posicionamiento del titulo de la pantalla de agregar plato
    lagregarplatotitle.grid(row = 1, column = 1)

    #Posicionamiento del logo de la pantalla de agregar plato
    liagregarplatotitle.grid(row = 2, column = 1)

    #Posicionamiento del frame de espacio superior central de la pantalla de agregar plato
    ftcapspace.grid(row = 0, column = 2)

    #Posicionamiento del frame de ubicacion de los elementos de la pantalla de agregar plato
    faptext.grid(row = 2, column = 3)

    #Posicionamiento del label de agregar plato
    lagregarplato.grid(row = 0, column = 0)

    #Posicionamiento del label de nombre de plato
    lnombreplato.grid(row = 1, column = 0)

    #Posicionamiento del entry de nombre de plato
    enombreplato.grid(row = 2, column = 0)

    #Posicionamiento del label de precio de plato
    lprecioplato.grid(row = 3, column = 0)

    #Posicionamiento del entry de precio de plato
    eprecioplato.grid(row = 4, column = 0)

    #Posicionamiento del label de descripcion de plato
    ldescripcionplato.grid(row = 5, column = 0)

    #Posicionamiento del entry de descripcion de plato
    edescripcionplato.grid(row = 6, column = 0)

    #Posicionamiento del label de disponibilidad de plato
    ldisponibilidadplato.grid(row = 7, column = 0)

    #Posicionamiento del entry de disponibilidad de plato
    edisponibilidadplato.grid(row = 8, column = 0)

    #Posicionamiento del boton de agregar plato
    bagregarplato.grid(row = 9, column = 0)

    #Posicionamiento del frame de espacio superior derecho de la pantalla de agregar plato
    ftrapspace.grid(row = 0, column = 4)

#Funcion para posicionar la pantalla de eliminar o actualizar plato
def poseliminaractualizarplato():
    #Posicionamiento del logo de la pantalla de eliminar o actualizar plato
    lieliminaractualizarplatotitle.grid(row = 0, column = 0)

    #Posicionamiento del titulo de la pantalla de eliminar o actualizar plato
    leliminaractualizarplatotitle.grid(row = 0, column = 1)

    #Posicionamiento del boton de eliminar plato
    beliminarplato.grid(row = 0, column = 2, padx = (int(ssize[0] * 0.4), 0))

    #Posicionamiento del boton de actualizar plato
    bactualizarplato.grid(row = 0, column = 3)

    #Posicionamiento del frame de ubicacion de los elementos de la pantalla de eliminar o actualizar plato
    featext.grid(row = 1, column = 0, columnspan = 4)

    #Posicionamiento del label de eliminar o actualizar plato
    leliminaractualizarplato.grid(row = 0, column = 0, columnspan = 4)

    #Posicionamiento del label del listbox de nombre de platos
    lnplatos.grid(row = 1, column = 0)

    #Posicionamiento del listbox del nombre de los platos
    lbnplatos.grid(row = 2, column = 0)

    #Posicionamiento del label del listbox de precio de platos
    lpplatos.grid(row = 1, column = 1)

    #Posicionamiento del listbox del precio de los platos
    lbpplatos.grid(row = 2, column = 1)

    #Posicionamiento del label del listbox de descripcion de platos
    ldesplatos.grid(row = 1, column = 2)

    #Posicionamiento del listbox de la descripcion de los platos
    lbdesplatos.grid(row = 2, column = 2)

    #Posicionamiento del label del listbox de disponibilidad de platos
    ldplatos.grid(row = 1, column = 3)

    #Posicionamiento del listbox de la disponibilidad de los platos
    lbdplatos.grid(row = 2, column = 3)

#Funcion para posicionar la pantalla de actualizar plato
def posactualizarplato():
    #Posicionamiento del frame de espacio superior izquierdo de la pantalla de actualizar plato
    ftlacpspace.grid(row = 0, column = 0)

    #Posicionamiento del titulo de la pantalla de actualizar plato
    lactualizarplatotitle.grid(row = 1, column = 1)

    #Posicionamiento del logo de la pantalla de actualizar plato
    liactualizarplatotitle.grid(row = 2, column = 1)

    #Posicionamiento del frame de espacio superior central de la pantalla de actualizar plato
    ftcacpspace.grid(row = 0, column = 2)

    #Posicionamiento del frame de ubicacion de los elementos de la pantalla de actualizar plato
    facptext.grid(row = 2, column = 3)

    #Posicionamiento del label de actualizar plato
    lactualizarplato.grid(row = 0, column = 0)

    #Posicionamiento del label de nombre de plato
    lanombreplato.grid(row = 1, column = 0)

    #Posicionamiento del entry de nombre de plato
    eanombreplato.grid(row = 2, column = 0)

    #Posicionamiento del label de precio de plato
    laprecioplato.grid(row = 3, column = 0)

    #Posicionamiento del entry de precio de plato
    eaprecioplato.grid(row = 4, column = 0)

    #Posicionamiento del label de descripcion de plato
    ladescripcionplato.grid(row = 5, column = 0)

    #Posicionamiento del entry de descripcion de plato
    eadescripcionplato.grid(row = 6, column = 0)

    #Posicionamiento del label de disponibilidad de plato
    ladisponibilidadplato.grid(row = 7, column = 0)

    #Posicionamiento del entry de disponibilidad de plato
    eadisponibilidadplato.grid(row = 8, column = 0)

    #Posicionamiento del boton de actualizar plato
    baactualizarplato.grid(row = 9, column = 0)

    #Posicionamiento del frame de espacio superior derecho de la pantalla de actualizar plato
    ftracpspace.grid(row = 0, column = 4)

#Funcion para posicionar las pestañas
def pospestañas():
    #Se agregan las pestañas
    main.add(finicio, text = "Inicio")
    main.add(flogin, text = "Iniciar sesion")
    main.add(fregist, text = "Registrarse")
    main.add(fwelcome, text = "Menu principal")
    main.add(fgestionplatos, text = "Gestion de platos")
    main.add(fagregarplato, text = "Agregar plato")
    main.add(feliminaractualizarplato, text = "Eliminar o actualizar plato")
    main.add(factualizarplato, text = "Actualizar plato")
    #main.add(fgestionmesas, text = "Gestion de mesas")
    #main.add(fgestionpedidos, text = "Gestion de pedidos")

#Funcion principal
def run():
    #Variables globales
    global ssize, fsize, root, ico, usuario

    #Variables globales de las pantallas
    global main, finicio

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
    pmainmenu()

    #INICIO
    #Se crea la pantalla de inicio
    finicio = Frame(main, bg = bgcolor)

    #LOGIN
    plogin()

    #REGISTRO  
    pregist()

    #BIENVENIDO
    pwelcome()

    #GESTION DE PLATOS
    pgestionplatos()

    #AGREGAR PLATO
    pagregarplato()

    #ELIMINAR O ACTUALIZAR PLATO
    peliminaractualizarplato()

    #ACTUALIZAR PLATO
    pactualizarplato()

    #Posicionamiento de las pestañas
    pospestañas()

    #Posicionamiento de pantalla principal
    pospprincipal()

    #Posicionamiento de la pantalla de login
    poslogin()

    #Posicionamiento de la pantalla de registro
    posregist()

    #Posicionamiento de la pantalla de menu principal
    poswelcome()

    #Posicionamiento de la pantalla de gestion de platos
    posgestionplatos()

    #Posicionamiento de la pantalla de agregar plato
    posagregarplato()

    #Posicionamiento de la pantalla de eliminar o actualizar plato
    poseliminaractualizarplato()

    #Posicionamiento de la pantalla de actualizar plato
    posactualizarplato()

    #Bucle de la ventana
    root.mainloop()

#Ejecucion del programa
if __name__ == "__main__":
    run()
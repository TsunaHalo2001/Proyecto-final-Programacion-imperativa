from configfile import *

#Funciones
#Funcion para la pantalla de registro
def regist():
    global pstate

    root.title(mrtitle + " - " + rtitle)

    #Variable del estado del programa en el valor de login y registro
    pstate = 1

    #Se remueve la pantalla principal
    fmainmenu.grid_remove()

    #Se agrega la pantalla de funcionamiento
    main.grid(row = 0, column = 0)

    #Se agregan las pestañas
    main.add(finicio, text = ititle)
    main.add(fregist, text = rtitle)

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

    root.title(mrtitle + " - " + ltitle)

    #Variable del estado del programa en el valor de login y registro
    pstate = 1

    #Se remueve la pantalla principal
    fmainmenu.grid_remove()

    #Se agrega la pantalla de funcionamiento
    main.grid(row = 0, column = 0)

    #Se agregan las pestañas
    main.add(finicio, text = ititle)
    main.add(flogin, text = ltitle)

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

    root.title(mrtitle + " - " + mptitle)

    #Variable del estado del programa en el valor de menu principal
    pstate = 2

    #Se agrega la pestaña del menu principal
    main.add(finicio, text = ititle)
    main.add(fwelcome, text = mptitle)

    #Se remueven las pestañas
    main.hide(flogin)
    main.hide(fgestionplatos)
    main.hide(fgestionmesas)
    #main.hide(fgestionpedidos)

    #Se selecciona la pestaña del menu principal
    main.select(fwelcome)

    #Se asigna la funcion de volver a la pantalla anterior
    main.bind("<<NotebookTabChanged>>", lambda event: back())

    #Se asigna el texto del mensaje de bienvenida
    lwelcomemessage.config(text = "Bienvenido " + usuario)

#Funcion para la pantalla de gestion de platos
def gestionplatos():
    global pstate

    root.title(mrtitle + " - " + mptitle + " / " + gptitle)

    #Variable del estado del programa en el valor de gestion de platos
    pstate = 4

    #Se agrega la pestaña de gestion de platos
    main.add(fwelcome, text = mptitle)
    main.add(fgestionplatos, text = gptitle)

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

    root.title(mrtitle + " - " + mptitle + " / " + gptitle + " / " + aptitle)

    #Variable del estado del programa en el valor de agregar plato
    pstate = 5

    #Se agrega la pestaña de agregar plato
    main.add(fagregarplato, text = aptitle)

    #Se selecciona la pestaña de agregar plato
    main.select(fagregarplato)

    #Se asigna la funcion de volver a la pantalla anterior
    main.bind("<<NotebookTabChanged>>", lambda event: back())

    #Se muestra la pestaña de menu principal
    main.hide(fwelcome)

#Funcion para la pantalla de eliminar o actualizar plato
def eliminaractualizarplato():
    global pstate

    root.title(mrtitle + " - " + mptitle + " / " + gptitle + " / " + eaptitle)

    #Variable del estado del programa en el valor de eliminar o actualizar plato
    pstate = 6

    #Variables de listas de platos
    snplatos = []
    spplatos = []
    sdesplatos = []
    sdplatos = []

    #Se agrega la pestaña de agregar plato
    main.add(fgestionplatos, text = gptitle)
    main.add(feliminaractualizarplato, text = eaptitle)

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

    if len(lplatos) > 0:
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

    root.title(mrtitle + " - " + mptitle + " / " + gptitle + " / " + eaptitle + " / " + acptitle)

    #Condicional para verificar si se selecciono un plato
    if lbnplatos.curselection() != ():
        #Variable del estado del programa en el valor de actualizar plato
        pstate = 7

        #Se agrega la pestaña de agregar plato
        main.add(factualizarplato, text = acptitle)

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
    global pstate

    root.title(mrtitle + " - " + mptitle + " / " + gmtitle)

    #Variable del estado del programa en el valor de gestion de mesas
    pstate = 8

    #Se agrega la pestaña de gestion de mesas
    main.add(fwelcome, text = mptitle)
    main.add(fgestionmesas, text = gmtitle)

    #Se selecciona la pestaña de gestion de mesas
    main.select(fgestionmesas)

    #Se asigna la funcion de volver a la pantalla anterior
    main.bind("<<NotebookTabChanged>>", lambda event: back())

    #Se remueven las pestañas
    main.hide(finicio)
    main.hide(fagregarmesa)
    main.hide(feliminaractualizarmesa)

#Funcion para la pantalla de agregar mesa
def agregarmesa():
    global pstate

    root.title(mrtitle + " - " + mptitle + " / " + gmtitle + " / " + aptitle)

    #Variable del estado del programa en el valor de agregar mesa
    pstate = 9

    #Se agrega la pestaña de agregar mesa
    main.add(fagregarmesa, text = aptitle)

    #Se selecciona la pestaña de agregar mesa
    main.select(fagregarmesa)

    #Se asigna la funcion de volver a la pantalla anterior
    main.bind("<<NotebookTabChanged>>", lambda event: back())

    #Se muestra la pestaña de menu principal
    main.hide(fwelcome)

#Funcion para la pantalla de eliminar o actualizar mesa
def eliminaractualizarmesa():
    global pstate

    root.title(mrtitle + " - " + mptitle + " / " + gmtitle + " / " + eamtitle)

    #Variable del estado del programa en el valor de eliminar o actualizar mesa
    pstate = 10

    #Variables de listas de mesas
    snmesas = []
    sfrmesas = []
    shrmesas = []
    snpmesas = []

    #Se agrega la pestaña de agregar mesa
    main.add(fgestionmesas, text = gmtitle)
    main.add(feliminaractualizarmesa, text = eamtitle)

    #Se selecciona la pestaña de agregar mesa
    main.select(feliminaractualizarmesa)

    #Se asigna la funcion de volver a la pantalla anterior
    main.bind("<<NotebookTabChanged>>", lambda event: back())

    #Se asigna la funcion de seleccionar lineas de listbox
    lbnmesas.bind("<ButtonRelease-1>", lambda event: selneliminarmesa())
    lbfrmesas.bind("<ButtonRelease-1>", lambda event: selfreliminarmesa())
    lbhrmesas.bind("<ButtonRelease-1>", lambda event: selhreliminarmesa())
    lbnpmesas.bind("<ButtonRelease-1>", lambda event: selnpeliminarmesa())

    #Se muestra la pestaña de menu principal
    main.hide(fwelcome)
    main.hide(factualizarmesa)

    if len(lmesas) > 0:
        #Se organiza la lista de numeros de mesas
        for i in range(len(lmesas)):
            snmesas.append(lmesas[i][0])

        #Se organiza la lista de fechas de reservacion de mesas
        for i in range(len(lmesas)):
            sfrmesas.append(lmesas[i][1])

        #Se organiza la lista de horas de reservacion de mesas
        for i in range(len(lmesas)):
            shrmesas.append(lmesas[i][2])

        #Se organiza la lista de numeros de personas de mesas
        for i in range(len(lmesas)):
            snpmesas.append(lmesas[i][3])

    #Se asigna el listado de numeros de mesas
    lbnmesas.delete(0, END)
    lbnmesas.insert(0, *snmesas)

    #Se asigna el listado de fechas de reservacion de mesas
    lbfrmesas.delete(0, END)
    lbfrmesas.insert(0, *sfrmesas)

    #Se asigna el listado de horas de reservacion de mesas
    lbhrmesas.delete(0, END)
    lbhrmesas.insert(0, *shrmesas)

    #Se asigna el listado de numeros de personas de mesas
    lbnpmesas.delete(0, END)
    lbnpmesas.insert(0, *snpmesas)

#Funcion para la pantalla de actualizar mesa
def actualizarmesa():
    global pstate

    root.title(mrtitle + " - " + mptitle + " / " + gmtitle + " / " + eamtitle + " / " + acmtitle)

    #Condicional para verificar si se selecciono una mesa
    if lbnmesas.curselection() != ():
        #Variable del estado del programa en el valor de actualizar mesa
        pstate = 11

        #Se agrega la pestaña de agregar mesa
        main.add(factualizarmesa, text = acmtitle)

        #Se selecciona la pestaña de agregar mesa
        main.select(factualizarmesa)
        
        #Se limpian los entrys
        eanumeromesa.delete(0, END)
        eafechareservacion.delete(0, END)
        eahorareservacion.delete(0, END)
        eanumeropersonas.delete(0, END)

        #Se asignan los entrys con los valores de la mesa seleccionada
        eanumeromesa.insert(0, lbnmesas.get(lbnmesas.curselection()))
        eafechareservacion.insert(0, lbfrmesas.get(lbfrmesas.curselection()))
        eahorareservacion.insert(0, lbhrmesas.get(lbhrmesas.curselection()))
        eanumeropersonas.insert(0, lbnpmesas.get(lbnpmesas.curselection()))

        #Se asigna la funcion de volver a la pantalla anterior
        main.bind("<<NotebookTabChanged>>", lambda event: back())

        #Se muestra la pestaña de menu principal
        main.hide(fgestionmesas)

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
    bandera = False
    
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
        for i in range(len(lplatos)):
            if lplatos[i][0] == enombreplato.get().lower():
                messagebox.showerror("Error", "El plato ya existe")
                bandera = True
                break

            else:
                bandera = False
        
        if bandera == False:
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
            gestionplatos()

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

    bandera = False

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
        tlplatos.append(eanombreplato.get().lower())
        tlplatos.append(eaprecioplato.get())
        tlplatos.append(eadescripcionplato.get())
        tlplatos.append(eadisponibilidadplato.get().lower())

        for i in range(len(lplatos)):
            if lplatos[i][0] == eanombreplato.get().lower() and lplatos[i] == tlplatos:
                messagebox.showerror("Error", "El plato ya existe")
                bandera = True
                break

            else:
                if bandera == False:
                    for j in range(len(lplatos)):
                        if lplatos[j][0] == eanombreplato.get().lower() and j != lbnplatos.curselection()[0]:
                            messagebox.showerror("Error", "El plato ya existe")
                            bandera = True
                            break
                        else:
                            bandera = False

        if bandera == False:
            lplatos.pop(lbnplatos.curselection()[0])
            lplatos.insert(lbnplatos.curselection()[0], tlplatos)

            #Se guarda la base de datos de platos
            txtplatos = open(plist, "w")
            txtplatos.write(str(lplatos))
            txtplatos.close()

            messagebox.showinfo("Actualizado", "Plato actualizado con exito")

            eliminaractualizarplato()

#Funciones para seleccionar lineas de listbox de platos 
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

#Funcion para agregar mesa
def sagregarmesa():
    global lmesas

    #Lista temporal de mesas
    tlmesas = []

    bandera = False

    #Condicional para verificar si los campos estan vacios
    if enumeromesa.get() == "" or efechareservacion.get() == "" or ehorareservacion.get() == "" or enumeropersonas.get() == "":
        messagebox.showerror("Error", "No se pueden dejar campos vacios")

    #Condicional para verificar si el numero de mesa es un numero
    elif enumeromesa.get().isdigit() == False:
        messagebox.showerror("Error", "El numero de mesa solo puede ser un numero y no puede ser negativo")

    #Condicional para verificar si el numero de personas es un numero
    elif enumeropersonas.get().isdigit() == False:
        messagebox.showerror("Error", "El numero de personas solo puede ser un numero y no puede ser negativo")

    #Condicional para validar fecha y hora
    try:
        #Condicional para verificar que la fecha de reservacion sea valida
        if efechareservacion.get()[2] != "/" and efechareservacion.get()[5] != "/" and efechareservacion.get()[0:2].isdigit() == True and efechareservacion.get()[3:5].isdigit() == True and efechareservacion.get()[6:10].isdigit() == True:
            messagebox.showerror("Error", "La fecha de reservacion debe tener el formato dd/mm/aaaa")

        #Condicional para verificar que la fecha de reservacion sea valida teniendo en cuenta los dias de cada mes
        elif int(efechareservacion.get()[0:2]) > 31 or int(efechareservacion.get()[3:5]) > 12 or int(efechareservacion.get()[6:10]) < 2023 or (int(efechareservacion.get()[3:5]) == 2 and int(efechareservacion.get()[0:2]) > 28) or ((int(efechareservacion.get()[3:5]) == 4 or int(efechareservacion.get()[3:5]) == 6 or int(efechareservacion.get()[3:5]) == 9 or int(efechareservacion.get()[3:5]) == 11) and int(efechareservacion.get()[0:2]) > 30) or int(efechareservacion.get()[0:2]) < 1 or int(efechareservacion.get()[3:5]) < 1 or int(efechareservacion.get()[6:10]) < 1 or (int(efechareservacion.get()[0:2]) <= now.day and int(efechareservacion.get()[3:5]) <= now.month and int(efechareservacion.get()[6:10]) <= now.year):
            messagebox.showerror("Error", "La fecha de reservacion debe ser valida")

        #Condicional para verificar que la hora de reservacion sea valida
        elif ehorareservacion.get()[2] != ":" and ehorareservacion.get()[0:2].isdigit() == True and ehorareservacion.get()[3:5].isdigit() == True:
            messagebox.showerror("Error", "La hora de reservacion debe tener el formato hh:mm")

        #Condicional para verificar que la hora de reservacion sea valida teniendo en cuenta los minutos
        elif int(ehorareservacion.get()[0:2]) > 23 or int(ehorareservacion.get()[3:5]) > 59 or int(ehorareservacion.get()[0:2]) < 0 or int(ehorareservacion.get()[3:5]) < 0:
            messagebox.showerror("Error", "La hora de reservacion debe ser valida")

        else:
            #Condicional para verificar si la reservacion de la mesa ya existe
            for i in range(len(lmesas)):
                if lmesas[i][0] == enumeromesa.get():
                    messagebox.showerror("Error", "La mesa ya esta reservada")
                    bandera = True
                    break
                    
                else:
                    bandera = False

            #Excepcion para cuando la reservacion de la mesa no existe
            if bandera == False:
                #Se agrega la mesa a la base de datos
                tlmesas.append(enumeromesa.get())
                tlmesas.append(efechareservacion.get())
                tlmesas.append(ehorareservacion.get())
                tlmesas.append(enumeropersonas.get())

                lmesas.append(tlmesas)

                #Se guarda la base de datos de mesas
                txtmesas = open(mlist, "w")
                txtmesas.write(str(lmesas))
                txtmesas.close()

                messagebox.showinfo("Agregado", "Mesa agregada con exito")
                gestionmesas()

    #Excepcion para cuando la fecha o la hora de reservacion no tienen el formato correcto
    except IndexError:
        messagebox.showerror("Error", "La fecha o la hora de reservacion no tienen el formato correcto")

#Funcion para eliminar mesa
def seliminarmesa():
    #Condicional para verificar si se selecciono una mesa
    if lbnmesas.curselection() != ():
        #Se elimina la mesa de la base de datos
        lmesas.pop(lbnmesas.curselection()[0])

        #Se eliminan las mesas de los listbox
        lbnmesas.delete(lbnmesas.curselection())
        lbfrmesas.delete(lbfrmesas.curselection())
        lbhrmesas.delete(lbhrmesas.curselection())
        lbnpmesas.delete(lbnpmesas.curselection())

        #Se guarda la base de datos de mesas
        txtmesas = open(mlist, "w")
        txtmesas.write(str(lmesas))
        txtmesas.close()

        messagebox.showinfo("Eliminado", "Mesa eliminada con exito")

#Funcion para actualizar mesa
def sactualizarmesa():
    global lmesas

    #Lista temporal de mesas
    tlmesas = []

    bandera = False

    #Condicional para verificar si los campos estan vacios
    if eanumeromesa.get() == "" or eafechareservacion.get() == "" or eahorareservacion.get() == "" or eanumeropersonas.get() == "":
        messagebox.showerror("Error", "No se pueden dejar campos vacios")

    #Condicional para verificar si el numero de mesa es un numero
    elif eanumeromesa.get().isdigit() == False:
        messagebox.showerror("Error", "El numero de mesa solo puede ser un numero y no puede ser negativo")

    #Condicional para verificar si el numero de personas es un numero
    elif eanumeropersonas.get().isdigit() == False:
        messagebox.showerror("Error", "El numero de personas solo puede ser un numero y no puede ser negativo")

    #Condicional para validar fecha y hora
    try:
        #Condicional para verificar que la fecha de reservacion sea valida
        if eafechareservacion.get()[2] != "/" and eafechareservacion.get()[5] != "/" and eafechareservacion.get()[0:2].isdigit() == True and eafechareservacion.get()[3:5].isdigit() == True and eafechareservacion.get()[6:10].isdigit() == True:
            messagebox.showerror("Error", "La fecha de reservacion debe tener el formato dd/mm/aaaa")

        #Condicional para verificar que la fecha de reservacion sea valida teniendo en cuenta los dias de cada mes
        elif int(eafechareservacion.get()[0:2]) > 31 or int(eafechareservacion.get()[3:5]) > 12 or int(eafechareservacion.get()[6:10]) < 2023 or (int(eafechareservacion.get()[3:5]) == 2 and int(eafechareservacion.get()[0:2]) > 28) or ((int(eafechareservacion.get()[3:5]) == 4 or int(eafechareservacion.get()[3:5]) == 6 or int(eafechareservacion.get()[3:5]) == 9 or int(eafechareservacion.get()[3:5]) == 11) and int(eafechareservacion.get()[0:2]) > 30) or int(eafechareservacion.get()[0:2]) < 0 or int(eafechareservacion.get()[3:5]) < 0 or int(eafechareservacion.get()[6:10]) < 0 or (int(eafechareservacion.get()[0:2]) <= now.day and int(eafechareservacion.get()[3:5]) <= now.month and int(eafechareservacion.get()[6:10]) <= now.year):
            messagebox.showerror("Error", "La fecha de reservacion debe ser valida")

        #Condicional para verificar que la hora de reservacion sea valida
        elif eahorareservacion.get()[2] != ":" and eahorareservacion.get()[0:2].isdigit() == True and eahorareservacion.get()[3:5].isdigit() == True:
            messagebox.showerror("Error", "La hora de reservacion debe tener el formato hh:mm")

        #Condicional para verificar que la hora de reservacion sea valida teniendo en cuenta los minutos
        elif int(eahorareservacion.get()[0:2]) > 23 or int(eahorareservacion.get()[3:5]) > 59 or int(eahorareservacion.get()[0:2]) < 0 or int(eahorareservacion.get()[3:5]) < 0:
            messagebox.showerror("Error", "La hora de reservacion debe ser valida")

        else:
            #Condicional para verificar si la reservacion de la mesa ya existe
            tlmesas.append(eanumeromesa.get())
            tlmesas.append(eafechareservacion.get())
            tlmesas.append(eahorareservacion.get())
            tlmesas.append(eanumeropersonas.get())

            for i in range(len(lmesas)):
                if lmesas[i][0] == eanumeromesa.get() and lmesas[i] == tlmesas:
                    messagebox.showerror("Error", "La mesa ya esta reservada")
                    bandera = True
                    break
                
                else:
                    if bandera == False:
                        for j in range(len(lmesas)):
                            if lmesas[j][0] == eanumeromesa.get() and j != lbnmesas.curselection()[0]:
                                messagebox.showerror("Error", "La mesa ya esta reservada")
                                bandera = True
                                break
                            else:
                                bandera = False

            if bandera == False:
                lmesas.pop(lbnmesas.curselection()[0])
                lmesas.insert(lbnmesas.curselection()[0], tlmesas)

                #Se guarda la base de datos de mesas
                txtmesas = open(mlist, "w")
                txtmesas.write(str(lmesas))
                txtmesas.close()

                messagebox.showinfo("Actualizado", "Mesa actualizada con exito")

                eliminaractualizarmesa()

    #Excepcion para cuando la fecha o la hora de reservacion no tienen el formato correcto
    except IndexError:
        messagebox.showerror("Error", "La fecha o la hora de reservacion no tienen el formato correcto")

#Funciones para seleccionar lineas de listbox de mesas
def selneliminarmesa():
    lbfrmesas.selection_clear(0, END)
    lbhrmesas.selection_clear(0, END)
    lbnpmesas.selection_clear(0, END)

    lbfrmesas.selection_set(lbnmesas.curselection())
    lbhrmesas.selection_set(lbnmesas.curselection())
    lbnpmesas.selection_set(lbnmesas.curselection())

def selfreliminarmesa():
    lbnmesas.selection_clear(0, END)
    lbhrmesas.selection_clear(0, END)
    lbnpmesas.selection_clear(0, END)

    lbnmesas.selection_set(lbfrmesas.curselection())
    lbhrmesas.selection_set(lbfrmesas.curselection())
    lbnpmesas.selection_set(lbfrmesas.curselection())

def selhreliminarmesa():
    lbnmesas.selection_clear(0, END)
    lbfrmesas.selection_clear(0, END)
    lbnpmesas.selection_clear(0, END)

    lbnmesas.selection_set(lbhrmesas.curselection())
    lbfrmesas.selection_set(lbhrmesas.curselection())
    lbnpmesas.selection_set(lbhrmesas.curselection())

def selnpeliminarmesa():
    lbnmesas.selection_clear(0, END)
    lbfrmesas.selection_clear(0, END)
    lbhrmesas.selection_clear(0, END)

    lbnmesas.selection_set(lbnpmesas.curselection())
    lbfrmesas.selection_set(lbnpmesas.curselection())
    lbhrmesas.selection_set(lbnpmesas.curselection())

#Funcion para volver a la pantalla anterior
def back():
    global pstate

    #Condicional para volver a la pantalla principal
    if pstate == 1:
        #Variable del estado del programa en el valor de pagina principal
        pstate = 0

        root.title(mrtitle)

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
        main.hide(fgestionmesas)
        main.hide(fagregarmesa)
        main.hide(feliminaractualizarmesa)
        main.hide(factualizarmesa)
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

    #Condicional para volver a la pantalla de menu principal
    elif pstate == 8:
        #Se reinician los entrys
        enumeromesa.delete(0, END)
        efechareservacion.delete(0, END)
        ehorareservacion.delete(0, END)
        enumeropersonas.delete(0, END)

        #Se vuelve a la pantalla de menu principal
        gestionmesas()
        pstate = 3

    #Condicional para volver a la pantalla de gestion de mesas
    elif pstate == 9:
        pstate = 8

    elif pstate == 10:
        #Se vuelve a la pantalla de eliminar o actualizar mesas
        eliminaractualizarmesa()
        pstate = 8

    #Condicional para volver a la pantalla de eliminar o actualizar mesas
    elif pstate == 11:
        pstate = 10

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
    bregist = Button(fmainmenu, text = rtitle, font = (ftitle, int(fsize / 2), "bold"), command = regist, height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

    #Se crea el boton de login de la pantalla principal
    blogin = Button(fmainmenu, text = ltitle, font = (ftitle, int(fsize / 2), "bold"), command = login, height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

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
    bslogin = Button(fltext, text = ltitle, command = slogin, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.002), width = int(ssize[0] * 0.009))

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
    bsregist = Button(frtext, text = rtitle, command = sregist, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.002), width = int(ssize[0] * 0.009))

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
    bwgestionplatos = Button(fwtext, text = gptitle, command = gestionplatos, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

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
    lgestionplatos = Label(fgptext, text = gptitle, font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el boton de agregar plato
    bgpagregarplato = Button(fgptext, text = aptitle, command = agregarplato, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

    #Se crea el boton de eliminar o actualizar plato
    bgpeliminaractualizarplato = Button(fgptext, text = eaptitle, command = eliminaractualizarplato, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

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
    lagregarplato = Label(faptext, text = aptitle, font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

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
    bagregarplato = Button(faptext, text = aptitle, command = sagregarplato, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.001), width = int(ssize[0] * 0.01))

#Funcion para definir la pantalla de eliminar o actualizar plato
def peliminaractualizarplato():
    global logosmall, feliminaractualizarplato, lieliminaractualizarplatotitle, leliminaractualizarplatotitle, feaptext, leliminaractualizarplato, beliminarplato, bactualizarplato, lbnplatos, lbpplatos, lbdesplatos, lbdplatos, lnplatos, lpplatos, ldesplatos, ldplatos

    #Se crea la pantalla de eliminar o actualizar plato
    feliminaractualizarplato = Frame(main, bg = bgcolor)

    #Se crea el logo de la pantalla de eliminar o actualizar plato
    logosmall = ImageTk.PhotoImage(ico.resize((int(ssize[0] * 0.05), int(ssize[0] * 0.05 * logoar))))
    lieliminaractualizarplatotitle = Label(feliminaractualizarplato, image = logosmall, bg = bgcolor)

    #Se crea el frame de titulo de la pantalla de eliminar o actualizar plato
    leliminaractualizarplatotitle = Label(feliminaractualizarplato, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    #Se crea el boton de eliminar plato
    beliminarplato = Button(feliminaractualizarplato, bg = "red", text = "Eliminar plato", command = seliminarplato, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.001), width = int(ssize[0] * 0.01))

    #Se crea el boton de actualizar plato
    bactualizarplato = Button(feliminaractualizarplato, text = acptitle, command = actualizarplato, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.001), width = int(ssize[0] * 0.01))

    #Se crea el frame de ubicacion de los elementos de la pantalla de eliminar o actualizar plato
    feaptext = Frame(feliminaractualizarplato, bg = bgcolor)

    #Se crea el label de eliminar o actualizar plato
    leliminaractualizarplato = Label(feaptext, text = "Platos", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea label del listbox de nombre de platos
    lnplatos = Label(feaptext, text = "Nombre", font = (ftitle, int(fsize / 3), "bold"), relief = "raised")

    #Se crea el listbox del nombre de los platos
    lbnplatos = Listbox(feaptext, exportselection = 0,font = (ftitle, int(fsize / 3), "bold"))

    #Se crea label del listbox de precio de platos
    lpplatos = Label(feaptext, text = "Precio", font = (ftitle, int(fsize / 3), "bold"), relief = "raised")

    #Se crea el listbox del precio de los platos
    lbpplatos = Listbox(feaptext, exportselection = 0, font = (ftitle, int(fsize / 3), "bold"))

    #Se crea label del listbox de descripcion de platos
    ldesplatos = Label(feaptext, text = "Descripcion", font = (ftitle, int(fsize / 3), "bold"), relief = "raised")

    #Se crea el listbox de la descripcion de los platos
    lbdesplatos = Listbox(feaptext, exportselection = 0, font = (ftitle, int(fsize / 3), "bold"))

    #Se crea label del listbox de disponibilidad de platos
    ldplatos = Label(feaptext, text = "Disponibilidad", font = (ftitle, int(fsize / 3), "bold"), relief = "raised")

    #Se crea el listbox de la disponibilidad de los platos
    lbdplatos = Listbox(feaptext, exportselection = 0, font = (ftitle, int(fsize / 3), "bold"))

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
    lactualizarplato = Label(facptext, text = acptitle, font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

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
    baactualizarplato = Button(facptext, text = acptitle, command = sactualizarplato, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.001), width = int(ssize[0] * 0.01))

#Funcion para definir la pantalla de gestion de mesas
def pgestionmesas():
    global fgestionmesas, ftlgmspace, ftcgmspace, ftrgmspace, lgestionmesastitle, ligestionmesastitle, fgmtext, lgestionmesas, bgmagregarmesa, bgmeliminaractualizarmesa

    #Se crea la pantalla de gestion de mesas
    fgestionmesas = Frame(main, bg = bgcolor)

    #Se crea el frame de espacio superior izquierdo de la pantalla de gestion de mesas
    ftlgmspace = Frame(fgestionmesas, width = ssize[0] * 0.11, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el titulo de la pantalla de gestion de mesas
    lgestionmesastitle = Label(fgestionmesas, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    #Se crea el logo de la pantalla de gestion de mesas
    ligestionmesastitle = Label(fgestionmesas, image = logo, bg = bgcolor)

    #Se crea el frame de espacio superior central de la pantalla de gestion de mesas
    ftcgmspace = Frame(fgestionmesas, width = ssize[0] * 0.11, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de espacio superior derecho de la pantalla de gestion de mesas
    ftrgmspace = Frame(fgestionmesas, width = ssize[0] * 0.16, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de ubicacion de los elementos de la pantalla de gestion de mesas
    fgmtext = Frame(fgestionmesas, bg = bgcolor)

    #Se crea el label de gestion de mesas
    lgestionmesas = Label(fgmtext, text = "Gestion de mesas", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el boton de agregar mesa
    bgmagregarmesa = Button(fgmtext, text = "Agregar mesa", command = agregarmesa, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

    #Se crea el boton de eliminar o actualizar mesa
    bgmeliminaractualizarmesa = Button(fgmtext, text = "Eliminar o actualizar mesa", command = eliminaractualizarmesa, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

#Funcion para definir la pantalla de agregar mesa
def pagregarmesa():
    global fagregarmesa, ftlagmspace, lagregarmesatitle, liagregarmesatitle, ftcagmspace, ftragmspace, fagmtext, lagregarmesa, lnumeromesa, enumeromesa, lfechareservacion, efechareservacion, lhorareservacion, ehorareservacion, lnumeropersonas, enumeropersonas, bagregarmesa

    #Se crea la pantalla de agregar mesa
    fagregarmesa = Frame(main, bg = bgcolor)

    #Se crea el frame de espacio superior izquierdo de la pantalla de agregar mesa
    ftlagmspace = Frame(fagregarmesa, width = ssize[0] * 0.11, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el titulo de la pantalla de agregar mesa
    lagregarmesatitle = Label(fagregarmesa, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    #Se crea el logo de la pantalla de agregar mesa
    liagregarmesatitle = Label(fagregarmesa, image = logo, bg = bgcolor)

    #Se crea el frame de espacio superior central de la pantalla de agregar mesa
    ftcagmspace = Frame(fagregarmesa, width = ssize[0] * 0.11, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de espacio superior derecho de la pantalla de agregar mesa
    ftragmspace = Frame(fagregarmesa, width = ssize[0] * 0.16, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de ubicacion de los elementos de la pantalla de agregar mesa
    fagmtext = Frame(fagregarmesa, bg = bgcolor)

    #Se crea el label de agregar mesa
    lagregarmesa = Label(fagmtext, text = "Agregar mesa", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea label de numero de mesa
    lnumeromesa = Label(fagmtext, text = "Numero de mesa", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de numero de mesa
    enumeromesa = Entry(fagmtext, font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.04))

    #Se crea el label de fecha de la reservacion
    lfechareservacion = Label(fagmtext, text = "Fecha de la reservacion: dd/mm/aaaa", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de fecha de la reservacion
    efechareservacion = Entry(fagmtext, font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.04))

    #Se crea el label de hora de la reservacion
    lhorareservacion = Label(fagmtext, text = "Hora de la reservacion: hh:mm", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de hora de la reservacion
    ehorareservacion = Entry(fagmtext, font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.04))

    #Se crea el label de numero de personas
    lnumeropersonas = Label(fagmtext, text = "Numero de personas", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de numero de personas
    enumeropersonas = Entry(fagmtext, font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.04))

    #Se crea el boton de agregar mesa
    bagregarmesa = Button(fagmtext, text = "Agregar mesa", command = sagregarmesa, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.001), width = int(ssize[0] * 0.01))

#Funcion para definir la pantalla de eliminar o actualizar mesa
def peliminaractualizarmesa():
    global feliminaractualizarmesa, lieliminaractualizarmesatitle, leliminaractualizarmesatitle, feamtext, leliminaractualizarmesa, beliminarmesa, bactualizarmesa, lbnmesas, lbfrmesas, lbhrmesas, lbnpmesas, lnmesas, lfrmesas, lhrmesas, lnpmesas

    #Se crea la pantalla de eliminar o actualizar mesa
    feliminaractualizarmesa = Frame(main, bg = bgcolor)

    #Se crea el logo de la pantalla de eliminar o actualizar mesa
    lieliminaractualizarmesatitle = Label(feliminaractualizarmesa, image = logosmall, bg = bgcolor)

    #Se crea el frame de titulo de la pantalla de eliminar o actualizar mesa
    leliminaractualizarmesatitle = Label(feliminaractualizarmesa, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    #Se crea el boton de eliminar mesa
    beliminarmesa = Button(feliminaractualizarmesa, bg = "red", text = "Eliminar mesa", command = seliminarmesa, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.001), width = int(ssize[0] * 0.01))

    #Se crea el boton de actualizar mesa
    bactualizarmesa = Button(feliminaractualizarmesa, text = acmtitle, command = actualizarmesa, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.001), width = int(ssize[0] * 0.01))

    #Se crea el frame de ubicacion de los elementos de la pantalla de eliminar o actualizar mesa
    feamtext = Frame(feliminaractualizarmesa, bg = bgcolor)

    #Se crea el label de eliminar o actualizar mesa
    leliminaractualizarmesa = Label(feamtext, text = "Mesas", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea label del listbox de numero de mesas
    lnmesas = Label(feamtext, text = "Numero", font = (ftitle, int(fsize / 3), "bold"), relief = "raised")

    #Se crea el listbox del numero de las mesas
    lbnmesas = Listbox(feamtext, exportselection = 0,font = (ftitle, int(fsize / 3), "bold"))

    #Se crea label del listbox de fecha de reservacion de mesas
    lfrmesas = Label(feamtext, text = "Fecha de reservacion", font = (ftitle, int(fsize / 3), "bold"), relief = "raised")

    #Se crea el listbox de la fecha de reservacion de las mesas
    lbfrmesas = Listbox(feamtext, exportselection = 0, font = (ftitle, int(fsize / 3), "bold"))

    #Se crea label del listbox de hora de reservacion de mesas
    lhrmesas = Label(feamtext, text = "Hora de reservacion", font = (ftitle, int(fsize / 3), "bold"), relief = "raised")

    #Se crea el listbox de la hora de reservacion de las mesas
    lbhrmesas = Listbox(feamtext, exportselection = 0, font = (ftitle, int(fsize / 3), "bold"))

    #Se crea label del listbox de numero de personas de mesas
    lnpmesas = Label(feamtext, text = "Numero de personas", font = (ftitle, int(fsize / 3), "bold"), relief = "raised")

    #Se crea el listbox del numero de personas de las mesas
    lbnpmesas = Listbox(feamtext, exportselection = 0, font = (ftitle, int(fsize / 3), "bold"))

#Funcion para definir la pantalla de actualizar mesa
def pactualizarmesa():
    global factualizarmesa, ftlacmspace, lactualizarmesatitle, liactualizarmesatitle, ftcacmspace, ftracmspace, facmtext, lactualizarmesa, lanumeromesa, eanumeromesa, lafechareservacion, eafechareservacion, lahorareservacion, eahorareservacion, lanumeropersonas, eanumeropersonas, baactualizarmesa

    #Se crea la pantalla de actualizar mesa
    factualizarmesa = Frame(main, bg = bgcolor)

    #Se crea el frame de espacio superior izquierdo de la pantalla de actualizar mesa
    ftlacmspace = Frame(factualizarmesa, width = ssize[0] * 0.11, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el titulo de la pantalla de actualizar mesa
    lactualizarmesatitle = Label(factualizarmesa, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    #Se crea el logo de la pantalla de actualizar mesa
    liactualizarmesatitle = Label(factualizarmesa, image = logo, bg = bgcolor)

    #Se crea el frame de espacio superior central de la pantalla de actualizar mesa
    ftcacmspace = Frame(factualizarmesa, width = ssize[0] * 0.11, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de espacio superior derecho de la pantalla de actualizar mesa
    ftracmspace = Frame(factualizarmesa, width = ssize[0] * 0.16, height = ssize[0] * 0.05, bg = bgcolor)

    #Se crea el frame de ubicacion de los elementos de la pantalla de actualizar mesa
    facmtext = Frame(factualizarmesa, bg = bgcolor)

    #Se crea el label de actualizar mesa
    lactualizarmesa = Label(facmtext, text = acmtitle, font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea label de numero de mesa
    lanumeromesa = Label(facmtext, text = "Numero de mesa", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de numero de mesa
    eanumeromesa = Entry(facmtext, font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.04))

    #Se crea el label de fecha de la reservacion
    lafechareservacion = Label(facmtext, text = "Fecha de la reservacion: dd/mm/aaaa", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de fecha de la reservacion
    eafechareservacion = Entry(facmtext, font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.04))

    #Se crea el label de hora de la reservacion
    lahorareservacion = Label(facmtext, text = "Hora de la reservacion: hh:mm", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de hora de la reservacion
    eahorareservacion = Entry(facmtext, font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.04))

    #Se crea el label de numero de personas
    lanumeropersonas = Label(facmtext, text = "Numero de personas", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    #Se crea el entry de numero de personas
    eanumeropersonas = Entry(facmtext, font = (ftitle, int(fsize / 3), "bold"), width = int(ssize[0] * 0.04))

    #Se crea el boton de actualizar mesa
    baactualizarmesa = Button(facmtext, text = acmtitle, command = sactualizarmesa, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.001), width = int(ssize[0] * 0.01))

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
    feaptext.grid(row = 1, column = 0, columnspan = 4)

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

#Funcion para posicionar la pantalla de gestion de mesas
def posgestionmesas():
    #Posicionamiento del frame de espacio superior izquierdo de la pantalla de gestion de mesas
    ftlgmspace.grid(row = 0, column = 0)

    #Posicionamiento del titulo de la pantalla de gestion de mesas
    lgestionmesastitle.grid(row = 1, column = 1)

    #Posicionamiento del logo de la pantalla de gestion de mesas
    ligestionmesastitle.grid(row = 2, column = 1)

    #Posicionamiento del frame de espacio superior central de la pantalla de gestion de mesas
    ftcgmspace.grid(row = 0, column = 2)

    #Posicionamiento del frame de ubicacion de los elementos de la pantalla de gestion de mesas
    fgmtext.grid(row = 2, column = 3)

    #Posicionamiento del label de gestion de mesas
    lgestionmesas.grid(row = 0, column = 0)

    #Posicionamiento del boton de agregar mesa
    bgmagregarmesa.grid(row = 1, column = 0)

    #Posicionamiento del boton de eliminar o actualizar mesa
    bgmeliminaractualizarmesa.grid(row = 2, column = 0)

    #Posicionamiento del frame de espacio superior derecho de la pantalla de gestion de mesas
    ftrgmspace.grid(row = 0, column = 4)

#Funcion para posicionar la pantalla de agregar mesa
def posagregarmesa():
    #Posicionamiento del frame de espacio superior izquierdo de la pantalla de agregar mesa
    ftlagmspace.grid(row = 0, column = 0)

    #Posicionamiento del titulo de la pantalla de agregar mesa
    lagregarmesatitle.grid(row = 1, column = 1)

    #Posicionamiento del logo de la pantalla de agregar mesa
    liagregarmesatitle.grid(row = 2, column = 1)

    #Posicionamiento del frame de espacio superior central de la pantalla de agregar mesa
    ftcagmspace.grid(row = 0, column = 2)

    #Posicionamiento del frame de ubicacion de los elementos de la pantalla de agregar mesa
    fagmtext.grid(row = 2, column = 3)

    #Posicionamiento del label de agregar mesa
    lagregarmesa.grid(row = 0, column = 0)

    #Posicionamiento del label de numero de mesa
    lnumeromesa.grid(row = 1, column = 0)

    #Posicionamiento del entry de numero de mesa
    enumeromesa.grid(row = 2, column = 0)

    #Posicionamiento del label de fecha de la reservacion
    lfechareservacion.grid(row = 3, column = 0)

    #Posicionamiento del entry de fecha de la reservacion
    efechareservacion.grid(row = 4, column = 0)

    #Posicionamiento del label de hora de la reservacion
    lhorareservacion.grid(row = 5, column = 0)

    #Posicionamiento del entry de hora de la reservacion
    ehorareservacion.grid(row = 6, column = 0)

    #Posicionamiento del label de numero de personas
    lnumeropersonas.grid(row = 7, column = 0)

    #Posicionamiento del entry de numero de personas
    enumeropersonas.grid(row = 8, column = 0)

    #Posicionamiento del boton de agregar mesa
    bagregarmesa.grid(row = 9, column = 0)

#Funcion para posicionar la pantalla de eliminar o actualizar mesa
def poseliminaractualizarmesa():
    #Posicionamiento del logo de la pantalla de eliminar o actualizar mesa
    lieliminaractualizarmesatitle.grid(row = 0, column = 0)

    #Posicionamiento del titulo de la pantalla de eliminar o actualizar mesa
    leliminaractualizarmesatitle.grid(row = 0, column = 1)

    #Posicionamiento del boton de eliminar mesa
    beliminarmesa.grid(row = 0, column = 2, padx = (int(ssize[0] * 0.4), 0))

    #Posicionamiento del boton de actualizar mesa
    bactualizarmesa.grid(row = 0, column = 3)

    #Posicionamiento del frame de ubicacion de los elementos de la pantalla de eliminar o actualizar mesa
    feamtext.grid(row = 1, column = 0, columnspan = 4)

    #Posicionamiento del label de eliminar o actualizar mesa
    leliminaractualizarmesa.grid(row = 0, column = 0, columnspan = 4)

    #Posicionamiento del label del listbox de numero de mesas
    lnmesas.grid(row = 1, column = 0)

    #Posicionamiento del listbox del numero de las mesas
    lbnmesas.grid(row = 2, column = 0)

    #Posicionamiento del label del listbox de fecha de reservacion de mesas
    lfrmesas.grid(row = 1, column = 1)

    #Posicionamiento del listbox de la fecha de reservacion de las mesas
    lbfrmesas.grid(row = 2, column = 1)

    #Posicionamiento del label del listbox de hora de reservacion de mesas
    lhrmesas.grid(row = 1, column = 2)

    #Posicionamiento del listbox de la hora de reservacion de las mesas
    lbhrmesas.grid(row = 2, column = 2)

    #Posicionamiento del label del listbox de numero de personas de mesas
    lnpmesas.grid(row = 1, column = 3)

    #Posicionamiento del listbox del numero de personas de las mesas
    lbnpmesas.grid(row = 2, column = 3)

#Funcion para posicionar la pantalla de actualizar mesa
def posactualizarmesa():
    #Posicionamiento del frame de espacio superior izquierdo de la pantalla de actualizar mesa
    ftlacmspace.grid(row = 0, column = 0)

    #Posicionamiento del titulo de la pantalla de actualizar mesa
    lactualizarmesatitle.grid(row = 1, column = 1)

    #Posicionamiento del logo de la pantalla de actualizar mesa
    liactualizarmesatitle.grid(row = 2, column = 1)

    #Posicionamiento del frame de espacio superior central de la pantalla de actualizar mesa
    ftcacmspace.grid(row = 0, column = 2)

    #Posicionamiento del frame de ubicacion de los elementos de la pantalla de actualizar mesa
    facmtext.grid(row = 2, column = 3)

    #Posicionamiento del label de actualizar mesa
    lactualizarmesa.grid(row = 0, column = 0)

    #Posicionamiento del label de numero de mesa
    lanumeromesa.grid(row = 1, column = 0)

    #Posicionamiento del entry de numero de mesa
    eanumeromesa.grid(row = 2, column = 0)

    #Posicionamiento del label de fecha de la reservacion
    lafechareservacion.grid(row = 3, column = 0)

    #Posicionamiento del entry de fecha de la reservacion
    eafechareservacion.grid(row = 4, column = 0)

    #Posicionamiento del label de hora de la reservacion
    lahorareservacion.grid(row = 5, column = 0)

    #Posicionamiento del entry de hora de la reservacion
    eahorareservacion.grid(row = 6, column = 0)

    #Posicionamiento del label de numero de personas
    lanumeropersonas.grid(row = 7, column = 0)

    #Posicionamiento del entry de numero de personas
    eanumeropersonas.grid(row = 8, column = 0)

    #Posicionamiento del boton de actualizar mesa
    baactualizarmesa.grid(row = 9, column = 0)

    #Posicionamiento del frame de espacio superior derecho de la pantalla de actualizar mesa
    ftracmspace.grid(row = 0, column = 4)

#Funcion para posicionar las pestañas
def pospestañas():
    #Se agregan las pestañas
    main.add(finicio, text = ititle)
    main.add(flogin, text = ltitle)
    main.add(fregist, text = rtitle)
    main.add(fwelcome, text = mptitle)
    main.add(fgestionplatos, text = gptitle)
    main.add(fagregarplato, text = aptitle)
    main.add(feliminaractualizarplato, text = eaptitle)
    main.add(factualizarplato, text = acptitle)
    main.add(fgestionmesas, text = gmtitle)
    main.add(fagregarmesa, text = amtitle)
    main.add(feliminaractualizarmesa, text = eamtitle)
    main.add(factualizarmesa, text = acmtitle)
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

    #GESTION DE MESAS
    pgestionmesas()

    #AGREGAR MESA
    pagregarmesa()

    #ELIMINAR O ACTUALIZAR MESA
    peliminaractualizarmesa()

    #ACTUALIZAR MESA
    pactualizarmesa()

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

    #Posicionamiento de la pantalla de gestion de mesas
    posgestionmesas()

    #Posicionamiento de la pantalla de agregar mesa
    posagregarmesa()

    #Posicionamiento de la pantalla de eliminar o actualizar mesa
    poseliminaractualizarmesa()

    #Posicionamiento de la pantalla de actualizar mesa
    posactualizarmesa()

    #Bucle de la ventana
    root.mainloop()

#Ejecucion del programa
if __name__ == "__main__":
    run()
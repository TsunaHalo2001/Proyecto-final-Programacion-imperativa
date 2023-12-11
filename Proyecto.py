import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import numpy as np
import hashlib

import sv_ttk

pstate = 0

mrtitle = "My restaurant"
ftitle = "MS Sans Serif"
fctitle = "#505050"
logoar = 567 / 487
bgcolor = "#DCDCDC"
mydescription = "\nYa sea que busques un almuerzo casual con\namigos, una cena romántica o un evento\nespecial, nuestro restaurante\npromete una experiencia que cautivará tu\npaladar y creará recuerdos duraderos.\n"
bwregist = 37 / 1366

txtloginlist = open("txt/tloginlist.txt", "r")
loginlist = txtloginlist.read()
txtloginlist.close()
loginlist = loginlist.replace(" ", "")
loginlist = loginlist.replace("'", "")
loginlist = loginlist.replace("],[", "/")
loginlist = loginlist.replace("]]", "")
loginlist = loginlist.replace("[[", "")
lloginlist = loginlist.split("/")

for i in range(len(lloginlist)):
    lloginlist[i] = lloginlist[i].split(",")

emaildb = ["@correounivalle.edu.co","@gmail.com", "@hotmail.com", "@outlook.com", "@yahoo.com", "@icloud.com", "@live.com", "@msn.com", "@aol.com", "@yandex.com", "@protonmail.com", "@zoho.com", "@gmx.com", "@mail.com", "@yopmail.com", "@tutanota.com", "@mail.ru", "@gmx.us", "@gmx.de", "@gmx.fr", "@gmx.at", "@gmx.ch", "@gmx.net", "@gmx.co.uk", "@gmx.com.mx", "@gmx.es", "@gmx.eu", "@gmx.it", "@gmx.com.br", "@gmx.com.ar", "@gmx.com.co", "@gmx.com.ve", "@gmx.com.pe", "@gmx.com.ec", "@gmx.com.bo", "@gmx.com.py", "@gmx.com.uy", "@gmx.com.pa", "@gmx.com.do", "@gmx.com.gt", "@gmx.com.sv", "@gmx.com.hn", "@gmx.com.ni", "@gmx.com.cr", "@gmx.com.cu", "@gmx.com.pr", "@gmx.com.jm", "@gmx.com.bb", "@gmx.com.ag", "@gmx.com.dm", "@gmx.com.vc", "@gmx.com.lc", "@gmx.com.gy", "@gmx.com.sr", "@gmx.com.bo", "@gmx.com.py", "@gmx.com.uy", "@gmx.com.ar", "@gmx.com.co", "@gmx.com.ve", "@gmx.com.pe", "@gmx.com.ec", "@gmx.com.bo", "@gmx.com.py", "@gmx.com.uy", "@gmx.com.pa", "@gmx.com.do", "@gmx.com.gt", "@gmx.com.sv", "@gmx.com.hn", "@gmx.com.ni", "@gmx.com.cr", "@gmx.com.cu", "@gmx.com.pr", "@gmx.com.jm", "@gmx.com.bb", "@gmx.com.ag", "@gmx.com.dm", "@gmx.com.vc", "@gmx.com.lc", "@gmx.com.gy", "@gmx.com.sr", "@gmx.com.bo", "@gmx.com.py", "@gmx.com.uy"]

def back():
    global main, fmainmenu, finicio, flogin, fregist, pstate

    if pstate == 1:
        pstate = 0

        main.grid_remove()
        fmainmenu.grid(row = 0, column = 0)

def regist():
    global main, fmainmenu, finicio, flogin, fregist, pstate

    pstate = 1

    fmainmenu.grid_remove()
    main.grid(row = 0, column = 0)

    main.add(finicio, text = "Inicio")
    main.add(fregist, text = "Registrarse")
    main.add(flogin, text = "Iniciar sesion")
    main.select(fregist)
    main.bind("<<NotebookTabChanged>>", lambda event: back())
    main.forget(flogin)

def login():
    global main, fmainmenu, finicio, flogin ,fregist, pstate

    pstate = 1

    fmainmenu.grid_remove()
    main.grid(row = 0, column = 0)

    main.add(finicio, text = "Inicio")
    main.add(flogin, text = "Iniciar sesion")
    main.add(fregist, text = "Registrarse")
    main.select(flogin)
    main.bind("<<NotebookTabChanged>>", lambda event: back())
    main.forget(fregist)

def welcome():
    global main, fwelcome, pstate

    pstate = 2

    main.add(fwelcome, text = "Menu principal")
    main.select(fwelcome)
    main.bind("<<NotebookTabChanged>>", lambda event: back())
    main.forget(flogin)

def slogin():
    global main, finicio, flogin, pstate, lloginlist, eluser, elpassword

    tloginlist = []

    if elpassword.get() == "" or eluser.get() == "":
        messagebox.showerror("Error", "No se pueden dejar campos vacios")

    else:
        try:
            tloginlist.append(hashlib.sha256(eluser.get().lower().encode()).hexdigest())
            tloginlist.append(hashlib.sha256(elpassword.get().encode()).hexdigest())

            lloginlist.index(tloginlist)

            messagebox.showinfo("Iniciado", "Sesion iniciada con exito")
            
            welcome()

        except ValueError:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def sregist():
    global main, finicio, fregist, pstate, lloginlist, eruser, erpassword, ercpassword

    tloginlist = []

    if erpassword.get() == "" or eruser.get() == "" or ercpassword.get() == "":
        messagebox.showerror("Error", "No se pueden dejar campos vacios")

    elif eruser.get().count("@") != 1 or eruser.get()[eruser.get().index("@"):] not in emaildb:
        messagebox.showerror("Error", "Correo invalido")

    elif erpassword.get() == ercpassword.get():
        try:
            erpassword.get().index(" ")
            ercpassword.get().index(" ")
            eruser.get().index(" ")
            messagebox.showerror("Error", "No se pueden usar espacios en los campos")

        except ValueError:
            tloginlist.append(hashlib.sha256(eruser.get().lower().encode()).hexdigest())
            tloginlist.append(hashlib.sha256(erpassword.get().encode()).hexdigest())

            try:
                lloginlist.index(tloginlist)
                messagebox.showerror("Error", "El usuario ya existe")

            except ValueError:
                lloginlist.append(tloginlist)

                txtloginlist = open("txt/tloginlist.txt", "w")
                txtloginlist.write(str(lloginlist))
                txtloginlist.close()

                messagebox.showinfo("Registrado", "Usuario registrado con exito")
                back()

    else:
        messagebox.showerror("Error", "Las contraseñas no coinciden")

def run():
    global ssize, fsize, root, ico, photo
    global main, fmainmenu, finicio, flogin, fregist, fwelcome
    global eluser, elpassword
    global eruser, erpassword, ercpassword

    root = tkinter.Tk()
    
    sv_ttk.set_theme("light")

    ssize = (root.winfo_screenwidth(), root.winfo_screenheight())
    fsize = int((35 / 1366) * ssize[0])
    trissize = int((455 / 1366) * ssize[0])
    root.state("zoomed")
    root.title(mrtitle)
    root.config(bg = bgcolor)

    ico = Image.open("img/logo.png")
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)

    main = ttk.Notebook(root)

    #MENU PRINCIPAL

    fmainmenu = Frame(root, bg = bgcolor)

    ftlmspace = Frame(fmainmenu, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    lmaintitle = Label(fmainmenu, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    imaintitle = ImageTk.PhotoImage(ico.resize((int(ssize[0] * 0.1), int(ssize[0] * 0.1 * logoar))))
    limaintitle = tkinter.Label(fmainmenu, image = imaintitle, bg = bgcolor)
    
    fmlmspace = Frame(fmainmenu, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    lmaindesc = Label(fmainmenu, text = mydescription, font = (ftitle, int(fsize / 2), "bold"), relief = "raised", padx = int(ssize[0] * 0.03), pady = int(ssize[1] * 0.01))

    ftcmspace = Frame(fmainmenu, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    bregist = Button(fmainmenu, text = "Registrarse", font = (ftitle, int(fsize / 2), "bold"), command = regist, height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

    blogin = Button(fmainmenu, text = "Iniciar sesion", font = (ftitle, int(fsize / 2), "bold"), command = login, height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

    ftrmspace = Frame(fmainmenu, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    fblmspace = Frame(fmainmenu, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    #INICIO

    finicio = Frame(main, bg = bgcolor)

    #LOGIN

    flogin = Frame(main, bg = bgcolor)

    ftllspace = Frame(flogin, width = ssize[0] * 0.39, height = ssize[0] * 0.05, bg = bgcolor)

    llogintitle = Label(flogin, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    ilogintitle = ImageTk.PhotoImage(ico.resize((int(ssize[0] * 0.1), int(ssize[0] * 0.1 * logoar))))
    lilogintitle = tkinter.Label(flogin, image = ilogintitle, bg = bgcolor)

    fltext = Frame(flogin, bg = bgcolor)

    lluser = Label(fltext, text = "Email", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    eluser = Entry(fltext, font = (ftitle, int(fsize / 2), "bold"), width = int(ssize[0] * 0.01))

    llpassword = Label(fltext, text = "Contraseña", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    elpassword = Entry(fltext, show = "*",font = (ftitle, int(fsize / 2), "bold"), width = int(ssize[0] * 0.01))

    ltlogin = Label(fltext, text = " ", font = (ftitle, int(fsize / 5), "bold"), bg = bgcolor)

    bslogin = Button(flogin, text = "Iniciar sesion", command = slogin, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.002), width = int(ssize[0] * 0.009))

    ftrlspace = Frame(flogin, width = ssize[0] * 0.39, height = ssize[0] * 0.05, bg = bgcolor)

    fcllspace = Frame(flogin, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    #REGISTRO

    fregist = Frame(main, bg = bgcolor)

    ftlrspace = Frame(fregist, width = ssize[0] * 0.39, height = ssize[0] * 0.05, bg = bgcolor)

    lregisttitle = Label(fregist, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    iregisttitle = ImageTk.PhotoImage(ico.resize((int(ssize[0] * 0.1), int(ssize[0] * 0.1 * logoar))))
    liregisttitle = tkinter.Label(fregist, image = ilogintitle, bg = bgcolor)

    frtext = Frame(fregist, bg = bgcolor)

    lruser = Label(frtext, text = "Email", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    eruser = Entry(frtext, font = (ftitle, int(fsize / 2), "bold"), width = int(ssize[0] * 0.01))

    lrpassword = Label(frtext, text = "Contraseña", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    erpassword = Entry(frtext, show = "*",font = (ftitle, int(fsize / 2), "bold"), width = int(ssize[0] * 0.01))

    lrcpassword = Label(frtext, text = "Confirmar contraseña", font = (ftitle, int(fsize / 2), "bold"), bg = bgcolor)

    ercpassword = Entry(frtext, show = "*",font = (ftitle, int(fsize / 2), "bold"), width = int(ssize[0] * 0.01))

    ltregist = Label(frtext, text = " ", font = (ftitle, int(fsize / 5), "bold"), bg = bgcolor)

    bsregist = Button(fregist, text = "Registrarse", command = sregist, font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.002), width = int(ssize[0] * 0.009))

    ftrrspace = Frame(fregist, width = ssize[0] * 0.39, height = ssize[0] * 0.05, bg = bgcolor)

    fclrspace = Frame(fregist, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    #BIENVENIDO

    fwelcome = Frame(main, bg = bgcolor)

    #Posicionamiento de Frames

    fmainmenu.grid(row = 0, column = 0)

    #Posicionamiento del menu principal

    ftlmspace.grid(row = 0, column = 0)
    fmlmspace.grid(row = 3, column = 0)
    fblmspace.grid(row = 5, column = 0)
    lmaintitle.grid(row = 1, column = 1)
    limaintitle.grid(row = 2, column = 1)
    lmaindesc.grid(row = 4, column = 1)
    ftcmspace.grid(row = 0, column = 2)
    bregist.grid(row = 1, column = 4)
    bregist.bind("<Button-1>", lambda event: regist())
    blogin.grid(row = 2, column = 4)
    blogin.bind("<Button-1>", lambda event: login())
    ftrmspace.grid(row = 0, column = 5)

    #Posicionamiento del login

    ftllspace.grid(row = 0, column = 0)
    fcllspace.grid(row = 3, column = 0)
    llogintitle.grid(row = 1, column = 1)
    lilogintitle.grid(row = 2, column = 1)
    fltext.grid(row = 4, column = 1)
    lluser.grid(row = 4, column = 1)
    eluser.grid(row = 5, column = 1)
    llpassword.grid(row = 6, column = 1)
    elpassword.grid(row = 7, column = 1)
    ltlogin.grid(row = 8, column = 1)
    bslogin.grid(row = 9, column = 1)
    ftrlspace.grid(row = 0, column = 2)

    #Posicionamiento del registro

    ftlrspace.grid(row = 0, column = 0)
    fclrspace.grid(row = 3, column = 0)
    lregisttitle.grid(row = 1, column = 1)
    liregisttitle.grid(row = 2, column = 1)
    frtext.grid(row = 4, column = 1)
    lruser.grid(row = 4, column = 1)
    eruser.grid(row = 5, column = 1)
    lrpassword.grid(row = 6, column = 1)
    erpassword.grid(row = 7, column = 1)
    lrcpassword.grid(row = 8, column = 1)
    ercpassword.grid(row = 9, column = 1)
    ltregist.grid(row = 10, column = 1)
    bsregist.grid(row = 11, column = 1)
    ftrrspace.grid(row = 0, column = 2)

    root.mainloop()

if __name__ == "__main__":
    run()
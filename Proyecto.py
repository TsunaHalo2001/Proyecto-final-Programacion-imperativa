import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import sv_ttk

pstate = 0

mrtitle = "My restaurant"
ftitle = "MS Sans Serif"
fctitle = "#505050"
logoar = 567 / 487
bgcolor = "#DCDCDC"
mydescription = "\nYa sea que busques un almuerzo casual con\namigos, una cena romántica o un evento\nespecial, nuestro restaurante\npromete una experiencia que cautivará tu\npaladar y creará recuerdos duraderos.\n"
bwregist = 37 / 1366

def back():
    global main, fmainmenu, finicio, flogin, fregist, pstate

    if pstate == 1:
        pstate = 0

        main.grid_remove()
        fmainmenu.grid(row = 0, column = 0)

def regist():
    global main, fmainmenu, finicio, fregist, pstate

    pstate = 1

    fmainmenu.grid_remove()
    main.grid(row = 0, column = 0)

    main.add(finicio, text = "Inicio")
    main.add(fregist, text = "Registrarse")
    main.select(fregist)
    main.bind("<<NotebookTabChanged>>", lambda event: back())
    main.forget(flogin)

def login():
    global main, fmainmenu, finicio, fregist, pstate

    pstate = 1

    fmainmenu.grid_remove()
    main.grid(row = 0, column = 0)

    main.add(finicio, text = "Inicio")
    main.add(flogin, text = "Iniciar sesion")
    main.select(flogin)
    main.bind("<<NotebookTabChanged>>", lambda event: back())
    main.forget(fregist)

def slogin():
    global main, finicio, flogin, pstate

def run():
    global ssize, fsize, root, ico, photo, main, fmainmenu, finicio, flogin, fregist

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

    euser = Entry(fltext, font = (ftitle, int(fsize / 2), "bold"), width = int(ssize[0] * 0.01))
    euser.insert(0, "Usuario")
    euser.bind("<FocusIn>", lambda event: euser.delete(0, END))

    epassword = Entry(fltext, show = "*",font = (ftitle, int(fsize / 2), "bold"), width = int(ssize[0] * 0.01))
    epassword.insert(0, "Contraseña")
    epassword.bind("<FocusIn>", lambda event: epassword.delete(0, END))

    bslogin = Button(flogin, text = "Iniciar sesion", font = (ftitle, int(fsize / 2), "bold"), height = int(ssize[1] * 0.002), width = int(ssize[0] * 0.009))

    ftrlspace = Frame(flogin, width = ssize[0] * 0.39, height = ssize[0] * 0.05, bg = bgcolor)

    fcllspace = Frame(flogin, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    #REGISTRO

    fregist = Frame(main, bg = bgcolor)

    ftlrspace = Frame(fregist, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    lregisttitle = Label(fregist, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    iregisttitle = ImageTk.PhotoImage(ico.resize((int(ssize[0] * 0.1), int(ssize[0] * 0.1 * logoar))))
    liregisttitle = tkinter.Label(fregist, image = ilogintitle, bg = bgcolor)

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
    euser.grid(row = 4, column = 1)
    epassword.grid(row = 5, column = 1)
    bslogin.grid(row = 6, column = 1)
    ftrlspace.grid(row = 0, column = 2)

    #Posicionamiento del registro

    ftlrspace.grid(row = 0, column = 0)
    lregisttitle.grid(row = 1, column = 1)
    liregisttitle.grid(row = 2, column = 1)

    root.mainloop()

if __name__ == "__main__":
    run()
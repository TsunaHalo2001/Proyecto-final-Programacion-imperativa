import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import sv_ttk

mrtitle = "My restaurant"
ftitle = "MS Sans Serif"
fctitle = "#505050"
logoar = 567 / 487
bgcolor = "#DCDCDC"
mydescription = "\nYa sea que busques un almuerzo casual con\namigos, una cena romántica o un evento\nespecial, nuestro restaurante\npromete una experiencia que cautivará tu\npaladar y creará recuerdos duraderos.\n"
bwregist = 37 / 1366

def regist():
    pass

def login():
    pass

def run():
    global ssize, fsize, root, ico, photo, fmainmenu

    root = tkinter.Tk()
    
    sv_ttk.set_theme("light")

    ssize = (root.winfo_screenwidth() , root.winfo_screenheight())
    fsize = int((35 / 1366) * ssize[0])
    trissize = int((455 / 1366) * ssize[0])
    root.state("zoomed")
    root.title(mrtitle)
    root.config(bg = bgcolor)

    ico = Image.open("img/logo.png")
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)

    #main = ttk.Notebook(root)

    #MENU PRINCIPAL

    fmainmenu = Frame(root, bg = bgcolor)

    ftlspace = Frame(fmainmenu, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    lmaintitle = Label(fmainmenu, text = mrtitle, font = (ftitle, fsize, "bold"), fg = fctitle, bg = bgcolor)

    imaintitle = ImageTk.PhotoImage(ico.resize((int(ssize[0] * 0.1), int(ssize[0] * 0.1 * logoar))))
    limaintitle = tkinter.Label(fmainmenu, image = imaintitle, bg = bgcolor)
    
    fmlspace = Frame(fmainmenu, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    lmaindesc = Label(fmainmenu, text = mydescription, font = (ftitle, int(fsize / 2), "bold"), relief = "raised", padx = int(ssize[0] * 0.03), pady = int(ssize[1] * 0.01))

    ftcspace = Frame(fmainmenu, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    bregist = Button(fmainmenu, text = "Registrarse", font = (ftitle, int(fsize / 2), "bold"), command = regist, height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

    blogin = Button(fmainmenu, text = "Iniciar sesion", font = (ftitle, int(fsize / 2), "bold"), command = login, height = int(ssize[1] * 0.005), width = int(ssize[0] * bwregist))

    ftrspace = Frame(fmainmenu, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    fblspace = Frame(fmainmenu, width = ssize[0] * 0.05, height = ssize[0] * 0.05, bg = bgcolor)

    #Posicionamiento de Frames

    fmainmenu.grid(row = 0, column = 0)

    #Posicionamiento del menu principal

    ftlspace.grid(row = 0, column = 0)
    fmlspace.grid(row = 3, column = 0)
    fblspace.grid(row = 5, column = 0)
    lmaintitle.grid(row = 1, column = 1)
    limaintitle.grid(row = 2, column = 1)
    lmaindesc.grid(row = 4, column = 1)
    ftcspace.grid(row = 0, column = 2)
    bregist.grid(row = 1, column = 4)
    blogin.grid(row = 2, column = 4)
    ftrspace.grid(row = 0, column = 5)

    #main.grid(row = 0, column = 0)

    root.mainloop()

if __name__ == "__main__":
    run()
import tkinter
from tkinter import *
from PIL import Image, ImageTk

def run():
    main = tkinter.Tk()
    ssize = (main.winfo_screenwidth() , main.winfo_screenheight())
    fsize = int((25 / 1366) * ssize[0])
    trissize = int((455 / 1366) * ssize[0])
    main.state("zoomed")
    main.title("My restaurant")

    ico = Image.open("img/logo.png")
    photo = ImageTk.PhotoImage(ico)
    main.wm_iconphoto(False, photo)

    lmaintitle = Label(main, text = "My restaurant", font = "Verdana " + str(fsize) + " bold").grid(row = 0, column = 0)

    imaintitle = ImageTk.PhotoImage(Image.open("img/logo.png"))
    limaintitle = tkinter.Label(main, image = imaintitle).grid(row = 1, column = 0)

    main.mainloop()

if __name__ == "__main__":
    run()
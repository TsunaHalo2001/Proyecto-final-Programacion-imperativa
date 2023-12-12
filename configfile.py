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
#0 = Pagina principal
#1 = Login y registro
#2 = Menu principal
#3 = Gestion de platos, mesas y pedidos
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

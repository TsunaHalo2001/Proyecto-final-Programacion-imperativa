# Description: Archivo de configuracion del programa
# Autor: Joan Esteban Villamil Largo

#Importar librerias
#Libreria para la interfaz grafica
import tkinter
from tkinter import *
from tkinter import ttk, messagebox

#Libreria para el manejo de archivos
from PIL import Image, ImageTk

import numpy as np

#Libreria para el manejo de contraseñas
import hashlib

#Libreria para el manejo de fechas
from datetime import datetime

#Tema mamalon Sun Valley
import sv_ttk

#Variables globales
#Variable de fecha
now = datetime.now()

#Variable del estado del programa
#0 = Pagina principal
#1 = Login y registro
#2 = Menu principal
#4 = Gestion de platos
#5 = Agragar platos
#6 = Eliminar o actualizar platos
#7 = Actualizar platos
#8 = Gestion de mesas
#9 = Agregar mesas
pstate = 0

#Variables de ruta de archivos
#Variable de ruta de la base de datos de usuarios y contraseñas
uplist = "txt/registro_inicio.txt"
cplist = "txt/password.txt"
plist = "txt/platos.txt"
mlist = "txt/mesas.txt"
pelist = "txt/pedidos.txt"

#Variables de fuente y color
ftitle = "MS Sans Serif"
fctitle = "#505050"
bgcolor = "#DCDCDC"

#Variables de texto
mrtitle = "My restaurant"
ititle = "Inicio"
rtitle = "Registrarse"
ltitle = "Iniciar sesión"
mptitle = "Menú principal"
gptitle = "Gestión de platos"
aptitle = "Agregar plato"
eaptitle = "Eliminar o actualizar platos"
acptitle = "Actualizar plato"
gmtitle = "Gestión mesas"
amtitle = "Agregar mesa"
eamtitle = "Eliminar o actualizar mesas"
acmtitle = "Actualizar mesa"
gpetitle = "Gestión de pedidos"
apetitle = "Agregar pedido"
eapetitle = "Eliminar o actualizar pedidos"
acpetitle = "Actualizar pedido"
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

#Descifrar lista de platos
txtplatos = open(plist, "r")
platos = txtplatos.read()
txtplatos.close()
platos = platos.replace("']]", "").replace("[['", "")
lplatos = platos.split("'], ['")

for i in range(len(lplatos)):
    lplatos[i] = lplatos[i].split("', '")

#Descifrar lista de mesas
txtmesas = open(mlist, "r")
mesas = txtmesas.read()
txtmesas.close()
mesas = mesas.replace("']]", "").replace("[['", "")
lmesas = mesas.split("'], ['")

for i in range(len(lmesas)):
    lmesas[i] = lmesas[i].split("', '")

#Descifrar lista de pedidos
txtpedidos = open(pelist, "r")
pedidos = txtpedidos.read()
txtpedidos.close()
pedidos = pedidos.replace("']]", "").replace("[['", "")
lpedidos = pedidos.split("'], ['")

for i in range(len(lpedidos)):
    lpedidos[i] = lpedidos[i].split("', '")

#Base de datos de correos
emaildb = ["@correounivalle.edu.co","@gmail.com", "@hotmail.com", "@outlook.com", "@yahoo.com", "@icloud.com", "@live.com", "@msn.com", "@aol.com", "@yandex.com", "@protonmail.com", "@zoho.com", "@gmx.com", "@mail.com", "@yopmail.com", "@tutanota.com", "@mail.ru", "@gmx.us", "@gmx.de", "@gmx.fr", "@gmx.at", "@gmx.ch", "@gmx.net", "@gmx.co.uk", "@gmx.com.mx", "@gmx.es", "@gmx.eu", "@gmx.it", "@gmx.com.br", "@gmx.com.ar", "@gmx.com.co", "@gmx.com.ve", "@gmx.com.pe", "@gmx.com.ec", "@gmx.com.bo", "@gmx.com.py", "@gmx.com.uy", "@gmx.com.pa", "@gmx.com.do", "@gmx.com.gt", "@gmx.com.sv", "@gmx.com.hn", "@gmx.com.ni", "@gmx.com.cr", "@gmx.com.cu", "@gmx.com.pr", "@gmx.com.jm", "@gmx.com.bb", "@gmx.com.ag", "@gmx.com.dm", "@gmx.com.vc", "@gmx.com.lc", "@gmx.com.gy", "@gmx.com.sr", "@gmx.com.bo", "@gmx.com.py", "@gmx.com.uy", "@gmx.com.ar", "@gmx.com.co", "@gmx.com.ve", "@gmx.com.pe", "@gmx.com.ec", "@gmx.com.bo", "@gmx.com.py", "@gmx.com.uy", "@gmx.com.pa", "@gmx.com.do", "@gmx.com.gt", "@gmx.com.sv", "@gmx.com.hn", "@gmx.com.ni", "@gmx.com.cr", "@gmx.com.cu", "@gmx.com.pr", "@gmx.com.jm", "@gmx.com.bb", "@gmx.com.ag", "@gmx.com.dm", "@gmx.com.vc", "@gmx.com.lc", "@gmx.com.gy", "@gmx.com.sr", "@gmx.com.bo", "@gmx.com.py", "@gmx.com.uy"]

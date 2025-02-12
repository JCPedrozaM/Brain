import tkinter as tk
import os
import sys

#VENTANA DE PANEL DE ADMINISTRACIÓN

window=tk.Tk()

window.title("Panel de Administración") #Título de la ventana

window.resizable(0,0) #Redimensión de la ventana

window.iconbitmap("cubre.ico") #Icono de la ventana


#Crear un frame dentro de la ventana
frame=tk.Frame(window,width=450, height=70)
frame.pack()
frame.config(bg="#93D8FF")

#Etiqueta de título de la ventana
label= tk.Label(frame, text="Panel de Administración",font=("Century Gothic", 16), bg="#93D8FF")
label.place(x=90, y=20)

#Creación Frame 2 para poner los botones
frame2=tk.Frame(window,width=450, height=300)
frame2.pack()
frame2.config(bg="#FFFFFF")

#Métodos para los botones
def captRostrosCon():
    os.system('python capturandoRostrosCon.py')

def captRostrosSin():
    os.system('python capturandoRostrosSin.py')

def entrenar():
    os.system('python entrenandoRF.py')

def atras():
    window.destroy()
    os.system('python menu.py')

def instalarRequerimientos():
    os.system('pip install -r requirements.txt')

#Botón Captura rostro con cubrebocas
con_btn= tk.PhotoImage(file="Botones/conbtn.png")
con_lbl= tk.Label(image=con_btn)
btn1= tk.Button(frame2, image=con_btn , command=captRostrosCon, bg="#FFFFFF", borderwidth=0).place(x=20, y=30)

#Botón Captura rostro sin cubrebocas
sin_btn= tk.PhotoImage(file="Botones/sinbtn.png")
sin_lbl= tk.Label(image=sin_btn)
btn1= tk.Button(frame2, image=sin_btn , command=captRostrosSin, bg="#FFFFFF", borderwidth=0).place(x=140, y=120)

#Botón Ejecutar entrenamiento
train_btn= tk.PhotoImage(file="Botones/entrenarbtn.png")
train_lbl= tk.Label(image=train_btn)
btn3= tk.Button(frame2, image=train_btn, command=entrenar, bg="#FFFFFF", borderwidth=0).place(x=250, y=200)

#Botón Regresar
back_btn= tk.PhotoImage(file="Botones/btnhome.png")
back_lbl= tk.Label(image=back_btn)
btn4= tk.Button(frame2, image=back_btn, command=atras, bg="#FFFFFF", borderwidth=0).place(x=40, y=240)

#Botón Instalar requerimientos
install_btn= tk.PhotoImage(file="Botones/btnrequerimientos.png")
install_lbl= tk.Label(image=install_btn)
btn5= tk.Button(frame2, image=install_btn, command=instalarRequerimientos, bg="#FFFFFF", borderwidth=0).place(x=320, y=30)

window.mainloop()

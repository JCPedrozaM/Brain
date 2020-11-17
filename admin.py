import tkinter as tk
#import ReconocimientoFacial
import os
import sys

window=tk.Tk()

window.title("Panel de Administración") #Título de la ventana

window.resizable(0,0) #Redimensión de la ventana

window.iconbitmap("cubre.ico") #Icono de la ventana


#Crear un frame dentro de la ventana
frame=tk.Frame(window,width=450, height=70)
frame.pack()
frame.config(bg="#93D8FF")


label= tk.Label(frame, text="Panel de Administración",font=("Century Gothic", 16), bg="#93D8FF")
label.place(x=90, y=20)

#Creación Frame 2
frame2=tk.Frame(window,width=450, height=300)
frame2.pack()
frame2.config(bg="#FFFFFF")

def captRostrosCon():
    os.system('python capturandoRostrosCon.py')

def captRostrosSin():
    os.system('python capturandoRostrosSin.py')

def entrenar():
    os.system('python entrenandoRF.py')

tk.Button(frame2, text="Capturar Rostros Con Cubrebocas",font=("Century Gothic", 12), command=captRostrosCon).place(x=130, y=70)
tk.Button(frame2, text="Capturar Rostros Sin Cubrebocas",font=("Century Gothic", 12), command=captRostrosSin).place(x=130, y=140)
tk.Button(frame2, text="Ejecutar Entrenamiento",font=("Century Gothic", 12), command=entrenar).place(x=130, y=210)
 

window.mainloop()

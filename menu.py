import tkinter as tk
import os
import sys

#VENTANA PRINCIPAL

window=tk.Tk()

window.title("Detección de Cubrebocas") #Título de la ventana

window.resizable(0,0) #Redimensión de la ventana

window.iconbitmap("cubre.ico") #Icono de la ventana


#Crear un frame dentro de la ventana
frame=tk.Frame(window,width=450, height=70)
frame.pack()
frame.config(bg="#93D8FF")

#Etiqueta de título de la ventana
label= tk.Label(frame, text="Detección de cubrebocas",font=("Century Gothic", 16), bg="#93D8FF")
label.place(x=90, y=20)

#Creación Frame 2 para colocar botones
frame2=tk.Frame(window,width=450, height=200)
frame2.pack()
frame2.config(bg="#FFFFFF")

#Métodos para los botones
def recFacial():
    os.system('python ReconocimientoFacial.py')

def openAdmin():
    window.destroy()
    os.system('python admin.py')

#Botón comenzar detección
start_btn= tk.PhotoImage(file="Botones/btncomenzar.png")
start_lbl= tk.Label(image=start_btn)
my_btn= tk.Button(frame2, image=start_btn, command=recFacial, borderwidth=0, bg="#FFFFFF").place(x=150, y=20)

#Botón para ir al Panel de Administración
admin_btn= tk.PhotoImage(file="Botones/btnadmin.png")
admin_lbl= tk.Label(image=admin_btn)
my_btn2= tk.Button(frame2, image=admin_btn, command=openAdmin, borderwidth=0, bg="#FFFFFF").place(x=335, y=145)

 
window.mainloop()

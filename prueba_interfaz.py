import tkinter as tk
import ReconocimientoFacial

window=tk.Tk()

window.title("Detección de Cubrebocas") #Título de la ventana

window.resizable(0,0) #Redimensión de la ventana

window.iconbitmap("cubre.ico") #Icono de la ventana


#Crear un frame dentro de la ventana
frame=tk.Frame(window,width=450, height=70)
frame.pack()
frame.config(bg="#93D8FF")


label= tk.Label(frame, text="Detección de cubrebocas",font=("Century Gothic", 16), bg="#93D8FF")
label.place(x=90, y=20)

#Creación Frame 2
frame2=tk.Frame(window,width=450, height=200)
frame2.pack()
frame2.config(bg="#FFFFFF")

tk.Button(frame2, text="Comenzar detección",font=("Century Gothic", 12), command=ReconocimientoFacial).place(x=130, y=70)
 

window.mainloop()

import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title("Detección de cubrebocas")
window.iconbitmap("cubre.ico") #Icono de la ventana
window.resizable=(0,0)

#Crear un frame dentro de la ventana
frame=tk.Frame(window,width=450, height=70)
frame.pack()
frame.config(bg="#93D8FF")

label= tk.Label(frame, text="Iniciando video",font=("Century Gothic", 16), bg="#93D8FF")
label.place(x=150, y=20)


#Creación Frame 2
frame2=tk.Frame(window,width=450, height=200)
frame2.pack()
frame2.config(bg="#FFFFFF")

progressbar = ttk.Progressbar(frame2, mode="indeterminate")
progressbar.place(x=30, y=60, width=30)
progressbar.place(width=400, height=30)
progressbar.start(10)

window.geometry("450x270")


        
window.mainloop()


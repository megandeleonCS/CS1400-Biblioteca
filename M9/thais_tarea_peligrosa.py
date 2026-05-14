import tkinter as tk

ventana = tk.Tk()
ventana.title("Prueba Tkinter")

label = tk.Label(ventana, text="Tkinter funciona")
label.pack()

ventana.mainloop()
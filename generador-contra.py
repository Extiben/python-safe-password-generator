import tkinter as tk
import random
import string 

def generar_contraseña():
    longitud = 16
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    resultado.config(text=contraseña)

#closing the window

ventana = tk.Tk()
ventana.title("random password generator")
ventana.geometry("400x200")

titulo = tk.Label(ventana, text="haz click para generar una contraseña segura:", font=("Arial", 12))

boton = tk.Button(ventana, text="Generar", command=generar_contraseña, font=("Arial", 11), bg="#4CAF50", fg="white")
boton.pack(pady=10)

resultado = tk.Label(ventana, text="", font=("Courier", 14), fg="#333")
resultado.pack(pady=10)

ventana.mainloop()
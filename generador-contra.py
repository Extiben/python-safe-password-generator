import tkinter as tk
from tkinter import messagebox
import random
import string
import datetime
import os

def generar_contraseña():
    longitud = 20
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    # Mostrar en ventana
    resultado.config(text=contraseña)
    
    # Guardar en el escritorio
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    ruta_archivo = os.path.join(desktop, "historial_contraseñas.txt")
    with open(ruta_archivo, "a") as archivo:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"[{timestamp}] {contraseña}\n")
    
    # Mostrar mensaje emergente
    messagebox.showinfo("Password Saved", "Your password history file is in your Desktop.")

# Crear ventana
ventana = tk.Tk()
ventana.title("password generator")
ventana.geometry("400x200")

# Etiqueta de título
titulo = tk.Label(ventana, text="Click to create a safe password:", font=("Arial", 12))
titulo.pack(pady=10)

# Botón para generar
boton = tk.Button(ventana, text="Generate", command=generar_contraseña, font=("Arial", 11), bg="#4CAF50", fg="white")
boton.pack(pady=10)


resultado = tk.Label(ventana, text="", font=("Courier", 14), fg="#333")
resultado.pack(pady=10)


ventana.mainloop()

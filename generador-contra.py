import tkinter as tk
from tkinter import messagebox, Toplevel
import random
import string
import datetime
import os
import json

# Create "data" folder if it doesn't exists
CARPETA_DATA = "data"
ARCHIVO_HISTORIAL = os.path.join(CARPETA_DATA, "history.json")

if not os.path.exists(CARPETA_DATA):
    os.makedirs(CARPETA_DATA)

if not os.path.exists(ARCHIVO_HISTORIAL):
    with open(ARCHIVO_HISTORIAL, "w") as f:
        json.dump([], f)

# password generator's logic
def generar_contraseña():
    longitud = 20
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    resultado.config(text=contraseña)
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entrada = {"fecha": timestamp, "contraseña": contraseña}

    # load history
    with open(ARCHIVO_HISTORIAL, "r") as f:
        historial = json.load(f)
    
    historial.append(entrada)

    # Save new history
    with open(ARCHIVO_HISTORIAL, "w") as f:
        json.dump(historial, f, indent=2)

    messagebox.showinfo("Saved!", "password saved in your history.")


def ver_historial():
    with open(ARCHIVO_HISTORIAL, "r") as f:
        historial = json.load(f)

    if not historial:
        messagebox.showinfo("empty history", "There is no saved passwords yet.")
        return

    ventana_historial = Toplevel(ventana)
    ventana_historial.title("password history")
    ventana_historial.geometry("400x300")

    texto = tk.Text(ventana_historial, wrap="word")
    texto.pack(expand=True, fill="both")

    for entrada in historial[::-1]:  # Show most recent ones on top
        texto.insert("end", f"{entrada['fecha']}: {entrada['contraseña']}\n")


# Creating the main window
ventana = tk.Tk()
ventana.title("Password Generator")
ventana.geometry("400x250")

titulo = tk.Label(ventana, text="Click to create a safe password:", font=("Arial", 12))
titulo.pack(pady=10)

boton = tk.Button(ventana, text="Generate", command=generar_contraseña, font=("Arial", 11), bg="#4CAF50", fg="white")
boton.pack(pady=10)

resultado = tk.Label(ventana, text="", font=("Courier", 14), fg="#333")
resultado.pack(pady=10)

boton_historial = tk.Button(ventana, text="history", command=ver_historial, font=("Arial", 10), bg="#2196F3", fg="white")
boton_historial.pack(pady=5)    

ventana.mainloop()

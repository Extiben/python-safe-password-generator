import tkinter as tk
import random
import string
import datetime

def generar_contraseña():
    longitud = 20
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    # Mostrar en ventana
    resultado.config(text=contraseña)
    
    # Guardar en archivo
    with open("historial_contraseñas.txt", "a") as archivo:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"[{timestamp}] {contraseña}\n")

# Crear ventana
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("400x200")

# Etiqueta de título
titulo = tk.Label(ventana, text="click to create a safe password:", font=("Arial", 12))
titulo.pack(pady=10)

# Botón para generar
boton = tk.Button(ventana, text="Generate", command=generar_contraseña, font=("Arial", 11), bg="#4CAF50", fg="white")
boton.pack(pady=10)


resultado = tk.Label(ventana, text="", font=("Courier", 14), fg="#333")
resultado.pack(pady=10)


ventana.mainloop()

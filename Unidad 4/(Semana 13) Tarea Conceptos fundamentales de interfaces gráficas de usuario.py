import tkinter as tk
from tkinter import messagebox, ttk

def agregar_datos():
    item = entrada.get()
    if item:
        lista.insert(tk.END, item)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

def limpiar_datos():
    lista.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")
ventana.geometry("400x400")  # Ajusta el tamaño de la ventana

# Etiquetas
label = tk.Label(ventana, text="Introduce datos:", font=("Arial", 14))
label.pack(pady=10)

# Campo de texto
entrada = tk.Entry(ventana, font=("Arial", 12), width=30)
entrada.pack(pady=10)

# Botones
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_datos, font=("Arial", 12))
boton_agregar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos, font=("Arial", 12))
boton_limpiar.pack(pady=5)

# Lista para mostrar datos
lista = tk.Listbox(ventana, font=("Arial", 12), width=30, height=10)
lista.pack(pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()

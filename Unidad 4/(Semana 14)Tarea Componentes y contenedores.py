import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Frame para la lista de eventos
        self.frame_eventos = tk.Frame(root)
        self.frame_eventos.pack(pady=10)

        # TreeView para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_eventos, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para los campos de entrada
        self.frame_entrada = tk.Frame(root)
        self.frame_entrada.pack(pady=10)

        tk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0)
        self.fecha_entry = DateEntry(self.frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.fecha_entry.grid(row=0, column=1, padx=5)

        tk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0)
        self.hora_entry = tk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=1, column=1, padx=5)

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.descripcion_entry = tk.Entry(self.frame_entrada)
        self.descripcion_entry.grid(row=2, column=1, padx=5)

        # Frame para los botones
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=10)

        self.agregar_btn = tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento)
        self.agregar_btn.grid(row=0, column=0, padx=10)

        self.eliminar_btn = tk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.eliminar_btn.grid(row=0, column=1, padx=10)

        self.salir_btn = tk.Button(self.frame_botones, text="Salir", command=root.quit)
        self.salir_btn.grid(row=0, column=2, padx=10)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert('', 'end', values=(fecha, hora, descripcion))
            self.limpiar_campos()
        else:
            messagebox.showwarning("Campos Vacíos", "Por favor, completa todos los campos.")

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            self.tree.delete(seleccionado)
        else:
            messagebox.showwarning("Selección", "Por favor, selecciona un evento para eliminar.")

    def limpiar_campos(self):
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()

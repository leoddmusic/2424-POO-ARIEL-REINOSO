import tkinter as tk
from tkinter import messagebox, simpledialog

# Archivo para guardar las tareas
TASKS_FILE = "tareas.txt"


# Función para cargar las tareas desde el archivo
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task = task.strip()
                tasks_listbox.insert(tk.END, task)
                if "(Completada)" in task:
                    tasks_listbox.itemconfig(tk.END, {'fg': 'blue'})
    except FileNotFoundError:
        pass  # Si no existe el archivo, no se hace nada (será creado al guardar)


# Función para guardar las tareas en un archivo
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        tasks = tasks_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")


# Función para añadir una tarea a la lista
def add_task(event=None):
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Vacía", "Por favor, ingrese una tarea.")


# Función para marcar o desmarcar una tarea como completada
def toggle_complete(event=None):
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)

        if "(Completada)" not in task:
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, f"{task} (Completada)")
            tasks_listbox.itemconfig(selected_task_index, {'fg': 'blue'})  # Cambiar el color a azul
        else:
            original_task = task.replace(" (Completada)", "")
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, original_task)
            tasks_listbox.itemconfig(selected_task_index, {'fg': 'black'})  # Regresar a color negro
    except IndexError:
        pass  # No hacer nada si no hay tarea seleccionada


# Función para eliminar una tarea
def delete_task(event=None):
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        pass  # No hacer nada si no hay tarea seleccionada


# Función para editar una tarea seleccionada
def edit_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)

        new_task = simpledialog.askstring("Editar Tarea", f"Editar tarea: {task}")
        if new_task:
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, new_task)
            tasks_listbox.itemconfig(selected_task_index, {'fg': 'black'})  # Por defecto, tarea no completada
    except:
        messagebox.showwarning("Selección Inválida", "Por favor, seleccione una tarea para editar.")


# Función para salir de la aplicación guardando las tareas
def exit_app(event=None):
    save_tasks()  # Guardar tareas antes de salir
    root.quit()


# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Crear el campo de entrada y botón "Añadir Tarea"
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)
task_entry.bind("<Return>", add_task)  # Añadir tarea con Enter

add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.pack(pady=5)

# Crear el Listbox para mostrar las tareas
tasks_listbox = tk.Listbox(root, width=40, height=10)
tasks_listbox.pack(pady=10)
tasks_listbox.bind("<Double-1>", toggle_complete)  # Doble clic para marcar/desmarcar como completada

# Crear los botones "Marcar/Desmarcar Completada", "Eliminar Tarea", y "Editar Tarea"
complete_button = tk.Button(root, text="Marcar/Desmarcar Completada", command=toggle_complete)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.pack(pady=5)

edit_button = tk.Button(root, text="Editar Tarea", command=edit_task)
edit_button.pack(pady=5)

# Vincular los atajos de teclado
root.bind("<Escape>", exit_app)  # Salir con "Escape"
root.bind_all("<c>", toggle_complete)  # Marcar/Desmarcar con "C" o "c"
root.bind_all("<C>", toggle_complete)  # Marcar/Desmarcar con "C" o "c"
root.bind_all("<d>", delete_task)  # Eliminar con "D" o "d"
root.bind_all("<D>", delete_task)  # Eliminar con "D" o "d"

# Cargar las tareas desde el archivo al iniciar
load_tasks()

# Iniciar el bucle principal de la GUI
root.mainloop()

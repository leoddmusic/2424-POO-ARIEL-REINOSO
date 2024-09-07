import json
import os


class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.detalle = (titulo, autor)  # Usamos una tupla para autor y título
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.detalle[0]}' por {self.detalle[1]} (ISBN: {self.isbn}, Categoría: {self.categoria})"

    def to_dict(self):
        return {
            "titulo": self.detalle[0],
            "autor": self.detalle[1],
            "categoria": self.categoria,
            "isbn": self.isbn
        }

    @staticmethod
    def from_dict(data):
        return Libro(data['titulo'], data['autor'], data['categoria'], data['isbn'])


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {len(self.libros_prestados)}"

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        self.libros_prestados = [libro for libro in self.libros_prestados if libro.isbn != isbn]

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "id_usuario": self.id_usuario,
            "libros_prestados": [libro.to_dict() for libro in self.libros_prestados]
        }

    @staticmethod
    def from_dict(data):
        usuario = Usuario(data['nombre'], data['id_usuario'])
        usuario.libros_prestados = [Libro.from_dict(libro) for libro in data['libros_prestados']]
        return usuario


class Biblioteca:
    def __init__(self, archivo='biblioteca.json'):
        self.libros = {}  # Diccionario con ISBN como clave
        self.usuarios = {}  # Diccionario con ID de usuario como clave
        self.archivo = archivo
        self.cargar_datos()

    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print("Error: Ya existe un libro con ese ISBN.")
        else:
            self.libros[libro.isbn] = libro
            self.guardar_datos()
            print(f"Libro '{libro.detalle[0]}' añadido exitosamente.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            self.guardar_datos()
            print(f"Libro con ISBN {isbn} eliminado exitosamente.")
        else:
            print("Error: No se encontró el libro con ese ISBN.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print("Error: Ya existe un usuario con ese ID.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.guardar_datos()
            print(f"Usuario '{usuario.nombre}' registrado exitosamente.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.guardar_datos()
            print(f"Usuario con ID {id_usuario} dado de baja exitosamente.")
        else:
            print("Error: No se encontró el usuario con ese ID.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.prestar_libro(libro)
            self.guardar_datos()
            print(f"Libro '{libro.detalle[0]}' prestado a {usuario.nombre}.")
        else:
            print("Error: Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            usuario.devolver_libro(isbn)
            self.guardar_datos()
            print(f"Libro con ISBN {isbn} devuelto por {usuario.nombre}.")
        else:
            print("Error: Usuario no encontrado.")

    def buscar_libro(self, criterio):
        resultados = [libro for libro in self.libros.values() if criterio.lower() in libro.detalle[0].lower() or criterio.lower() in libro.detalle[1].lower() or criterio.lower() in libro.categoria.lower()]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"El usuario {usuario.nombre} no tiene libros prestados.")
        else:
            print("Error: Usuario no encontrado.")

    def guardar_datos(self):
        data = {
            "libros": {isbn: libro.to_dict() for isbn, libro in self.libros.items()},
            "usuarios": {id_usuario: usuario.to_dict() for id_usuario, usuario in self.usuarios.items()}
        }
        with open(self.archivo, 'w') as file:
            json.dump(data, file, indent=4)

    def cargar_datos(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r') as file:
                data = json.load(file)
                self.libros = {isbn: Libro.from_dict(libro) for isbn, libro in data['libros'].items()}
                self.usuarios = {id_usuario: Usuario.from_dict(usuario) for id_usuario, usuario in data['usuarios'].items()}


def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n--- Sistema de Gestión de Biblioteca Digital ---")
        print("1. Añadir nuevo libro")
        print("2. Eliminar libro por ISBN")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados a un usuario")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            isbn = input("ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == '2':
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.eliminar_libro(isbn)

        elif opcion == '3':
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == '4':
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == '5':
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == '6':
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == '7':
            criterio = input("Ingresa el título, autor o categoría para buscar: ")
            biblioteca.buscar_libro(criterio)

        elif opcion == '8':
            id_usuario = input("ID del usuario: ")
            biblioteca.listar_libros_prestados(id_usuario)

        elif opcion == '0':
            print("Saliendo del sistema de gestión de biblioteca digital.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()

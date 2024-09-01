import os
import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"{self._id},{self._nombre},{self._cantidad},{self._precio:.2f}"

    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    @staticmethod
    def from_dict(data_dict):
        return Producto(
            data_dict["id"],
            data_dict["nombre"],
            data_dict["cantidad"],
            data_dict["precio"]
        )


class Inventario:
    def __init__(self, archivo='inventario.json'):
        self.productos = {}  # Usamos un diccionario para almacenamiento eficiente
        self.archivo = archivo
        self._cargar_inventario()

    def _guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                productos_dict = {id_: producto.to_dict() for id_, producto in self.productos.items()}
                json.dump(productos_dict, file, indent=4)  # Se agrega indent=4 para "pretty print"
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No se tiene permiso para escribir en el archivo.")

    def _cargar_inventario(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as file:
                    productos_dict = json.load(file)
                    self.productos = {id_: Producto.from_dict(data) for id_, data in productos_dict.items()}
                print("Inventario cargado exitosamente.")
            except FileNotFoundError:
                print("Error: El archivo no se encontró.")
            except PermissionError:
                print("Error: No se tiene permiso para leer el archivo.")
            except json.JSONDecodeError:
                print("Error: El archivo está corrupto o no contiene un formato válido.")
        else:
            print("No se encontró un archivo de inventario previo. Iniciando inventario vacío.")

    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.get_id()] = producto
            self._guardar_inventario()
            print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self._guardar_inventario()
            print("Producto eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            self._guardar_inventario()
            print("Producto actualizado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        productos_encontrados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if productos_encontrados:
            for p in productos_encontrados:
                print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: ${p.get_precio():.2f}")
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: ${producto.get_precio():.2f}")
        else:
            print("No hay productos en el inventario.")


def menu():
    inventario = Inventario()

    while True:
        print("\n--- Sistema Avanzado de Gestión de Inventarios ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar producto por ID")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("0. Salir")

        eleccion = input("Elige una opción: ")

        if eleccion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif eleccion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif eleccion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deja en blanco para no cambiar): ")
            precio = input("Nuevo precio (deja en blanco para no cambiar): ")
            nueva_cantidad = int(cantidad) if cantidad else None
            nuevo_precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif eleccion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif eleccion == '5':
            inventario.mostrar_productos()

        elif eleccion == '0':
            print("Saliendo del sistema avanzado de gestión de inventarios.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()

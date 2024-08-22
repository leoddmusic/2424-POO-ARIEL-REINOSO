import os

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

    @staticmethod
    def from_str(data_str):
        id_producto, nombre, cantidad, precio = data_str.split(',')
        return Producto(id_producto, nombre, int(cantidad), float(precio))


class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.productos = []
        self.archivo = archivo
        self._cargar_inventario()

    def _guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos:
                    file.write(str(producto) + '\n')
        except PermissionError:
            print("Error: No se tiene permiso para escribir en el archivo.")

    def _cargar_inventario(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as file:
                    for linea in file:
                        producto = Producto.from_str(linea.strip())
                        self.productos.append(producto)
            except FileNotFoundError:
                print("Error: El archivo no se encontró.")
            except PermissionError:
                print("Error: No se tiene permiso para leer el archivo.")

    def agregar_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos.append(producto)
            self._guardar_inventario()
            print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        self._guardar_inventario()
        print("Producto eliminado exitosamente.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                self._guardar_inventario()
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        productos_encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if productos_encontrados:
            for p in productos_encontrados:
                print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: ${p.get_precio():.2f}")
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos:
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: ${producto.get_precio():.2f}")
        else:
            print("No hay productos en el inventario.")

def menu():
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
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
            print("Saliendo del sistema de gestión de inventarios.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()

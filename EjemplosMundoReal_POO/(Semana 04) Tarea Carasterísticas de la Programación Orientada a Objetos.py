# archivo: EjemplosMundoReal_POO/sistema_reservas.py

class Cliente:
    """
    Clase que representa a un cliente.
    """

    def __init__(self, nombre, email):
        """
        Inicializa un nuevo cliente.

        :param nombre: Nombre del cliente
        :param email: Email del cliente
        """
        self.nombre = nombre
        self.email = email


class Reserva:
    """
    Clase que representa una reserva en un hotel.
    """

    def __init__(self, cliente, fecha_entrada, fecha_salida):
        """
        Inicializa una nueva reserva.

        :param cliente: Objeto Cliente que realiza la reserva
        :param fecha_entrada: Fecha de entrada
        :param fecha_salida: Fecha de salida
        """
        self.cliente = cliente
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida

    def mostrar_detalles(self):
        """
        Muestra los detalles de la reserva.
        """
        print(
            f"Reserva para {self.cliente.nombre} ({self.cliente.email}) del {self.fecha_entrada} al {self.fecha_salida}")


# Ejemplo de uso
cliente1 = Cliente("Ariel Reinoso", "arielraphi@gmail.com")
reserva1 = Reserva(cliente1, "2024-07-01", "2024-07-07")
reserva1.mostrar_detalles()

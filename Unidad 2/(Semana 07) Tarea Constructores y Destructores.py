class DatabaseConnection:
    def __init__(self, db_name):
        # Constructor que inicia una conexión a la base de datos
        self.db_name = db_name
        self.connection = None
        self.connect()

    def connect(self):
        # Simulación de establecimiento de conexión
        print(f"Conectando a la base de datos {self.db_name}...")
        self.connection = True  # Simulación: conexión establecida
        print("Conexión establecida.")

    def disconnect(self):
        # Simulación de cierre de conexión
        if self.connection:
            print(f"Desconectando de la base de datos {self.db_name}...")
            self.connection = None
            print("Conexión cerrada.")

    def __del__(self):
        # Destructor que asegura que la conexión se cierre
        self.disconnect()

# Ejemplo de uso
if __name__ == "__main__":
    db_conn = DatabaseConnection("MyDatabase")
    # La conexión se cerrará automáticamente al final del programa o cuando se elimine el objeto
    del db_conn

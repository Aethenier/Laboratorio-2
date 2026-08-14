import unicodedata


class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None
        self.anterior = None


class ListaDoblemente:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tam = 0
        self.reporte_path = "reporte.txt"
        self.limpiarReporte()

    def limpiarReporte(self):
        with open(self.reporte_path, "w", encoding="utf-8") as archivo:
            archivo.write("=== REPORTE ===\n")

    def registrar(self, mensaje):
        print(mensaje)
        with open(self.reporte_path, "a", encoding="utf-8") as archivo:
            archivo.write(mensaje + "\n")

    def listaVacia(self):
        return self.cabeza is None

    def getTamano(self):
        return self.tam

    def insertarAlFinal(self, nombre):
        nuevo = Nodo(nombre)
        if self.listaVacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.anterior = self.cola
            self.cola.siguiente = nuevo
            self.cola = nuevo
        self.tam += 1
        self.registrar(f"Se insertó '{nombre}'")

    def buscarNombre(self, nombre):
        posicion = 0
        actual = self.cabeza

        while actual is not None:
            if actual.nombre == nombre:
                self.registrar(f"El nombre '{nombre}' se encuentra en la posición {posicion}")
                return True
            actual = actual.siguiente
            posicion += 1

        self.registrar(f"El nombre '{nombre}' no se encontró en la lista")
        return False

    def buscar(self, nombre):
        return self.buscarNombre(nombre)

    def sustituir(self, nombre_actual, nombre_nuevo):
        if self.listaVacia():
            self.registrar("La lista está vacía, no hay elementos para sustituir")
            return False

        actual = self.cabeza
        cambios = 0
        while actual is not None:
            if actual.nombre == nombre_actual:
                actual.nombre = nombre_nuevo
                cambios += 1
            actual = actual.siguiente

        if cambios > 0:
            self.registrar(f"Se sustituyó '{nombre_actual}' por '{nombre_nuevo}' en {cambios} registro(s)")
            return True

        self.registrar(f"No se encontró '{nombre_actual}' para sustituir")
        return False

    @staticmethod
    def normalizarTexto(nombre):
        nombre = unicodedata.normalize("NFD", nombre)
        nombre = nombre.encode("ascii", "ignore").decode("ascii")
        return nombre.lower()

    def ordenarLista(self):
        if self.cabeza is None or self.cabeza.siguiente is None:
            self.registrar("La lista no requiere ordenamiento")
            return False

        actual = self.cabeza
        while actual is not None:
            siguiente = actual.siguiente
            while siguiente is not None:
                if self.normalizarTexto(siguiente.nombre) < self.normalizarTexto(actual.nombre):
                    actual.nombre, siguiente.nombre = siguiente.nombre, actual.nombre
                siguiente = siguiente.siguiente
            actual = actual.siguiente

        self.registrar("La lista fue ordenada alfabéticamente")
        return True

    def imprimirAdelante(self):
        actual = self.cabeza
        elementos = []

        while actual is not None:
            elementos.append(actual.nombre)
            actual = actual.siguiente

        if not elementos:
            self.registrar("La lista está vacía")
            return

        self.registrar(" -> ".join(elementos))

    def generarReporte(self):
        mensaje = "Reporte generado"
        print(mensaje)
        with open(self.reporte_path, "a", encoding="utf-8") as archivo:
            archivo.write(mensaje + "\n")
        return self.reporte_path


def cargarDesdeArchivo(lista):
    try:
        with open("datos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                nombre = linea.strip()
                if nombre != "":
                    lista.insertarAlFinal(nombre)

        lista.registrar(f"Se cargaron {lista.getTamano()} nombres desde datos.txt")
    except FileNotFoundError:
        lista.registrar("No se encontró el archivo datos.txt")


def menu():
    lista = ListaDoblemente()
    lista.registrar("Inicio del sistema")

    while True:
        print("\n===== MENU =====")
        print("1. Cargar nombres desde datos.txt")
        print("2. Mostrar lista")
        print("3. Buscar nombre")
        print("4. Sustituir nombre")
        print("5. Ordenar lista")
        print("6. Generar reporte final")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            cargarDesdeArchivo(lista)
        elif opcion == "2":
            if lista.listaVacia():
                lista.registrar("La lista está vacía")
            else:
                lista.imprimirAdelante()
        elif opcion == "3":
            nombre = input("Ingrese el nombre a buscar: ").strip()
            lista.buscarNombre(nombre)
        elif opcion == "4":
            nombre_actual = input("Ingrese el nombre a sustituir: ").strip()
            nombre_nuevo = input("Ingrese el nuevo nombre: ").strip()
            lista.sustituir(nombre_actual, nombre_nuevo)
        elif opcion == "5":
            lista.ordenarLista()
            if not lista.listaVacia():
                print("Lista ordenada:")
                lista.imprimirAdelante()
        elif opcion == "6":
            lista.generarReporte()
        elif opcion == "0":
            lista.registrar("Fin del sistema")
            print("Gracias por usar el programa.")
            break
        else:
            lista.registrar("Opción inválida")


if __name__ == "__main__":
    menu()

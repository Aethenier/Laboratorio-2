import unicodedata
from datetime import datetime


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
        self.historial = []
        self.reporte_path = "reporte.txt"
        self._crear_reporte()

    def _crear_reporte(self):
        with open(self.reporte_path, "w", encoding="utf-8") as archivo:
            archivo.write("=== REPORTE DE ACTIVIDADES ===\n")

    def _registrar_evento(self, metodo, detalle):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        registro = f"[{fecha}] {metodo}: {detalle}\n"
        self.historial.append(registro)
        with open(self.reporte_path, "a", encoding="utf-8") as archivo:
            archivo.write(registro)

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
        self._registrar_evento("insertarAlFinal", f"Se inserto '{nombre}'")

    def buscarNombre(self, nombre):
        posicion = 0
        actual = self.cabeza
        while actual is not None:
            if actual.nombre == nombre:
                detalle = f"El nombre '{nombre}' se encontro en la posicion {posicion}"
                print(detalle)
                self._registrar_evento("buscarNombre", detalle)
                return True
            actual = actual.siguiente
            posicion += 1

        detalle = f"El nombre '{nombre}' no se encontro en la lista"
        print(detalle)
        self._registrar_evento("buscarNombre", detalle)
        return False

    def buscar(self, nombre):
        return self.buscarNombre(nombre)

    def sustituir(self, nombre_actual, nombre_nuevo):
        if self.listaVacia():
            detalle = "La lista esta vacia, no hay elementos para sustituir"
            print(detalle)
            self._registrar_evento("sustituir", detalle)
            return False

        actual = self.cabeza
        cambios = 0
        while actual is not None:
            if actual.nombre == nombre_actual:
                actual.nombre = nombre_nuevo
                cambios += 1
            actual = actual.siguiente

        if cambios > 0:
            detalle = f"Se sustituyo '{nombre_actual}' por '{nombre_nuevo}' en {cambios} registro(s)"
            print(detalle)
            self._registrar_evento("sustituir", detalle)
            return True

        detalle = f"No se encontro '{nombre_actual}' para sustituir"
        print(detalle)
        self._registrar_evento("sustituir", detalle)
        return False

    @staticmethod
    def normalizarTexto(nombre):
        nombre = unicodedata.normalize("NFD", nombre)
        nombre = nombre.encode("ascii", "ignore").decode("ascii")
        return nombre.lower()

    def ordenarLista(self):
        if self.cabeza is None or self.cabeza.siguiente is None:
            detalle = "La lista no requiere ordenamiento"
            print(detalle)
            self._registrar_evento("ordenarLista", detalle)
            return False

        actual = self.cabeza
        while actual is not None:
            siguiente = actual.siguiente
            while siguiente is not None:
                if self.normalizarTexto(siguiente.nombre) < self.normalizarTexto(actual.nombre):
                    actual.nombre, siguiente.nombre = siguiente.nombre, actual.nombre
                siguiente = siguiente.siguiente
            actual = actual.siguiente

        detalle = "La lista fue ordenada alfabeticamente"
        print(detalle)
        self._registrar_evento("ordenarLista", detalle)
        return True

    def imprimirAdelante(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.nombre, end=" -> ")
            actual = actual.siguiente
        print("None")

    def generarReporte(self):
        with open(self.reporte_path, "w", encoding="utf-8") as archivo:
            archivo.write("=== REPORTE FINAL DEL USUARIO ===\n")
            archivo.write(f"Cantidad de eventos registrados: {len(self.historial)}\n\n")
            archivo.write("Historial:\n")
            for registro in self.historial:
                archivo.write(registro)

        print(f"\nReporte generado en: {self.reporte_path}")
        return self.reporte_path


def cargarDesdeArchivo(lista):
    try:
        with open("datos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                nombre = linea.strip()
                if nombre != "":
                    lista.insertarAlFinal(nombre)
        detalle = f"Se cargaron {lista.getTamano()} nombres desde datos.txt"
        print(detalle)
        lista._registrar_evento("cargarDesdeArchivo", detalle)
    except FileNotFoundError:
        detalle = "No se encontro el archivo datos.txt"
        print(detalle)
        lista._registrar_evento("cargarDesdeArchivo", detalle)


def menu():
    lista = ListaDoblemente()
    lista._registrar_evento("inicio", "Se inicio la aplicacion")

    while True:
        print("\n===== MENU =====")
        print("1. Cargar nombres desde datos.txt")
        print("2. Mostrar lista")
        print("3. Buscar nombre")
        print("4. Sustituir nombre")
        print("5. Ordenar lista")
        print("6. Generar reporte final")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            cargarDesdeArchivo(lista)
        elif opcion == "2":
            if lista.listaVacia():
                print("La lista esta vacia.")
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
            lista._registrar_evento("salir", "El usuario salio del sistema")
            print("Gracias por usar el programa.")
            break
        else:
            print("Opcion invalida, intente otra vez.")


if __name__ == "__main__":
    menu()

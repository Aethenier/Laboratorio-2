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

    def buscarNombre(self, nombre):
        posicion = 0
        actual = self.cabeza

        while actual is not None:
            if actual.nombre == nombre:
                print(f"El nombre {nombre} se encuentra en la posicion {posicion}")
                return True
            actual = actual.siguiente
            posicion += 1

        return False

    @staticmethod
    def _normalizar(nombre):
        nombre = unicodedata.normalize("NFD", nombre)
        nombre = nombre.encode("ascii", "ignore").decode("ascii")
        return nombre.lower()

    def ordenarLista(self):
        if self.cabeza is None or self.cabeza.siguiente is None:
            return

        actual = self.cabeza.siguiente
        while actual is not None:
            temp = actual
            while temp.anterior is not None and self._normalizar(temp.nombre) < self._normalizar(temp.anterior.nombre):
                temp.anterior.nombre, temp.nombre = temp.nombre, temp.anterior.nombre
                temp = temp.anterior
            actual = actual.siguiente

    def sustituir(self, posicion, palabra):
        if self.listaVacia():
            print("Lista vacia.")
        actual = self.cabeza

        while actual is not None:
            if posicion < 0  or posicion >= self.tam:
                print("Posicion invalida.")
                return False

        actual = self.cabeza
        indice = 0

        while actual is not None:
            if indice == posicion:
                actual.producto = palabra
                print(f"Posicion {posicion} sustuida por '{palabra}'.")
                return True
            actual = actual.siguiente
            indice += 1

        return False

    def imprimirAdelante(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.nombre)
            actual = actual.siguiente


if __name__ == "__main__":
    lista = ListaDoblemente()
    try:
        with open("datos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                nombre = linea.strip()
                if nombre != "":
                    lista.insertarAlFinal(nombre)

        print("Lista original:")
        lista.imprimirAdelante()

        lista.ordenarLista()

        print("\nLista ordenada alfabeticamente:")
        lista.imprimirAdelante()
        print(f"\nCantidad de elementos: {lista.getTamano()}")

    except FileNotFoundError:
        print("Error: el archivo datos.txt no existe.")
        exit()

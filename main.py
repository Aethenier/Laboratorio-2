"""
Hecho por:
Saul Saenz Vargas
Jose Mauricio Ramirez Chinchilla

Link de GitHub:
https://github.com/Aethenier/Laboratorio-2.git
"""



class nodo:
    def __init__(self, producto):
        self.producto = producto
        self.siguiente = None
        self.anterior = None


class ListaDoblemente():
    def __init__(self):
        self.cabeza = None  # Inicio
        self.cola = None    # Fin
        self.tam = 0

    def getTamano(self):
        return self.tam

    def listaVacia(self):
        return self.cabeza is None

    def buscarNombre(self, producto):
        posicion = 0
        if self.listaVacia():
            print("La lista esta vacia")
            return False
        actual = self.cabeza
        while actual is not None:
            if actual.producto == producto:
                print(f"El nombre {producto} se encuentra en la posicion {posicion}")
                return True
            actual = actual.siguiente
            posicion += 1
        return False

  
 





    if __name__ == "__main__":
# Crear la lista doblemente enlazada
    lista = ListaDoblemente()
    try:
        with open("datos.txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                # Evitar líneas vacías
                if linea != "":
                    valor = int(linea)
                    # Insertar el valor en la lista
                    lista.insertarAlInicio(valor)
                    lista.imprimirAdelante()
                    print(f"Cantidad de elementos: {lista.cantidadElementos()}")

    except FileNotFoundError:
        print("Error: el archivo datos.txt no existe.")
        exit()

    except ValueError:
        print("Error: el archivo contiene un dato que no es entero.")
        exit()

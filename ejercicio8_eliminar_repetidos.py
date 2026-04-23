"""
============================================================
  Laboratorio #3 - Ejercicio #8: Eliminar Repetidos
  EDL - Escuela de Ciencias Exactas e Ingeniería

  Estructuras usadas: Pila (origen) + Cola (extraídos)
  - La Pila contiene los datos originales (algunos repetidos).
  - Se extraen TODOS los elementos iguales al dato buscado
    y se guardan en una Cola preservando el orden de llegada
    original a la Pila (orden de inserción = FIFO en la Cola).
  - La Pila se reconstruye con los elementos restantes
    en su orden original.
============================================================
"""

import random


# ── Nodo genérico ────────────────────────────────────────
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# ── Pila (LIFO) ──────────────────────────────────────────
class Pila:
    def __init__(self):
        self._tope = None
        self._tamanio = 0

    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self._tope
        self._tope = nuevo
        self._tamanio += 1

    def pop(self):
        if self.esta_vacia():
            raise IndexError("Pila vacía")
        dato = self._tope.dato
        self._tope = self._tope.siguiente
        self._tamanio -= 1
        return dato

    def esta_vacia(self):
        return self._tope is None

    def tamanio(self):
        return self._tamanio

    def __str__(self):
        elementos = []
        nodo = self._tope
        while nodo:
            elementos.append(str(nodo.dato))
            nodo = nodo.siguiente
        return "Pila [tope→base]: " + " → ".join(elementos) if elementos else "Pila: (vacía)"


# ── Cola (FIFO) ──────────────────────────────────────────
class Cola:
    def __init__(self):
        self._frente = None
        self._final = None
        self._tamanio = 0

    def encolar(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self._frente = nuevo
            self._final = nuevo
        else:
            self._final.siguiente = nuevo
            self._final = nuevo
        self._tamanio += 1

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("Cola vacía")
        dato = self._frente.dato
        self._frente = self._frente.siguiente
        if self._frente is None:
            self._final = None
        self._tamanio -= 1
        return dato

    def esta_vacia(self):
        return self._frente is None

    def tamanio(self):
        return self._tamanio

    def __str__(self):
        elementos = []
        nodo = self._frente
        while nodo:
            elementos.append(str(nodo.dato))
            nodo = nodo.siguiente
        return "Cola [frente→final]: " + " → ".join(elementos) if elementos else "Cola: (vacía)"


# ── Función principal ────────────────────────────────────
def eliminar_repetidos(pila: Pila, dato):
    """
    Extrae de la Pila todos los elementos iguales a 'dato'.
    Los guarda en una Cola en el orden de llegada original a la Pila.
    Reconstruye la Pila con los elementos restantes.

    Lógica:
      1. Vaciamos la Pila → buffer en orden tope→base.
      2. Recorremos en orden inverso (base→tope = push order).
         - Si e == dato → encolar en cola_extraidos.
         - Si e != dato → guardar en lista para reconstruir Pila.
      3. Reconstruimos la Pila empujando en push order original.
      4. Mostramos la Cola de extraídos, el conteo y la Pila final.
    """
    # Paso 1: vaciar la pila → buffer en orden tope→base
    buffer = []
    while not pila.esta_vacia():
        buffer.append(pila.pop())
    # reversed(buffer) = orden original de inserción (base→tope)

    cola_extraidos = Cola()
    restantes = []
    contador = 0

    # Paso 2: clasificar en push order
    for e in reversed(buffer):
        if e == dato:
            cola_extraidos.encolar(e)   # respeta orden de llegada original
            contador += 1
        else:
            restantes.append(e)         # push order de los que quedan

    # Paso 3: reconstruir Pila con los restantes en orden original
    for e in restantes:
        pila.push(e)

    # Paso 4: mostrar resultados
    print(f"Dato buscado   : {dato}")
    print(f"Extraídos      : {cola_extraidos}")
    print(f"Total extraídos: {contador}")
    print(f"Pila restante  : {pila}")


# ── Prueba ────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  EJERCICIO #8 — ELIMINAR REPETIDOS DE UNA PILA")
    print("=" * 55)

    # Caso 1: dato = 3, varios repetidos
    print("\n[ Caso 1: extraer todos los 3 ]")
    print("─" * 45)
    pila1 = Pila()
    numeros1 = [3, 7, 3, 1, 5, 3, 9, 3, 2, 3]
    print(f"Orden de inserción: {numeros1}")
    for n in numeros1:
        pila1.push(n)
    print(f"{pila1}\n")
    eliminar_repetidos(pila1, 3)

    # Caso 2: dato = 7, aparece una sola vez
    print("\n[ Caso 2: extraer todos los 7 (una ocurrencia) ]")
    print("─" * 45)
    pila2 = Pila()
    numeros2 = [1, 7, 2, 7, 4]
    print(f"Orden de inserción: {numeros2}")
    for n in numeros2:
        pila2.push(n)
    print(f"{pila2}\n")
    eliminar_repetidos(pila2, 7)

    # Caso 3: dato = 9, no existe en la pila
    print("\n[ Caso 3: dato que no existe en la pila ]")
    print("─" * 45)
    pila3 = Pila()
    numeros3 = [4, 5, 6, 7, 8]
    print(f"Orden de inserción: {numeros3}")
    for n in numeros3:
        pila3.push(n)
    print(f"{pila3}\n")
    eliminar_repetidos(pila3, 9)

    # Caso 4: pila aleatoria
    print("\n[ Caso 4: pila aleatoria (semilla fija) ]")
    print("─" * 45)
    random.seed(10)
    pila4 = Pila()
    numeros4 = [random.randint(1, 5) for _ in range(15)]
    print(f"Orden de inserción: {numeros4}")
    for n in numeros4:
        pila4.push(n)
    print(f"{pila4}\n")
    eliminar_repetidos(pila4, 3)

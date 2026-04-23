"""
EDL – Laboratorio #3
Ejercicio #8: Eliminar Repetidos de la Pila
============================================
Función que recibe una Pila de enteros (algunos repetidos) y un dato:

  1. Extrae de la Pila TODOS los elementos iguales al dato,
     y los guarda en una Cola sin modificar el orden de llegada
     a la Pila (base → tope).
  2. Muestra los datos en la Cola y el total extraído.
  3. Muestra la Pila resultante tras el proceso.

Implementación OOP en Python – sin clase Nodo.
"""

import random
from collections import deque


# ══════════════════════════════════════════════════════
#  CLASE COLA
# ══════════════════════════════════════════════════════

class Cola:
    """Cola FIFO implementada con collections.deque (sin clase Nodo)."""

    def __init__(self):
        self._datos: deque = deque()

    def encolar(self, dato) -> None:
        self._datos.append(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self._datos.popleft()

    def esta_vacia(self) -> bool:
        return len(self._datos) == 0

    def tamano(self) -> int:
        return len(self._datos)

    def mostrar(self, etiqueta: str = "Cola") -> None:
        print(f"  {etiqueta} (frente → fondo): {list(self._datos)}")

    def __repr__(self):
        return f"Cola({list(self._datos)})"


# ══════════════════════════════════════════════════════
#  CLASE PILA
# ══════════════════════════════════════════════════════

class Pila:
    """Pila LIFO implementada con lista de Python (sin clase Nodo)."""

    def __init__(self):
        self._datos: list = []

    def apilar(self, dato) -> None:
        self._datos.append(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self._datos.pop()

    def esta_vacia(self) -> bool:
        return len(self._datos) == 0

    def tamano(self) -> int:
        return len(self._datos)

    def mostrar(self, etiqueta: str = "Pila") -> None:
        print(f"  {etiqueta} (tope → base): {list(reversed(self._datos))}")

    def __repr__(self):
        return f"Pila({list(reversed(self._datos))})"


# ══════════════════════════════════════════════════════
#  EJERCICIO 8 – Eliminar Repetidos
# ══════════════════════════════════════════════════════

def eliminar_repetidos(pila: Pila, dato) -> Cola:
    """
    Extrae TODAS las ocurrencias de 'dato' de la pila y las
    guarda en una Cola respetando el orden de llegada a la Pila.

    Orden de llegada = orden en que se apilaron (base → tope).

    Estrategia:
      1. Invertir la Pila en 'pila_inv':
           desapilar el tope → apilar en pila_inv
           Al terminar, pila_inv tiene el fondo de la original en el tope.
      2. Recorrer pila_inv (= orden de llegada):
           - Si el elemento == dato  → encolar en cola_extraidos.
           - Si el elemento != dato  → apilar de vuelta en pila.
         Al terminar, 'pila' queda reconstruida en su orden original
         (sin las ocurrencias de dato) y 'cola_extraidos' tiene los
         extraídos en orden de llegada.
    """
    pila_inv       = Pila()
    cola_extraidos = Cola()

    # Paso 1: invertir la pila
    while not pila.esta_vacia():
        pila_inv.apilar(pila.desapilar())

    # Paso 2: procesar en orden de llegada
    while not pila_inv.esta_vacia():
        e = pila_inv.desapilar()        # orden de llegada (primero el de la base)
        if e == dato:
            cola_extraidos.encolar(e)   # va a la cola en orden de llegada
        else:
            pila.apilar(e)              # reconstruye la pila en orden original

    # Mostrar resultados
    cola_extraidos.mostrar(f"Cola de extraídos (dato = {dato})")
    print(f"  Total extraídos   : {cola_extraidos.tamano()}")
    pila.mostrar("Pila resultante")

    return cola_extraidos


# ══════════════════════════════════════════════════════
#  MAIN – DEMOSTRACIÓN
# ══════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 54)
    print("  Ejercicio #8 – Eliminar Repetidos de la Pila")
    print("=" * 54)

    # ── Caso 1: varios repetidos del dato ────────────
    print("\n── Caso 1: múltiples ocurrencias del dato ─────")
    pila1 = Pila()
    numeros1 = [3, 7, 3, 1, 5, 3, 2, 3, 8, 3]
    print(f"  Orden de inserción (base → tope): {numeros1}")
    for n in numeros1:
        pila1.apilar(n)
    pila1.mostrar("Pila inicial")
    print()
    eliminar_repetidos(pila1, 3)

    # ── Caso 2: el dato no existe ─────────────────────
    print("\n── Caso 2: el dato no existe en la pila ───────")
    pila2 = Pila()
    numeros2 = [1, 2, 4, 5, 6]
    print(f"  Orden de inserción: {numeros2}")
    for n in numeros2:
        pila2.apilar(n)
    pila2.mostrar("Pila inicial")
    print()
    eliminar_repetidos(pila2, 99)

    # ── Caso 3: todos los elementos son el dato ───────
    print("\n── Caso 3: todos los elementos son el dato ────")
    pila3 = Pila()
    numeros3 = [7, 7, 7, 7, 7]
    print(f"  Orden de inserción: {numeros3}")
    for n in numeros3:
        pila3.apilar(n)
    pila3.mostrar("Pila inicial")
    print()
    eliminar_repetidos(pila3, 7)

    # ── Caso 4: pila generada aleatoriamente ─────────
    print("\n── Caso 4: pila aleatoria ─────────────────────")
    random.seed(42)
    pila4    = Pila()
    numeros4 = [random.randint(1, 5) for _ in range(15)]
    dato4    = 2
    print(f"  Orden de inserción: {numeros4}")
    for n in numeros4:
        pila4.apilar(n)
    pila4.mostrar("Pila inicial")
    print(f"\n  Eliminando dato = {dato4}")
    eliminar_repetidos(pila4, dato4)

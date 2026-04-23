"""
EDL – Laboratorio #3
Ejercicio #1: Eliminar elemento de la Cola
==========================================
Función que recibe una cola y un dato:
  1. Elimina la primera ocurrencia del dato.
  2. Muestra la cola resultante en orden de llegada.
  3. SIN declarar estructura de datos auxiliar.

Implementación OOP en Python – sin clase Nodo.
"""

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

    def frente(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self._datos[0]

    def esta_vacia(self) -> bool:
        return len(self._datos) == 0

    def tamano(self) -> int:
        return len(self._datos)

    def mostrar(self, etiqueta: str = "Cola") -> None:
        print(f"  {etiqueta} (frente → fondo): {list(self._datos)}")

    def __repr__(self):
        return f"Cola({list(self._datos)})"


# ══════════════════════════════════════════════════════
#  EJERCICIO 1 – Eliminar elemento
# ══════════════════════════════════════════════════════

def eliminar_elemento(cola: Cola, dato) -> None:
    """
    Elimina la PRIMERA ocurrencia de 'dato' en la cola.

    Restricción cumplida: no usa ninguna estructura de datos auxiliar.
    Solo variables escalares: 'n' (entero) y 'encontrado' (booleano).

    Estrategia: ciclar los n elementos de la cola una sola vez.
    El primer elemento que coincida con 'dato' se descarta;
    todos los demás se re-encolan manteniendo el orden original.
    """
    n = cola.tamano()
    encontrado = False

    for _ in range(n):
        frente = cola.desencolar()
        if not encontrado and frente == dato:
            encontrado = True        # se omite esta sola ocurrencia
        else:
            cola.encolar(frente)     # se conserva en la cola

    if encontrado:
        print(f"  Elemento '{dato}' eliminado correctamente.")
    else:
        print(f"  Elemento '{dato}' no se encontró en la cola.")

    cola.mostrar("Cola resultante")


# ══════════════════════════════════════════════════════
#  MAIN – DEMOSTRACIÓN
# ══════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 50)
    print("  Ejercicio #1 – Eliminar elemento de la Cola")
    print("=" * 50)

    # Caso 1: el dato existe (primera ocurrencia)
    cola1 = Cola()
    for v in [10, 20, 30, 40, 30, 50]:
        cola1.encolar(v)
    cola1.mostrar("Cola inicial")
    print("  Eliminando primera ocurrencia de 30:")
    eliminar_elemento(cola1, 30)

    # Caso 2: el dato no existe
    print()
    cola2 = Cola()
    for v in [5, 10, 15, 20]:
        cola2.encolar(v)
    cola2.mostrar("Cola inicial")
    print("  Eliminando dato 99 (no existe):")
    eliminar_elemento(cola2, 99)

    # Caso 3: solo un elemento
    print()
    cola3 = Cola()
    cola3.encolar(42)
    cola3.mostrar("Cola inicial")
    print("  Eliminando dato 42:")
    eliminar_elemento(cola3, 42)

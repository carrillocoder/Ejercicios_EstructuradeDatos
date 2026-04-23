"""
EDL – Laboratorio #3
Ejercicio #2: Invertir una Cola
================================
Función que recibe una cola:
  1. Invierte la cola.
  2. Muestra la cola invertida.
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
#  EJERCICIO 2 – Invertir Cola
# ══════════════════════════════════════════════════════

def invertir_cola(cola: Cola) -> None:
    """
    Invierte la cola IN-PLACE usando recursión.

    Restricción cumplida: no declara ninguna estructura de datos
    auxiliar. Utiliza únicamente la pila de llamadas del sistema
    (call stack) para "recordar" los elementos.

    Idea recursiva:
      1. Desencola el frente.
      2. Invierte recursivamente el resto de la cola.
      3. Encola el frente al fondo → queda en su posición invertida.

    Traza con [1, 2, 3]:
      - Saca 1, invierte [2, 3] → [3, 2], encola 1 → [3, 2, 1] ✓
    """
    if cola.esta_vacia():
        return
    frente = cola.desencolar()
    invertir_cola(cola)       # invierte el resto primero
    cola.encolar(frente)      # el antiguo frente pasa al fondo


# ══════════════════════════════════════════════════════
#  MAIN – DEMOSTRACIÓN
# ══════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 50)
    print("  Ejercicio #2 – Invertir Cola (sin auxiliar)")
    print("=" * 50)

    # Caso 1: cola con varios elementos
    cola1 = Cola()
    for v in [1, 2, 3, 4, 5]:
        cola1.encolar(v)
    cola1.mostrar("Cola original")
    invertir_cola(cola1)
    cola1.mostrar("Cola invertida")

    # Caso 2: cola con strings
    print()
    cola2 = Cola()
    for palabra in ["hola", "mundo", "python", "colas"]:
        cola2.encolar(palabra)
    cola2.mostrar("Cola original")
    invertir_cola(cola2)
    cola2.mostrar("Cola invertida")

    # Caso 3: cola con un solo elemento
    print()
    cola3 = Cola()
    cola3.encolar(99)
    cola3.mostrar("Cola original")
    invertir_cola(cola3)
    cola3.mostrar("Cola invertida")

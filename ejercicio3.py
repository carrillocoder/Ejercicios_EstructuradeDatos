"""
EDL – Laboratorio #3
Ejercicio #3: Mediciones Diarias – Hospital
============================================
Un hospital almacena las mediciones diarias de temperatura de un
paciente con cáncer durante un mes (4 semanas = 28 días) en una
estructura de dato dinámica lineal (Cola).

Requisitos:
  - Imprimir las temperaturas de las 3 ÚLTIMAS semanas (21 días)
    en ORDEN INVERSO (de la más reciente a la más antigua).
  - Calcular e imprimir el PROMEDIO de esas 21 temperaturas.

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
#  EJERCICIO 3 – Mediciones Diarias
# ══════════════════════════════════════════════════════

def mediciones_diarias(cola_temps: Cola) -> None:
    """
    Recibe una Cola con exactamente 28 temperaturas (días 1-28).

    Proceso:
      1. Descarta la primera semana (días 1-7) → 7 dequeue.
      2. Apila las 21 temperaturas restantes (días 8-28) en una Pila.
         Al desapilar salen automáticamente en orden inverso
         (día 28 primero, día 8 último).
      3. Acumula la suma e imprime cada temperatura con su día.
      4. Calcula e imprime el promedio.
    """
    if cola_temps.tamano() != 28:
        print("  ERROR: se esperaban exactamente 28 temperaturas.")
        return

    # Descartar semana 1 (días 1 a 7)
    print("  Descartando semana 1 (días 1-7)...")
    for _ in range(7):
        cola_temps.desencolar()

    # Apilar días 8-28 para invertir el orden de impresión
    pila_inv = Pila()
    for _ in range(21):
        pila_inv.apilar(cola_temps.desencolar())

    # Imprimir en orden inverso y acumular suma
    total = 0.0
    print("\n  Temperaturas – últimas 3 semanas (más reciente → más antigua):")
    print("  " + "-" * 30)
    dia = 28
    while not pila_inv.esta_vacia():
        temp = pila_inv.desapilar()
        print(f"    Día {dia:2d}: {temp:.1f} °C")
        total += temp
        dia -= 1

    promedio = total / 21
    print("  " + "-" * 30)
    print(f"  Promedio de las 21 temperaturas: {promedio:.2f} °C")


# ══════════════════════════════════════════════════════
#  MAIN – DEMOSTRACIÓN
# ══════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 52)
    print("  Ejercicio #3 – Mediciones Diarias – Hospital")
    print("=" * 52)

    # Generar 28 temperaturas aleatorias y cargarlas en la cola
    random.seed(7)
    cola_temps = Cola()

    print("\n  Temperaturas ingresadas (semanas 1 a 4):")
    for dia in range(1, 29):
        temp = round(random.uniform(36.0, 40.5), 1)
        cola_temps.encolar(temp)
        print(f"    Día {dia:2d}: {temp:.1f} °C", end="")
        if dia % 7 == 0:
            print(f"   ← semana {dia // 7}")
        else:
            print()

    print()
    mediciones_diarias(cola_temps)

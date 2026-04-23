"""
============================================================
  Laboratorio #3 - Ejercicio #3: Mediciones Diarias
  EDL - Escuela de Ciencias Exactas e Ingeniería

  Estructuras usadas: Cola (FIFO) + Pila (LIFO)
  - Cola: almacena las 28 temperaturas en orden cronológico.
  - Pila: recibe las últimas 21 temperaturas; al hacer pop
    las entrega de la más reciente a la más antigua (LIFO),
    logrando el orden inverso requerido sin lógica extra.
============================================================
"""

import random


# ── Nodo genérico ────────────────────────────────────────
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


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


# ── Función principal ────────────────────────────────────
def mediciones_diarias():
    """
    1. Carga 28 temperaturas en una Cola (orden cronológico).
    2. Descarta los primeros 7 días (semana 1) con desencolar.
    3. Pasa las 21 restantes a una Pila (acumulando inversión).
    4. Hace pop de la Pila → imprime día 28 → día 8 (inverso).
    5. Calcula e imprime el promedio de las 21 temperaturas.
    """
    cola = Cola()

    # Simular 28 mediciones aleatorias entre 36.0 y 40.5 °C
    temperaturas = [round(random.uniform(36.0, 40.5), 1) for _ in range(28)]

    print("Temperaturas del mes (día 1 → día 28):")
    for i, t in enumerate(temperaturas, 1):
        print(f"  Día {i:2d}: {t}°C")

    for temp in temperaturas:
        cola.encolar(temp)

    # Descartar semana 1 (7 días)
    print("\nDescartando semana 1 (días 1 al 7)...")
    for _ in range(7):
        cola.desencolar()

    # Volcar días 8-28 en la Pila → el tope será el día 28
    pila = Pila()
    total = 0.0

    while not cola.esta_vacia():
        temp = cola.desencolar()
        pila.push(temp)
        total += temp

    # Pop de la Pila → día 28, 27, 26 ... 8
    print("\nTemperaturas últimas 3 semanas en orden INVERSO (día 28 → día 8):")
    dia = 28
    while not pila.esta_vacia():
        print(f"  Día {dia:2d}: {pila.pop()}°C")
        dia -= 1

    promedio = total / 21
    print(f"\nPromedio de las 21 temperaturas: {promedio:.2f}°C")


# ── Prueba ────────────────────────────────────────────────
if __name__ == "__main__":
    random.seed(42)
    print("=" * 50)
    print("  EJERCICIO #3 — MEDICIONES DIARIAS")
    print("=" * 50)
    print()
    mediciones_diarias()

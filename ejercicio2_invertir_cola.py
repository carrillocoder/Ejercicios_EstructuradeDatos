"""
============================================================
  Laboratorio #3 - Ejercicio #2: Invertir una Cola
  EDL - Escuela de Ciencias Exactas e Ingeniería

  Estructura usada: Cola (FIFO)
  - SIN estructura de datos auxiliar declarada explícitamente.
  - Técnica: RECURSIÓN. La pila de llamadas del sistema actúa
    como estructura auxiliar implícita (no declarada por el
    programador). Al desenrollar la recursión, cada elemento
    queda re-encolado en orden inverso al original.
============================================================
"""


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

    def __str__(self):
        elementos = []
        nodo = self._frente
        while nodo:
            elementos.append(str(nodo.dato))
            nodo = nodo.siguiente
        return "Cola [frente→final]: " + " → ".join(elementos) if elementos else "Cola: (vacía)"


# ── Funciones principales ────────────────────────────────
def _invertir_recursivo(cola: Cola):
    """
    Función interna recursiva.

    Traza de ejecución con cola [1, 2, 3, 4, 5]:
      desencola 1  → llama recursivo([2,3,4,5])
        desencola 2  → llama recursivo([3,4,5])
          desencola 3  → llama recursivo([4,5])
            desencola 4  → llama recursivo([5])
              desencola 5  → llama recursivo([])
              ← cola vacía, retorna
              encola 5   → cola: [5]
            ← retorna
            encola 4   → cola: [5, 4]
          ← retorna
          encola 3   → cola: [5, 4, 3]
        ← retorna
        encola 2   → cola: [5, 4, 3, 2]
      ← retorna
      encola 1   → cola: [5, 4, 3, 2, 1]  ✓
    """
    if cola.esta_vacia():
        return
    dato = cola.desencolar()       # Guardamos el frente en la pila de llamadas
    _invertir_recursivo(cola)      # Procesamos el resto
    cola.encolar(dato)             # Al regresar, ponemos el dato al final → invertido


def invertir_cola(cola: Cola):
    """
    Invierte la cola SIN estructura auxiliar declarada explícitamente.
    Muestra la cola invertida por consola.
    """
    _invertir_recursivo(cola)
    print(f"Cola invertida: {cola}")


# ── Pruebas ───────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("  EJERCICIO #2 — INVERTIR UNA COLA")
    print("=" * 50)

    # Caso 1: cola de números
    cola1 = Cola()
    for x in [1, 2, 3, 4, 5]:
        cola1.encolar(x)
    print(f"\nCola original:  {cola1}")
    invertir_cola(cola1)

    # Caso 2: cola de letras
    cola2 = Cola()
    for c in ['A', 'B', 'C', 'D']:
        cola2.encolar(c)
    print(f"\nCola original:  {cola2}")
    invertir_cola(cola2)

    # Caso 3: cola con un solo elemento
    cola3 = Cola()
    cola3.encolar(42)
    print(f"\nCola original:  {cola3}")
    invertir_cola(cola3)

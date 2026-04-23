"""
============================================================
  Laboratorio #3 - Ejercicio #1: Eliminar Elemento
  EDL - Escuela de Ciencias Exactas e Ingeniería

  Estructura usada: Cola (FIFO)
  - Se elimina el dato directamente sobre la cola.
  - SIN estructura de datos auxiliar.
  - Técnica: desencolar del frente y re-encolar al final,
    omitiendo el elemento que se desea eliminar.
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


# ── Función principal ─────────────────────────────────────
def eliminar_elemento(cola: Cola, dato):
    """
    Elimina la primera ocurrencia de 'dato' en la cola
    SIN usar ninguna estructura de datos auxiliar.

    Técnica:
      Se recorre la cola exactamente n veces usando el propio
      mecanismo FIFO: desencolar del frente y re-encolar al final.
      Al encontrar el dato, se omite una sola vez en lugar de
      re-encolarlo, logrando su eliminación sin estructuras extra.
    """
    n = cola.tamanio()
    encontrado = False

    for _ in range(n):
        actual = cola.desencolar()
        if actual == dato and not encontrado:
            encontrado = True          # Omitimos este nodo (eliminado)
        else:
            cola.encolar(actual)       # Re-encolamos manteniendo el orden

    if encontrado:
        print(f"Elemento '{dato}' eliminado exitosamente.")
    else:
        print(f"El elemento '{dato}' no se encontró en la cola.")

    print(cola)


# ── Pruebas ───────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("  EJERCICIO #1 — ELIMINAR ELEMENTO DE UNA COLA")
    print("=" * 50)

    cola = Cola()
    for x in [10, 20, 30, 40, 50]:
        cola.encolar(x)

    print(f"\nCola original: {cola}\n")

    print("→ Eliminando el 30 (elemento del medio):")
    eliminar_elemento(cola, 30)

    print("\n→ Eliminando el 10 (primer elemento):")
    eliminar_elemento(cola, 10)

    print("\n→ Eliminando el 50 (último elemento):")
    eliminar_elemento(cola, 50)

    print("\n→ Eliminando el 99 (no existe):")
    eliminar_elemento(cola, 99)

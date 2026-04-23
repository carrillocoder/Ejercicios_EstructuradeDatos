"""
============================================================
  Laboratorio #3 - Ejercicio #5: Transmilenio
  EDL - Escuela de Ciencias Exactas e Ingeniería

  Estructuras usadas: Cola (FIFO) + Pila (LIFO)
  - Cola (IDA): el bus avanza estación por estación en orden
    de llegada → FIFO es perfecto.
  - Pila (VUELTA): mientras avanza se van apilando estaciones;
    al regresar, el pop entrega exactamente el camino inverso
    → LIFO es perfecto para el retorno por el mismo recorrido.
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

    def encolar(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self._frente = nuevo
            self._final = nuevo
        else:
            self._final.siguiente = nuevo
            self._final = nuevo

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("Cola vacía")
        dato = self._frente.dato
        self._frente = self._frente.siguiente
        if self._frente is None:
            self._final = None
        return dato

    def esta_vacia(self):
        return self._frente is None


# ── Pila (LIFO) ──────────────────────────────────────────
class Pila:
    def __init__(self):
        self._tope = None

    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self._tope
        self._tope = nuevo

    def pop(self):
        if self.esta_vacia():
            raise IndexError("Pila vacía")
        dato = self._tope.dato
        self._tope = self._tope.siguiente
        return dato

    def esta_vacia(self):
        return self._tope is None


# ── Función principal ────────────────────────────────────
def transmilenio(estaciones: list):
    """
    Simula el recorrido de ida (Cola) y vuelta (Pila)
    de un bus de Transmilenio entre origen y destino.

    Parámetros:
      estaciones: lista ordenada de estaciones origen→destino
    """
    cola_ida = Cola()
    pila_vuelta = Pila()

    for est in estaciones:
        cola_ida.encolar(est)

    origen = estaciones[0]
    destino = estaciones[-1]
    print(f"Origen : {origen}")
    print(f"Destino: {destino}")

    print(f"\n{'─'*40}")
    print("CAMINO DE IDA  (origen → destino):")
    print(f"{'─'*40}")
    paso = 1
    while not cola_ida.esta_vacia():
        estacion = cola_ida.desencolar()
        pila_vuelta.push(estacion)          # Apilamos para la vuelta
        print(f"  Parada {paso:2d} ➡  {estacion}")
        paso += 1

    print(f"\n{'─'*40}")
    print("CAMINO DE VUELTA (destino → origen):")
    print(f"{'─'*40}")
    paso = 1
    while not pila_vuelta.esta_vacia():
        estacion = pila_vuelta.pop()        # LIFO: sale en orden inverso
        print(f"  Parada {paso:2d} ⬅  {estacion}")
        paso += 1


# ── Prueba ────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("  EJERCICIO #5 — TRANSMILENIO")
    print("=" * 50)
    print()

    ruta = [
        "Portal Norte",
        "Toberin",
        "Cardio Infantil",
        "Calle 127",
        "Pepe Sierra",
        "Calle 100",
        "Virrey",
        "Calle 72",
        "Calle 63",
        "Terminal del Sur"
    ]

    transmilenio(ruta)

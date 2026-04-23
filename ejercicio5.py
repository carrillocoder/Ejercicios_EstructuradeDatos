"""
EDL – Laboratorio #3
Ejercicio #5: Transmilenio
===========================
Un conductor de Transmilenio maneja de una estación origen
a una estación destino pasando por todas las estaciones.
Una vez en el destino, regresa por el mismo camino.

Mostrar el camino recorrido tanto de IDA como de VUELTA.

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
        print(f"  {etiqueta}: {list(self._datos)}")

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

    def tope(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self._datos[-1]

    def esta_vacia(self) -> bool:
        return len(self._datos) == 0

    def tamano(self) -> int:
        return len(self._datos)

    def mostrar(self, etiqueta: str = "Pila") -> None:
        print(f"  {etiqueta} (tope → base): {list(reversed(self._datos))}")

    def __repr__(self):
        return f"Pila({list(reversed(self._datos))})"


# ══════════════════════════════════════════════════════
#  EJERCICIO 5 – Transmilenio
# ══════════════════════════════════════════════════════

def transmilenio(cola_estaciones: Cola) -> None:
    """
    Muestra el recorrido de IDA (orden de la cola, FIFO)
    y el de VUELTA (orden inverso, usando una Pila).

    Estrategia:
      - Al recorrer la cola de ida, cada estación visitada
        se apila en 'pila_regreso'.
      - Al terminar la ida, se desapila para mostrar el
        camino de vuelta en orden inverso.
      - La cola queda restaurada al finalizar.
    """
    pila_regreso = Pila()
    n = cola_estaciones.tamano()
    origen  = cola_estaciones.frente() if not cola_estaciones.esta_vacia() else "?"

    print(f"  Estación origen  : {origen}")

    # ── Recorrido de IDA ──────────────────────────────
    print("\n  ► Ruta de IDA:")
    for paso in range(1, n + 1):
        estacion = cola_estaciones.desencolar()
        if paso == n:
            print(f"    [{paso:2d}] → {estacion}  ★ DESTINO")
        else:
            print(f"    [{paso:2d}] → {estacion}")
        pila_regreso.apilar(estacion)
        cola_estaciones.encolar(estacion)   # restaurar cola

    destino = pila_regreso.tope() if not pila_regreso.esta_vacia() else "?"
    print(f"\n  Estación destino : {destino}")

    # ── Recorrido de VUELTA ───────────────────────────
    print("\n  ◄ Ruta de REGRESO:")
    paso = 1
    while not pila_regreso.esta_vacia():
        estacion = pila_regreso.desapilar()
        if paso == n:
            print(f"    [{paso:2d}] ← {estacion}  ★ ORIGEN")
        else:
            print(f"    [{paso:2d}] ← {estacion}")
        paso += 1

    print(f"\n  Total estaciones recorridas (ida + vuelta): {n * 2 - 1}")


# ══════════════════════════════════════════════════════
#  MAIN – DEMOSTRACIÓN
# ══════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 52)
    print("  Ejercicio #5 – Transmilenio – Ida y Vuelta")
    print("=" * 52)

    cola_est = Cola()
    estaciones = [
        "Portal Norte",
        "Toberín",
        "Cardio Infantil",
        "Alcalá",
        "Calle 100",
        "Pepe Sierra",
        "Calle 72",
        "El Polo",
        "Flores",
        "Portal Sur"
    ]
    for est in estaciones:
        cola_est.encolar(est)

    print(f"\n  Ruta registrada: {len(estaciones)} estaciones\n")
    transmilenio(cola_est)

"""
============================================================
  Laboratorio #3 - Ejercicio #4: Transacciones Bancarias
  EDL - Escuela de Ciencias Exactas e Ingeniería

  Estructura usada: Cola (FIFO)
  - Las transacciones bancarias llegan y se procesan en
    estricto orden de llegada (FIFO), lo que hace a la Cola
    la estructura ideal para este problema.
  - Cada nodo guarda: (tipo: str, monto: float)
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
            tipo, monto = nodo.dato
            simbolo = "+" if tipo == "deposito" else "-"
            elementos.append(f"{simbolo}${monto:,.0f}")
            nodo = nodo.siguiente
        return "Cola: " + " | ".join(elementos) if elementos else "Cola: (vacía)"


# ── Función principal ────────────────────────────────────
def calcular_resumen(cola: Cola):
    """
    Recorre la cola FIFO procesando cada transacción.
    Calcula:
      - Total de depósitos
      - Total de retiros
      - Balance final = depósitos − retiros
    """
    total_depositos = 0.0
    total_retiros = 0.0

    while not cola.esta_vacia():
        tipo, monto = cola.desencolar()
        if tipo == "deposito":
            total_depositos += monto
        else:
            total_retiros += monto

    balance = total_depositos - total_retiros
    return total_depositos, total_retiros, balance


# ── Prueba ────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 52)
    print("  EJERCICIO #4 — TRANSACCIONES BANCARIAS")
    print("=" * 52)

    cola = Cola()

    # Transacciones: (tipo, monto en pesos colombianos)
    transacciones = [
        ("deposito", 1_000_000),
        ("retiro",     200_000),
        ("deposito",   500_000),
        ("retiro",     150_000),
        ("deposito",   750_000),
        ("retiro",     300_000),
        ("deposito", 2_000_000),
        ("retiro",     500_000),
    ]

    print("\nRegistrando transacciones:")
    print(f"  {'#':<4} {'Tipo':<12} {'Monto':>15}")
    print(f"  {'─'*4} {'─'*12} {'─'*15}")
    for i, (tipo, monto) in enumerate(transacciones, 1):
        cola.encolar((tipo, monto))
        simbolo = "+" if tipo == "deposito" else "-"
        etiqueta = "Depósito" if tipo == "deposito" else "Retiro"
        print(f"  {i:<4} {etiqueta:<12} {simbolo}${monto:>13,.0f}")

    print(f"\n{cola}\n")

    depositos, retiros, balance = calcular_resumen(cola)

    print(f"  {'═' * 40}")
    print(f"  Total depósitos : ${depositos:>15,.0f}")
    print(f"  Total retiros   : ${retiros:>15,.0f}")
    print(f"  {'─' * 40}")
    print(f"  Balance final   : ${balance:>15,.0f}")
    print(f"  {'═' * 40}")

    estado = "POSITIVO ✓" if balance >= 0 else "NEGATIVO ✗"
    print(f"\n  Estado de la cuenta: {estado}")

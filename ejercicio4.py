"""
EDL – Laboratorio #3
Ejercicio #4: Transacciones Bancarias
======================================
Una entidad bancaria guarda en una Cola las transacciones
de un cliente (depósitos y retiros).

Implementar una función que calcule:
  - Total de depósitos
  - Total de retiros
  - Balance final (depósitos – retiros)

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

    def esta_vacia(self) -> bool:
        return len(self._datos) == 0

    def tamano(self) -> int:
        return len(self._datos)

    def mostrar(self, etiqueta: str = "Cola") -> None:
        print(f"  {etiqueta} (frente → fondo): {list(self._datos)}")

    def __repr__(self):
        return f"Cola({list(self._datos)})"


# ══════════════════════════════════════════════════════
#  CLASE TRANSACCION
# ══════════════════════════════════════════════════════

class Transaccion:
    """
    Representa una transacción bancaria.
    Tipo: 'deposito' o 'retiro'.
    """

    DEPOSITO = "deposito"
    RETIRO   = "retiro"

    def __init__(self, tipo: str, monto: float):
        if tipo not in (self.DEPOSITO, self.RETIRO):
            raise ValueError(f"Tipo de transacción inválido: '{tipo}'")
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a 0")
        self.tipo  = tipo
        self.monto = monto

    def __str__(self):
        signo = "+" if self.tipo == self.DEPOSITO else "-"
        return f"  {signo}${self.monto:>12,.2f}   ({self.tipo})"

    def __repr__(self):
        return f"Transaccion({self.tipo}, {self.monto})"


# ══════════════════════════════════════════════════════
#  EJERCICIO 4 – Resumen de Transacciones
# ══════════════════════════════════════════════════════

def resumen_transacciones(cola_tx: Cola) -> None:
    """
    Recorre la cola de transacciones calculando:
      - Total de depósitos
      - Total de retiros
      - Balance final = depósitos - retiros

    La cola queda INTACTA al finalizar (se restaura
    re-encolando cada elemento después de procesarlo).
    """
    total_depositos = 0.0
    total_retiros   = 0.0
    n = cola_tx.tamano()

    for _ in range(n):
        tx = cola_tx.desencolar()

        if tx.tipo == Transaccion.DEPOSITO:
            total_depositos += tx.monto
        else:
            total_retiros += tx.monto

        cola_tx.encolar(tx)           # restaurar la cola

    balance = total_depositos - total_retiros

    print("  " + "─" * 38)
    print(f"  {'Total depósitos':<16} : ${total_depositos:>12,.2f}")
    print(f"  {'Total retiros':<16} : ${total_retiros:>12,.2f}")
    print("  " + "─" * 38)
    estado = "✓ POSITIVO" if balance >= 0 else "✗ NEGATIVO"
    print(f"  {'Balance final':<16} : ${balance:>12,.2f}   {estado}")
    print("  " + "─" * 38)


# ══════════════════════════════════════════════════════
#  MAIN – DEMOSTRACIÓN
# ══════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 50)
    print("  Ejercicio #4 – Transacciones Bancarias")
    print("=" * 50)

    cola_tx = Cola()

    movimientos = [
        (Transaccion.DEPOSITO, 1_500_000),
        (Transaccion.RETIRO,     250_000),
        (Transaccion.DEPOSITO,   800_000),
        (Transaccion.RETIRO,     100_000),
        (Transaccion.DEPOSITO,   500_000),
        (Transaccion.RETIRO,     450_000),
        (Transaccion.DEPOSITO,   200_000),
        (Transaccion.RETIRO,     900_000),
    ]

    print("\n  Historial de transacciones:")
    for tipo, monto in movimientos:
        tx = Transaccion(tipo, monto)
        cola_tx.encolar(tx)
        print(tx)

    print()
    print("  Resumen financiero:")
    resumen_transacciones(cola_tx)

    # Verificar que la cola quedó intacta
    print(f"\n  Cola intacta: {cola_tx.tamano()} transacciones aún en cola ✓")

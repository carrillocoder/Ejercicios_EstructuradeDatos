"""
EDL – Laboratorio #3
Ejercicio #7: Determinar Inverso
==================================
Dadas las Pilas P1, P2 y la Cola C1, implementar:

  Funcion1(P1, C1):
    Determina si la Cola C1 es el INVERSO de la Pila P1.
    (El tope de P1 coincide con el frente de C1, etc.)

  Funcion2(P1, P2):
    Crea una Cola C1 con los elementos de P1 que NO
    están en P2, respetando el orden de llegada a P1.

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

    def _absorber(self, otra: "Pila") -> None:
        """Copia el contenido interno de 'otra' pila (uso interno)."""
        self._datos = list(otra._datos)

    def __repr__(self):
        return f"Pila({list(reversed(self._datos))})"


# ══════════════════════════════════════════════════════
#  FUNCIÓN 1 – ¿C1 es el inverso de P1?
# ══════════════════════════════════════════════════════

def funcion1(p1: Pila, c1: Cola) -> bool:
    """
    Determina si C1 es el INVERSO de P1.

    Un Cola es inversa de una Pila cuando:
      tope(P1) == frente(C1)
      penúltimo(P1) == segundo(C1)  ... y así sucesivamente.

    Ejemplo:
      P1 = [1,2,3,4,5] (tope=5)
      C1 = [5,4,3,2,1] (frente=5)  → C1 ES inverso de P1 ✓

    Estrategia:
      - Se extraen simultáneamente elementos de P1 (desapilar)
        y de C1 (desencolar) comparándolos uno a uno.
      - Se guarda snapshot de C1 en una lista temporal para
        restaurarla; P1 se restaura usando una pila auxiliar.
    """
    if p1.tamano() != c1.tamano():
        return False

    n = p1.tamano()
    es_inverso = True
    pila_aux = Pila()
    cola_snap: list = []        # snapshot de C1 para restaurar

    for _ in range(n):
        ep = p1.desapilar()
        ec = c1.desencolar()
        pila_aux.apilar(ep)
        cola_snap.append(ec)
        if ep != ec:
            es_inverso = False

    # Restaurar P1
    while not pila_aux.esta_vacia():
        p1.apilar(pila_aux.desapilar())

    # Restaurar C1
    for e in cola_snap:
        c1.encolar(e)

    return es_inverso


# ══════════════════════════════════════════════════════
#  FUNCIÓN 2 – Cola con elementos de P1 que no están en P2
# ══════════════════════════════════════════════════════

def funcion2(p1: Pila, p2: Pila) -> Cola:
    """
    Crea una Cola C1 con los elementos de P1 que NO están en P2.
    El orden en C1 respeta el orden de LLEGADA a P1 (base → tope).
    Ambas pilas quedan RESTAURADAS al finalizar.

    Estrategia:
      1. Volcar P2 en un set para búsqueda O(1); restaurar P2.
      2. Invertir P1 en pila_inv para poder recorrerla en
         orden de llegada (base → tope).
      3. Recorrer pila_inv: los que no están en P2 se encolan en C1.
         Todos se acumulan en pila_rb que queda con el mismo
         contenido interno que el P1 original.
      4. Usar _absorber para restaurar P1 desde pila_rb.
    """
    # ── Paso 1: construir conjunto con los elementos de P2 ──
    conj_p2: set = set()
    aux = Pila()
    while not p2.esta_vacia():
        e = p2.desapilar()
        conj_p2.add(e)
        aux.apilar(e)
    while not aux.esta_vacia():          # restaurar P2
        p2.apilar(aux.desapilar())

    # ── Paso 2: invertir P1 para recorrer en orden de llegada ──
    pila_inv = Pila()
    while not p1.esta_vacia():
        pila_inv.apilar(p1.desapilar())

    # ── Paso 3: procesar en orden de llegada y construir C1 ──
    c1      = Cola()
    pila_rb = Pila()             # copia de P1 para restaurarla
    while not pila_inv.esta_vacia():
        e = pila_inv.desapilar()    # orden de llegada (base → tope)
        if e not in conj_p2:
            c1.encolar(e)
        pila_rb.apilar(e)

    # pila_rb._datos es idéntico al _datos original de P1
    p1._absorber(pila_rb)        # restaurar P1

    return c1


# ══════════════════════════════════════════════════════
#  MAIN – DEMOSTRACIÓN
# ══════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 50)
    print("  Ejercicio #7 – Determinar Inverso")
    print("=" * 50)

    # ── Función 1 ────────────────────────────────────
    print("\n── Función 1: ¿C1 es inverso de P1? ──────────")

    p1 = Pila()
    for v in [1, 2, 3, 4, 5]:
        p1.apilar(v)                        # tope = 5

    # C1 correcto: frente = 5 (inverso de P1)
    c1_si = Cola()
    for v in [5, 4, 3, 2, 1]:
        c1_si.encolar(v)

    # C1 incorrecto: frente = 1 (mismo orden, NO inverso)
    c1_no = Cola()
    for v in [1, 2, 3, 4, 5]:
        c1_no.encolar(v)

    # C1 distinto tamaño
    c1_tam = Cola()
    for v in [5, 4, 3]:
        c1_tam.encolar(v)

    p1.mostrar("P1")

    c1_si.mostrar("C1 (frente=5)")
    resultado = funcion1(p1, c1_si)
    print(f"  ¿C1 es inverso de P1? → {resultado}")    # True

    print()
    c1_no.mostrar("C2 (frente=1)")
    resultado = funcion1(p1, c1_no)
    print(f"  ¿C2 es inverso de P1? → {resultado}")    # False

    print()
    c1_tam.mostrar("C3 (solo 3 elementos)")
    resultado = funcion1(p1, c1_tam)
    print(f"  ¿C3 es inverso de P1? → {resultado}")    # False (distinto tamaño)

    # Verificar que P1 quedó restaurada
    print()
    p1.mostrar("P1 después de Función 1 (debe estar intacta)")

    # ── Función 2 ────────────────────────────────────
    print("\n── Función 2: C1 = elementos de P1 que NO están en P2 ──")

    p1 = Pila()
    for v in [1, 2, 3, 4, 5]:
        p1.apilar(v)                # tope = 5

    p2 = Pila()
    for v in [3, 4, 5, 9, 10]:
        p2.apilar(v)                # tope = 10

    p1.mostrar("P1")
    p2.mostrar("P2")
    c_res = funcion2(p1, p2)
    print()
    c_res.mostrar("C1 = P1 \\ P2  (orden de llegada)")

    # Verificar restauración
    print()
    p1.mostrar("P1 restaurada")
    p2.mostrar("P2 restaurada")

    # Caso 2: ningún elemento en común
    print("\n── Caso 2: P1 y P2 sin elementos en común ────")
    p1b = Pila()
    for v in [10, 20, 30]:
        p1b.apilar(v)

    p2b = Pila()
    for v in [1, 2, 3]:
        p2b.apilar(v)

    p1b.mostrar("P1")
    p2b.mostrar("P2")
    c_res2 = funcion2(p1b, p2b)
    c_res2.mostrar("C1 (todos los elementos de P1)")

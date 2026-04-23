"""
============================================================
  Laboratorio #3 - Ejercicio #7: Determinar Inverso
  EDL - Escuela de Ciencias Exactas e Ingeniería

  Estructuras usadas: Pila P1, Pila P2, Cola C1

  Función1(P1, C1):
    Determina si C1 es el INVERSO de P1.
    C1 es inverso de P1 si su secuencia frente→final
    coincide con la secuencia base→tope de P1.

  Función2(P1, P2) → C1:
    Crea una Cola C1 con los elementos de P1 que NO
    están en P2, respetando el orden de inserción de P1.

  Ambas funciones restauran las estructuras originales.
============================================================
"""


# ── Nodo genérico ────────────────────────────────────────
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


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

    def __str__(self):
        elementos = []
        nodo = self._tope
        while nodo:
            elementos.append(str(nodo.dato))
            nodo = nodo.siguiente
        return "Pila [tope→base]: " + " → ".join(elementos) if elementos else "Pila: (vacía)"


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


# ── Función 1 ─────────────────────────────────────────────
def funcion1(p1: Pila, c1: Cola) -> bool:
    """
    Determina si C1 es el inverso de P1.

    Lógica:
      - C1 es inverso de P1 si C1[frente..final] == P1[base..tope].
      - Vaciamos P1 en una pila temporal 'temp'; esto invierte P1,
        por lo que temp.pop() entrega P1 de base→tope.
      - Comparamos cada temp.pop() con c1.desencolar().
      - Restauramos ambas estructuras al terminar.

    Ejemplo:
      P1 (push 1,2,3,4,5 → tope=5): base→tope = [1,2,3,4,5]
      C1 (frente→final) = [1,2,3,4,5]  → inverso = True  ✓
      C1 (frente→final) = [5,4,3,2,1]  → inverso = False ✗
    """
    if p1.tamanio() != c1.tamanio():
        return False

    # Vaciar P1 en temp (invierte P1) y guardar para restaurar
    temp = Pila()
    buffer_p1 = []
    while not p1.esta_vacia():
        dato = p1.pop()
        buffer_p1.append(dato)
        temp.push(dato)

    # Restaurar P1 (buffer está tope→base, push en reversed = base→tope)
    for dato in reversed(buffer_p1):
        p1.push(dato)

    # Comparar temp (base→tope de P1) con C1 (frente→final)
    buffer_c1 = []
    es_inverso = True
    while not temp.esta_vacia():
        v_p1 = temp.pop()        # sale base→tope de P1
        v_c1 = c1.desencolar()
        buffer_c1.append(v_c1)
        if v_p1 != v_c1:
            es_inverso = False

    # Restaurar C1
    for dato in buffer_c1:
        c1.encolar(dato)

    return es_inverso


# ── Función 2 ─────────────────────────────────────────────
def funcion2(p1: Pila, p2: Pila) -> Cola:
    """
    Crea una Cola C1 con los elementos de P1 que NO están en P2.
    El orden en C1 respeta el orden original de inserción en P1.
    Restaura P1 y P2 al terminar.

    Lógica:
      1. Vaciar P2 → conjunto para búsqueda O(1). Restaurar P2.
      2. Vaciar P1 → lista en orden tope→base. Restaurar P1.
      3. Recorrer P1 en orden original (reversed): si el elemento
         no está en P2, se encola en C1.
    """
    # Paso 1: recolectar elementos de P2
    elementos_p2 = set()
    buffer_p2 = []
    while not p2.esta_vacia():
        dato = p2.pop()
        elementos_p2.add(dato)
        buffer_p2.append(dato)
    for dato in reversed(buffer_p2):   # Restaurar P2
        p2.push(dato)

    # Paso 2: vaciar P1 y guardar en buffer
    buffer_p1 = []
    while not p1.esta_vacia():
        buffer_p1.append(p1.pop())     # Orden tope→base
    for dato in reversed(buffer_p1):   # Restaurar P1 (base→tope)
        p1.push(dato)

    # Paso 3: crear C1 con elementos de P1 no en P2 (orden original)
    c1 = Cola()
    for dato in reversed(buffer_p1):   # reversed = base→tope = push order
        if dato not in elementos_p2:
            c1.encolar(dato)

    return c1


# ── Prueba ────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  EJERCICIO #7 — DETERMINAR INVERSO")
    print("=" * 55)

    # ──────────────────────────────────────────────────────
    print("\n[ Función 1: ¿Es C1 el inverso de P1? ]")
    print("─" * 45)

    p1 = Pila()
    for x in [1, 2, 3, 4, 5]:   # tope = 5, base = 1
        p1.push(x)
    print(f"P1: {p1}  (push order: 1→2→3→4→5)")

    # C1 con mismo orden de inserción de P1 → SÍ es inverso
    c1_si = Cola()
    for x in [1, 2, 3, 4, 5]:
        c1_si.encolar(x)
    resultado = funcion1(p1, c1_si)
    print(f"\nC1 = {c1_si}")
    print(f"¿C1 es inverso de P1? → {resultado}")   # True

    # C1 con orden opuesto → NO es inverso
    c1_no = Cola()
    for x in [5, 4, 3, 2, 1]:
        c1_no.encolar(x)
    resultado2 = funcion1(p1, c1_no)
    print(f"\nC1 = {c1_no}")
    print(f"¿C1 es inverso de P1? → {resultado2}")  # False

    # C1 con tamaños distintos
    c1_diff = Cola()
    for x in [1, 2]:
        c1_diff.encolar(x)
    resultado3 = funcion1(p1, c1_diff)
    print(f"\nC1 = {c1_diff}  (tamaño distinto)")
    print(f"¿C1 es inverso de P1? → {resultado3}")  # False

    # ──────────────────────────────────────────────────────
    print("\n" + "─" * 45)
    print("[ Función 2: C1 = elementos de P1 que NO están en P2 ]")
    print("─" * 45)

    p1 = Pila()
    for x in [1, 2, 3, 4, 5, 6]:
        p1.push(x)   # tope = 6

    p2 = Pila()
    for x in [2, 4, 6]:
        p2.push(x)   # P2 contiene {2, 4, 6}

    print(f"P1: {p1}  (push order: 1→2→3→4→5→6)")
    print(f"P2: {p2}  (elementos a excluir: 2, 4, 6)")

    c1_resultado = funcion2(p1, p2)
    print(f"\nC1 = P1 − P2: {c1_resultado}")
    print(f"(P1 restaurada: {p1})")
    print(f"(P2 restaurada: {p2})")

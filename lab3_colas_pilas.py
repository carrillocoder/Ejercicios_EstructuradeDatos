"""
╔══════════════════════════════════════════════════════════════╗
║   EDL – Laboratorio #3: Listas, Colas y Pilas               ║
║   Escuela de Ciencias Exactas e Ingeniería                  ║
║   Ciencias de la Computación e Inteligencia Artificial      ║
║                                                              ║
║   Implementación 100 % Orientada a Objetos en Python        ║
║   ► Sin clase Nodo                                          ║
║   ► Cola usa collections.deque internamente                 ║
║   ► Pila usa list internamente                              ║
╚══════════════════════════════════════════════════════════════╝
"""

import random
from collections import deque
from typing import Optional


# ══════════════════════════════════════════════════════════════
#  ESTRUCTURAS BASE: Cola y Pila
# ══════════════════════════════════════════════════════════════

class Cola:
    """
    Cola FIFO (First In, First Out).
    Implementada internamente con collections.deque — sin clase Nodo.
    """

    def __init__(self):
        self._datos: deque = deque()

    # ── operaciones principales ──────────────────────────────

    def encolar(self, dato) -> None:
        """Agrega un elemento al fondo de la cola."""
        self._datos.append(dato)

    def desencolar(self):
        """Extrae y retorna el elemento del frente de la cola."""
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self._datos.popleft()

    def frente(self):
        """Consulta (sin extraer) el elemento del frente."""
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self._datos[0]

    # ── consultas ────────────────────────────────────────────

    def esta_vacia(self) -> bool:
        return len(self._datos) == 0

    def tamano(self) -> int:
        return len(self._datos)

    # ── visualización ────────────────────────────────────────

    def mostrar(self, etiqueta: str = "Cola") -> None:
        print(f"  {etiqueta} (frente → fondo): {list(self._datos)}")

    def __repr__(self):
        return f"Cola({list(self._datos)})"


class Pila:
    """
    Pila LIFO (Last In, First Out).
    Implementada internamente con una lista de Python — sin clase Nodo.
    """

    def __init__(self):
        self._datos: list = []

    # ── operaciones principales ──────────────────────────────

    def apilar(self, dato) -> None:
        """Agrega un elemento en el tope de la pila."""
        self._datos.append(dato)

    def desapilar(self):
        """Extrae y retorna el elemento del tope de la pila."""
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self._datos.pop()

    def tope(self):
        """Consulta (sin extraer) el elemento del tope."""
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self._datos[-1]

    # ── consultas ────────────────────────────────────────────

    def esta_vacia(self) -> bool:
        return len(self._datos) == 0

    def tamano(self) -> int:
        return len(self._datos)

    # ── visualización ────────────────────────────────────────

    def mostrar(self, etiqueta: str = "Pila") -> None:
        print(f"  {etiqueta} (tope → base): {list(reversed(self._datos))}")

    # ── utilidad interna (no rompe encapsulamiento externo) ──

    def _absorber(self, otra: "Pila") -> None:
        """
        Reemplaza el contenido interno por el de 'otra' pila.
        Usado en funciones que necesitan restaurar la pila
        sin una inversión extra.
        """
        self._datos = list(otra._datos)

    def __repr__(self):
        return f"Pila(tope→base: {list(reversed(self._datos))})"


# ══════════════════════════════════════════════════════════════
#  EJERCICIO 1 – Eliminar elemento de la Cola
# ══════════════════════════════════════════════════════════════

def eliminar_elemento(cola: Cola, dato) -> None:
    """
    Elimina la PRIMERA ocurrencia de 'dato' en la cola.

    Restricción cumplida: no declara ninguna estructura
    de datos auxiliar — solo variables escalares (n, encontrado).

    Estrategia: se recorren los n elementos ciclando la cola;
    el primero que coincida se descarta, los demás se re-encolan.
    """
    n = cola.tamano()
    encontrado = False

    for _ in range(n):
        frente = cola.desencolar()
        if not encontrado and frente == dato:
            encontrado = True           # se omite esta ocurrencia
        else:
            cola.encolar(frente)        # se conserva en la cola

    msg = f"Elemento {dato} {'eliminado ✓' if encontrado else 'no encontrado ✗'}."
    print(f"  {msg}")
    cola.mostrar("Cola resultante")


# ══════════════════════════════════════════════════════════════
#  EJERCICIO 2 – Invertir la Cola
# ══════════════════════════════════════════════════════════════

def invertir_cola(cola: Cola) -> None:
    """
    Invierte la cola IN-PLACE mediante recursión.

    Restricción cumplida: no declara ninguna estructura
    de datos auxiliar — usa la pila de llamadas del sistema.

    Idea recursiva:
      1. Desencola el frente.
      2. Invierte recursivamente el resto.
      3. Encola el frente al final → queda en posición invertida.
    """
    if cola.esta_vacia():
        return
    frente = cola.desencolar()
    invertir_cola(cola)        # invierte el resto primero
    cola.encolar(frente)       # el antiguo frente pasa al fondo


# ══════════════════════════════════════════════════════════════
#  EJERCICIO 3 – Mediciones Diarias (hospital)
# ══════════════════════════════════════════════════════════════

def mediciones_diarias(cola_temps: Cola) -> None:
    """
    Recibe una cola con exactamente 28 temperaturas (4 semanas).
    Imprime las últimas 21 (semanas 2-4) en orden INVERSO
    (de la más reciente a la más antigua) y calcula su promedio.
    """
    if cola_temps.tamano() != 28:
        print("  ERROR: se esperaban exactamente 28 temperaturas.")
        return

    # Descartar la primera semana (días 1-7)
    for _ in range(7):
        cola_temps.desencolar()

    # Cargar las 21 restantes en una Pila → al desapilar quedan invertidas
    pila_inv = Pila()
    for _ in range(21):
        pila_inv.apilar(cola_temps.desencolar())

    total = 0.0
    print("  Temperaturas – últimas 3 semanas (más reciente → más antigua):")
    dia = 28
    while not pila_inv.esta_vacia():
        temp = pila_inv.desapilar()
        print(f"    Día {dia:2d}: {temp:.1f} °C")
        total += temp
        dia -= 1

    print(f"\n  Promedio de las 21 temperaturas: {total / 21:.2f} °C")


# ══════════════════════════════════════════════════════════════
#  EJERCICIO 4 – Transacciones Bancarias
# ══════════════════════════════════════════════════════════════

class Transaccion:
    """Representa una transacción bancaria (depósito o retiro)."""

    DEPOSITO = "deposito"
    RETIRO   = "retiro"

    def __init__(self, tipo: str, monto: float):
        if tipo not in (self.DEPOSITO, self.RETIRO):
            raise ValueError(f"Tipo de transacción inválido: '{tipo}'")
        self.tipo  = tipo
        self.monto = monto

    def __str__(self):
        signo = "+" if self.tipo == self.DEPOSITO else "-"
        return f"  {signo}${self.monto:>12,.2f}   ({self.tipo})"


def resumen_transacciones(cola_tx: Cola) -> None:
    """
    Calcula total depósitos, total retiros y balance final.
    La cola queda intacta después del recorrido.
    """
    total_dep = 0.0
    total_ret = 0.0
    n = cola_tx.tamano()

    for _ in range(n):
        tx = cola_tx.desencolar()
        if tx.tipo == Transaccion.DEPOSITO:
            total_dep += tx.monto
        else:
            total_ret += tx.monto
        cola_tx.encolar(tx)                # se restaura la cola

    balance = total_dep - total_ret
    print(f"  Total depósitos : ${total_dep:>12,.2f}")
    print(f"  Total retiros   : ${total_ret:>12,.2f}")
    print(f"  {'─'*30}")
    print(f"  Balance final   : ${balance:>12,.2f}")


# ══════════════════════════════════════════════════════════════
#  EJERCICIO 5 – Transmilenio
# ══════════════════════════════════════════════════════════════

def transmilenio(cola_estaciones: Cola) -> None:
    """
    Muestra el recorrido de IDA (en orden de la cola)
    y el de REGRESO (en orden inverso, usando una pila).
    La cola de estaciones queda restaurada al finalizar.
    """
    pila_regreso = Pila()
    n = cola_estaciones.tamano()

    print("  ► Ruta de IDA:")
    for _ in range(n):
        estacion = cola_estaciones.desencolar()
        print(f"      → {estacion}")
        pila_regreso.apilar(estacion)
        cola_estaciones.encolar(estacion)   # restaurar cola

    print("\n  ◄ Ruta de REGRESO:")
    while not pila_regreso.esta_vacia():
        print(f"      ← {pila_regreso.desapilar()}")


# ══════════════════════════════════════════════════════════════
#  EJERCICIO 6 – Gestión de Tareas con Prioridad
# ══════════════════════════════════════════════════════════════

class SistemaGestionTareas:
    """
    Gestiona dos colas: alta y baja prioridad.
    Las tareas de ALTA prioridad se extraen primero (FIFO dentro de cada nivel).
    Muestra el estado completo tras cada operación.
    """

    ALTA = "alta"
    BAJA = "baja"

    def __init__(self):
        self._alta: Cola = Cola()
        self._baja: Cola = Cola()

    def agregar_tarea(self, tarea: str, prioridad: str) -> None:
        """Agrega una tarea a la cola correspondiente según su prioridad."""
        if prioridad == self.ALTA:
            self._alta.encolar(tarea)
        else:
            self._baja.encolar(tarea)
        print(f"  [AGREGAR] '{tarea}'  →  prioridad {prioridad.upper()}")
        self._mostrar_estado()

    def extraer_tarea(self) -> Optional[str]:
        """Extrae la tarea más prioritaria disponible."""
        if not self._alta.esta_vacia():
            tarea = self._alta.desencolar()
        elif not self._baja.esta_vacia():
            tarea = self._baja.desencolar()
        else:
            print("  [EXTRAER] No hay tareas pendientes.")
            return None
        print(f"  [EXTRAER] Procesando: '{tarea}'")
        self._mostrar_estado()
        return tarea

    def _mostrar_estado(self) -> None:
        alta = list(self._alta._datos)
        baja = list(self._baja._datos)
        print(f"           Estado → ALTA: {alta}")
        print(f"                    BAJA: {baja}")


# ══════════════════════════════════════════════════════════════
#  EJERCICIO 7 – Determinar Inverso
# ══════════════════════════════════════════════════════════════

def funcion1(p1: Pila, c1: Cola) -> bool:
    """
    Función 1: determina si C1 es el INVERSO de P1.

    El tope de P1 debe coincidir con el frente de C1,
    el segundo elemento de P1 con el segundo de C1, etc.
    Ambas estructuras quedan restauradas al finalizar.
    """
    if p1.tamano() != c1.tamano():
        return False

    n = p1.tamano()
    es_inverso = True
    pila_aux = Pila()
    cola_snap: list = []       # lista temporal solo para snapshot de c1

    for _ in range(n):
        ep = p1.desapilar()
        ec = c1.desencolar()
        pila_aux.apilar(ep)
        cola_snap.append(ec)
        if ep != ec:
            es_inverso = False

    # Restaurar P1 (pila_aux es el reverso → al desapilar y apilar queda igual)
    while not pila_aux.esta_vacia():
        p1.apilar(pila_aux.desapilar())

    # Restaurar C1
    for e in cola_snap:
        c1.encolar(e)

    return es_inverso


def funcion2(p1: Pila, p2: Pila) -> Cola:
    """
    Función 2: crea Cola C1 con los elementos de P1 que NO están en P2.

    El orden en C1 respeta el orden de llegada a P1 (base → tope).
    Ambas pilas quedan restauradas al finalizar.
    """
    # ── Paso 1: recolectar elementos de P2 en un set (O(1) búsqueda) ──
    conj_p2: set = set()
    aux = Pila()
    while not p2.esta_vacia():
        e = p2.desapilar()
        conj_p2.add(e)
        aux.apilar(e)
    # Restaurar P2 (aux es el reverso de P2)
    while not aux.esta_vacia():
        p2.apilar(aux.desapilar())

    # ── Paso 2: invertir P1 para iterar en orden de llegada ──
    pila_inv = Pila()
    while not p1.esta_vacia():
        pila_inv.apilar(p1.desapilar())

    # ── Paso 3: procesar en orden de llegada y construir C1 ──
    c1      = Cola()
    pila_rb = Pila()           # reconstruye P1 al mismo tiempo
    while not pila_inv.esta_vacia():
        e = pila_inv.desapilar()    # en orden de llegada (base → tope)
        if e not in conj_p2:
            c1.encolar(e)
        pila_rb.apilar(e)

    # pila_rb._datos == p1._datos original → restaurar usando _absorber
    p1._absorber(pila_rb)

    return c1


# ══════════════════════════════════════════════════════════════
#  EJERCICIO 8 – Eliminar Repetidos de la Pila
# ══════════════════════════════════════════════════════════════

def eliminar_repetidos(pila: Pila, dato) -> None:
    """
    Extrae TODAS las ocurrencias de 'dato' de la pila y las
    guarda en una cola respetando el orden de llegada a la pila.
    Muestra la cola de extraídos y la pila resultante.

    Estrategia:
      1. Invertir la pila → permite recorrer en orden de llegada.
      2. Procesar: los iguales a 'dato' van a la cola;
         los demás se re-apilan directamente (reconstruyen la pila
         en su orden original).
    """
    pila_inv       = Pila()
    cola_extraidos = Cola()

    # Paso 1: invertir para procesar en orden de llegada
    while not pila.esta_vacia():
        pila_inv.apilar(pila.desapilar())

    # Paso 2: procesar en orden de llegada
    while not pila_inv.esta_vacia():
        e = pila_inv.desapilar()
        if e == dato:
            cola_extraidos.encolar(e)
        else:
            pila.apilar(e)      # reconstruye pila en orden original

    # Resultados
    cola_extraidos.mostrar(f"Cola de extraídos (dato = {dato})")
    print(f"  Total extraídos : {cola_extraidos.tamano()}")
    pila.mostrar("Pila resultante")


# ══════════════════════════════════════════════════════════════
#  UTILIDADES DE PRESENTACIÓN
# ══════════════════════════════════════════════════════════════

def titulo(n: int, texto: str) -> None:
    linea = "═" * 60
    print(f"\n{linea}")
    print(f"  Ejercicio #{n} – {texto}")
    print(linea)


# ══════════════════════════════════════════════════════════════
#  MAIN – DEMOSTRACIONES DE CADA EJERCICIO
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":

    # ─────────────────────────────────────────────────────────
    # Ejercicio 1: Eliminar elemento
    # ─────────────────────────────────────────────────────────
    titulo(1, "Eliminar elemento de la Cola")
    cola1 = Cola()
    for v in [10, 20, 30, 40, 30, 50]:
        cola1.encolar(v)
    cola1.mostrar("Cola inicial")
    print("  Eliminando primera ocurrencia de 30:")
    eliminar_elemento(cola1, 30)

    # ─────────────────────────────────────────────────────────
    # Ejercicio 2: Invertir Cola
    # ─────────────────────────────────────────────────────────
    titulo(2, "Invertir Cola (recursión, sin auxiliar)")
    cola2 = Cola()
    for v in [1, 2, 3, 4, 5]:
        cola2.encolar(v)
    cola2.mostrar("Cola original")
    invertir_cola(cola2)
    cola2.mostrar("Cola invertida")

    # ─────────────────────────────────────────────────────────
    # Ejercicio 3: Mediciones Diarias
    # ─────────────────────────────────────────────────────────
    titulo(3, "Mediciones Diarias – Hospital")
    cola_temps = Cola()
    random.seed(7)
    print("  28 temperaturas generadas (semanas 1 a 4):")
    temps = [round(random.uniform(36.0, 40.5), 1) for _ in range(28)]
    for i, t in enumerate(temps, 1):
        cola_temps.encolar(t)
        print(f"    Día {i:2d}: {t:.1f} °C", end="\n" if i % 7 == 0 else "   ")
    print()
    mediciones_diarias(cola_temps)

    # ─────────────────────────────────────────────────────────
    # Ejercicio 4: Transacciones Bancarias
    # ─────────────────────────────────────────────────────────
    titulo(4, "Transacciones Bancarias")
    cola_tx = Cola()
    datos_tx = [
        (Transaccion.DEPOSITO, 1_500_000),
        (Transaccion.RETIRO,     250_000),
        (Transaccion.DEPOSITO,   800_000),
        (Transaccion.RETIRO,     100_000),
        (Transaccion.DEPOSITO,   500_000),
        (Transaccion.RETIRO,     450_000),
    ]
    print("  Transacciones registradas:")
    for tipo, monto in datos_tx:
        tx = Transaccion(tipo, monto)
        cola_tx.encolar(tx)
        print(tx)
    print()
    resumen_transacciones(cola_tx)

    # ─────────────────────────────────────────────────────────
    # Ejercicio 5: Transmilenio
    # ─────────────────────────────────────────────────────────
    titulo(5, "Transmilenio – Ida y Vuelta")
    cola_est = Cola()
    estaciones = [
        "Portal Norte", "Toberín", "Cardio Infantil",
        "Alcalá", "Calle 100", "Pepe Sierra",
        "Calle 72", "El Polo", "Flores", "Portal Sur"
    ]
    for est in estaciones:
        cola_est.encolar(est)
    transmilenio(cola_est)

    # ─────────────────────────────────────────────────────────
    # Ejercicio 6: Gestión de Tareas con Prioridad
    # ─────────────────────────────────────────────────────────
    titulo(6, "Gestión de Tareas con Prioridad")
    sgt = SistemaGestionTareas()
    sgt.agregar_tarea("Actualizar documentación",   SistemaGestionTareas.BAJA)
    sgt.agregar_tarea("Servidor caído – revisar",   SistemaGestionTareas.ALTA)
    sgt.agregar_tarea("Bug crítico en producción",  SistemaGestionTareas.ALTA)
    sgt.agregar_tarea("Reunión semanal del equipo", SistemaGestionTareas.BAJA)
    print()
    sgt.extraer_tarea()
    sgt.extraer_tarea()
    sgt.extraer_tarea()

    # ─────────────────────────────────────────────────────────
    # Ejercicio 7: Determinar Inverso
    # ─────────────────────────────────────────────────────────
    titulo(7, "Determinar Inverso")

    p1 = Pila()
    for v in [1, 2, 3, 4, 5]:
        p1.apilar(v)                    # tope = 5

    c1_inv = Cola()
    for v in [5, 4, 3, 2, 1]:          # frente = 5 → sí es inverso
        c1_inv.encolar(v)

    c2_no_inv = Cola()
    for v in [1, 2, 3, 4, 5]:          # frente = 1 → NO es inverso
        c2_no_inv.encolar(v)

    print("  — Función 1: ¿C1 es inverso de P1? —")
    p1.mostrar("P1")
    c1_inv.mostrar("C1 (frente=5, esperado inverso)")
    print(f"  Resultado → {funcion1(p1, c1_inv)}")

    c2_no_inv.mostrar("C2 (frente=1, mismo orden)")
    print(f"  Resultado → {funcion1(p1, c2_no_inv)}")

    print()
    p2 = Pila()
    for v in [3, 4, 5, 9, 10]:
        p2.apilar(v)

    print("  — Función 2: elementos de P1 que NO están en P2 —")
    p1.mostrar("P1")
    p2.mostrar("P2")
    c_res = funcion2(p1, p2)
    c_res.mostrar("C1 = P1 \\ P2  (orden de llegada)")
    p1.mostrar("P1 restaurada")
    p2.mostrar("P2 restaurada")

    # ─────────────────────────────────────────────────────────
    # Ejercicio 8: Eliminar Repetidos
    # ─────────────────────────────────────────────────────────
    titulo(8, "Eliminar Repetidos de la Pila")
    pila8 = Pila()
    numeros = [3, 7, 3, 1, 5, 3, 2, 3, 8, 3]
    for num in numeros:
        pila8.apilar(num)
    pila8.mostrar("Pila inicial (tope→base)")
    print(f"  Extrayendo todas las ocurrencias del dato = 3\n")
    eliminar_repetidos(pila8, 3)

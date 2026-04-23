"""
============================================================
  Laboratorio #3 - Ejercicio #6: Gestión de Tareas
  EDL - Escuela de Ciencias Exactas e Ingeniería

  Estructura usada: Bicola (Deque — Double Ended Queue)
  - Alta prioridad → agregar_frente() → se procesa primero.
  - Baja prioridad → agregar_final()  → se procesa al final.
  - La Bicola permite insertar/extraer por ambos extremos
    en O(1), ideal para una cola de prioridad simple sin
    necesidad de dos estructuras separadas.
  - Cada operación (agregar/extraer) muestra el estado actual.
============================================================
"""

from collections import deque


# ── Bicola (Deque) ────────────────────────────────────────
class Bicola:
    """
    Bicola implementada sobre collections.deque.
    Alta prioridad → frente  |  Baja prioridad → final
    Siempre se procesa desde el frente.
    """

    def __init__(self):
        self._datos = deque()

    def agregar_frente(self, dato):
        """Inserta al frente (alta prioridad) — O(1)."""
        self._datos.appendleft(dato)

    def agregar_final(self, dato):
        """Inserta al final (baja prioridad) — O(1)."""
        self._datos.append(dato)

    def extraer_frente(self):
        """Extrae el elemento de mayor prioridad — O(1)."""
        if self.esta_vacia():
            raise IndexError("Bicola vacía")
        return self._datos.popleft()

    def esta_vacia(self):
        return len(self._datos) == 0

    def tamanio(self):
        return len(self._datos)

    def mostrar_estado(self):
        if self.esta_vacia():
            print("  Estado actual → Bicola: (vacía)\n")
            return
        print("  Estado actual:")
        for i, tarea in enumerate(self._datos):
            indicador = "◀ siguiente" if i == 0 else ""
            print(f"    [{i + 1}] {tarea}  {indicador}")
        print()


# ── Sistema de gestión ────────────────────────────────────
class SistemaGestionTareas:
    def __init__(self):
        self._bicola = Bicola()

    def agregar_tarea(self, nombre: str, prioridad: str):
        """
        Agrega una tarea según su prioridad.
        'alta' → frente de la bicola
        'baja' → final de la bicola
        """
        etiqueta = f"[{'ALTA' if prioridad == 'alta' else 'BAJA'}] {nombre}"
        if prioridad == 'alta':
            self._bicola.agregar_frente(etiqueta)
        else:
            self._bicola.agregar_final(etiqueta)
        print(f"+ AGREGADA ({prioridad.upper()}): {nombre}")
        self._bicola.mostrar_estado()

    def procesar_tarea(self):
        """Extrae y procesa la tarea de mayor prioridad (frente)."""
        if self._bicola.esta_vacia():
            print("⚠ No hay tareas pendientes.\n")
            return
        tarea = self._bicola.extraer_frente()
        print(f"✓ PROCESADA: {tarea}")
        self._bicola.mostrar_estado()


# ── Prueba ────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  EJERCICIO #6 — GESTIÓN DE TAREAS CON BICOLA")
    print("=" * 55)
    print()

    sistema = SistemaGestionTareas()

    # Agregar tareas
    sistema.agregar_tarea("Revisar correos pendientes", "baja")
    sistema.agregar_tarea("Servidor caído - URGENTE", "alta")
    sistema.agregar_tarea("Actualizar documentación", "baja")
    sistema.agregar_tarea("Bug crítico en producción", "alta")
    sistema.agregar_tarea("Reunión de equipo viernes", "baja")

    print("─" * 55)
    print("  Procesando tareas en orden de prioridad:")
    print("─" * 55 + "\n")

    sistema.procesar_tarea()   # Bug crítico (última alta → frente)
    sistema.procesar_tarea()   # Servidor caído (primera alta)

    # Llega nueva tarea urgente
    sistema.agregar_tarea("Parche de seguridad crítico", "alta")

    sistema.procesar_tarea()   # Parche seguridad
    sistema.procesar_tarea()   # Revisar correos (primera baja)
    sistema.procesar_tarea()   # Actualizar docs
    sistema.procesar_tarea()   # Reunión de equipo
    sistema.procesar_tarea()   # Cola vacía

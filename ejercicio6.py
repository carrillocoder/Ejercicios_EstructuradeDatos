"""
EDL – Laboratorio #3
Ejercicio #6: Gestión de Tareas con Prioridad
==============================================
Un sistema gestiona tareas con DOS prioridades:
  - ALTA: se procesan primero (FIFO dentro del nivel).
  - BAJA: se procesan al final (FIFO dentro del nivel).

El sistema debe permitir:
  • Agregar tareas según su prioridad.
  • Extraer tareas según su prioridad.
  • Mostrar el estado de TODAS las tareas tras cada operación.

Implementación OOP en Python – sin clase Nodo.
"""

from collections import deque
from typing import Optional


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

    def elementos(self) -> list:
        return list(self._datos)

    def __repr__(self):
        return f"Cola({list(self._datos)})"


# ══════════════════════════════════════════════════════
#  CLASE SISTEMA DE GESTIÓN DE TAREAS
# ══════════════════════════════════════════════════════

class SistemaGestionTareas:
    """
    Gestiona tareas con dos niveles de prioridad usando dos Colas.

    Estructura interna:
      _cola_alta : Cola → tareas de ALTA prioridad (procesadas primero)
      _cola_baja : Cola → tareas de BAJA prioridad (procesadas al final)

    Cada operación de agregar o extraer muestra el estado actual
    de ambas colas.
    """

    ALTA = "alta"
    BAJA = "baja"

    def __init__(self):
        self._cola_alta: Cola = Cola()
        self._cola_baja: Cola = Cola()

    # ── Operaciones públicas ─────────────────────────

    def agregar_tarea(self, tarea: str, prioridad: str) -> None:
        """
        Agrega una tarea a la cola de alta o baja prioridad.
        Muestra el estado actual después de agregar.
        """
        prioridad = prioridad.lower()
        if prioridad not in (self.ALTA, self.BAJA):
            raise ValueError(f"Prioridad inválida: '{prioridad}'. Use 'alta' o 'baja'.")

        if prioridad == self.ALTA:
            self._cola_alta.encolar(tarea)
        else:
            self._cola_baja.encolar(tarea)

        print(f"  [+] AGREGAR → '{tarea}'  (prioridad {prioridad.upper()})")
        self._mostrar_estado()

    def extraer_tarea(self) -> Optional[str]:
        """
        Extrae la tarea más prioritaria disponible.
        Primero agota todas las de ALTA, luego las de BAJA.
        Muestra el estado actual después de extraer.
        """
        if not self._cola_alta.esta_vacia():
            tarea = self._cola_alta.desencolar()
            nivel = self.ALTA
        elif not self._cola_baja.esta_vacia():
            tarea = self._cola_baja.desencolar()
            nivel = self.BAJA
        else:
            print("  [-] EXTRAER → No hay tareas pendientes.")
            return None

        print(f"  [-] EXTRAER → '{tarea}'  (era de prioridad {nivel.upper()})")
        self._mostrar_estado()
        return tarea

    def total_tareas(self) -> int:
        return self._cola_alta.tamano() + self._cola_baja.tamano()

    # ── Visualización interna ────────────────────────

    def _mostrar_estado(self) -> None:
        alta = self._cola_alta.elementos()
        baja = self._cola_baja.elementos()
        total = len(alta) + len(baja)
        print(f"       Estado actual ({total} tarea(s) pendiente(s)):")
        print(f"         ALTA → {alta if alta else '[vacía]'}")
        print(f"         BAJA → {baja if baja else '[vacía]'}")


# ══════════════════════════════════════════════════════
#  MAIN – DEMOSTRACIÓN
# ══════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 54)
    print("  Ejercicio #6 – Gestión de Tareas con Prioridad")
    print("=" * 54)

    sgt = SistemaGestionTareas()

    # Agregar tareas mezcladas
    print("\n── Agregando tareas ──────────────────────────")
    sgt.agregar_tarea("Actualizar documentación",    SistemaGestionTareas.BAJA)
    print()
    sgt.agregar_tarea("Servidor caído – revisar",    SistemaGestionTareas.ALTA)
    print()
    sgt.agregar_tarea("Bug crítico en producción",   SistemaGestionTareas.ALTA)
    print()
    sgt.agregar_tarea("Reunión semanal del equipo",  SistemaGestionTareas.BAJA)
    print()
    sgt.agregar_tarea("Optimizar consulta de BD",    SistemaGestionTareas.ALTA)
    print()
    sgt.agregar_tarea("Revisar pull requests",       SistemaGestionTareas.BAJA)

    # Extraer tareas (alta primero)
    print("\n── Extrayendo tareas (alta prioridad primero) ─")
    while sgt.total_tareas() > 0:
        print()
        sgt.extraer_tarea()

    print()
    sgt.extraer_tarea()     # intento cuando está vacía

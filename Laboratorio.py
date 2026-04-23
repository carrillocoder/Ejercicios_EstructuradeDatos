# ============================================================
#  Laboratorio de Recursion
#  Ejercicio 1: Mostrar pila en orden invertido (tope al fondo)
# ============================================================

def mostrar_invertida(pila):
    # CASO BASE: pila vacia, no hay nada que mostrar, se detiene la recursion
    if len(pila) == 0:
        return

    # CASO RECURSIVO: extraer el tope, imprimirlo y llamar recursivamente
    tope = pila.pop()        # saca el elemento del tope
    print(tope, end=" ")     # lo imprime
    mostrar_invertida(pila)  # llamada recursiva con la pila reducida


# ============================================================
#  Programa principal
# ============================================================

pila = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("=" * 45)
print("  LABORATORIO RECURSION - Pila Invertida")
print("=" * 45)
print("Pila inicial  (fondo -> tope) : " + str(pila))
print("Salida        (tope  -> fondo): ", end="")

mostrar_invertida(pila)

print()
print("Pila al finalizar             : " + str(pila))
print("=" * 45)
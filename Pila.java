/**
 * Implementación de una Pila (Stack) usando un arreglo estático
 * y una variable índice que apunta a la siguiente posición libre.
 *
 * Reglas del índice:
 *   - indice == 0          -> pila vacía
 *   - indice == capacidad  -> pila llena
 *   - push: arreglo[indice] = valor; indice++
 *   - pop:  indice--; return arreglo[indice]
 */
public class Pila {
    private int[] arreglo;      // Arreglo estático
    private int indice;         // Índice del tope de la pila
    private int capacidad;      // Tamaño máximo
 
    // Constructor
    public Pila(int tamaño) {
        capacidad = tamaño;
        arreglo = new int[capacidad];
        indice = 0;             // El índice empieza en 0 (pila vacía)
    }
 
    // Insertar un elemento (push)
    public void push(int valor) {
        if (indice == capacidad) {
            System.out.println("Error: La pila está llena");
            return;
        }
        arreglo[indice] = valor;   // Guarda el valor en la posición del índice
        indice++;                  // Avanza el índice
    }
 
    // Eliminar un elemento (pop)
    public int pop() {
        if (indice == 0) {
            System.out.println("Error: La pila está vacía");
            return -1;
        }
        indice--;                  // Retrocede el índice
        return arreglo[indice];    // Devuelve el valor en esa posición
    }
 
    // Ver el tope sin eliminarlo
    public int peek() {
        if (indice == 0) {
            System.out.println("Error: La pila está vacía");
            return -1;
        }
        return arreglo[indice - 1];
    }
 
    // Verificar si está vacía
    public boolean estaVacia() {
        return indice == 0;
    }
 
    // Verificar si está llena
    public boolean estaLlena() {
        return indice == capacidad;
    }
 
    // Mostrar el contenido de la pila
    public void mostrar() {
        if (estaVacia()) {
            System.out.println("Pila vacía");
            return;
        }
        System.out.print("Pila (tope -> base): ");
        for (int i = indice - 1; i >= 0; i--) {
            System.out.print(arreglo[i] + " ");
        }
        System.out.println();
    }
 
    // Programa principal de prueba
    public static void main(String[] args) {
        Pila pila = new Pila(5);
 
        pila.push(10);
        pila.push(20);
        pila.push(30);
        pila.mostrar();                                // 30 20 10
 
        System.out.println("Tope: " + pila.peek());    // 30
        System.out.println("Pop:  " + pila.pop());     // 30
        pila.mostrar();                                // 20 10
    }
}
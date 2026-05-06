using System; // Importa las herramiejntas basicas de C#, como la consola.

class Saludo {
    static void Main(string[] args) { // Punto de entrada del programa.
        Console.Write("¿Cuál es tu nombre? "); // Muestra texto sin saltar de linea, para que el usuario escriba.
        string nombre = Console.ReadLine(); // Lee lo que el usuario escribe y lo guarda en la variable "nombre".
        Console.WriteLine("¡Hola, " + nombre + "! Bienvenido."); // Muestra el saludo con salto de linea al final
    }
}

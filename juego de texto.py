import os
import msvcrt  # Módulo para leer la entrada del teclado en Windows

# Representación del laberinto en una lista de listas
laberinto = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '.', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '#', '#'],
    ['#', '#', '#', '#', '#', '.', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', 'P', '#'],
]

def mostrar_laberinto():
    os.system("cls")  # Limpia la consola (Windows)
    for fila in laberinto:
        print("".join(fila))

def encontrar_personaje(P):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == 'P':
                return i, j

def mover_personaje(fila, columna, direccion):
    if direccion == '↑' and laberinto[fila - 1][columna] != '#':
        laberinto[fila][columna] = '.'
        laberinto[fila - 1][columna] = 'P'
    elif direccion == '↓' and laberinto[fila + 1][columna] != '#':
        laberinto[fila][columna] = '.'
        laberinto[fila + 1][columna] = 'P'
    elif direccion == '←' and laberinto[fila][columna - 1] != '#':
        laberinto[fila][columna] = '.'
        laberinto[fila][columna - 1] = 'P'
    elif direccion == '→' and laberinto[fila][columna + 1] != '#':
        laberinto[fila][columna] = '.'
        laberinto[fila][columna + 1] = 'P'

def juego():
    while True:
        mostrar_laberinto()
        fila, columna = encontrar_personaje()
        
        # Leer la entrada del teclado (Windows)
        direccion = msvcrt.getch().decode('utf-8').lower()

        if direccion in ['↑', '↓', '←', '→']:
            mover_personaje(fila, columna, direccion)
        else:
            print("Entrada inválida. Usa ↑ ↓ ← → para mover al personaje.")
        
        # Comprobar condición de victoria
        if laberinto[1][6] == 'P':
            mostrar_laberinto()
            print("¡Has ganado!")
            break

if __name__ == "__main__":
    juego()

# Videojuego de Texto de Recorrer Laberintos
"""
Este proyecto es un videojuego de texto en el que el jugador tiene que recorrer laberintos representados por caracteres ASCII. El objetivo es guiar al personaje (representado por la letra P) a través del laberinto, evitando las paredes (#) y alcanzando la meta (por ejemplo, un punto específico). El jugador puede mover al personaje utilizando las teclas ↑ ↓ ← → de su teclado.
"""
## Instrucciones
"""
1. Ejecuta el archivo `main.py` para comenzar el juego.
2. Sigue las instrucciones en la consola para mover al personaje por el laberinto.
3. Alcanza la meta para ganar el juego.

¡Diviértete y buena suerte!

Este proyecto forma parte de un curso de programación. Si tienes alguna sugerencia o mejora, no dudes en contribuir al repositorio.

---
Realizado por [Tu Nombre]
"""
if __name__ == "__main__":
    # Pedir el nombre del jugador por teclado
    nombre_jugador = input("KEVIN: ")

    # Imprimir un mensaje de bienvenida con el nombre del jugador
    print(f"Bienvenido/a, {nombre_jugador}!")

    juego()
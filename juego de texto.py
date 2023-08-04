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
    
if __name__ == "__main__":
    # Pedir el nombre del jugador por teclado
    nombre_jugador = input("KEVIN: ")

    # Imprimir un mensaje de bienvenida con el nombre del jugador
    print(f"Bienvenido/a, {nombre_jugador}!")

    juego()
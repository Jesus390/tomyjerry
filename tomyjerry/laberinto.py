ancho = int(input("Elija el ancho de su laberinto: "))
alto = int(input("Elija el largo de su laberinto: "))

# Forzar a impar y/o sumar si es impar.
if ancho % 2 == 0:
    ancho += 1

else:
    ancho += 2

if alto % 2 == 0:
    alto += 1

else:
    alto += 2

laberinto = [["#" for columna in range(ancho)] for fila in range(alto)]

# Función de Imprimir Tablero:
def mostrar_tablero(laberinto):
    for fila in laberinto:
        print(" ".join(fila))

import random
def generar_mapa(x, y):
    laberinto[x][y] = "."
    movimientos_posibles = [(0, 2), (0, -2), (2, 0), (-2, 0)]
    random.shuffle(movimientos_posibles)

    for dx, dy in movimientos_posibles:
        nueva_x = x + dx
        nueva_y = y + dy
        
        if 0 <= nueva_x < alto and 0 <= nueva_y < ancho and laberinto[nueva_x][nueva_y] == "#":
            laberinto[x + dx // 2][y + dy // 2] = "."  # Rompe la pared entre ellos
            generar_mapa(nueva_x, nueva_y)


generar_mapa(alto-2, ancho-2)

# Poner la entrada:
laberinto[1][1] = "E"
# Poner la salida:
laberinto[alto-2][ancho-2] = "S"

print("")
mostrar_tablero(laberinto)


# Movimiento de jugador manual:
def juego_manual():
# Movimientos:
    movimientos = {
        "w": (-1, 0),
        "s": (1, 0),
        "a": (0, -1),
        "d": (0, 1)
    }

    x, y = 1, 1
    while True:
        # Condición de salida (si llega a la 'S'):
        if (x, y) == (alto-2, ancho-2):
            print("")
            print("¡Has llegado a la salida!")
            break

        direccion = input("Mover (w/a/s/d): ").lower()

        if direccion not in movimientos:
            print("Dirección inválida. Usa w/a/s/d")
            continue

        dx, dy = movimientos[direccion]
        nueva_x = x + dx
        nueva_y = y + dy

        # Verifica que la nueva posición esté dentro del laberinto
        if 0 <= nueva_x < alto and 0 <= nueva_y < ancho and laberinto[nueva_x][nueva_y] != "#":
            laberinto[x][y] = "."
            
            # Poner la entrada otra vez:
            laberinto[1][1] = "E"

            # Actualiza a la nueva posición
            x, y = nueva_x, nueva_y
            laberinto[x][y] = "O"

            # Muestra el laberinto actualizado
            print("")
            mostrar_tablero(laberinto)

        else:
            print("No se puede chocar con paredes ni salir de los límites")


from collections import deque

def resolver_laberinto_automatico():
    # Tener entrada y salida:
    entrada = 1, 1 
    salida = alto-2, ancho-2

    # Cola para BFS: (posición, camino recorrido)
    cola = deque()
    cola.append((entrada, [entrada])) # Estoy en la celda: (1, 1), y mi camino recorrido hasta ahora son las celdas: [(1, 1)]

    visitado = set()
    visitado.add(entrada)

    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, abajo, izquierda, derecha

    while cola: # Minetras haya elementos en la cola.
        (x, y), camino = cola.popleft()

        if (x, y) == salida:
            for camino_x, camino_y in camino:
                laberinto[camino_x][camino_y] = "x"


            # Poner la entrada:
            laberinto[1][1] = "E"
            # Poner la salida:
            laberinto[alto-2][ancho-2] = "S"

            print("El Laberinto se ha resuelto automáticamente:")
            print("")
            mostrar_tablero(laberinto)
            print("")
            return


        for dx, dy in movimientos:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < alto and 0 <= ny < ancho:
                if laberinto[nx][ny] in [".", "S"] and (nx, ny) not in visitado:
                    visitado.add((nx, ny))
                    cola.append(((nx, ny), camino + [(nx, ny)]))

    print("No se pudo encontrar un camino hasta la salida.")


# Eleccion del usuario:
print("")
eleccion = input("¿Desea resolver el laberinto de forma automatica?(Sí/No): ").lower()

if eleccion ==  "si":
    resolver_laberinto_automatico()

elif eleccion == "no":
    juego_manual()

else:
    print("")
    print('Por favor, elija entre "Sí" o "No')
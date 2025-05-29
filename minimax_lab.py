# dimensiones del tablero
columna = 10
fila = 10

# posiciones iniciales de los jugadores
posicion_raton = (0, 0)
posicion_gato = (-1, -1)

# movimiento para el minimax (columna, fila) (derecha, izquierda, arriba, abajo)
movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
movimientos_manuales = {'d':(0, 1), 'a':(0, -1), 'w':(-1, 0), 's':(1, 0)}

# emojis
gato = '🐱'
raton = '🐭'
background = '⬛'

def tablero():
    return [[background for _ in range(columna)] for j in range(fila)]

def imprimir_tablero(tablero):
    concatenador = ''
    for fila in tablero:
        for columna in fila:
            concatenador += columna
        concatenador += '\n'
    print(concatenador)

def agregar_gato(tablero, posicion):
    tablero[posicion[0]][posicion[1]] = gato

def agregar_raton(tablero, posicion):
    tablero[posicion[0]][posicion[1]] = raton

def tipo_jugador(jugador):
    return '🐭' if jugador.lower()=='r' else '🐱'

def posicion_actual(tablero, jugador):
    jugador = tipo_jugador(jugador)
    pos_actual = (None, None)
    for i, filas in enumerate(tablero):
        for j, _ in enumerate(filas):
            if tablero[i][j] == jugador:
                pos_actual = (i, j)
    return pos_actual

def delimitar_tablero(posicion):
    return posicion[0] < 0 or posicion[0] > columna or posicion[1] < 0 or posicion[1] > fila

def mover(tablero, jugador, movimiento):
    jugador = tipo_jugador(jugador)
    siguiente_movimiento = movimientos_manuales[movimiento]
    pos_actual = posicion_actual(tablero, jugador)
    posicion_tmp = (pos_actual[0]+siguiente_movimiento[0], pos_actual[1]+siguiente_movimiento[1])
    print(pos_actual, siguiente_movimiento, posicion_tmp)
    if delimitar_tablero(posicion_tmp):
        return
    for i, filas in enumerate(tablero):
        for j, _ in enumerate(filas):
            if tablero[i][j] == jugador:
                tablero[i][j] = background
                tablero[i + movimientos_manuales[movimiento][0]][j + movimientos_manuales[movimiento][1]] = jugador
                return

if __name__=="__main__":
    tablero = tablero()

    agregar_gato(tablero, posicion_gato)
    agregar_raton(tablero, posicion_raton)

    imprimir_tablero(tablero)

    mover(tablero, 'R', 'd')
    imprimir_tablero(tablero)
    mover(tablero, 'R', 'w')
    imprimir_tablero(tablero)
    mover(tablero, 'R', 'w')
    imprimir_tablero(tablero)
    mover(tablero, 'R', 'd')
    imprimir_tablero(tablero)

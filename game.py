import time
from tablero import Tablero
from jugador import Raton, Gato
from minimax import Minimax

def juego():
    tablero = Tablero(color='verde', alto=7, largo=7)
    raton = Raton(0, 0)
    gato = Gato(6, 6)
    tablero.agregar_entidad(raton)
    tablero.agregar_entidad(gato)
    tablero.crear()
    tablero.imprimir()

    minimax = Minimax()
    max_turnos = 30

    for turno in range(max_turnos):
        print(f"\nTurno {turno + 1}")

        # Turno gato (maximizador)
        _, mov_gato = minimax.minimax(raton, gato, tablero, 4, 'gato')
        gato.mover(mov_gato)
        tablero.update(gato)
        tablero.imprimir()
        time.sleep(1)

        if raton.posicion_x == gato.posicion_x and raton.posicion_y == gato.posicion_y:
            print("¡El gato atrapó al ratón!")
            break

        # Turno ratón (maximizador)
        _, mov_raton = minimax.minimax(raton, gato, tablero, 4, 'raton')
        raton.mover(mov_raton)
        tablero.update(raton)
        tablero.imprimir()
        time.sleep(1)

        if raton.posicion_x == gato.posicion_x and raton.posicion_y == gato.posicion_y:
            print("¡El gato atrapó al ratón!")
            break
    else:
        print("¡El ratón escapó!")

if __name__ == "__main__":
    juego()

from tomyjerry.functions import cls
from tomyjerry.tablero import Tablero


class GameTomyJerry():
    
    def __init__(self):
        pass

    def es_ganador(self, tablero, jugador_actual, jugador_siguiente):
        if (jugador_actual.posicion_x == jugador_siguiente.posicion_x) and (jugador_actual.posicion_y == jugador_siguiente.posicion_y):
            return (True, (jugador_actual.posicion_x, jugador_actual.posicion_y))
        else:
            return (False, None)

    def run(self):
        print("Bienvenido a GameTomyJerry")

if __name__=="__main__":
    # instancias de entidades
    juego = GameTomyJerry()
    tablero = Tablero()
    gato = Gato(0, 0)
    raton = Raton(7, 7)

    # agregar entidades
    tablero.agregar_entidad(gato)
    tablero.agregar_entidad(raton)

    # crear el tablero
    tablero.crear()

    tablero.imprimir()

    # run game
    juego.run()

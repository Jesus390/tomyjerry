from jugador import Gato, Raton
from functions import cls
from tablero import Tablero


class GameTomyJerry():
    
    def __init__(self):
        pass

    def es_ganador(self, tablero, jugador_actual, jugador_siguiente):
        if (jugador_actual.posicion_x == jugador_siguiente.posicion_x) and (jugador_actual.posicion_y == jugador_siguiente.posicion_y):
            return (True, (jugador_actual.posicion_x, jugador_actual.posicion_y))
        else:
            return (False, None)

    def obtener_movimiento(self):
        while True:
            print("+ Movimientos:\n(w)Arriba\n(a)Izquierda\n(d)Derecha\n(s)Abajo")
            movimiento = input("Ingrese movimiento: ")
            if movimiento in ['w', 'a', 'd', 's']:
                return movimiento

    def run(self):
        print("Bienvenido a GameTomyJerry")
        while True:
            input()
            cls()
            print("Ingrese el movimiento para el raton: ")
            movimiento_raton = self.obtener_movimiento()
            raton.mover(movimiento_raton)
            tablero.update(raton)
            tablero.imprimir()


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

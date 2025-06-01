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

    def obtener_movimiento(self):
        while True:
            cls()
            print("+ Movimientos:\n(w)Arriba\n(a)Izquierda\n(d)Derecha\n(s)Abajo")
            movimiento = input("Ingrese movimiento: ")
            if movimiento in ['w', 'a', 'd', 's']:
                return movimiento

    def run(self):
        print("Bienvenido a GameTomyJerry")
        print(self.obtener_movimiento())

if __name__=="__main__":
    juego = GameTomyJerry()
    juego.run()

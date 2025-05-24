from functions import *
from tablero import Tablero

class GameTomyJerry():
    def __init__(self):
        pass

    def obtener_movimiento(self):
        while True:
            print('''
+ Movimientos:
w - Arriba
a - Izquierda
d - Derecha
s - Abajo
''')
            movimiento = input("Ingrese el movimiento: ")
            if movimiento in ['w', 'a', 'd', 's']:
                return movimiento


    def run(self):
        print("Bienvenido a GameTomyJerry")
        print("El juego se juega en un tablero de 10x10 casillas")
        print("El jugador puede moverse en las cuatro direcciones")

if __name__=="__main__":
    juego = GameTomyJerry()
    juego.run()

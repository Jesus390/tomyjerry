import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_movimiento():
    while True:
        print("+ Movimientos:\n(w)Arriba\n(a)Izquierda\n(d)Derecha\n(s)Abajo")
        movimiento = input("Ingrese movimiento: ")
        if movimiento in ['w', 'a', 'd', 's']:
            return movimiento
from posicion import Posicion

class Entidad():
    def __init__(self, posicion_x, posicion_y):
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.ultima_posicion_x = None
        self.ultima_posicion_y = None

class Jugador(Entidad):
    def __init__(self, nombre, posicion_x, posicion_y, tablero):
        super().__init__(posicion_x, posicion_y)
        self.nombre = nombre
        self.tablero = tablero
        self.movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)] # para el minimax

    def is_movimiento_valido(self, movimiento):
        return 0 <= movimiento[0] < self.tablero.fila and 0 <= movimiento[1] < self.tablero.columna

    def mover(self, movimiento, tablero):
        if self.is_movimiento_valido(movimiento):
            self.posicion_x = self.posicion_x + movimiento[0]
            self.posicion_y = self.posicion_y + movimiento[1]
        
        if movimiento == "w":
            self.mover_arriba()
        elif movimiento == "a":
            self.mover_izquierda()
        elif movimiento == "d":
            self.mover_derecha()
        else:
            self.mover_abajo()
        return (self.posicion_x, self.posicion_y)


class Raton(Jugador):
    emojis = {'full':'🐁', 'cara':'🐭'}

    def __init__(self, pos_x, pos_y, tablero, nombre='Jerry', emoji='full'):
        super().__init__(nombre, pos_x, pos_y, tablero)
        self.emoji = self.emojis[emoji]

class Gato(Jugador):
    emojis = {'full':'🐈', 'cara': '🐱'}
    
    def __init__(self, pos_x, pos_y, tablero, nombre='Tom', emoji='full'):
        super().__init__(nombre, pos_x, pos_y, tablero)
        self.emoji = self.emojis[emoji]

    def __str__(self):
        return f"Class {self.nombre} {self.emoji}"
    
class Obstaculo(Entidad):
    pass

class Pared(Obstaculo):
    emojis = {'default': '🚧', 'ladrillo': '🧱'}

    def __init__(self, pos_x, pos_y, emoji='default'):
        super().__init__(pos_x, pos_y)
        self.emoji = self.emojis[emoji]

    def __str__(self):
        return f"Class {self.pos_x} {self.pos_y} {self.emoji}"

from posicion import Posicion

class Entidad():
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.ultima_fila = None
        self.ultima_columna = None

class Jugador(Entidad):
    def __init__(self, fila, columna):
        super().__init__(fila, columna)
        self.movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)] # para el minimax

    def is_movimiento_valido(self, movimiento, tablero):
        return 0 <= movimiento[0] < tablero.fila and 0 <= movimiento[1] < tablero.columna

    def mover(self, movimiento, tablero):
        if self.is_movimiento_valido(movimiento):
            self.fila = self.fila + movimiento[0]
            self.columna = self.columna + movimiento[1]
        
        if movimiento == "w":
            self.mover_arriba()
        elif movimiento == "a":
            self.mover_izquierda()
        elif movimiento == "d":
            self.mover_derecha()
        else:
            self.mover_abajo()
        return (self.fila, self.columna)


class Raton(Jugador):
    emojis = {'default':'🐭', 'full':'🐁', 'cara':'🐭'}

    def __init__(self, pos_x, pos_y, emoji='default'):
        super().__init__(pos_x, pos_y)
        self.emoji = self.emojis[emoji]

class Gato(Jugador):
    emojis = {'default':'🐱', 'full':'🐈', 'cara': '🐱'}
    
    def __init__(self, pos_x, pos_y, emoji='default'):
        super().__init__(pos_x, pos_y)
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

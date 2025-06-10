import random

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

    def calcular_movimiento(self, movimiento):
        return self.fila+movimiento[0], self.columna+movimiento[1]

    def mover(self, fila, columna):
        self.ultima_columna = self.columna
        self.ultima_fila = self.fila
        self.columna = columna
        self.fila = fila

    def mover_arriba(self):
        return (self.movimientos[1][0], self.movimientos[1][1])
    
    def mover_abajo(self):
        return (self.movimientos[0][0], self.movimientos[0][1])
    
    def mover_izquierda(self):
        return (self.movimientos[3][0], self.movimientos[3][1])
    
    def mover_derecha(self):
        return (self.movimientos[2][0], self.movimientos[2][1])

    def movimientos_disponibles(self, tablero):
        return [(posicion[0], posicion[1]) for posicion in self.movimientos if tablero.is_inTablero(self.fila+posicion[0], self.columna+posicion[1])]
    
    def mover_random(self, tablero):
        return random.choice(self.movimientos_disponibles(tablero))

class Raton(Jugador):
    emojis = {'default':'🐭', 'full':'🐁', 'cara':'🐭'}

    def __init__(self, fila, columna, emoji='default'):
        super().__init__(fila, columna)
        self.emoji = self.emojis[emoji]

class Gato(Jugador):
    emojis = {'default':'🐱', 'full':'🐈', 'cara': '🐱'}
    
    def __init__(self, fila, columna, emoji='default'):
        super().__init__(fila, columna)
        self.emoji = self.emojis[emoji]

    def __str__(self):
        return f"Class {self.nombre} {self.emoji}"
    
class Obstaculo(Entidad):
    pass

class Pared(Obstaculo):
    emojis = {'default': '🚧', 'ladrillo': '🧱'}

    def __init__(self, fila, columna, emoji='default'):
        super().__init__(fila, columna)
        self.emoji = self.emojis[emoji]

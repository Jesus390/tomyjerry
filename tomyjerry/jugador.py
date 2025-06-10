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

    def is_movimiento_valido(self, fila, columna, tablero):
        return 0 <= fila < tablero.fila and 0 <= columna < tablero.columna

    def mover(self, fila, columna):
        self.ultima_columna = self.columna
        self.ultima_fila = self.fila
        self.columna = columna
        self.fila = fila

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

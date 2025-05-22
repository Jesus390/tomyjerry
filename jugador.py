from posicion import Posicion

class Jugador(Posicion):
    def __init__(self, nombre, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.nombre = nombre

    def mover_arriba(self):
        self.pos_y = self.pos_y + 1
    
    def mover_abajo(self):
        self.pos_y = self.pos_y - 1
    
    def mover_derecha(self):
        self.pos_x = self.pos_x + 1

    def mover_izquierda(self):
        self.pos_x = self.pos_x - 1

class Raton(Jugador):
    emojis = {'full':'🐁', 'cara':'🐭'}

    def __init__(self, pos_x, pos_y, nombre='Jerry', emoji='full'):
        super().__init__(nombre, pos_x, pos_y)
        self.emoji = self.emojis[emoji]

class Gato(Jugador):
    emojis = {'full':'🐈', 'cara': '🐱'}
    
    def __init__(self, pos_x, pos_y, nombre='Tom', emoji='full'):
        super().__init__(nombre, pos_x, pos_y)
        self.emoji = self.emojis[emoji]

    def __str__(self):
        return f"Class {self.nombre} {self.emoji}"

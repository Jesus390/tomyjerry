from posicion import Posicion

class Jugador(Posicion):
    def __init__(self, nombre, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.nombre = nombre

class Raton(Jugador):
    emojis = {'raton':'🐁', 'cara':'🐭'}

    def __init__(self, nombre='Jerry', emoji='full'):
        super().__init__(nombre, 0, 0)
        self.emoji = self.emojis[emoji]

class Gato(Jugador):
    emojis = {'full':'🐈', 'cara': '🐱'}
    
    def __init__(self, nombre='Tom', emoji='full'):
        super().__init__(nombre, 0, 0)
        self.emoji = self.emojis[emoji]

    def __str__(self):
        return f"Class {self.nombre} {self.emoji}"

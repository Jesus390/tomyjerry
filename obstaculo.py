from posicion import Posicion

class Pared(Posicion):
    emojis = {'default': '🚧', 'ladrillo': '🧱'}

    def __init__(self, pos_x, pos_y, emoji='default'):
        super().__init__(pos_x, pos_y)
        self.emoji = emoji

    def __str__(self):
        return f"Class {self.pos_x} {self.pos_y} {self.emoji}"

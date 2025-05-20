class Tablero:
    colores = {'blanco': '⬜', 'negro': '⬛', 'azul': '🟦', 'verde': '🟩', 'morado': '🟪', 'amarillo': '🟨', 'rojo': '🟥', 'marron': '🟫', 'naranja': '🟧'}

    def __init__(self, color='blanco', alto=10, largo=10):
        self.color = color
        self.alto = alto
        self.largo = largo

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
    
    def get_alto(self):
        return self.alto

    def set_alto(self, alto):
        self.alto = alto

    def get_largo(self):
        return self.largo
    
    def set_largo(self, largo):
        self.largo = largo

    def crear(self):
        '''
        Crear un tablero de 'x' tamaño alto x largo con el cuadrado blanco en el centro.
        '''
        return (self.colores[self.color] * self.largo + '\n') * self.alto


class TomyJerry:
    emojis_gato = {'full':'🐈', 'cara': '🐱'}
    emojis_raton = {'raton':'🐁', 'cara':'🐭'}

    def __init__(self, emoji_gato='full', emoji_raton='full'):
        self.tom = emoji_gato
        self.jerry = emoji_raton


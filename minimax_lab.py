class Tablero:
    colores = {'blanco': '⬜', 'negro': '⬛', 'azul': '🟦', 'verde': '🟩', 'morado': '🟪', 'amarillo': '🟨', 'rojo': '🟥', 'marron': '🟫', 'naranja': '🟧'}

    def __init__(self, color='blanco'):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color


    def crear(self, alto=10, largo=10):
        '''
        Crear un tablero de 'x' tamaño alto x largo con el cuadrado blanco en el centro.
        '''
        return (self.colores[self.color] * largo + '\n') * alto


class TomyJerry:
    emojis_gato = {'full':'🐈', 'cara': '🐱'}
    emojis_raton = {'raton':'🐁', 'cara':'🐭'}

    def __init__(self, emoji_gato='full', emoji_raton='full'):
        self.tom = emoji_gato
        self.jerry = emoji_raton


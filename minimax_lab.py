class TomyJerry:
    colores_del_cuadro = {'blanco': '⬜', 'negro': '⬛', 'azul': '🟦', 'verde': '🟩', 'morado': '🟪', 'amarillo': '🟨', 'rojo': '🟥', 'marron': '🟫', 'naranja': '🟧'}
    emojis_gato = {'full':'🐈', 'cara': '🐱'}
    emojis_raton = {'raton':'🐁', 'cara':'🐭'}

    def __init__(self, color_cuadro='blanco', emoji_gato='full', emoji_raton='full'):
        self.cuadrado = color_cuadro
        self.tom = emoji_gato
        self.jerry = emoji_raton

    def print_(self):
        print(self.cuadrado['blanco'], self.tom['cara'], self.jerry['cara'])

    def print_tablero(self, alto=10, largo=10):
        '''
        Imprime un tablero de 'x' tamaño alto x largo con el cuadrado blanco en el centro.
        '''
        return (self.cuadrado['blanco'] * largo + '\n') * alto

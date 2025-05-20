class Tablero:
    colores_del_cuadro = {'blanco': '⬜', 'negro': '⬛', 'azul': '🟦', 'verde': '🟩', 'morado': '🟪', 'amarillo': '🟨', 'rojo': '🟥', 'marron': '🟫', 'naranja': '🟧'}

    def __init__(self, color_cuadro='blanco'):
        self.cuadrado = color_cuadro

    def crear(self, alto=10, largo=10):
        '''
        Crear un tablero de 'x' tamaño alto x largo con el cuadrado blanco en el centro.
        '''
        return (self.colores_del_cuadro[self.cuadrado] * largo + '\n') * alto


class TomyJerry:
    emojis_gato = {'full':'🐈', 'cara': '🐱'}
    emojis_raton = {'raton':'🐁', 'cara':'🐭'}

    def __init__(self, emoji_gato='full', emoji_raton='full'):
        self.tom = emoji_gato
        self.jerry = emoji_raton


if __name__=='__main__':
    t = Tablero()
    print(t.crear())


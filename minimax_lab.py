class TomyJerry:
    
    def __init__(self):
        self.cuadrado = {'blanco': '⬜'}
        self.tom = {'gato':'🐈', 'cara': '🐱'} 
        self.jerry = {'raton':'🐁', 'cara':'🐭'}

    def print_(self):
        print(self.cuadrado['blanco'], self.tom['cara'], self.jerry['cara'])

    def print_tablero(self, alto=10, largo=10):
        '''
        Imprime un tablero de 'x' tamaño alto x largo con el cuadrado blanco en el centro.
        '''
        tablero = ''
        for _ in range(alto):
            for _ in range(largo):
                tablero += self.cuadrado['blanco']
            tablero += '\n'
        return tablero

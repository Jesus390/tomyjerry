class Tablero:
    colores = {'blanco': '⬜', 'negro': '⬛', 'azul': '🟦', 'verde': '🟩', 'morado': '🟪', 'amarillo': '🟨', 'rojo': '🟥', 'marron': '🟫', 'naranja': '🟧'}
    tablero = []

    def __init__(self, color='blanco', alto=10, largo=10):
        self.color = color
        self.alto = alto
        self.largo = largo
        if self.alto <=2 or self.largo <=2:
            raise("Error: El tablero debe tener un alto y un largo de al menos 3")

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
        for a in range(self.alto):
            for l in range(self.largo):
                self.tablero.append({
                    'color_de_fondo': self.colores[self.color],
                    'posicion': (a, l),
                    'ocupado': False,
                    })
        return self.tablero
    
    def imprimir(self):
        print(f"Alto: {self.alto}\nLargo: {self.largo}\nLongitud: {len(self.tablero)}\n")
        aux = ''
        for tablero in self.tablero:
            aux += tablero['color_de_fondo']
            if tablero['posicion'][1] == self.largo -1:
                aux += '\n'
        print(aux)
        

class Animal:
    pass

class TomyJerry:
    emojis_gato = {'full':'🐈', 'cara': '🐱'}
    emojis_raton = {'raton':'🐁', 'cara':'🐭'}

    def __init__(self, emoji_gato='full', emoji_raton='full'):
        self.tom = emoji_gato
        self.jerry = emoji_raton


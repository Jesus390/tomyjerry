class Tablero:
    colores = {'blanco': '⬜', 'negro': '⬛', 'azul': '🟦', 'verde': '🟩', 'morado': '🟪', 'amarillo': '🟨', 'rojo': '🟥', 'marron': '🟫', 'naranja': '🟧'}
    tablero = []

    def __init__(self, color='blanco', alto=10, largo=10):
        self.color = color
        self.alto = alto
        self.largo = largo
        if self.alto <= 2:
            raise("Error: El tablero debe tener un alto de al menos 3")
        if self.largo <= 2:
            raise("Error: El tablero debe tener un largo de al menos 3")

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


class Gato(Animal):
    emojis = {'full':'🐈', 'cara': '🐱'}
    
    def __init__(self, nombre='Tom', emoji='full'):
        self.nombre = nombre
        self.emoji = self.emojis[emoji]

    def __str__(self):
        return f"Class {self.nombre} {self.emoji}"


class Raton(Animal):
    emojis = {'raton':'🐁', 'cara':'🐭'}

    def __init__(self, nombre='Jerry', emoji='full'):
        self.nombre = nombre
        self.emoji = self.emojis[emoji]


class Posicion():
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


class Pared(Posicion):
    emojis = {'default': '🚧', 'ladrillo': '🧱'}

    def __init__(self, pos_x, pos_y, emoji='default'):
        super().__init__(pos_x, pos_y)
        self.emoji = emoji

        

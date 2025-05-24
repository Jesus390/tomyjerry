class Tablero:
    colores = {'blanco': '⬜', 'negro': '⬛', 'azul': '🟦', 'verde': '🟩', 'morado': '🟪', 'amarillo': '🟨', 'rojo': '🟥', 'marron': '🟫', 'naranja': '🟧'}
    tablero = []
    endidades = []

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

    def agregar_entidad(self, entidad):
        self.endidades.append(entidad)


    def crear(self):
        '''
        Crear un tablero de 'x' tamaño alto x largo con el cuadrado blanco en el centro.
        '''
        for a in range(self.alto):
            fila = []
            for l in range(self.largo):
                fila.append({
                    'fondo': self.colores[self.color],
                    'posicion': (a, l),
                    'ocupado': False,
                    })
            self.tablero.append(fila)
        
        for entidad in self.endidades:
            self.tablero[entidad.pos_x][entidad.pos_y] = {
                'fondo': entidad.emoji,
                'posicion': (entidad.pos_x, entidad.pos_y),
                'ocupado': True,
            }

        return self.tablero
    
    def update(self, entidad):
        pass
    
    def imprimir(self):
        print(f"Alto: {self.alto}\nLargo: {self.largo}\nLongitud: {len(self.tablero)}\n")
        aux = ''
        for filas in self.tablero:
            for elemento in filas:
                aux += elemento['fondo']
                if elemento['posicion'][1] == self.largo -1:
                    aux += '\n'
        print(aux)
        


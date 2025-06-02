class Tablero:
    colores = {'default': ' . ', 'blanco': '⬜', 'negro': '⬛', 'azul': '🟦', 'verde': '🟩', 'morado': '🟪', 'amarillo': '🟨', 'rojo': '🟥', 'marron': '🟫', 'naranja': '🟧'}
    tablero = []
    endidades = []

    def __init__(self, color='default', fila=10, columna=10):
        self.color = color
        self.fila = fila
        self.columna = columna
        if self.fila < 5:
            raise("Error: El tablero debe tener un fila de al menos 5")
        if self.columna < 5:
            raise("Error: El tablero debe tener un columna de al menos 5")

    def agregar_entidad(self, entidad):
        self.endidades.append(entidad)


    def crear(self):
        '''
        Crear un tablero de 'x' tamaño fila x columna con el cuadrado blanco en el centro.
        '''
        for a in range(self.fila):
            fila = []
            for l in range(self.columna):
                fila.append({
                    'fondo': self.colores[self.color],
                    'ocupado': False,
                    })
            self.tablero.append(fila)
        
        for entidad in self.endidades:
            self.tablero[entidad.posicion_x][entidad.posicion_y] = {
                'fondo': entidad.emoji,
                'ocupado': True,
            }

        return self.tablero
    
    def update(self, entidad):
        self.tablero[entidad.ultima_posicion_x][entidad.ultima_posicion_y] = {
            'fondo': self.colores[self.color],
            'ocupado': False,
        }
        self.tablero[entidad.posicion_x][entidad.posicion_y] = {
            'fondo': entidad.emoji,
            'ocupado': True,
        }


    def imprimir(self):
        print(f"fila: {self.fila} | Largo: {self.columna} | Longitud: {len(self.tablero)}\n")
        aux = ''
        for filas in self.tablero:
            for elemento in filas:
                aux += elemento['fondo']
            aux += '\n'
        print(aux)
        
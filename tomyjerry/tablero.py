class Tablero:
    colores = {'default': '⬜', 'negro': '⬛', 'azul': '🟦', 'verde': '🟩', 'morado': '🟪', 'amarillo': '🟨', 'rojo': '🟥', 'marron': '🟫', 'naranja': '🟧'}

    def __init__(self, color='default', fila=10, columna=10):
        self.color = color
        self.fila = fila
        self.columna = columna
        if color not in self.colores:
            color = 'default'
        self.tablero = [[self.colores[color] for _ in range(fila)] for _ in range(columna)]

    def agregar_entidad(self, entidad):
        self.endidades.append(entidad)
   
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
        for filas in self.tablero:
            print("".join(filas))
        
if __name__ == "__main__":
    tablero = Tablero()
    tablero.imprimir()
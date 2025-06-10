from jugador import *

class Tablero:
    colores = {'default': '⬜', 'negro': '⬛', 'azul': '🟦', 'verde': '🟩', 'morado': '🟪', 'amarillo': '🟨', 'rojo': '🟥', 'marron': '🟫', 'naranja': '🟧'}

    def __init__(self, color='default', fila=10, columna=10):
        self.color = color
        self.fila = fila
        self.columna = columna
        if color not in self.colores:
            color = 'default'
        self.tablero = [[self.colores[color] for _ in range(fila)] for _ in range(columna)]

    def agregar_entidad(self, entidad:Jugador):
        self.tablero[entidad.fila][entidad.columna] = entidad.emoji
   
    def update(self, entidad):
        self.tablero[entidad.ultima_posicion_x][entidad.ultima_posicion_y] = self.colores[self.color]
        self.tablero[entidad.posicion_x][entidad.posicion_y] = entidad.emoji

    def imprimir(self):
        for filas in self.tablero:
            print("".join(filas))
        print()
        
    def is_inTablero(self, fila, columna):
        return 0 <= fila < self.fila and 0 <= columna < self.columna
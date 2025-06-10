from jugador import *

class Tablero:
    colores = {'default': '⬜', 'negro': '⬛', 'azul': '🟦', 'verde': '🟩', 'morado': '🟪', 'amarillo': '🟨', 'rojo': '🟥', 'marron': '🟫', 'naranja': '🟧'}

    def __init__(self, filas=10, columnas=10, color='default'):
        self.color = color
        self.fila = filas
        self.columna = columnas
        if color not in self.colores:
            color = 'default'
        self.tablero = [[self.colores[color] for _ in range(self.fila)] for _ in range(self.columna)]

    def agregar_entidad(self, entidad:Jugador):
        self.tablero[entidad.fila][entidad.columna] = entidad.emoji
   
    def update(self, entidad):
        self.tablero[entidad.ultima_fila][entidad.ultima_columna] = self.colores[self.color]
        self.tablero[entidad.fila][entidad.columna] = entidad.emoji

    def imprimir(self):
        for filas in self.tablero:
            print("".join(filas))
        print()
        
    def is_inTablero(self, fila, columna):
        return 0 <= fila < self.fila and 0 <= columna < self.columna
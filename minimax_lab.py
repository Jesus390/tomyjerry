      
import math
from copy import deepcopy

class Minimax:
    def __init__(self, max_depth=3):
        self.max_depth = max_depth
        self.movimientos = ['w', 'a', 's', 'd']

    def evaluar(self, raton, gato):
        return abs(raton.posicion_x - gato.posicion_x) + abs(raton.posicion_y - gato.posicion_y)

    def posibles_movimientos(self, entidad, tablero):
        movimientos_validos = []
        for mov in self.movimientos:
            copia = deepcopy(entidad)
            copia.mover(mov)
            if 0 <= copia.posicion_x < tablero.alto and 0 <= copia.posicion_y < tablero.largo:
                movimientos_validos.append(mov)
        return movimientos_validos

    def minimax(self, raton, gato, tablero, profundidad, maximizando):
        if profundidad == 0 or (raton.posicion_x == gato.posicion_x and raton.posicion_y == gato.posicion_y):
            return self.evaluar(raton, gato), None

        mejores_mov = None
        if maximizando:
            max_eval = -math.inf
            for mov in self.posibles_movimientos(raton, tablero):
                copia_raton = deepcopy(raton)
                copia_raton.mover(mov)
                eval, _ = self.minimax(copia_raton, gato, tablero, profundidad - 1, False)
                if eval > max_eval:
                    max_eval = eval
                    mejores_mov = mov
            return max_eval, mejores_mov
        else:
            min_eval = math.inf
            for mov in self.posibles_movimientos(gato, tablero):
                copia_gato = deepcopy(gato)
                copia_gato.mover(mov)
                eval, _ = self.minimax(raton, copia_gato, tablero, profundidad - 1, True)
                if eval < min_eval:
                    min_eval = eval
                    mejores_mov = mov
            return min_eval, mejores_mov

import math
from copy import deepcopy

class Minimax:
    def __init__(self, profundidad=3):
        self.profundidad = profundidad

    def posibles_movimientos(self, jugador, tablero):
        movimientos = ['w', 'a', 's', 'd']
        movimientos_validos = []
        for mov in movimientos:
            copia = deepcopy(jugador)
            copia.mover(mov)
            # Verifica límites del tablero
            if 0 <= copia.posicion_x < tablero.alto and 0 <= copia.posicion_y < tablero.largo:
                movimientos_validos.append(mov)
        return movimientos_validos

    def minimax(self, raton, gato, tablero, profundidad, maximizador,
                historial_raton=None, historial_gato=None):

        if historial_raton is None:
            historial_raton = []
        if historial_gato is None:
            historial_gato = []

        # Termina si profundidad 0 o captura
        if profundidad == 0 or (raton.posicion_x == gato.posicion_x and raton.posicion_y == gato.posicion_y):
            distancia = abs(raton.posicion_x - gato.posicion_x) + abs(raton.posicion_y - gato.posicion_y)
            return distancia, None  # ratón maximiza distancia

        if maximizador == 'raton':
            max_eval = -math.inf
            mejor_mov = None
            for mov in self.posibles_movimientos(raton, tablero):
                copia_raton = deepcopy(raton)
                copia_raton.mover(mov)
                pos = (copia_raton.posicion_x, copia_raton.posicion_y)
                if pos in historial_raton:
                    continue
                eval, _ = self.minimax(copia_raton, gato, tablero, profundidad - 1, 'gato',
                                      historial_raton + [pos], historial_gato)
                if eval > max_eval:
                    max_eval = eval
                    mejor_mov = mov
            return max_eval, mejor_mov

        else:  # turno gato, minimiza distancia
            min_eval = math.inf
            mejor_mov = None
            for mov in self.posibles_movimientos(gato, tablero):
                copia_gato = deepcopy(gato)
                copia_gato.mover(mov)
                pos = (copia_gato.posicion_x, copia_gato.posicion_y)
                if pos in historial_gato:
                    continue
                eval, _ = self.minimax(raton, copia_gato, tablero, profundidad - 1, 'raton',
                                      historial_raton, historial_gato + [pos])
                if eval < min_eval:
                    min_eval = eval
                    mejor_mov = mov
            return min_eval, mejor_mov

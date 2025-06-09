from jugador import Raton, Gato

class Minimax:
    def __init__(self, tablero, profundidad_max=3):
        self.profundidad_max = profundidad_max
        self.tablero = tablero

    def distancia_manhattan(self, entidad, objetivo):
        return abs(entidad.fila - objetivo.fila) + abs(entidad.columna - objetivo.columna)

    def evaluar(self, raton, gato, jugador_actual):
        if raton.fila == gato.fila and raton.columna == gato.columna:
            return -100 if jugador_actual == 'raton' else 100

        distancia = self.distancia_manhattan(raton, gato)
        return distancia if jugador_actual == 'raton' else -distancia

    def minimax(self, raton, gato, profundidad, maximizador):
        if profundidad == 0 or (raton.fila == gato.fila and raton.columna == gato.columna):
            return self.evaluar(raton, gato, 'raton' if maximizador else 'gato'), None

        mejor_valor = float('-inf') if maximizador else float('inf')
        mejor_mov = None

        jugador = raton if maximizador else gato
        for mov in jugador.movimientos_disponibles(self.tablero):
            nuevo_raton = Raton(raton.fila, raton.columna)
            nuevo_gato = Gato(gato.fila, gato.columna)

            if maximizador:
                nuevo_raton.fila, nuevo_raton.columna = mov
            else:
                nuevo_gato.fila, nuevo_gato.columna = mov

            valor, _ = self.minimax(nuevo_raton, nuevo_gato, profundidad - 1, not maximizador)

            if maximizador and valor > mejor_valor:
                mejor_valor, mejor_mov = valor, mov
            elif not maximizador and valor < mejor_valor:
                mejor_valor, mejor_mov = valor, mov

        return mejor_valor, mejor_mov

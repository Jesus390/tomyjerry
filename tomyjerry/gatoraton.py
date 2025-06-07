class Tablero:
    def __init__(self, columnas, filas):
        self.columnas = columnas
        self.filas = filas
        self.tablero = None

    def crear(self):
        self.tablero = [[' . ' for _ in range(self.filas)] for _ in range(self.columnas)]

    def agregar(self, entidad):
        self.tablero[entidad.columna][entidad.fila] = f' {entidad.name} '

    def update(self, entidad):
        self.tablero[entidad.ultima_columna][entidad.ultima_fila] = ' . '
        self.tablero[entidad.columna][entidad.fila] = f' {entidad.name} '

    def imprimir(self):
        aux = ''
        for i, columnas in enumerate(self.tablero):
            for j, fila in enumerate(columnas):
                aux += f'{fila}'
            aux += '\n'
        print(aux)


class Jugador:
    def __init__(self, columna, fila, tablero):
        self.ultima_columna = columna
        self.ultima_fila = fila
        self.columna = columna
        self.fila = fila
        self.movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.tablero = tablero

    def calcular_movimiento(self, posicion):
        return (self.columna + posicion[0], self.fila + posicion[1])
    
    def movimientos_disponibles(self):
        return [(self.columna + i, self.fila + j) for i, j in self.movimientos if self.is_inTablero((self.columna + i, self.fila + j))]

    def is_inTablero(self, posicion):
        return 0 <= posicion[0] < self.tablero.filas and 0 <= posicion[1] < self.tablero.columnas
    
    def arriba(self):
        return self.movimientos[3] # (-1, 0)
    
    def abajo(self):
        return self.movimientos[2] # (1, 0)
    
    def izquierda(self):
        return self.movimientos[1] # (0, -1)
    
    def derecha(self):
        return self.movimientos[0] # (0, 1)

    def mover(self, movimiento:str):
        if movimiento.lower() == 'w':
            posicion = self.calcular_movimiento(self.arriba())
            if not self.is_inTablero(posicion):
                print(f"Arriba... fuera de posicion {posicion}")
                return
            self.ultima_columna = self.columna
            self.ultima_fila = self.fila
            self.columna = posicion[0]
            self.fila = posicion[1]
        if movimiento.lower() == 'a':
            posicion = self.calcular_movimiento(self.izquierda())
            if not self.is_inTablero(posicion):
                print(f"Izquierda... fuera de posicion {posicion}")
                return
            self.ultima_columna = self.columna
            self.ultima_fila = self.fila
            self.columna = posicion[0]
            self.fila = posicion[1]
        if movimiento.lower() == 'd':
            posicion = self.calcular_movimiento(self.derecha())
            if not self.is_inTablero(posicion):
                print(f"Derecha... fuera de posicion {posicion}")
                return
            self.ultima_columna = self.columna
            self.ultima_fila = self.fila
            self.columna = posicion[0]
            self.fila = posicion[1]
        if movimiento.lower() == 's':
            posicion = self.calcular_movimiento(self.abajo())
            if not self.is_inTablero(posicion):
                print(f"Abajo... fuera de posicion {posicion}")
                return
            self.ultima_columna = self.columna
            self.ultima_fila = self.fila
            self.columna = posicion[0]
            self.fila = posicion[1]
        
    def get_posicion(self):
        return (self.columna, self.fila)
    
class Gato(Jugador):
    def __init__(self, columna, fila, tablero, name='G'):
        super().__init__(columna, fila, tablero)
        self.name = name

class Raton(Jugador):
    def __init__(self, columna, fila, tablero, name='R'):
        super().__init__(columna, fila, tablero)
        self.name = name

class Game():
    def __init__(self):
        pass

    def is_over(self, pos_raton, pos_gato):
        return pos_raton[0]==pos_gato[0] and pos_raton[1]==pos_gato[1]

def is_gato_win(raton, gato):
    return gato.fila == raton.fila and gato.columna == raton.columna

# Heuristica: DISTANCIA MANHATAN
# def distancia_manh(xr, yr, xg, yg):
def distancia_manh(raton, gato):
    distancia= abs(raton.fila - gato.fila) + abs(raton.columna - gato.columna)
    # distancia= abs(xr - xg) + abs(yr - yg)
    return distancia

class Minimax:
    def __init__(self, profundidad_max=4):
        self.profundidad_max = profundidad_max

    def evaluar(self, raton, gato):
        if is_gato_win(raton, gato):
            return -100  # pérdida para el ratón
        return distancia_manh(raton, gato)

    def minimax(self, raton, gato, profundidad, maximizando):
        if profundidad == 0 or is_gato_win(raton, gato):
            return self.evaluar(raton, gato), None

        mejor_valor = float('-inf') if maximizando else float('inf')
        mejor_mov = None

        jugador = raton if maximizando else gato
        for mov in jugador.movimientos_disponibles():
            copia_raton = Raton(raton.columna, raton.fila, raton.tablero)
            copia_gato = Gato(gato.columna, gato.fila, gato.tablero)

            if maximizando:
                copia_raton.columna, copia_raton.fila = mov
            else:
                copia_gato.columna, copia_gato.fila = mov

            valor, _ = self.minimax(copia_raton, copia_gato, profundidad - 1, not maximizando)

            if maximizando and valor > mejor_valor:
                mejor_valor, mejor_mov = valor, mov
            elif not maximizando and valor < mejor_valor:
                mejor_valor, mejor_mov = valor, mov

        return mejor_valor, mejor_mov


if __name__=="__main__":
    minimax = Minimax(profundidad_max=4)

    filas = 5
    columnas = 5
    turnos = 15

    # instancias
    game = Game()
    tablero = Tablero(filas, columnas)
    raton = Raton(0, 0, tablero)
    gato = Gato(filas-1, columnas-1, tablero)
    
    tablero.crear()
    
    tablero.agregar(raton)
    tablero.agregar(gato)
    
    tablero.imprimir()

    print(f" Posicion Gato: {gato.get_posicion()}")
    print(f" Posicion Raton: {raton.get_posicion()}")

    while turnos >= 0:
        print(f"\nTurno: {5 - turnos}")
        print(f"Distancia Manhattan: {distancia_manh(raton, gato)}")
        
        # Movimiento del RATÓN con Minimax (Max)
        _, mejor_mov = minimax.minimax(raton, gato, 3, True)
        if mejor_mov:
            raton.ultima_columna, raton.ultima_fila = raton.columna, raton.fila
            raton.columna, raton.fila = mejor_mov
            tablero.update(raton)

        # Movimiento del GATO con Minimax (Min)
        _, mejor_mov = minimax.minimax(raton, gato, 3, False)
        if mejor_mov:
            gato.ultima_columna, gato.ultima_fila = gato.columna, gato.fila
            gato.columna, gato.fila = mejor_mov
            tablero.update(gato)

        if game.is_over(raton.get_posicion(), gato.get_posicion()):
            print(f"Juego terminado.... GATO is WIN.")
            break

        tablero.imprimir()
        turnos -= 1



#     filas = 5
#     columnas = 5
#     turnos = 5

#     # instancias
#     game = Game()
#     tablero = Tablero(filas, columnas)
#     raton = Raton(0, 0, tablero)
#     gato = Gato(filas-1, columnas-1, tablero)
    
#     tablero.crear()
    
#     tablero.agregar(raton)
#     tablero.agregar(gato)
    
#     tablero.imprimir()

#     print(f" Posicion Gato: {gato.get_posicion()}")
#     print(f" Posicion Raton: {raton.get_posicion()}")
#     while turnos >= 0:
#         print()
#         print(f"Distancia Manhattan: {distancia_manh(raton, gato)}")
#         print("1. Mover raton")
#         print("Movimientos disponibles Raton:", raton.movimientos_disponibles())
#         movimiento = input("Ingresa el movimiento (Raton): ")
#         raton.mover(movimiento)
#         tablero.update(raton)

#         print("2. Mover gato")
#         print("Movimientos disponibles Gato:", gato.movimientos_disponibles())
#         movimiento = input("Ingresa el movimiento (Gato): ")
#         gato.mover(movimiento)
#         tablero.update(gato)
        
#         if game.is_over(raton.get_posicion(), gato.get_posicion()):
#             print(f"Juego terminado.... GATO is WIN.")
#             break

#         tablero.imprimir()
#         turnos -= 1
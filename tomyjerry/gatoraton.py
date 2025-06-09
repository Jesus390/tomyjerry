import os
import time

def clear():
    '''
    Limpia la pantalla
    '''
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar(tiempo):
    '''
    Espera un tiempo determinado
    '''
    time.sleep(tiempo)

class Tablero:
    '''
    Clase Tablero 2 dimensiones
    '''
    # variable contenedor del tablero
    tablero = None

    def __init__(self, filas, columnas):
        '''
        Inicializa el tablero
        '''
        self.filas = filas
        self.columnas = columnas

    def crear(self):
        '''
        Crea el tablero
        '''
        self.tablero =  [['.' for _ in range(self.columnas)] for _ in range(self.filas)]
    
    def imprimir(self):
        '''
        Imprime el tablero
        '''
        for filas in self.tablero:
            print(' '.join(filas))
        print("-"*20)

    def agregar_entidad(self, entidad):
        '''
        Agrega una entidad en el tablero
        '''
        self.tablero[entidad.fila][entidad.columna] = entidad.simbolo

    def is_inTablero(self, fila, columna):
        '''
        Verifica si la entidad se encuentra dentro del tablero
        '''
        return 0 <= fila < self.filas and 0 <= columna < self.columnas
    
    # def actualizar_entidad(self, entidad):
    #     # Limpia la posición anterior de esta entidad
    #     for f in range(self.filas):
    #         for c in range(self.columnas):
    #             if self.tablero[f][c] == entidad.simbolo:
    #                 self.tablero[f][c] = '.'
    #     # Coloca la nueva posición
    #     self.tablero[entidad.fila][entidad.columna] = entidad.simbolo

    def actualizar_entidad(self, entidad):
        self.tablero[entidad.ultima_fila][entidad.ultima_columna] = '.'
        self.tablero[entidad.fila][entidad.columna] = entidad.simbolo

class Entidad:
    '''
    Clase Entidad
    '''
    def __init__(self, fila, columna):
        '''
        Inicializa la entidad
        '''
        self.fila = fila
        self.columna = columna

class Jugador(Entidad):
    '''
    Clase Jugador
    '''
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def __init__(self, fila, columna):
        '''
        Inicializa el jugador
        '''
        super().__init__(fila, columna)
        self.ultima_fila = self.fila
        self.ultima_columna = self.columna

    def movimientos_disponibles(self, tablero):
        '''
        Obtiene los movimientos disponibles para el jugador
        '''
        return [(self.fila+movimiento[0], self.columna+movimiento[1]) for movimiento in self.movimientos if tablero.is_inTablero(self.fila+movimiento[0], self.columna+movimiento[1])]
        
class Raton(Jugador):
    '''
    Clase Raton
    '''

    def __init__(self, fila, columna, simbolo="R"):
        '''
        Inicializa el raton
        '''
        super().__init__(fila, columna)
        self.simbolo = simbolo
        
    def ha_escapado(self, zona_escape):
        return self.fila == zona_escape[0] and self.columna == zona_escape[1]

class Gato(Jugador):
    '''
    Clase Gato
    '''
    def __init__(self, fila, columna, simbolo="G"):
        '''
        Inicializa el gato
        '''
        super().__init__(fila, columna)
        self.simbolo = simbolo
    
    def is_win(self, entidad):
        '''
        Verifica si el gato ha ganado
        '''
        return self.fila == entidad.fila and self.columna == entidad.columna

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


if __name__ == "__main__":
    filas = 5
    columnas = 7
    tablero = Tablero(filas, columnas)
    raton = Raton(0, 0)
    gato = Gato(filas-1, columnas-1)
    minimax = Minimax(tablero)

    tablero.crear()
    tablero.agregar_entidad(raton)
    tablero.agregar_entidad(gato)

    turnos = 10
    zona_escape = (filas - 1, columnas - 1)
    
    print("Inicio del juego")
    tablero.imprimir()
    esperar(1)
    while turnos > 0:
        if gato.is_win(raton):
            print("El gato ha ganado")
            break  # 🚨 Salimos del ciclo

        if raton.ha_escapado(zona_escape):
            print("¡El ratón ha escapado!")
            break
                
        # Movimiento del ratón
        mejor_movimiento_raton = minimax.minimax(raton, gato, 3, True)
        if mejor_movimiento_raton and mejor_movimiento_raton[1]:
            raton.ultima_fila, raton.ultima_columna = raton.fila, raton.columna
            raton.fila, raton.columna = mejor_movimiento_raton[1]
            tablero.actualizar_entidad(raton)
        
            clear()
            tablero.imprimir()
            print(f"Turnos restantes: {turnos}")
            esperar(1)

        if gato.is_win(raton):  # Verificamos otra vez
            print("El gato ha ganado")
            break

        tablero.imprimir()

        # Movimiento del gato
        mejor_movimiento_gato = minimax.minimax(raton, gato, 3, False)
        if mejor_movimiento_gato and mejor_movimiento_gato[1]:
            gato.ultima_fila, gato.ultima_columna = gato.fila, gato.columna
            gato.fila, gato.columna = mejor_movimiento_gato[1]
            tablero.actualizar_entidad(gato)

            clear()
            tablero.imprimir()
            print(f"Turnos restantes: {turnos}")
            esperar(1)

        turnos -= 1
    else:
        clear()
        print("El juego ha terminado")
        print("El juego terminó por límite de turnos.")

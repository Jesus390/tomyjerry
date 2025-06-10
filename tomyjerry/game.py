import random
import time # Para pausar la simulación

# --- Clase Tablero ---
class Tablero:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        # Inicializa la matriz del tablero con espacios vacíos
        self.grid = [[' ' for _ in range(columnas)] for _ in range(filas)]
        self.entidades = {} # Para almacenar las posiciones de Gato y Raton

    def agregar_entidad(self, entidad):
        # Asigna la entidad a su posición inicial en el tablero
        self.grid[entidad.fila][entidad.columna] = entidad.char
        self.entidades[entidad.char] = entidad # Guarda la referencia a la entidad

    def actualizar(self, entidad):
        # Borra la posición anterior de la entidad
        for r in range(self.filas):
            for c in range(self.columnas):
                if self.grid[r][c] == entidad.char:
                    self.grid[r][c] = ' ' # Limpiar la posición anterior
                    break # Asumimos solo una entidad por caracter
            else: # Ejecuta si el break no fue llamado
                continue
            break # Rompe el ciclo exterior si se encontró la entidad

        # Actualiza la nueva posición de la entidad
        self.grid[entidad.fila][entidad.columna] = entidad.char

    def es_en_tablero(self, fila, columna):
        return 0 <= fila < self.filas and 0 <= columna < self.columnas

    def imprimir(self):
        print("-" * (self.columnas * 2 + 1))
        for fila in self.grid:
            print("|" + "|".join(fila) + "|")
        print("-" * (self.columnas * 2 + 1))
        print("\n")


# --- Clase Jugador Base ---
class Jugador:
    def __init__(self, fila, columna, char):
        self.fila = fila
        self.columna = columna
        self.char = char

    def mover(self, nueva_fila, nueva_columna):
        self.fila = nueva_fila
        self.columna = nueva_columna

    def movimientos_disponibles(self, tablero):
        posibles = []
        # Definir los 4 movimientos cardinales
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Arriba, Abajo, Izquierda, Derecha

        for dr, dc in direcciones:
            nueva_fila = self.fila + dr
            nueva_columna = self.columna + dc
            if tablero.es_en_tablero(nueva_fila, nueva_columna):
                posibles.append((nueva_fila, nueva_columna))
        return posibles

# --- Clase Raton ---
class Raton(Jugador):
    def __init__(self, fila, columna):
        super().__init__(fila, columna, 'R')

    def mover_random(self, tablero):
        movs_posibles = self.movimientos_disponibles(tablero)
        if movs_posibles:
            return random.choice(movs_posibles)
        return self.fila, self.columna # Si no hay movimientos, se queda en el mismo lugar

# --- Clase Gato ---
class Gato(Jugador):
    def __init__(self, fila, columna):
        super().__init__(fila, columna, 'G')

# --- Funciones del Juego ---

def es_victoria(gato, raton):
    """Verifica si el gato ha atrapado al ratón."""
    return gato.fila == raton.fila and gato.columna == raton.columna

def distancia_manhattan(gato, raton):
    """Calcula la distancia de Manhattan entre el gato y el ratón."""
    return abs(gato.fila - raton.fila) + abs(gato.columna - raton.columna)

def evaluar_estado(gato, raton):
    """
    Función de evaluación para Minimax.
    Un valor alto es bueno para el Gato (maximizador).
    """
    if es_victoria(gato, raton):
        return 1000 # El Gato gana, puntuación muy alta
    
    # El Gato quiere minimizar la distancia. Por lo tanto, una distancia
    # más pequeña debería traducirse en una puntuación más alta para el Gato.
    # Negamos la distancia para que funcione con el objetivo de maximización.
    distancia = distancia_manhattan(gato, raton)
    return -distancia

def minimax(profundidad, gato_actual, raton_actual, es_turno_maximizador, tablero_simulado):
    """
    Implementación del algoritmo Minimax.
    :param profundidad: La profundidad restante de búsqueda.
    :param gato_actual: Objeto Gato en el estado actual de la simulación.
    :param raton_actual: Objeto Raton en el estado actual de la simulación.
    :param es_turno_maximizador: True si es el turno del Gato (maximizador), False si es el del Ratón (minimizador).
    :param tablero_simulado: El objeto Tablero que representa el estado actual del juego.
    :return: Una tupla (mejor_valor, mejor_movimiento).
    """
    # Caso base: si la profundidad es 0 o el juego ha terminado
    if profundidad == 0 or es_victoria(gato_actual, raton_actual):
        return evaluar_estado(gato_actual, raton_actual), None

    mejor_valor = float('-inf') if es_turno_maximizador else float('inf')
    mejor_movimiento = None

    jugador_actual = gato_actual if es_turno_maximizador else raton_actual

    for movimiento_posible in jugador_actual.movimientos_disponibles(tablero_simulado):
        # Crear nuevas instancias de Gato y Raton para simular el movimiento
        # Esto es crucial para no modificar el estado actual del juego
        gato_siguiente = Gato(gato_actual.fila, gato_actual.columna)
        raton_siguiente = Raton(raton_actual.fila, raton_actual.columna)

        # Aplicar el movimiento simulado al jugador correcto
        if es_turno_maximizador: # Si es el turno del Gato
            gato_siguiente.mover(movimiento_posible[0], movimiento_posible[1])
        else: # Si es el turno del Ratón
            raton_siguiente.mover(movimiento_posible[0], movimiento_posible[1])

        # Llamada recursiva a minimax para el siguiente turno
        valor, _ = minimax(
            profundidad - 1, 
            gato_siguiente, 
            raton_siguiente, 
            not es_turno_maximizador, 
            tablero_simulado
        )

        # Actualizar el mejor valor y movimiento para el jugador actual
        if es_turno_maximizador: # El Gato (maximizador) busca el valor más alto
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_movimiento = movimiento_posible
        else: # El Ratón (minimizador) busca el valor más bajo
            if valor < mejor_valor:
                mejor_valor = valor
                mejor_movimiento = movimiento_posible
        
        # print(f"Prof: {profundidad}, Jugador: {type(jugador_actual).__name__}, Evaluando Mov: {movimiento_posible}, Valor Rec: {valor}, Mejor Valor Acum: {mejor_valor}, Mejor Mov Acum: {mejor_movimiento}")


    return mejor_valor, mejor_movimiento

# --- Función Principal de Ejecución ---
def ejecutar_juego():
    # Variables de inicialización
    filas = 5 # Puedes ajustar el tamaño del tablero
    columnas = 5
    max_turnos = 50 # Límite para evitar partidas infinitas

    # Instancias
    tablero = Tablero(filas, columnas)
    raton = Raton(0, 0) # Ratón empieza en la esquina superior izquierda
    gato = Gato(filas - 1, columnas - 1) # Gato empieza en la esquina inferior derecha

    # Agregar entidades al tablero
    tablero.agregar_entidad(raton)
    tablero.agregar_entidad(gato)

    print("--- ¡Comienza el Laberinto del Gato y el Ratón! ---")
    tablero.imprimir()

    turnos_actuales = 0
    while turnos_actuales < max_turnos:
        time.sleep(0.5) # Pausa para ver la simulación
        print(f"--- Turno: {turnos_actuales + 1} / {max_turnos} ---")

        # --- Turno del Ratón (se mueve al azar por ahora) ---
        print("Turno del Ratón...")
        mov_raton = raton.mover_random(tablero) # Obtiene un movimiento aleatorio
        raton.mover(mov_raton[0], mov_raton[1])
        tablero.actualizar(raton)
        tablero.imprimir()

        if es_victoria(gato, raton):
            print("¡El Gato ha atrapado al Ratón! ¡Gato gana!")
            break

        # --- Turno del Gato (usa Minimax) ---
        print("Turno del Gato...")
        # Profundidad de búsqueda para el Gato
        # Puedes experimentar con diferentes valores (2, 3, 4 son comunes para empezar)
        profundidad_minimax_gato = 3 
        
        # El Gato es el maximizador (True)
        _, mov_gato = minimax(profundidad_minimax_gato, gato, raton, True, tablero)
        
        if mov_gato: # Asegurarse de que se encontró un movimiento válido
            gato.mover(mov_gato[0], mov_gato[1])
            tablero.actualizar(gato)
            tablero.imprimir()
        else:
            print("El Gato no encontró movimientos válidos y se queda quieto.")

        if es_victoria(gato, raton):
            print("¡El Gato ha atrapado al Ratón! ¡Gato gana!")
            break

        turnos_actuales += 1
    
    if turnos_actuales == max_turnos and not es_victoria(gato, raton):
        print("¡Se agotaron los turnos! El Ratón logra escapar. ¡Ratón gana!")

    print("--- Fin del Juego ---")

# --- Ejecución del Juego ---
if __name__ == "__main__":
    ejecutar_juego()







# from tablero import Tablero
# from jugador import Raton, Gato
# from minimax import Minimax
# from functions import *

# import time

# def is_win(gato, raton):
#     return gato.fila == raton.fila and gato.columna == raton.columna
    
# def distancia_manhattan(gato, raton):
#     return abs(gato.fila - raton.fila) + abs(gato.columna - raton.columna)

# def evaluar(gato, raton):
#     if is_win(gato, raton):
#         return 1000
    
#     distancia = distancia_manhattan(gato, raton)
#     return -distancia
    

# def minimax(profundidad, gato, raton, maximizador, tablero):
#     if profundidad==0 or is_win(gato, raton):
#         return evaluar(gato, raton), None
    
#     mejor_valor = float('-inf') if maximizador else float('inf')
#     mejor_mov = None

#     jugador = gato if maximizador else raton
#     for mov in jugador.movimientos_disponibles(tablero):
#         nuevo_gato = Gato(gato.fila, gato.columna)
#         nuevo_raton = Raton(raton.fila, raton.columna)

#         if maximizador: # It's Gato's turn (Gato is the maximizer)
#             nuevo_gato.fila, nuevo_gato.columna = mov
#         else: # It's Raton's turn (Raton is the minimizer)
#             nuevo_raton.fila, nuevo_raton.columna = mov
        
#         valor, _ = minimax(profundidad-1, nuevo_gato, nuevo_raton, not maximizador, tablero)

#         if maximizador and valor > mejor_valor:
#             mejor_valor, mejor_mov = valor, mov
#         elif not maximizador and valor < mejor_valor:
#             mejor_valor, mejor_mov = valor, mov

#     print(f"Jugador: {type(jugador)}, Puntuacion: {mejor_valor}, Movimiento: {mejor_mov}")
#     return mejor_valor, mejor_mov


# def run():
#     turnos = filas * columnas // 5
#     while turnos > 0:
#         time.sleep(1)
#         print(f"Turnos disponibles: {turnos}")

#         print("Turno del Raton...")
#         tmp_fila, tmp_columna = raton.calcular_movimiento(raton.mover_random(tablero))
#         if tablero.is_inTablero(tmp_fila, tmp_columna):
#             raton.mover(tmp_fila, tmp_columna)
#             tablero.update(raton)
#             tablero.imprimir()
#         # else:
#         #     print("No se puede mover en esa direccion")

#         if is_win(gato, raton):
#             tablero.tablero[raton.fila][raton.columna] = gato.emoji
#             print("Gato gana, autoeliminación.")
#             break

#         print("Turno del Gato...")
#         # tmp_fila, tmp_columna = gato.calcular_movimiento(gato.mover_random(tablero))
#         # if tablero.is_inTablero(tmp_fila, tmp_columna):
#         _, mov = minimax(3, gato, raton, True, tablero)
#         print(mov)
#         gato.mover(mov[0], mov[1])
#         tablero.update(gato)
#         tablero.imprimir()
#         # else:
#         #     print("No se puede mover en esa direccion")

#         if is_win(gato, raton):
#             tablero.tablero[gato.fila][gato.columna] = gato.emoji
#             print("Gato gana")
#             break

#         turnos -= 1

# if __name__ == "__main__":
#     # variables de inicializacion
#     filas = 10
#     columnas = 10

#     # instacias
#     tablero = Tablero(filas, columnas)
#     raton = Raton(0, 0)
#     gato = Gato(filas-1, columnas-1)

#     # agregar entidades
#     tablero.agregar_entidad(raton)
#     tablero.agregar_entidad(gato)

#     # imprimir tablero
#     tablero.imprimir()
#     run()

class Tablero:
    def __init__(self, columnas, filas):
        self.columnas = columnas
        self.filas = filas
        self.tablero = None

    def crear(self):
        self.tablero = [[' . ' for _ in range(self.filas)] for _ in range(self.columnas)]

    def agregar(self, entidad):
        self.tablero[entidad.columna][entidad.fila] = entidad.name

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

if __name__=="__main__":
    filas = 10
    columnas = 10

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
    while True:
        print()
        
        movimiento = input("Ingresa el movimiento (Raton): ")
        raton.mover(movimiento)
        tablero.update(raton)

        movimiento = input("Ingresa el movimiento (Gato): ")
        gato.mover(movimiento)
        tablero.update(gato)
        
        if game.is_over(raton.get_posicion(), gato.get_posicion()):
            print(f"Juego terminado.... GATO is WIN.")
            break

        tablero.imprimir()
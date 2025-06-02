class Tablero:
    def __init__(self, columnas=10, filas=10):
        self.columnas = columnas
        self.filas = filas
        self.tablero = None

    def crear(self):
        self.tablero = [[' . ' for _ in range(self.filas)] for _ in range(self.columnas)]

    def agregar(self, entidad):
        self.tablero[entidad.columna][entidad.fila] = entidad.name

    def update(self, entidad):
        # for columnas in self.tablero:
        #     for fila in columnas:
        #         if entidad.name.strip() == 'R':
        #             self.tablero[entidad.ultima_posicion_columna][entidad.ultima_posicion_fila] = ' . '
        #             break
        self.tablero[entidad.ultima_columna][entidad.ultima_fila] = ' . '
        self.tablero[entidad.posicion_columna][entidad.posicion_fila] = f' {entidad.name} '

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
        return 0 <= posicion[0] < self.tablero.fila and 0 <= posicion[1] < self.tablero.columna
    
    def arriba(self):
        return (-1, 0)
    
    def abajo(self):
        return (1, 0)
    
    def izquierda(self):
        return (0, -1)
    
    def derecha(self):
        return (0, 1)

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
    def __init__(self, columna, fila, tablero, name='R'):
        super().__init__(columna, fila, tablero)
        self.name = name

if __name__=="__main__":
    tablero = Tablero()
    gato = Gato(0, 0, tablero)
    
    tablero.crear()
    tablero.imprimir()
    
    tablero.agregar(gato)

    print(gato.get_posicion())
    while True:
        print()
        movimiento = input("Ingresa el movimiento: ")
        gato.mover(movimiento)
        tablero.update(gato)
        tablero.imprimir()
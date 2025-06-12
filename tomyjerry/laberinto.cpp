#include <iostream>
#include <random>
#include <algorithm>
#include <vector>
#include <deque>
#include <set>
#include <utility>

typedef char** Matriz;

// funciones
Matriz crear_tablero(int &filas, int &columnas);
void imprimir_tablero( Matriz tablero, int &filas, int &columnas);
void generar_laberinto(Matriz &tablero, int fila, int columna, int &filas, int &columnas);
void agregarES(Matriz &tablero, int &filas, int &columnas);
void resolver(Matriz &tablero, int &filas, int &columnas);
void liberar_tablero(Matriz &tablero, int &filas);

int main() {
    // valores de las filas y columnas
    int filas = 30, columnas = 30;

    // asegura impar
    if (filas % 2 == 0) filas--;  // asegura impar
    if (columnas % 2 == 0) columnas--;

    // std::cout << "Filas: ";
    // std::cin >> filas;
    // std::cout << "Columnas: ";
    // std::cin >> columnas;
    // std::cout << std::endl;
    // std::cout << "Filas: " << filas << ", Columnas: " << columnas << std::endl;

    // crear tablero
    std::cout << "Creando tablero..." << std::endl;
    Matriz tablero = crear_tablero(filas, columnas);

    // mostramos el tablero
    std::cout << "Tablero creado." << std::endl;
    imprimir_tablero(tablero, filas, columnas);

    // fila/columna -> para generar el laberinto - debe ser numero impar
    int fila_inicial_laberinto = 1;
    int columna_inicial_laberinto = 1;

    // generar laberinto
    std::cout << "Generando laberinto..." << std::endl;
    generar_laberinto(tablero, fila_inicial_laberinto, columna_inicial_laberinto, filas, columnas);

    // muestra el tablero con el laberinto generado
    std::cout << "Laberinto generado." << std::endl;
    agregarES(tablero, filas, columnas);
    imprimir_tablero(tablero, filas, columnas);

    // resolver laberinto
    resolver(tablero, filas, columnas);

    // liberar espacio en memoria
    liberar_tablero(tablero, filas);
    
    return 0;
}

void liberar_tablero(Matriz &tablero, int &filas) {
    for (int i=0; i<filas; i++) {
        delete[] tablero[i];
    }
    delete[] tablero;
}

void resolver(Matriz &tablero, int &filas, int &columnas) {
    std::pair<int, int> entrada = {1, 1};
    std::pair<int, int> salida = {filas - 2, columnas - 2};

    std::deque<std::pair<std::pair<int, int>, std::vector<std::pair<int, int>>>> cola;
    std::set<std::pair<int, int>> visitado;

    cola.push_back({entrada, {entrada}});
    visitado.insert(entrada);

    std::vector<std::pair<int, int>> movimientos = {{1,0}, {-1,0}, {0,1}, {0,-1}};

    while (!cola.empty()) {
        auto [pos, camino] = cola.front();
        cola.pop_front();

        auto [x, y] = pos;
        if (pos == salida) {
            for (const auto& [camino_x, camino_y] : camino) {
                tablero[camino_x][camino_y] = 'x';
            }

            tablero[1][1] = 'E';
            tablero[filas - 2][columnas - 2] = 'S';

            std::cout << "El laberinto se ha resuelto automáticamente:\n\n";
            imprimir_tablero(tablero, filas, columnas);
            // for (int i = 0; i < filas; ++i) {
            //     for (int j = 0; j < columnas; ++j) {
            //         std::cout << tablero[i][j] << " ";
            //     }
            //     std::cout << "\n";
            // }
            
            // for (const auto& fila : tablero) {
            //     for (char c : fila) std::cout << c << " ";
            //     std::cout << "\n";
            // }
            std::cout << "\n";
            return;
        }

        for (auto [dx, dy] : movimientos) {
            int nx = x + dx;
            int ny = y + dy;
            if (nx >= 0 && nx < filas && ny >= 0 && ny < columnas) {
                if ((tablero[nx][ny] == '.' || tablero[nx][ny] == 'S') && !visitado.count({nx, ny})) {
                    visitado.insert({nx, ny});
                    auto nuevo_camino = camino;
                    nuevo_camino.push_back({nx, ny});
                    cola.push_back({{nx, ny}, nuevo_camino});
                }
            }
        }
    }
}

void agregarES(Matriz &tablero, int &filas, int &columnas) {
    tablero[1][1] = 'E';
    tablero[filas-2][columnas-2] = 'S';
}

// void resolver(Laberinto &laberinto, int &filas, int &columnas) {
//     std::pair<int, int> entrada = {1, 1};
//     std::pair<int, int> salida = {filas - 2, columnas - 2};

//     std::deque<std::pair<std::pair<int, int>, std::vector<std::pair<int, int>>>> cola;
//     std::set<std::pair<int, int>> visitado;

//     cola.push_back({entrada, {entrada}});
//     visitado.insert(entrada);

//     std::vector<std::pair<int, int>> movimientos = {{1,0}, {-1,0}, {0,1}, {0,-1}};

//     while (!cola.empty()) {
//         auto [pos, camino] = cola.front();
//         cola.pop_front();

//         auto [x, y] = pos;
//         if (pos == salida) {
//             for (const auto& [camino_x, camino_y] : camino) {
//                 laberinto[camino_x][camino_y] = 'x';
//             }

//             laberinto[1][1] = 'E';
//             laberinto[filas - 2][columnas - 2] = 'S';

//             std::cout << "El laberinto se ha resuelto automáticamente:\n\n";
//             for (const auto& fila : laberinto) {
//                 for (char c : fila) std::cout << c << " ";
//                 std::cout << "\n";
//             }
//             std::cout << "\n";
//             return;
//         }

//         for (auto [dx, dy] : movimientos) {
//             int nx = x + dx;
//             int ny = y + dy;
//             if (nx >= 0 && nx < filas && ny >= 0 && ny < columnas) {
//                 if ((laberinto[nx][ny] == '.' || laberinto[nx][ny] == 'S') && !visitado.count({nx, ny})) {
//                     visitado.insert({nx, ny});
//                     auto nuevo_camino = camino;
//                     nuevo_camino.push_back({nx, ny});
//                     cola.push_back({{nx, ny}, nuevo_camino});
//                 }
//             }
//         }
//     }
// }


// void resolver(Matriz &tablero, int &filas, int &columnas) {
//     std::pair<int, int> entrada = {1, 1};
//     std::pair<int, int> salida = {filas-2, columnas-2};

//     std::deque<std::pair<std::pair<int, int>, std::vector<std::pair<int, int>>>> cola;
//     cola.push_front({entrada, {entrada}});

//     std::set<std::pair<int, int>> visitado;
//     visitado.insert(entrada);

//     std::vector<std::pair<int, int>> movimientos = {{0, 2}, {0, -2}, {2, 0}, {-2, 0}};



// }


void generar_laberinto(Matriz &tablero, int fila, int columna, int &filas, int &columnas) {
    tablero[fila][columna] = '.';

    std::vector<std::pair<int, int>> movimientos = {{0, 2}, {0, -2}, {2, 0}, {-2, 0}};
    
    std::random_device rd;
    std::mt19937 mezcla_aleatoria(rd());

    std::shuffle(movimientos.begin(), movimientos.end(), mezcla_aleatoria);

    // std::cout << "Generando laberinto..." << std::endl;

    for (const auto& [dfila, dcolumna]: movimientos) {
        int nueva_fila = fila + dfila;
        int nueva_columna = columna + dcolumna;
        
        if (nueva_fila >= 0 && nueva_fila < filas &&
            nueva_columna >= 0 && nueva_columna < columnas && 
            tablero[nueva_fila][nueva_columna] == '#') {
                tablero[fila + dfila / 2][columna + dcolumna / 2] = '.';
                generar_laberinto(tablero, nueva_fila, nueva_columna, filas, columnas);
        }
    }
}

void imprimir_tablero(Matriz tablero, int &filas, int &columnas) {
    for (int i = 0; i < filas; ++i) {
        for (int j = 0; j < columnas; ++j) {
            switch (tablero[i][j]) {
                case '#': std::cout << "\033[1;30m#\033[0m "; break; // gris oscuro (pared)
                case '.': std::cout << "\033[1;37m.\033[0m "; break; // blanco (camino)
                case 'E': std::cout << "\033[1;32mE\033[0m "; break; // verde (entrada)
                case 'S': std::cout << "\033[1;31mS\033[0m "; break; // rojo (salida)
                case 'x': std::cout << "\033[1;34mx\033[0m "; break; // azul (camino solución)
                default:  std::cout << tablero[i][j] << " "; break;
            }
        }
        std::cout << std::endl;
    }
}

Matriz crear_tablero(int &filas, int &columnas) {
    std::cout << std::endl << "Creando tablero: " << filas << "x" << columnas << std::endl;

    // Inicializa matriz
    // filas
    Matriz matriz = new char*[filas];

    // columnas
    for(int i = 0; i<filas; i++) {
        matriz[i] = new char[columnas];
    }

    // agregar las paredes
    for (int i=0; i<filas; i++) {
        for (int j=0; j<columnas; j++) {
            matriz[i][j] = '#';
        }
    }

    std::cout << "Tablero creado exitosamente." << std::endl;
    
    return matriz;
}
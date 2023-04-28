from nodo import Nodo as nodo
from posicion import Posicion
matriz = [
    [0, 3, 0, 3, 0],
    [1, 5, 0, 0, 0],
    [0, 0, 5, 5, 4],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0]
]

def newG(new):
    if new == 0:
        return 1
    elif new == 4:
        return 1
    return new


def crearNodo(y, x, g, camino, matriz):
    copia = camino.copy()
    if (y >= 0 and y < len(matriz) and x >= 0 and x < len(matriz[0])):
        new = newG(int(matriz[y][x]))
        if (new != 5):
            copia.append(Posicion(y, x))
            return nodo(Posicion(y, x), copia, new+g)
    return [0]


def ExpandirNodo(nodo):
    camino = nodo.camino.copy()
    newNodos = []
    newNodos.append(crearNodo(nodo.pos.posx, nodo.pos.posy - 1, nodo.costo,
                    camino, matrizA))  # moverse izquierda  num1
    newNodos.append(crearNodo(nodo.pos.posx, nodo.pos.posy + 1, nodo.costo,
                    camino, matrizA))  # moverse derecha num2
    newNodos.append(crearNodo(nodo.pos.posx + 1, nodo.pos.posy, nodo.costo,
                    camino, matrizA))  # moverse abajo num3
    newNodos.append(crearNodo(nodo.pos.posx - 1, nodo.pos.posy, nodo.costo,
                    camino, matrizA))  # moverse arriba num4
    
    
    

    for newNodo in newNodos:  # decide si agregar o NO un nuevo nodo a la pila
        if (newNodo != [0]):
            Pila.append(newNodo)


def index(Matriz, buscar):
    index = (0, 0)
    for y, fila in enumerate(Matriz):
        for x, dato in enumerate(fila):
            if (dato == buscar):
                index = Posicion(y, x)
                return index
            
def Amplitud(Matriz):
    global matrizA
    matrizA = Matriz
    Pinocho = index(Matriz, 1)
    aux = []
    aux.append(Pinocho)
    nodoi = nodo(Pinocho, aux, 0)
    global Pila
    Pila = []
    Pila.append(nodoi)

    while (len(Pila) != 0):
        nodoAct = Pila.pop(0)
        posX = nodoAct.pos.posx
        posY = nodoAct.pos.posy
        if Matriz[posX][posY] == 4:
            return (nodoAct.camino)
        ExpandirNodo(nodoAct)

aux = Amplitud(matriz)
for i in aux:
    print(i.posx,",,,", i.posy)
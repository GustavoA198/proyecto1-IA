from nodoProfundidad import NodoProfundidad as nodo
from posicion import Posicion

def newG(new):
    if new == 0:
        return 1
    elif new == 4:
        return 1
    return new

def Verificador(nodo):
        aux=str(nodo.pos.posx) + " " + str(nodo.pos.posy) + " " + str(nodo.costo)+ " "
        for i in nodo.camino:
            aux = aux + " "+ str(i.posx) + " " +str(i.posy)
        print(aux)

def crearNodo(y, x, g, p, camino, matriz):
    copia = camino.copy()
    if (y >= 0 and y < len(matriz) and x >= 0 and x < len(matriz[0]) and Posicion(y,x).existe(copia)):
        new = newG(int(matriz[y][x]))
        if (new != 5):
            copia.append(Posicion(y, x))
            return nodo(Posicion(y, x), copia, p+1, new+g)
    return [0]

def ExpandirNodo(nodo):
    camino = nodo.camino.copy()
    newNodos = []
    newNodos.append(crearNodo(nodo.pos.posx - 1, nodo.pos.posy,
                    nodo.costo, nodo.profundidad, camino, matrizA))  # moverse arriba num4
    newNodos.append(crearNodo(nodo.pos.posx+1, nodo.pos.posy, nodo.costo,
                    nodo.profundidad, camino, matrizA))  # moverse abajo num3
    newNodos.append(crearNodo(nodo.pos.posx, nodo.pos.posy+1, nodo.costo,
                    nodo.profundidad, camino, matrizA))  # moverse derecha num2
    newNodos.append(crearNodo(nodo.pos.posx, nodo.pos.posy-1, nodo.costo,
                    nodo.profundidad, camino, matrizA))  # moverse izquierda  num1

    for newNodo in newNodos:  # decide si agregar o NO un nuevo nodo a la pila
        if (newNodo != [0]):
            Pila.append(newNodo)
            Verificador(newNodo)

def index(Matriz, buscar):
    index = (0, 0)
    for y, fila in enumerate(Matriz):
        for x, dato in enumerate(fila):
            if (dato == buscar):
                index = Posicion(y, x)
                return index

def ProfundidadIterativa(Matriz):
    global matrizA
    matrizA = Matriz
    Pinocho = index(Matriz, 1)
    maxPro = 0
    expandido1 = []
    while True:
        aux = []
        aux.append(Pinocho)
        nodoi = nodo(Pinocho, aux, 0, 0)
        global Pila
        Pila = []
        Pila.append(nodoi)

        while (len(Pila) != 0):
            expandido = []
            nodoAct = Pila.pop()
            posX = nodoAct.pos.posx
            posY = nodoAct.pos.posy
            if Matriz[posX][posY] == 4:
                print(expandido1)
                return (nodoAct.camino,nodoAct.costo)
            if nodoAct.profundidad < maxPro:
                ExpandirNodo(nodoAct)
                expandido.append((nodoAct.pos.posx,nodoAct.pos.posy))
        maxPro+=1
        expandido1.appende(expandido.copy())  
    
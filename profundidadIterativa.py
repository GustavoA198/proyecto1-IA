from nodoProfundidad import NodoProfundidad as nodo
from posicion import Posicion

def newG(new): # determina el costo de moverse a una posicion
    if new == 0:
        return 1
    elif new == 4:
        return 1
    return new

def Verificador(nodo): #imprime un nodo
        aux=str(nodo.pos.posx) + " " + str(nodo.pos.posy) + " " + str(nodo.costo)+ " "
        for i in nodo.camino:
            aux = aux + " "+ str(i.posx) + " " +str(i.posy)
        print(aux)

def crearNodo(y, x, g, p, camino, matriz): # crea un nodo
    copia = camino.copy()
    if (y >= 0 and y < len(matriz) and x >= 0 and x < len(matriz[0]) and Posicion(y,x).existe(copia)):
        new = newG(int(matriz[y][x])) # el costo de movermme a una posicion
        if (new != 5):
            copia.append(Posicion(y, x))
            return nodo(Posicion(y, x), copia, p+1, new+g)
    return [0]

def ExpandirNodo(nodo): # añade nodos creado a la pila principal
    camino = nodo.camino.copy()
    newNodos = [] #lista auxiliar donde se añaden los posible nuevos nodos
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
            Verificador(newNodo)# imprime el nodo

def index(Matriz, buscar): # busca Pinocho
    index = (0, 0)
    for y, fila in enumerate(Matriz):
        for x, dato in enumerate(fila):
            if (dato == buscar):
                index = Posicion(y, x)
                return index

def ProfundidadIterativa(Matriz):
    global matrizA
    matrizA = Matriz
    Pinocho = index(Matriz, 1) #busco a pinocho
    maxPro = 0
    expandido1 = [] # auxiliar para guarda nodos expandidos
    while True:
        nodoi = nodo(Pinocho, [Pinocho], 0, 0) #nodo inicial
        global Pila
        Pila = []
        Pila.append(nodoi)
        expandido = []
        while (len(Pila) != 0):
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
        aux = expandido.copy()
        expandido1.append(aux)  
    
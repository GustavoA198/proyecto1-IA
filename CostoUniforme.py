matriz =[[ 1 , 3, 1 , 3 , 1], 
         [ 4, 0, 1 , 1 , 1], 
         [ 1 , 1, 0 , 0 ,5],
         [ 1 , 1, 1 , 2 , 1]]

import csv

with open('Matriz.txt', newline='') as archivo:
    lector = csv.reader(archivo, delimiter=',')
    matriz = []
    for fila in lector:
        matriz.append(fila)

print(int (matriz[1][2]) == 1)

pila = []

# la funcion recibe los datos del nodo que estamos expandiendo
# con esto, crea un nodo el cual es un lista# en la que:
# la posicion 0 y 1 son  "y" y "x" respectivamente,
# la posicion 2 es el cosot acumulado, y 
# la posicion 3 es una lista con el camino recorrido


def crearNodo (y,x,g,camino):
    copia = camino.copy()
    if (y >= 0 and y<4 and x>=0 and x < 5):
        newG = int(matriz[y][x])
        if (newG != 0):
            copia.append((y,x))
            return [y,x,newG+g ,copia]
    return [0]


#  Este metodo inserta un elemento en su posicion correspondiente 
#  segun la costo acumulado, organizando cada en nodo en la lista 
#  de mayor a menor.

def Agregar (newNodo):
    for i,nodo in enumerate(pila):
        if newNodo[2]>nodo[2]:
            pila.insert(i,newNodo)
            return None
    pila.append(newNodo)

#la funcion recibe un posicon recibe un nodo a expandir
#este crear una lista con cuatro nodos, los correspondiente
# a moverse arriba, abajo,derecha o izquierda

# despues recorre la lista, en la que mediente un if decidimos si agregar o no,
# cada nodo a la pila
      
def Extender (pos):
    g = pos[2]
    camino = pos[3].copy()
    newNodos = []
    newNodos.append(crearNodo(pos[0]-1,pos[1],g,camino)) ## moverse arriba
    newNodos.append(crearNodo(pos[0]+1,pos[1],g,camino)) ## moverse abajo
    newNodos.append(crearNodo(pos[0],pos[1]+1,g,camino)) ## moverse derecha    
    newNodos.append(crearNodo(pos[0],pos[1]-1,g,camino)) ## moverse izquierda
    

    for newNodo in newNodos:
        if (newNodo != [0]):
            Agregar(newNodo) 

# esta funcion recibe un matriz que representa el ambiente actual y una letra a buscar
# se buscar la letra dentro de la matriz y se retorna una tupla con  "y" y "x" 

def index(Matriz, buscar):
    index = (0,0)
    for y, fila in enumerate(Matriz):
        for x, dato in enumerate(fila):
            if (dato == buscar):
                index = (y,x)
                matriz[y][x] = 1
                return index
            
# esta es la funcion principal
# recibe una matriz con el ambiente a trabajar
# se guaeda la posicion  de pinocho y la de geppetto
# se crea el primer nodo y se agrega a la pila
# expandimos nodos de la pila mientras se llega a la meta o ya no hayan mas nodos a expandir

def agenteP (MatrizPos):
    Pinocho = index(MatrizPos, 4)
    Meta = index(MatrizPos, 5)
    Nodo1 = [Pinocho[0],Pinocho[1],0,[Pinocho]]

    pila.append(Nodo1)

    isMeta = False

    while not(isMeta):
        nodoAct = pila.pop()
        posAct = (nodoAct[0], nodoAct[1])
        if (posAct == Meta):
            isMeta = True
        else:
            print(nodoAct,"este nodo actual")
            Extender (nodoAct)
    return nodoAct

    

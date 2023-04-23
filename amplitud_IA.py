from nodo import Nodo as nodo
from posicion import Posicion as posicion

""" 
0 -> vacio
1 -> pinocho
2 -> cigarrillos
3 -> zorro
4 -> geppeto
5 -> sin camino """

matriz = [
    [0, 3, 0, 3, 0],
    [1, 5, 0, 0, 0],
    [0, 0, 5, 5, 4],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0]
]

#buscar a pinocho que es el numero 1 en la matriz
def buscarPinocho(matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz)):
            if matriz[fila][columna] == 1:
                print("fila:", fila, ",columna:", columna)
                return fila, columna
            
#calculo del costo de pasar por la casilla
def costoAcumulado(posicionN, juego):
    costoN = 0
    if juego[posicionN.posx][posicionN.posy] == 0:
        costoN += 1
    elif juego[posicionN.posx][posicionN.posy] == 4: 
        costoN += 1
    else:
        costoN += juego[posicionN.posx][posicionN.posy] 
    return costoN



#expandir el nodo de arriba
def arriba(nodoActual, cola, juego):
    if (nodoActual.pos.posy > 0):
        posicionNueva = posicion(nodoActual.pos.posx, nodoActual.pos.posy-1)
        caminoA = nodoActual.camino.copy()
        costos = nodoActual.costo
        #calculo del costo de pasar por la casilla
        costos += costoAcumulado(posicionNueva,juego)

        if juego[posicionNueva.posx][posicionNueva.posy] != 5:
            caminoA.append(posicionNueva)
            nuevoNodo = nodo(posicionNueva, caminoA, costos)
            cola.append(nuevoNodo)            
            nodosExpandidos.append((nuevoNodo.pos.posx, nuevoNodo.pos.posy))

#expandir el nodo de abajo
def abajo(nodoActual, cola, juego):
    if (nodoActual.pos.posy < len(juego)-1):
        posicionNueva = posicion(nodoActual.pos.posx, nodoActual.pos.posy+1)
        caminoA = nodoActual.camino.copy()
        costos = nodoActual.costo
        #calculo del costo de pasar por la casilla
        costos += costoAcumulado(posicionNueva, juego) 

        if juego[posicionNueva.posx][posicionNueva.posy] != 5:
            caminoA.append(posicionNueva)
            nuevoNodo = nodo(posicionNueva, caminoA, costos)
            cola.append(nuevoNodo)            
            nodosExpandidos.append((nuevoNodo.pos.posx, nuevoNodo.pos.posy))

#expandir el nodo de la izquierda
def izquierda(nodoActual, cola, juego):
    if (nodoActual.pos.posx > 0):
        posicionNueva = posicion(nodoActual.pos.posx-1, nodoActual.pos.posy)
        caminoA = nodoActual.camino.copy()
        costos = nodoActual.costo
        #calculo del costo de pasar por la casilla
        costos += costoAcumulado(posicionNueva, juego)

        if juego[posicionNueva.posx][posicionNueva.posy] != 5:
            caminoA.append(posicionNueva)
            nuevoNodo = nodo(posicionNueva, caminoA, costos)
            cola.append(nuevoNodo)            
            nodosExpandidos.append((nuevoNodo.pos.posx, nuevoNodo.pos.posy))
            

#expandir el nodo de la derecha
def derecha(nodoActual, cola, juego):
    if nodoActual.pos.posx < len(juego)-1:
        posicionNueva = posicion(nodoActual.pos.posx+1, nodoActual.pos.posy)
        caminoA = nodoActual.camino.copy()
        costos = nodoActual.costo
        #calculo del costo de pasar por la casilla
        costos += costoAcumulado(posicionNueva, juego)

        if juego[posicionNueva.posx][posicionNueva.posy] != 5:
            caminoA.append(posicionNueva)
            nuevoNodo = nodo(posicionNueva, caminoA, costos)
            cola.append(nuevoNodo)
            nodosExpandidos.append((nuevoNodo.pos.posx, nuevoNodo.pos.posy))



nodosExpandidos = [] # lista para guardar una upla con los indices x y y de los nodos expandidos
def busquedaAmplitud(juegoo):    
    # nodo inicial
    pinocho = buscarPinocho(juegoo)
    pos = posicion(pinocho[0], pinocho[1])
    inicio = nodo(pos, [pos], 0) #raiz

    cola = []
    cola.append(inicio)  # añado el nodo raiz
    nodosExpandidos.append((inicio.pos.posx, inicio.pos.posy))
    # inicio de la busqueda amplitud
    iterador = 0 # selecciona el orden de izquierda o derecha
    while (True):
        if len(cola) == 0:
            print("No encontré")
            break
        #expando el nodo actual
        nodoActual = cola.pop(0)
        posX = nodoActual.pos.posx
        posY = nodoActual.pos.posy
        
        # paro si encontré a gepetto
        if juegoo[posX][posY] == 4:
            print("Encontre")
            break
        #print(nodoActual.costo , "costo")  
        
        #arriba
        arriba(nodoActual, cola, juegoo)                
        
        # abajo
        abajo(nodoActual, cola, juegoo)        

        
        if iterador == 0:                  
            izquierda(nodoActual, cola, juegoo)  # izquierda              
            derecha(nodoActual, cola, juegoo) # derecha
            iterador = 1
        else:
            derecha(nodoActual, cola, juegoo) # derecha
            izquierda(nodoActual, cola, juegoo)  # izquierda
            iterador = 0

    #imprimir los nodos expandidos
    for i in nodosExpandidos:
        print(i, end= ",")

    #imprimir los indices del camino rrecorrido por el ultimo nodo expandido        
    for i in nodoActual.camino:
        print("(",i.posx,",", i.posy, ")")
    print("el costo es:",nodoActual.costo)


busquedaAmplitud(matriz)
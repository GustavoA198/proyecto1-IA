from nodoProfundidad import NodoProfundidad as nodo
from posicion import Posicion as posicion

""" 
0 -> vacio
1 -> pinocho
2 -> cigarrillos
3 -> zorro
4 -> geppeto
5 -> sin camino """
"""matriz = [
    [0, 3, 0, 3, 0],
    [1, 5, 0, 0, 0],
    [0, 0, 5, 5, 4],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0]
]
"""

cola = []
def Verificador(nodo):
        aux=str(nodo.pos.posx) + " " + str(nodo.pos.posy) + " " +str(nodo.profundidad)+""+ str(nodo.costo)+ " "
        for i in nodo.camino:
            aux = aux + " "+ str(i.posx) + " " +str(i.posy)
        print(aux)

#buscar a pinocho que es el numero 1 en la matriz
def buscarPinocho(matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == 1:
                print("fila:", fila, ",columna:", columna)
                return fila, columna
            
def agregar (nodo):
    pro = nodo.profundidad
    for i in range (len(cola)):
        nodoi = cola[i]
        if pro <= nodoi.profundidad:
            cola.insert(i,nodo)
            return None
    cola.append(nodo)
        

            
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
def arriba(nodoActual, juego):
    if (nodoActual.pos.posx > 0):
        posicionNueva = posicion(nodoActual.pos.posx-1, nodoActual.pos.posy)
        caminoA = nodoActual.camino.copy()
        costos = nodoActual.costo
        #calculo del costo de pasar por la casilla
        costos += costoAcumulado(posicionNueva,juego)
        newP = nodoActual.profundidad + 1

        if juego[posicionNueva.posx][posicionNueva.posy] != 5 and posicionNueva.existe(caminoA):
            caminoA.append(posicionNueva)
            nuevoNodo = nodo(posicionNueva, caminoA, newP, costos)
            Verificador(nuevoNodo)
            agregar(nuevoNodo) 

#expandir el nodo de abajo
def abajo(nodoActual, juego):
    if (nodoActual.pos.posx < len(juego)-1):
        posicionNueva = posicion(nodoActual.pos.posx + 1, nodoActual.pos.posy)
        caminoA = nodoActual.camino.copy()
        costos = nodoActual.costo
        #calculo del costo de pasar por la casilla
        costos += costoAcumulado(posicionNueva, juego)
        newP = nodoActual.profundidad + 1

        if juego[posicionNueva.posx][posicionNueva.posy] != 5 and posicionNueva.existe(caminoA):
            caminoA.append(posicionNueva)
            nuevoNodo = nodo(posicionNueva, caminoA, newP, costos)
            Verificador(nuevoNodo)
            agregar(nuevoNodo) 

#expandir el nodo de la izquierda
def izquierda(nodoActual,  juego):
    if (nodoActual.pos.posy > 0):
        posicionNueva = posicion(nodoActual.pos.posx, nodoActual.pos.posy-1)
        caminoA = nodoActual.camino.copy()
        costos = nodoActual.costo
        #calculo del costo de pasar por la casilla
        costos += costoAcumulado(posicionNueva, juego)
        newP = nodoActual.profundidad + 1


        if juego[posicionNueva.posx][posicionNueva.posy] != 5 and posicionNueva.existe(caminoA):
            caminoA.append(posicionNueva)
            nuevoNodo = nodo(posicionNueva, caminoA, newP, costos)
            Verificador(nuevoNodo)
            agregar(nuevoNodo)
            

#expandir el nodo de la derecha
def derecha(nodoActual, juego):
    if nodoActual.pos.posy < len(juego[0])-1:
        posicionNueva = posicion(nodoActual.pos.posx, nodoActual.pos.posy + 1)
        caminoA = nodoActual.camino.copy()
        costos = nodoActual.costo
        #calculo del costo de pasar por la casilla
        costos += costoAcumulado(posicionNueva, juego)
        newP = nodoActual.profundidad + 1


        if juego[posicionNueva.posx][posicionNueva.posy] != 5 and posicionNueva.existe(caminoA):
            caminoA.append(posicionNueva)
            nuevoNodo = nodo(posicionNueva, caminoA, newP, costos)
            Verificador(nuevoNodo)  
            agregar(nuevoNodo)

def busquedaAmplitud(juegoo):    
    # nodo inicial
    pinocho = buscarPinocho(juegoo)
    pos = posicion(pinocho[0], pinocho[1])
    inicio = nodo(pos, [pos],0, 0) #raiz
    expandidos = []
    cola.append(inicio)  # añado el nodo raiz
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
        expandidos.append((posX,posY))
        if(nodoActual.profundidad % 2 == 1):
            arriba(nodoActual, juegoo)  # arriba num 1
            abajo(nodoActual, juegoo) # abajo num 2
            derecha(nodoActual,juegoo) # derecha num 3
            izquierda(nodoActual, juegoo)  # izquierda num 4       
        else:
            izquierda(nodoActual, juegoo)  # izquierda num 4
            derecha(nodoActual,juegoo) # derecha num 3
            abajo(nodoActual, juegoo) # abajo num 2
            arriba(nodoActual, juegoo)  # arriba num 1

    #imprimir los indices del camino rrecorrido por el ultimo nodo expandido        
    print(expandidos)
    return nodoActual.camino,nodoActual.costo

#busquedaAmplitud(matriz)
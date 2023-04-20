class nodo:
    def __init__(self, pos, camino, profundidad, costo):
        self.pos = pos
        self.camino = camino
        self.profundidad = profundidad
        self.costo = costo


class posicion:
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy

""" 
0 -> vacio
1 -> pinocho
2 -> cigarrillos
3 -> zorro
4 -> geppeto
5 -> sin camino """

juego = [
    [0, 3, 0, 3, 0],
    [1, 5, 0, 0, 0],
    [0, 0, 5, 5, 4],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0]
]

# ayuda a comparar la lista de recorridos con una posicion,para evitar expandir el mismo nodo dos veces
def buscarElemento(lista, elemento):
    for i in lista:
        if i.posx == elemento.posx and i.posy == elemento.posy:
            return True
    else:
        return False

#buscar a pinocho que es el numero 1 en la matriz
def buscarPinocho(matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz)):
            if matriz[fila][columna] == 1:
                print("fila:", fila, ",columna:", columna)
                return fila, columna
            
#calculo del costo de pasar por la casilla
def costoAcumulado(posicionN):
    costoN = 0
    if juego[posicionN.posx][posicionN.posy] == 0:
        costoN += 1
    elif juego[posicionN.posx][posicionN.posy] == 4: 
        costoN += 1
    else:
        costoN += juego[posicionN.posx][posicionN.posy] 
    return costoN

#def max profundidad actual
def maxProfundidad(profundidad1, profundidad2):
    r = 0
    if profundidad1 > profundidad2:
        r = profundidad1
        return r
    else:
        r = profundidad2
        return r

# nodo inicial
pinocho = buscarPinocho(juego)
pos = posicion(pinocho[0], pinocho[1])
inicio = nodo(pos, [pos], 0, 0)

def profundidadIterativa():
    maxPro = 0 # Variable que sirve para ver la profundidad a la que esta el ultimo nodo expueto
    auxiliarProfundidad = 0  
    encontre = False  
    caminoR = []
    while (maxPro >= auxiliarProfundidad and encontre== False): 
        costo = 0 #calcular el valor del costo
        pila = []
        pila.append(inicio)  # añado el nodo raiz
        # inicio de la busqueda por profundidad   
        while (True):
            if len(pila) == 0:
                print("No encontré")
                break
            #expando el nodo actual
            nodoActual = pila.pop()
            posX = nodoActual.pos.posx
            posY = nodoActual.pos.posy
            
            # paro si encontré a gepetto
            if juego[posX][posY] == 4:
                print("Encontre")
                encontre  = True
                caminoR = nodoActual.camino
                break############################################################
            print(nodoActual.costo , "costo")  
            
            # arriba
            if (nodoActual.pos.posy > 0):
                posicionNueva = posicion(nodoActual.pos.posx, nodoActual.pos.posy-1)
                profundidadA = nodoActual.profundidad + 1
                caminoA = nodoActual.camino.copy()
                costos = nodoActual.costo
                #calculo del costo de pasar por la casilla
                costos += costoAcumulado(posicionNueva)

                if buscarElemento(nodoActual.camino, posicionNueva) == False and juego[posicionNueva.posx][posicionNueva.posy] != 5:
                    caminoA.append(posicionNueva)
                    nuevoNodo = nodo(posicionNueva, caminoA, profundidadA, costos)
                    pila.append(nuevoNodo)
                    maxPro = maxProfundidad(int(profundidadA), int(maxPro)) 
                    

            # abajo
            if (nodoActual.pos.posy < len(juego)-1):
                posicionNueva = posicion(nodoActual.pos.posx, nodoActual.pos.posy+1)
                profundidadA = nodoActual.profundidad + 1
                caminoA = nodoActual.camino.copy()
                costos = nodoActual.costo
                #calculo del costo de pasar por la casilla
                costos += costoAcumulado(posicionNueva)

                if buscarElemento(nodoActual.camino, posicionNueva) == False and juego[posicionNueva.posx][posicionNueva.posy] != 5:
                    caminoA.append(posicionNueva)
                    nuevoNodo = nodo(posicionNueva, caminoA, profundidadA, costos)
                    pila.append(nuevoNodo)
                    maxPro2 = maxPro
                    aux = int(profundidadA)
                    maxPro = maxProfundidad(aux, maxPro2)
                    
            # izquierda
            if (nodoActual.pos.posx > 0):
                posicionNueva = posicion(nodoActual.pos.posx-1, nodoActual.pos.posy)
                profundidadA = nodoActual.profundidad + 1
                caminoA = nodoActual.camino.copy()
                costos = nodoActual.costo
                #calculo del costo de pasar por la casilla
                costos += costoAcumulado(posicionNueva)

                if buscarElemento(nodoActual.camino, posicionNueva) == False and juego[posicionNueva.posx][posicionNueva.posy] != 5:
                    caminoA.append(posicionNueva)
                    nuevoNodo = nodo(posicionNueva, caminoA, profundidadA, costos)
                    pila.append(nuevoNodo)
                    maxPro = maxProfundidad(int(profundidadA), maxPro) 

            # derecha
            if nodoActual.pos.posx < len(juego)-1:
                posicionNueva = posicion(nodoActual.pos.posx+1, nodoActual.pos.posy)
                profundidadA = nodoActual.profundidad + 1
                caminoA = nodoActual.camino.copy()
                costos = nodoActual.costo
                #calculo del costo de pasar por la casilla
                costos += costoAcumulado(posicionNueva)

                if buscarElemento(nodoActual.camino, posicionNueva) == False and juego[posicionNueva.posx][posicionNueva.posy] != 5:
                    caminoA.append(posicionNueva)
                    nuevoNodo = nodo(posicionNueva, caminoA, profundidadA, costos)
                    pila.append(nuevoNodo)
                    maxPro = maxProfundidad(int(profundidadA), maxPro)    
        
            
            for i in nodoActual.camino:
                print(i.posx, i.posy)
            print("el costo es:",nodoActual.costo)
            print("la profundidad es:",nodoActual.profundidad)
       
        auxiliarProfundidad += 1 ## iterador
    for i in caminoR:
                print(i.posx, i.posy)


profundidadIterativa()
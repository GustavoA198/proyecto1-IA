from posicion import Posicion
class CostoUniform:
    def __init__(self):
        self.respuesta =""
        self.pila = []
    # la funcion recibe los datos del nodo que estamos expandiendo
    # con esto, crea un nodo el cual es un lista# en la que:
    # la posicion 0 y 1 son  "y" y "x" respectivamente,
    # la posicion 2 es el cosot acumulado, y 
    # la posicion 3 es una lista con el camino recorrido
    """
    0 -> vacio
    1 -> pinocho 
    2 -> cigarrillos
    3 -> zorro
    4 -> geppeto
    5 -> sin camino """

    def newG (self,new):
        if new == 0 :return 1
        elif new == 4 : return 1
        return new

    def crearNodo (self,y,x,g,camino, matriz):
        copia = camino.copy()
        if (y >= 0 and y<5 and x>=0 and x < 5):
            new = self.newG(int(matriz[y][x]))
            if (new != 5):
                copia.append(Posicion(y,x))
                return [y,x,new+g ,copia]
        return [0]


    #  Este metodo inserta un elemento en su posicion correspondiente 
    #  segun la costo acumulado, organizando cada en nodo en la lista 
    #  de mayor a menor.

    def Agregar (self,newNodo):
        for i,nodo in enumerate(self.pila):
            if newNodo[2]>nodo[2]:
                self.pila.insert(i,newNodo)
                return None
        self.pila.append(newNodo)

    #la funcion recibe un posicon recibe un nodo a expandir
    #este crear una lista con cuatro nodos, los correspondiente
    # a moverse arriba, abajo,derecha o izquierda

    # despues recorre la lista, en la que mediente un if decidimos si agregar o no,
    # cada nodo a la pila
        
    def Extender (self,pos,matriz):
        g = pos[2]
        camino = pos[3].copy()
        newNodos = []
        newNodos.append(self.crearNodo(pos[0]-1,pos[1],g,camino,matriz)) ## moverse arriba
        newNodos.append(self.crearNodo(pos[0]+1,pos[1],g,camino,matriz)) ## moverse abajo
        newNodos.append(self.crearNodo(pos[0],pos[1]+1,g,camino,matriz)) ## moverse derecha    
        newNodos.append(self.crearNodo(pos[0],pos[1]-1,g,camino,matriz)) ## moverse izquierda

        for newNodo in newNodos: ## decide si agregar o NO un nuevo nodo a la pila
            if (newNodo != [0]):
                self.Agregar(newNodo) 

    # esta funcion recibe un matriz que representa el ambiente actual y una letra a buscar
    # se buscar la letra dentro de la matriz y se retorna una tupla con  "y" y "x" 

    def index(self,Matriz, buscar):
        index = (0,0)
        for y, fila in enumerate(Matriz):
            for x, dato in enumerate(fila):
                if (dato == buscar):
                    index = Posicion(y,x)
                    return index
                
    # esta es la funcion principal
    # recibe una matriz con el ambiente a trabajar
    # se guaeda la posicion  de pinocho y la de geppetto
    # se crea el primer nodo y se agrega a la pila
    # expandimos nodos de la pila mientras se llega a la meta o ya no hayan mas nodos a expandir

    def agenteP (self,MatrizPos):
        Pinocho = self.index(MatrizPos, 1)
        Meta =self.index(MatrizPos, 4)
        Nodo1 = [Pinocho.posx,Pinocho.posy,0,[Pinocho]]

        self.pila.append(Nodo1)

        isMeta = False
        while not(isMeta):
            nodoAct =self.pila.pop()
            posAct = (nodoAct[0], nodoAct[1])
            metaAux = (Meta.posx , Meta.posy)
            print( posAct , "========" , metaAux)
            if (posAct == metaAux):
                isMeta = True
            else:
                self.Extender (nodoAct,MatrizPos)
        self.respuesta = nodoAct
## PRUEBA
juego = [
    [0, 3, 0, 3, 0],
    [1, 5, 0, 0, 0],
    [0, 0, 5, 5, 4],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0]]
#print(juego)
p = CostoUniform()
p.agenteP(juego)
print(p.respuesta , "PPPPPPPPPP")  

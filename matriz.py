import csv 
    
def crearMat(ruta):
    matriz = []        
    with open(ruta, newline='') as archivo:
        lector = csv.reader(archivo, delimiter=',')    
        for fila in lector: # Añade fila por fila el texto en una matriz
            matriz.append(fila)

    matriz2=[]
    fila2=[]
    for fila in range (0,len(matriz)): #recorre la primera matriz, para pasarla a enteros
        for columna in range(0,len(matriz[fila])):
            fila2.append(int(matriz[fila][columna]))
        aux = fila2.copy()
        matriz2.append(aux)
        fila2=[]
        

    return matriz2


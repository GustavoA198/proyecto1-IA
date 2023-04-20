import csv 
    
def crearMat(ruta):
    matriz = []        
    with open(ruta, newline='') as archivo:
        lector = csv.reader(archivo, delimiter=',')    
        for fila in lector:
            matriz.append(fila)
    return matriz
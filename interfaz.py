import time
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog as FileDialog
import matriz as Matrizz
from CostoUniforme import CostoUniform
import amplitud_IA as amp
import profundidadIterativa as pIter

""" 
0 -> vacio
1 -> pinocho 
2 -> cigarrillos
3 -> zorro
4 -> geppeto
5 -> sin camino """

listaImg = ["img/vacio.jpg","img/pinocho1.jpg", "img\cigarrillo blanco.jpg","img/zorroBlanco.jpg","img/gepetoblanco.jpg","img/negro.jpg"]
listaImgRes = ["img/verde.jpg","img/piverde.jpg", "img\cigarrillo verde.jpg","img/zorroverde.jpg","img/gepetoverde.jpg","img/negro.jpg"]

# Funciones para los botones de búsqueda y carga de matriz
def buscar_1():
    # Aquí va la lógica para Amplitud
    Dibujar2(mat)
    camino = amp.busquedaAmplitud(mat)
    time.sleep(0.2)
    dibujarRespuesta(0,camino,mat)

def buscar_2():
    # Aquí va la lógica para Costo Uniforme
    Dibujar2(mat)
    pinocho = CostoUniform()
    pinocho.agenteP(mat)
    res = pinocho.respuesta
    time.sleep(0.2)
    dibujarRespuesta(0,res[3],mat)

def buscar_3():
    # Aquí va la lógica para Profundidad
    Dibujar2(mat)
    camino = pIter.profundidadIterativa(mat) 
    time.sleep(0.2)
    dibujarRespuesta(0,camino,mat)


def cargar_matriz():
    ruta = FileDialog.askopenfilename(title="Abrir un fichero",initialdir="C:",
                                         filetypes=(("Ficheros de texto","*.txt"),
                                                    ("Ficheros de CSV","*.csv"),
                                                    ("Todos los ficheros", "*.*"),)) 
    global mat
    mat = Matrizz.crearMat(ruta).copy()
    global matriz 
    matriz = Frame(ventana, width=570, height=600)
    matriz.place(x=125, y=50)

    global imgObjects
    global imgObjectsRes
    global Tam
    Tam = int(460/max(len(mat),len(mat[0])))
    imgObjects = crearImagenes(listaImg,Tam)
    imgObjectsRes = crearImagenes(listaImgRes,Tam)
    dibujar(70,0,0,mat) 

# Crear ventana
ventana = Tk()
ventana.title("Proyecto de IA" )
ventana.config(height=570,width=850)

# Crear botones de búsqueda y carga de matriz
btn_busq_1 = Button(ventana, text="Búsqueda por Amplitud", command=buscar_1)
btn_busq_2 = Button(ventana, text="Búsqueda por Costo Uniforme", command=buscar_2)
btn_busq_3 = Button(ventana, text="Búsqueda por Profunfidad Iterativa", command=buscar_3)
btn_cargar = Button(ventana, text="Cargar matriz", command=cargar_matriz)

# Colocar botones en la ventana
btn_busq_1.place(x=20, y=10,)
btn_busq_2.place(x=170, y=10)
btn_busq_3.place(x=355, y=10)
btn_cargar.place(x=750, y=10)

# Crear espacio para la matriz de imágenes


# Crear lista de objetos de imágenes
def crearImagenes(listImg,tam):
    imgObjects = []
    for img in listImg:
        imageness =[Image.open(img)]
        imagen = imageness[0].resize((tam,tam), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(imagen)
        imgObjects.append(image)
    return imgObjects



def dibujar(time,fila, columna,matrix): 
    if fila >= len(matrix):
        return
    if columna >= len(matrix[0]):
        fila += 1
        columna = 0
    if columna < len(matrix[0]) and fila < len(matrix):
        aux=int(matrix[fila][columna])
        Label(matriz, image=imgObjects[aux]).grid(row=fila, column=columna)
    matriz.after(time, lambda: dibujar(time,fila, columna+1,matrix))

def Dibujar2(matrizz):
    for i in range (len(matrizz)):
        for j in range (len(matrizz[i])):
            aux=int(matrizz[i][j])
            Label(matriz, image=imgObjects[aux]).grid(row=i, column=j)
    


def dibujarRespuesta(index,lista,matrix):
    if index < len(lista):
        pos = lista[index]
        aux = matrix[pos.posx][pos.posy]
        Label(matriz, image=imgObjectsRes[aux]).grid(row=pos.posx, column=pos.posy)
        matriz.after(100, lambda: dibujarRespuesta(index+1,lista,matrix))

# Iniciar bucle principal de la ventana
ventana.mainloop()

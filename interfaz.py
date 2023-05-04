from tkinter.font import Font
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog as FileDialog
import matriz as Matrizz
from CostoUniforme import CostoUniform
import amplitud_IA as amp
import ProfundidadIterativa as pIter

""" 
0 -> vacio
1 -> pinocho 
2 -> cigarrillos
3 -> zorro
4 -> geppeto
5 -> sin camino """

listaImg = ["img/vacio.jpg","img\pinocho1marco.jpg", "img\cigarrillo blancomarco.jpg","img\zorroblancomarco.jpg","img\gepetoblancomarco.jpg","img/negro.jpg"]
listaImgRes = ["img/verde.jpg","img\piVerdemarco.jpg", "img\cigarrillo verde marco.jpg","img\zorroverdemarco.jpg","img\gepetoverdemarco.jpg","img/negro.jpg"]


# Funciones para los botones de búsqueda y carga de matriz

def buscar_1():
    # Aquí va la lógica para Amplitud
    Dibujar2(mat)
    nodo = amp.busquedaAmplitud(mat)
    dibujarRespuesta(0,nodo[0],mat)
    result.set(str(nodo[1]))

def buscar_2():
    # Aquí va la lógica para Costo Uniforme
    Dibujar2(mat)
    pinocho = CostoUniform()
    pinocho.agenteP(mat)
    res = pinocho.respuesta
    dibujarRespuesta(0,res[3],mat)

    result.set(str(res[2]))

def buscar_3():
    # Aquí va la lógica para Profundidad
    Dibujar2(mat)
    nodo = pIter.ProfundidadIterativa(mat) 
    dibujarRespuesta(0,nodo[0],mat)
    result.set(str(nodo[1]))

def cargar_matriz():
    ruta = FileDialog.askopenfilename(title="Abrir un fichero",initialdir="C:",
                                         filetypes=(("Ficheros de texto","*.txt"),
                                                    ("Ficheros de CSV","*.csv"),
                                                    ("Todos los ficheros", "*.*"),)) 
    global mat
    mat = Matrizz.crearMat(ruta).copy()
    global matriz 
    matriz = Frame(ventana, width=570, height=600,bg= "white")
    matriz.place(x=125, y=100)
    result.set("")

    global imgObjects
    global imgObjectsRes
    global Tam
    Tam = int(460/max(len(mat),len(mat[0])))
    imgObjects = crearImagenes(listaImg,Tam)
    imgObjectsRes = crearImagenes(listaImgRes,Tam)
    dibujar(70,0,0,mat) 

# Crear ventana
ventana = Tk()
ventana.title("Proyecto de IA")
ventana.config(bg= "white")
imagen = ImageTk.PhotoImage(Image.open("img/fondo pinocho2jpg.jpg").resize((810,590),Image.ANTIALIAS))
Label(ventana, image=imagen, bd=0).pack()
fuente =  Font(family="Roboto Cn", size=14)
lCosto = Label(ventana,text = "Costo")
lCosto.place(x=720,y=120)
lCosto.config(font = fuente, bg = "white")

result = StringVar()
pCosto = Label(ventana,textvariable=result)
pCosto.place(x=735,y=150)
pCosto.config(font = fuente, bg = "white")
# Crear botones de búsqueda y carga de matriz

images_1 = ImageTk.PhotoImage(Image.open("img/amplitud.jpg").resize((150,40),Image.ANTIALIAS))
btn_busq_1 = Button(ventana, image=images_1, command=buscar_1)

images_2 = ImageTk.PhotoImage(Image.open("img\costo uniforme.jpg").resize((150,40),Image.ANTIALIAS))
btn_busq_2 = Button(ventana, image=images_2, command=buscar_2)

images_3 = ImageTk.PhotoImage(Image.open("img\iterativa.jpg").resize((150,40),Image.ANTIALIAS))
btn_busq_3 = Button(ventana, image=images_3, command=buscar_3)

images_4 = ImageTk.PhotoImage(Image.open("img\cargar matriz.jpg").resize((150,40),Image.ANTIALIAS))
btn_cargar = Button(ventana, image=images_4, command=cargar_matriz)

# Colocar botones en la ventana
btn_busq_1.place(x=20, y=50,)
btn_busq_2.place(x=175, y=50)
btn_busq_3.place(x=330, y=50)
btn_cargar.place(x=600, y=50)


##-----funciones Auxiliares -------

# Crear lista de objetos de imágenes
def crearImagenes(listImg,tam):
    imgObjects = []
    for img in listImg:
        imageness =[Image.open(img)]
        imagen = imageness[0].resize((tam,tam), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(imagen)
        imgObjects.append(image)
    return imgObjects

# dibuja el ambiente que hay en la matriz con animaciones
def dibujar(time,fila, columna,matrix): 
    if fila >= len(matrix):
        return
    if columna >= len(matrix[0]):
        fila += 1
        columna = 0
    if columna < len(matrix[0]) and fila < len(matrix):
        aux=int(matrix[fila][columna])
        Label(matriz, image=imgObjects[aux], bg= "white").grid(row=fila, column=columna)
    matriz.after(time, lambda: dibujar(time,fila, columna+1,matrix))

#dibuja el TODO ambiente de la matriz instataneamente
def Dibujar2(matrizz):
    for i in range (len(matrizz)):
        for j in range (len(matrizz[i])):
            aux=int(matrizz[i][j])
            Label(matriz, image=imgObjects[aux],bg= "white").grid(row=i, column=j)
 #dibuja el camino de respuesta del algoritmo correspondiente   
def dibujarRespuesta(index,lista,matrix):
    if index < len(lista):
        pos = lista[index]
        aux = matrix[pos.posx][pos.posy]
        Label(matriz, image=imgObjectsRes[aux],bg= "white").grid(row=pos.posx, column=pos.posy)
        matriz.after(100, lambda: dibujarRespuesta(index+1,lista,matrix))

# Iniciar bucle principal de la ventana
ventana.mainloop()

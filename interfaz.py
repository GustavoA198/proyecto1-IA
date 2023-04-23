from tkinter import *
from PIL import Image, ImageTk
import time
from tkinter import filedialog as FileDialog
import matriz as Matrizz
from CostoUniforme import CostoUniform

""" 
0 -> vacio
1 -> pinocho 
2 -> cigarrillos
3 -> zorro
4 -> geppeto
5 -> sin camino """

listaImg = ["img/vacio.jpg","img/pinocho1.jpg", "img\cigarrillo blanco.jpg","img/zorroBlanco.jpg","img/gepetoblanco.jpg","img\cigarrillo verde.jpg"]
# Funciones para los botones de búsqueda y carga de matriz
def buscar_1():
    pass # Aquí va la lógica para Amplitud

def buscar_2():
    # Aquí va la lógica para Costo Uniforme
    print(mat , "MAAAAAAAS")
    pinocho = CostoUniform()
    pinocho.agenteP(mat)
    res = pinocho.respuesta

    print(res)

def buscar_3():
    pass # Aquí va la lógica para Profundidad

def cargar_matriz():
    ruta = FileDialog.askopenfilename(title="Abrir un fichero",initialdir="C:",
                                         filetypes=(("Ficheros de texto","*.txt"),
                                                    ("Ficheros de CSV","*.csv"),
                                                    ("Todos los ficheros", "*.*"),)) 
    print("la ruta es ",ruta)
    global mat
    mat = Matrizz.crearMat(ruta).copy()
    print(mat,"MATRIZZZZZZZZZZZZZZZZZZZZZZZZZXXXXXXXXXXXXXXXXXXXXXXXXX")
    crearImagenes(listaImg)
    dibujar(0,0,mat) 

# Crear ventana
ventana = Tk()
ventana.title("Proyecto de IA")
ventana.config(height=570,width=850)
#ventana.resizable(False, False)

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
matriz = Frame(ventana, width=600, height=600)
matriz.place(x=125, y=50)

# Crear lista de imágenes

imgObjects = []
def crearImagenes(listImg):
    for img in listImg:
        imageness =[Image.open(img)]
        imagen = imageness[0].resize((90,90), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(imagen)
        imgObjects.append(image)


#imageness =[PhotoImage(file="pinocho80.gif")]


def dibujar(fila, columna,matrixxxxx): 
    if fila >= 5:
        return
    if columna >= 5:
        fila += 1
        columna = 0
    if columna < 5 and fila < 5:
        ##aux = matriz[fila][columna]
        aux=int(matrixxxxx[fila][columna])
        Label(matriz, image=imgObjects[aux],background="gray").grid(row=fila, column=columna)
    matriz.after(100, lambda: dibujar(fila, columna+1,matrixxxxx))


          






# Iniciar bucle principal de la ventana
ventana.mainloop()

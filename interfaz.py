from tkinter import *
from PIL import Image, ImageTk
import time
from tkinter import filedialog as FileDialog
import matriz as Matrizz

# Funciones para los botones de búsqueda y carga de matriz
def buscar_1():
    pass # Aquí va la lógica para la búsqueda 1

def buscar_2():
    pass # Aquí va la lógica para la búsqueda 2

def buscar_3():
    pass # Aquí va la lógica para la búsqueda 3

def cargar_matriz():
    ruta = FileDialog.askopenfilename(title="Abrir un fichero",initialdir="C:",
                                         filetypes=(("Ficheros de texto","*.txt"),
                                                    ("Ficheros de CSV","*.csv"),
                                                    ("Todos los ficheros", "*.*"),)) 
    print("la ruta es ",ruta)
    mat = Matrizz.crearMat(ruta)
    print("sadas",mat)

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

# Crear matriz de imágenes
#imageness =[PhotoImage(file="pinocho80.gif")]
imageness =[Image.open("pinocho.gif")]
imagen = imageness[0].resize((90,90), Image.ANTIALIAS)
img = ImageTk.PhotoImage(imagen)

def dibujar(fila, columna):    
    if fila >= 5:
        return
    if columna >= 5:
        fila += 1
        columna = 0
    if columna < 5 and fila < 5:
        Label(matriz, image=img,background="Blue").grid(row=fila, column=columna)
    matriz.after(100, lambda: dibujar(fila, columna+1))

dibujar(0,0) 

          






# Iniciar bucle principal de la ventana
ventana.mainloop()

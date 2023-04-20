from tkinter import * 

# Funciones para los botones de búsqueda y carga de matriz
def buscar_1():
    pass # Aquí va la lógica para la búsqueda 1

def buscar_2():
    pass # Aquí va la lógica para la búsqueda 2

def buscar_3():
    pass # Aquí va la lógica para la búsqueda 3

def cargar_matriz():
    pass # Aquí va la lógica para cargar la matriz

# Crear ventana
ventana = Tk()
ventana.title("Interfaz de prueba")

# Crear botones de búsqueda y carga de matriz
btn_busq_1 = Button(ventana, text="Búsqueda 1", command=buscar_1)
btn_busq_2 = Button(ventana, text="Búsqueda 2", command=buscar_2)
btn_busq_3 = Button(ventana, text="Búsqueda 3", command=buscar_3)
btn_cargar = Button(ventana, text="Cargar matriz", command=cargar_matriz)

# Colocar botones en la parte superior de la ventana
btn_busq_1.pack(side="left", padx=10, pady=10)
btn_busq_2.pack(side="left", padx=10, pady=10)
btn_busq_3.pack(side="left", padx=10, pady=10)
btn_cargar.pack(side="left", padx=10, pady=10)

# Crear espacio para la matriz de imágenes
matriz = Frame(ventana, width=400, height=400)
matriz.pack(padx=10, pady=10)

# Crear matriz de imágenes
for i in range(5):
    for j in range(5):
        imagen = PhotoImage(file="pinocho50.gif")
        label = Label(matriz, image=imagen)
        label.grid(row=i, column=j)
        print(i, "j=", j)


# Crear etiquetas para los nombres
lbl_camilo = Label(ventana, text="Camilo")
lbl_jesus = Label(ventana, text="Jesus")
lbl_gustavo = Label(ventana, text="Gustavo")

# Colocar etiquetas en la parte inferior de la ventana
lbl_camilo.pack(side="left", padx=10, pady=10)
lbl_jesus.pack(side="left", padx=10, pady=10)
lbl_gustavo.pack(side="left", padx=10, pady=10)

# Iniciar bucle principal de la ventana
ventana.mainloop()

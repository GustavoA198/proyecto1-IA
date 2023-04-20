import tkinter as tk

def imprimir_numero(numero):
    print(numero)
    if numero < 10:
        root.after(1000, lambda: imprimir_numero(numero+1))

root = tk.Tk()
root.after(1000, lambda: imprimir_numero(1))
root.mainloop()

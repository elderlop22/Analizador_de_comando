from asyncore import read
import tkinter
import os
from tkinter import CENTER, Label, PhotoImage, StringVar, ttk
from tkinter.tix import COLUMN
from turtle import bgcolor, color


ventana = tkinter.Tk()
ventana.geometry('1050x500')
ventana.title("ANALIZADOR DE COMANDO")

imagenL = PhotoImage(file= "logo.png")
lblImagen = Label(ventana, image= imagenL, height=700, width= 1000).place(x=0, y=70)

ventana.resizable(0,0)
path_file = "/tmp/Comando.txt"

bienvenida_lbl = tkinter.Label(ventana, text= "Bienvenido", font='Arial 20 bold italic')
bienvenida_lbl.grid(row=0, column=0)
create_lbl = Label(ventana, text="Elaborado por: \n Elder López Chavarría",font='Arial 15 bold italic')
create_lbl.grid(row=7)

os.system('who >' + path_file)
print("¡Guardado con exito!")

	
lista_datos = []
with open(path_file) as fname:
    for lineas in fname:
        lista_datos.append(lineas.split())
        


  

tabla = ttk.Treeview(ventana, columns=[f"#{n}" for n in range(1, 6)])
tabla.config(show='headings')
tabla.grid(row=3, column=0)
tabla.heading("#1", text="Usuario")
tabla.heading("#2", text="Acción")
tabla.heading("#3", text="Fecha")
tabla.heading("#4", text="Hora")
tabla.heading("#5", text="Origen")

def mostrarTabla():
    end = len(lista_datos)
    for index in range(end):
        try:
            tabla.delete(index + 1)
            tabla.insert(parent='', index='end', iid=(index + 1), values=(lista_datos[index][0], lista_datos[index][1], lista_datos[index][2], lista_datos[index][3], lista_datos[index][4] ))
        except:
            tabla.insert(parent='', index='end', iid=(index + 1), values=(lista_datos[index][0], lista_datos[index][1], lista_datos[index][2], lista_datos[index][3], lista_datos[index][4] ))




def refrescar():
    os.system('who >' + path_file)
    print("¡Guardado con exito!")
    lista_datos = []
    with open(path_file) as fname:
        for lineas in fname:
            lista_datos.append(lineas.split())
            
    mostrarTabla()


guardar_matricula_btn = tkinter.Button(ventana, text='Refrescar', command= refrescar)
guardar_matricula_btn.grid(row=6, column=0)

mostrarTabla()
ventana.mainloop()

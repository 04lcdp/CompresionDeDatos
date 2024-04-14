#Comprima el contenido de un archivo en bloc de notas y envíelo a un
#compañero, adjuntando la codificación de cada caracter del texto enviado,
#para que pueda descomprimirlo. El programa a implementar debe
#comprimir y descomprimir.
import tkinter as tk
from tkinter import filedialog

def elegir_y_leer_archivo():
    root = tk.Tk()
    root.withdraw()
    ruta_archivo = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    if ruta_archivo:
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                print(contenido)
            return contenido
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return None
    else:
        print("No se seleccionó ningún archivo")
        return None

def Compresion(mensaje):
    return mensaje


opcion = input ("COMPRESION DE DATOS\n1. Compresion de Datos\n2.Descompresion de Datos\n\nElige tu opcion -> ")
if opcion == '1':
    contenido = elegir_y_leer_archivo()
#if contenido_archivo:
    #print("Contenido del archivo:")
    #print(contenido_archivo)
#else:
    #print("No se pudo leer ningún contenido.")




#mensaje = "hola"
#print(mensaje)

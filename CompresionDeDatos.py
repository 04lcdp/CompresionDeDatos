#Comprima el contenido de un archivo en bloc de notas y envíelo a un
#compañero, adjuntando la codificación de cada caracter del texto enviado,
#para que pueda descomprimirlo. El programa a implementar debe
#comprimir y descomprimir.
import tkinter as tk
from tkinter import filedialog

import heapq
from collections import defaultdict, Counter

class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def construir_arbol_huffman(texto):
    contador = Counter(texto)
    cola_prioridad = [NodoHuffman(caracter, frecuencia) for caracter, frecuencia in contador.items()]
    heapq.heapify(cola_prioridad)

    while len(cola_prioridad) > 1:
        izquierda = heapq.heappop(cola_prioridad)
        derecha = heapq.heappop(cola_prioridad)
        nodo_padre = NodoHuffman(None, izquierda.frecuencia + derecha.frecuencia)
        nodo_padre.izquierda = izquierda
        nodo_padre.derecha = derecha
        heapq.heappush(cola_prioridad, nodo_padre)

    return cola_prioridad[0]

def construir_tabla_codigos(arbol_huffman):
    tabla_codigos = defaultdict(str)
    pila = [(arbol_huffman, "")]
    while pila:
        nodo, codigo = pila.pop()
        if nodo.caracter is not None:
            tabla_codigos[nodo.caracter] = codigo
        if nodo.izquierda is not None:
            pila.append((nodo.izquierda, codigo + "0"))
        if nodo.derecha is not None:
            pila.append((nodo.derecha, codigo + "1"))
    return tabla_codigos

def comprimir(texto):
    arbol_huffman = construir_arbol_huffman(texto)
    tabla_codigos = construir_tabla_codigos(arbol_huffman)
    texto_codificado = ''.join(tabla_codigos[caracter] for caracter in texto)
    return texto_codificado, tabla_codigos

def descomprimir(texto_codificado, tabla_codigos):
    texto_decodificado = ""
    codigo_inverso = {codigo: caracter for caracter, codigo in tabla_codigos.items()}
    codigo_actual = ""
    for bit in texto_codificado:
        codigo_actual += bit
        if codigo_actual in codigo_inverso:
            texto_decodificado += codigo_inverso[codigo_actual]
            codigo_actual = ""
    return texto_decodificado

def archivocompresion():
    root = tk.Tk()
    root.withdraw()
    ruta_archivo = filedialog.askopenfilename(
        title="Elige un archivo para comprimir",
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

#def Compresion(mensaje):
#   return mensaje

opcion = input ("COMPRESION DE DATOS\n1. Compresion de Datos\n2.Descompresion de Datos\n\nElige tu opcion -> ")
if opcion == '1':
    contenido = archivocompresion()
    texto_codificado, tabla_codigos = comprimir(contenido)
    print("Texto codificado:", texto_codificado, tabla_codigos)
    texto_decodificado = descomprimir(texto_codificado, tabla_codigos)
    print("Texto decodificado:", texto_decodificado)
#if contenido_archivo:
    #print("Contenido del archivo:")
    #print(contenido_archivo)
#else:
    #print("No se pudo leer ningún contenido.")

#01111100101010001111100


#mensaje = "hola"
#print(mensaje)

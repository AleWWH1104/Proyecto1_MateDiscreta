import tkinter as tk
from tkinter import ttk

referencial = {str(i) for i in range(21)}.union(set('abcdefghijklmnopqrstuvwxyz'))
conjuntos = {}

def convertir_entrada_a_lista(entrada, referencial):
    elementos = entrada.replace('(', '').replace(')', '').replace(' ', '').split(',')
    conjunto = [el for el in elementos if el in referencial]
    return conjunto

def agregar_conjunto():
    nombre = entry_nombre.get()
    elementos = entry_conjunto.get()
    lista_elementos = convertir_entrada_a_lista(elementos, referencial)
    conjuntos[nombre] = lista_elementos
    print(f"Conjunto {nombre} agregado: {lista_elementos}")

root = tk.Tk()
root.title("Crear Conjuntos")

frame_principal = tk.Frame(root, bg="#335b78")
frame_principal.pack(fill="both", expand=True)

label_crear = tk.Label(frame_principal, text="Crear conjuntos", font=("Arial", 16, "bold"), fg="white", bg="#335b78")
label_crear.pack(pady=10)

entry_nombre = ttk.Entry(frame_principal, font=("Arial", 12))
entry_nombre.pack(padx=10, pady=5)

entry_conjunto = ttk.Entry(frame_principal, font=("Arial", 12))
entry_conjunto.pack(padx=10, pady=5)

button_new = ttk.Button(frame_principal, text="New", command=agregar_conjunto)
button_new.pack(pady=20)

root.mainloop()

import tkinter as tk
from tkinter import ttk

referencial = {str(i) for i in range(21)}.union(set('abcdefghijklmnopqrstuvwxyz'))
conjuntos = {}

def convertir_entrada_a_lista(entrada, referencial):
    elementos = entrada.replace('(', '').replace(')', '').replace(' ', '').split(',')
    conjunto = [el for el in elementos if el in referencial]
    return conjunto

def agregar_conjunto():
    nombre = entry_nombre.get()
    elementos = entry_conjunto.get()
    lista_elementos = convertir_entrada_a_lista(elementos, referencial)
    conjuntos[nombre] = lista_elementos
    print(f"Conjunto {nombre} agregado: {lista_elementos}")

root = tk.Tk()
root.title("Crear Conjuntos")

frame_principal = tk.Frame(root, bg="#335b78")
frame_principal.pack(fill="both", expand=True)

label_crear = tk.Label(frame_principal, text="Crear conjuntos", font=("Arial", 16, "bold"), fg="white", bg="#335b78")
label_crear.pack(pady=10)

entry_nombre = ttk.Entry(frame_principal, font=("Arial", 12))
entry_nombre.pack(padx=10, pady=5)

entry_conjunto = ttk.Entry(frame_principal, font=("Arial", 12))
entry_conjunto.pack(padx=10, pady=5)

button_new = ttk.Button(frame_principal, text="New", command=agregar_conjunto)
button_new.pack(pady=20)

root.mainloop()
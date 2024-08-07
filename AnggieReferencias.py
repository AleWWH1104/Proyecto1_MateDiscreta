import tkinter as tk
from tkinter import ttk

# Variable global para el conjunto referencial
referencial = set()
conjuntos = {}

# Función para definir el conjunto referencial
def definir_referencial():
    elementos = entry_referencial.get()
    global referencial
    referencial = set(elementos.replace('(', '').replace(')', '').replace(' ', '').split(','))
    print(f"Conjunto referencial definido: {referencial}")
    root_referencial.destroy()  # Cierra la ventana una vez definido el conjunto referencial
    crear_conjuntos()  # Llama a la función para crear conjuntos

# Función para convertir la entrada en una lista, verificando contra el referencial
def convertir_entrada_a_lista(entrada, referencial):
    elementos = entrada.replace('(', '').replace(')', '').replace(' ', '').split(',')
    conjunto = [el for el in elementos if el in referencial]
    return conjunto

# Función para agregar conjuntos basados en el referencial
def agregar_conjunto():
    nombre = entry_nombre.get()
    elementos = entry_conjunto.get()
    lista_elementos = convertir_entrada_a_lista(elementos, referencial)
    conjuntos[nombre] = lista_elementos
    print(f"Conjunto {nombre} agregado: {lista_elementos}")

# Función para definir la interfaz gráfica para crear conjuntos
def crear_conjuntos():
    global entry_nombre, entry_conjunto
    root_conjuntos = tk.Tk()
    root_conjuntos.title("Crear Conjuntos")

    frame_principal = tk.Frame(root_conjuntos, bg="#335b78")
    frame_principal.pack(fill="both", expand=True)

    label_crear = tk.Label(frame_principal, text="Crear conjuntos", font=("Arial", 16, "bold"), fg="white", bg="#335b78")
    label_crear.pack(pady=10)

    entry_nombre = ttk.Entry(frame_principal, font=("Arial", 12))
    entry_nombre.pack(padx=10, pady=5)

    entry_conjunto = ttk.Entry(frame_principal, font=("Arial", 12))
    entry_conjunto.pack(padx=10, pady=5)

    button_new = ttk.Button(frame_principal, text="New", command=agregar_conjunto)
    button_new.pack(pady=20)

    root_conjuntos.mainloop()

# Función principal
def main():
    global entry_referencial, root_referencial
    root_referencial = tk.Tk()
    root_referencial.title("Definir Conjunto Referencial")

    frame_principal = tk.Frame(root_referencial, bg="#335b78")
    frame_principal.pack(fill="both", expand=True)

    label_referencial = tk.Label(frame_principal, text="Definir conjunto referencial", font=("Arial", 16, "bold"), fg="white", bg="#335b78")
    label_referencial.pack(pady=10)

    entry_referencial = ttk.Entry(frame_principal, font=("Arial", 12))
    entry_referencial.pack(padx=10, pady=5)

    button_referencial = ttk.Button(frame_principal, text="Definir", command=definir_referencial)
    button_referencial.pack(pady=10)

    root_referencial.mainloop()

if __name__ == "__main__":
    main()

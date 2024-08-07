import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ConjuntoManager:
    def __init__(self, referencial):
        self.referencial = referencial

    def convertir_entrada_a_lista(self, entrada):
        def parse(s):
            stack = []
            current_list = []
            current_str = ''
            i = 0
            while i < len(s):
                char = s[i]
                if char == '(':
                    # Push current list onto stack and start new list
                    stack.append(current_list)
                    current_list = []
                    i += 1
                elif char == ')':
                    # End current list and pop from stack
                    if current_str:
                        current_list.append(current_str.strip())
                        current_str = ''
                    top_list = stack.pop()
                    top_list.append(current_list)
                    current_list = top_list
                    i += 1
                elif char == ',':
                    if current_str:
                        current_list.append(current_str.strip())
                        current_str = ''
                    i += 1
                else:
                    current_str += char
                    i += 1
            
            if current_str:
                current_list.append(current_str.strip())
            
            return current_list
        
        s = entrada.replace(' ', '')  # Eliminar espacios
        return parse(s)

    def validar_elementos(self, lst):
        if isinstance(lst, list):
            for elem in lst:
                if isinstance(elem, list):
                    if not self.validar_elementos(elem):
                        return False
                elif elem not in self.referencial:
                    return False
            return True
        else:
            return lst in self.referencial

    def agregar_conjunto(self, entrada, nombre, conjuntos):
        lista_elementos = self.convertir_entrada_a_lista(entrada)
        if nombre == "U":
            return True, lista_elementos
        if self.validar_elementos(lista_elementos):
            conjuntos[nombre] = lista_elementos
            return True, lista_elementos
        else:
            return False, "Error: Un elemento no pertenece al conjunto referencial."

class ConjuntoApp:
    def __init__(self, root):
        self.conjuntos = {}
        self.root_referencial = root
        self.root_referencial.title("Definir Conjunto Referencial")
        
        self.frame_principal = tk.Frame(self.root_referencial, bg="#335b78")
        self.frame_principal.pack(fill="both", expand=True)
        
        self.label_referencial = tk.Label(self.frame_principal, text="Definir conjunto referencial", font=("Arial", 16, "bold"), fg="white", bg="#335b78")
        self.label_referencial.pack(pady=10)
        
        self.entry_referencial = ttk.Entry(self.frame_principal, font=("Arial", 12))
        self.entry_referencial.pack(padx=10, pady=5)
        
        self.button_referencial = ttk.Button(self.frame_principal, text="Definir", command=self.definir_referencial)
        self.button_referencial.pack(pady=10)

    def definir_referencial(self):
        elementos = self.entry_referencial.get()
        referencial = set(elementos.replace('(', '').replace(')', '').replace(' ', '').split(','))
        print(f"Conjunto referencial definido: {referencial}")
        self.manager = ConjuntoManager(referencial)
        self.root_referencial.destroy()  # Cierra la ventana una vez definido el conjunto referencial
        self.crear_conjuntos()  # Llama a la función para crear conjuntos

    def agregar_conjunto(self):
        nombre = self.entry_nombre.get()
        elementos = self.entry_conjunto.get()
        success, resultado = self.manager.agregar_conjunto(elementos, nombre, self.conjuntos)
        
        if success:
            print(f"Conjunto {nombre} agregado: {resultado}")
            messagebox.showinfo("Éxito", f"Conjunto '{nombre}' agregado correctamente.")
        else:
            messagebox.showerror("Error", resultado)

    def crear_conjuntos(self):
        self.root_conjuntos = tk.Tk()
        self.root_conjuntos.title("Crear Conjuntos")
        
        self.frame_principal = tk.Frame(self.root_conjuntos, bg="#335b78")
        self.frame_principal.pack(fill="both", expand=True)
        
        self.label_crear = tk.Label(self.frame_principal, text="Crear conjuntos", font=("Arial", 16, "bold"), fg="white", bg="#335b78")
        self.label_crear.pack(pady=10)
        
        self.label_nombre = ttk.Label(self.frame_principal, text="Nombre del conjunto", font=("Arial", 12), background="#335b78", foreground="white")
        self.label_nombre.pack(pady=5)
        
        self.entry_nombre = ttk.Entry(self.frame_principal, font=("Arial", 12))
        self.entry_nombre.pack(padx=10, pady=5)
        
        self.label_conjunto = ttk.Label(self.frame_principal, text="Elementos del conjunto", font=("Arial", 12), background="#335b78", foreground="white")
        self.label_conjunto.pack(pady=5)
        
        self.entry_conjunto = ttk.Entry(self.frame_principal, font=("Arial", 12))
        self.entry_conjunto.pack(padx=10, pady=5)
        
        self.button_new = ttk.Button(self.frame_principal, text="Agregar", command=self.agregar_conjunto)
        self.button_new.pack(pady=20)
        
        self.root_conjuntos.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ConjuntoApp(root)
    root.mainloop()

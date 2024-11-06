import tkinter as tk
from tkinter import ttk
from evaluador import CombinatoriaAvanzada  # Importar la clase CombinatoriaAvanzada

class UI:
    def __init__(self, root):
        root.title("Proyecto 4 MD")
        root.configure(bg="#0E2A47")

        # Crear frame principal
        main_frame = tk.Frame(root, bg="#6C95B3", padx=20, pady=20)
        main_frame.grid(row=0, column=0, padx=20, pady=20)

        # Etiqueta de título
        lbl_titulo = tk.Label(main_frame, text="Calculadora de permutaciones y combinaciones", bg="#6C95B3", fg="black", font=("Arial", 14, "bold"))
        lbl_titulo.grid(row=0, column=0, columnspan=2, sticky="w")

        # Etiqueta de instrucciones
        lbl_instrucciones = tk.Label(main_frame, text="Ingrese los objetos separados por coma", bg="#6C95B3", fg="black", font=("Arial", 12))
        lbl_instrucciones.grid(row=1, column=0, columnspan=2, sticky="w")

        # Campo de entrada para objetos
        self.entry_objetos = tk.Entry(main_frame, width=40)
        self.entry_objetos.grid(row=2, column=0, columnspan=2, pady=10)

        # Checkbox para opciones
        self.orden_var = tk.BooleanVar()
        self.repetir_var = tk.BooleanVar()

        chk_orden = tk.Checkbutton(main_frame, text="¿Importa el orden?", variable=self.orden_var, bg="#6C95B3")
        chk_orden.grid(row=3, column=0, sticky="w")

        chk_repetir = tk.Checkbutton(main_frame, text="¿Vale repetir?", variable=self.repetir_var, bg="#6C95B3")
        chk_repetir.grid(row=3, column=1, sticky="w")

        # Frame interno para las entradas (n) y (r)
        nr_frame = tk.Frame(main_frame, bg="#6C95B3")
        nr_frame.grid(row=4, column=0, columnspan=2, pady=10)

        # Etiqueta y campo de entrada para (n)
        lbl_n = tk.Label(nr_frame, text="(n):", bg="#6C95B3")
        lbl_n.pack(side="left")

        self.entry_n = tk.Entry(nr_frame, width=10)
        self.entry_n.pack(side="left", padx=5)

        # Etiqueta y campo de entrada para (r)
        lbl_r = tk.Label(nr_frame, text="(r):", bg="#6C95B3")
        lbl_r.pack(side="left", padx=(20, 5))  # Espacio entre (n) y (r)

        self.entry_r = tk.Entry(nr_frame, width=10)
        self.entry_r.pack(side="left")

        # Botón para ingresar
        btn_ingresar = tk.Button(main_frame, text="Ingresar", bg="#0E2A47", fg="white", command=self.calcular)
        btn_ingresar.grid(row=5, column=0, columnspan=2, pady=10)

        # Frame para el resultado
        resultado_frame = tk.Frame(root, bg="#6C95B3", padx=20)
        resultado_frame.grid(row=1, column=0, padx=20, pady=20)

        lbl_resultado = tk.Label(resultado_frame, text="Resultado:", bg="#6C95B3", font=("Arial", 12, "bold"))
        lbl_resultado.grid(row=0, column=0, sticky="w")

        # Crear widget Text para el resultado con Scrollbar
        self.text_resultado = tk.Text(resultado_frame, width=60, height=10, wrap="word", bg="#E1EAF2", fg="black")
        self.text_resultado.grid(row=1, column=0, pady=5)

        # Agregar Scrollbar al widget Text
        scrollbar = tk.Scrollbar(resultado_frame, command=self.text_resultado.yview)
        scrollbar.grid(row=1, column=1, sticky="ns")
        self.text_resultado['yscrollcommand'] = scrollbar.set

    def calcular(self):
        # Obtener los valores de entrada
        objetos = self.entry_objetos.get().split(",")
        orden = self.orden_var.get()
        repetir = self.repetir_var.get()
        
        # Obtener los valores de (n) y (r), y validar si son enteros
        try:
            n = int(self.entry_n.get())
        except ValueError:
            n = None  # Asigna None si no se proporciona (n)
        
        try:
            r = int(self.entry_r.get())
        except ValueError:
            r = None  # Asigna None si no se proporciona (r)
        
        # Llamar a la función evaluar y mostrar el resultado
        resultado = CombinatoriaAvanzada.evaluar(objetos, rep=repetir, orden=orden, r=r)
        
        # Limpiar el contenido anterior en el Text widget
        self.text_resultado.delete(1.0, tk.END)

        # Insertar el nuevo resultado
        self.text_resultado.insert(tk.END, str(resultado))

if __name__ == "__main__":
    root = tk.Tk()
    app = UI(root)
    root.mainloop()

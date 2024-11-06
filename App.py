import tkinter as tk
from tkinter import ttk
from CombinatoriaAvanzada import CombinatoriaAvanzada 
from Combinatoria import Combinatoria

class UI:
    def __init__(self, root):
        root.title("Proyecto 4 MD")
        root.configure(bg="#0E2A47")
        self.isN = False

        # Crear frame principal
        main_frame = tk.Frame(root, bg="#6C95B3", padx=20, pady=20)
        main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Configurar la expansión de filas y columnas en root y main_frame
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        # Etiqueta de título
        lbl_titulo = tk.Label(main_frame, text="Calculadora de permutaciones y combinaciones", bg="#6C95B3", fg="black", font=("Arial", 14, "bold"))
        lbl_titulo.grid(row=0, column=0, columnspan=2, sticky="w")

        # Etiqueta de instrucciones
        lbl_instrucciones = tk.Label(main_frame, text="Ingrese los objetos separados por coma", bg="#6C95B3", fg="black", font=("Arial", 12))
        lbl_instrucciones.grid(row=1, column=0, columnspan=2, sticky="w")

        # Campo de entrada para objetos
        self.entry_objetos = tk.Entry(main_frame)
        self.entry_objetos.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

        # Checkbox para opciones
        self.orden_var = tk.BooleanVar()
        self.repetir_var = tk.BooleanVar()

        chk_orden = tk.Checkbutton(main_frame, text="¿Importa el orden?", variable=self.orden_var, bg="#6C95B3")
        chk_orden.grid(row=3, column=0, sticky="w")

        chk_repetir = tk.Checkbutton(main_frame, text="¿Vale repetir?", variable=self.repetir_var, bg="#6C95B3")
        chk_repetir.grid(row=3, column=1, sticky="w")

        # Opción para alternar entre lista y valor de N
        self.use_n_var = tk.BooleanVar(value=False)  
        toggle_button = tk.Checkbutton(main_frame, text="Usar valor de N en lugar de la lista", variable=self.use_n_var, bg="#6C95B3", command=self.toggle_input_mode)
        toggle_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

        # Frame interno para las entradas (n) y (r)
        nr_frame = tk.Frame(main_frame, bg="#6C95B3")
        nr_frame.grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")
        nr_frame.columnconfigure(1, weight=1)
        nr_frame.columnconfigure(3, weight=1)

        # Etiqueta y campo de entrada para (n)
        lbl_n = tk.Label(nr_frame, text="(n):", bg="#6C95B3")
        lbl_n.grid(row=0, column=0, sticky="e")

        self.entry_n = tk.Entry(nr_frame, width=10, state="disabled")
        self.entry_n.grid(row=0, column=1, padx=5, sticky="w")

        # Etiqueta y campo de entrada para (r)
        lbl_r = tk.Label(nr_frame, text="(r):", bg="#6C95B3")
        lbl_r.grid(row=0, column=2, padx=(20, 5), sticky="e")

        self.entry_r = tk.Entry(nr_frame, width=10)
        self.entry_r.grid(row=0, column=3, sticky="w")

        # Botón para ingresar
        btn_ingresar = tk.Button(main_frame, text="Ingresar", bg="#0E2A47", fg="white", command=self.calcular)
        btn_ingresar.grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")

        # Frame para el resultado
        resultado_frame = tk.Frame(root, bg="#6C95B3", padx=20)
        resultado_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        resultado_frame.columnconfigure(0, weight=1)

        lbl_resultado = tk.Label(resultado_frame, text="Resultado:", bg="#6C95B3", font=("Arial", 12, "bold"))
        lbl_resultado.grid(row=0, column=0, sticky="w")

        # Crear widget Text para el resultado con Scrollbar
        self.text_resultado = tk.Text(resultado_frame, wrap="word", bg="#E1EAF2", fg="black")
        self.text_resultado.grid(row=1, column=0, pady=5, sticky="nsew")

        # Agregar Scrollbar al widget Text
        scrollbar = tk.Scrollbar(resultado_frame, command=self.text_resultado.yview)
        scrollbar.grid(row=1, column=1, sticky="ns")
        self.text_resultado['yscrollcommand'] = scrollbar.set

    def toggle_input_mode(self):
        if self.use_n_var.get():
            self.entry_objetos.config(state="disabled")
            self.entry_n.config(state="normal")
            self.isN = True
        else:
            self.isN = False
            self.entry_objetos.config(state="normal")
            self.entry_n.config(state="disabled")

    def calcular(self):
        orden = self.orden_var.get()
        repetir = self.repetir_var.get()

        if self.isN:  # Usar valor de (n) y no la lista
            try:
                n = int(self.entry_n.get())
            except ValueError:
                n = None
            try:
                r = int(self.entry_r.get())
            except ValueError:
                r = None

            if n is not None and r is not None:
                cantidad = Combinatoria.calcular_cantidad(n, rep=repetir, orden=orden, r=r)
                resultado = f"Cantidad calculada con valor de n: {cantidad}"
            else:
                resultado = "Por favor, ingrese valores válidos para (n) y (r)."
        else:
            objetos = self.entry_objetos.get().split(",")
            try:
                r = int(self.entry_r.get())
            except ValueError:
                r = None

            posible, combinaciones = CombinatoriaAvanzada.evaluar(objetos, rep=repetir, orden=orden, r=r)
            resultado = f"Número de combinaciones/permutaciones: {posible}\nPosibilidades:\n{combinaciones}"

        self.text_resultado.delete(1.0, tk.END)
        self.text_resultado.insert(tk.END, resultado)

if __name__ == "__main__":
    root = tk.Tk()
    app = UI(root)
    root.mainloop()

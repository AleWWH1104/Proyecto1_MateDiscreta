from tkinter import *
from tkinter.ttk import Entry, Button, Checkbutton, Scrollbar, Style  # Importamos solo los widgets necesarios
from CombinatoriaAvanzada import CombinatoriaAvanzada
from Combinatoria import Combinatoria  # Importamos las clases que contienen las funciones de cálculo combinatorio.

class UI:
    def __init__(self, root):
        # Configuración inicial de la ventana principal
        root.title("Proyecto 4 MD")  # Título de la ventana principal
        root.configure(bg="#0E2A47")  # Establecemos el color de fondo

        self.isN = False  # Indicador de si estamos usando una lista de objetos o un valor de N

        # Creamos el frame principal para contener los widgets
        main_frame = Frame(root, bg="#6C95B3", padx=20, pady=20)
        main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Configuramos el ajuste de tamaño relativo del frame y la ventana para cuando se redimensione
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        # Etiqueta para el título de la aplicación
        lbl_titulo = Label(main_frame, text="Calculadora de permutaciones y combinaciones", bg="#6C95B3", fg="black", font=("Arial", 14, "bold"))
        lbl_titulo.grid(row=0, column=0, columnspan=2, sticky="w")

        # Etiqueta de instrucciones para el usuario
        lbl_instrucciones = Label(main_frame, text="Ingrese los objetos separados por coma", bg="#6C95B3", fg="black", font=("Arial", 12))
        lbl_instrucciones.grid(row=1, column=0, columnspan=2, sticky="w")

        # Campo de entrada para la lista de objetos
        self.entry_objetos = Entry(main_frame)
        self.entry_objetos.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

        # Variables para opciones de entrada
        self.orden_var = BooleanVar()  # Opción para considerar el orden
        self.repetir_var = BooleanVar()  # Opción para permitir repeticiones

        # Configuración de estilo para los widgets de ttk
        style = Style()
        style.configure("TCheckbutton", background="#6C95B3", foreground="black")
        style.configure("TButton", background="#6C95B3", foreground="black")

        # Checkbox para la opción "¿Importa el orden?"
        chk_orden = Checkbutton(main_frame, text="¿Importa el orden?", variable=self.orden_var, style="TCheckbutton")
        chk_orden.grid(row=3, column=0, sticky="w")

        # Checkbox para la opción "¿Vale repetir?"
        chk_repetir = Checkbutton(main_frame, text="¿Vale repetir?", variable=self.repetir_var, style="TCheckbutton")
        chk_repetir.grid(row=3, column=1, sticky="w")

        # Opción para alternar entre lista de objetos y valor de N
        self.use_n_var = BooleanVar(value=False)
        toggle_button = Checkbutton(main_frame, text="Usar valor de N en lugar de la lista", variable=self.use_n_var, command=self.toggle_input_mode, style="TCheckbutton")
        toggle_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

        # Frame para las entradas de valores de (n) y (r)
        nr_frame = Frame(main_frame, bg="#6C95B3")
        nr_frame.grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")
        nr_frame.columnconfigure(1, weight=1)
        nr_frame.columnconfigure(3, weight=1)

        # Campo para la entrada de (n) desactivado por defecto
        lbl_n = Label(nr_frame, text="(n):", bg="#6C95B3")
        lbl_n.grid(row=0, column=0, sticky="e")
        self.entry_n = Entry(nr_frame, width=10, state="disabled")
        self.entry_n.grid(row=0, column=1, padx=5, sticky="w")

        # Campo para la entrada de (r)
        lbl_r = Label(nr_frame, text="(r):", bg="#6C95B3")
        lbl_r.grid(row=0, column=2, padx=(20, 5), sticky="e")
        self.entry_r = Entry(nr_frame, width=10)
        self.entry_r.grid(row=0, column=3, sticky="w")

        # Botón para ejecutar el cálculo
        btn_ingresar = Button(main_frame, text="Ingresar", command=self.calcular, style="TButton")
        btn_ingresar.grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")

        # Frame para mostrar el resultado
        resultado_frame = Frame(root, bg="#6C95B3", padx=20)
        resultado_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        resultado_frame.columnconfigure(0, weight=1)

        # Etiqueta para el resultado
        lbl_resultado = Label(resultado_frame, text="Resultado:", bg="#6C95B3", font=("Arial", 12, "bold"))
        lbl_resultado.grid(row=0, column=0, sticky="w")

        # Widget de texto para mostrar el resultado con scroll vertical
        self.text_resultado = Text(resultado_frame, wrap="word", bg="#E1EAF2", fg="black")
        self.text_resultado.grid(row=1, column=0, pady=5, sticky="nsew")

        # Scrollbar para el widget de texto
        scrollbar = Scrollbar(resultado_frame, command=self.text_resultado.yview)
        scrollbar.grid(row=1, column=1, sticky="ns")
        self.text_resultado['yscrollcommand'] = scrollbar.set

    def toggle_input_mode(self):
        """
        Alterna entre usar una lista de objetos o un valor de N, activando o desactivando los campos correspondientes.
        """
        if self.use_n_var.get():
            self.entry_objetos.config(state="disabled")  # Desactiva la entrada de lista de objetos
            self.entry_n.config(state="normal")  # Activa la entrada de N
            self.isN = True
        else:
            self.isN = False
            self.entry_objetos.config(state="normal")  # Activa la entrada de lista de objetos
            self.entry_n.config(state="disabled")  # Desactiva la entrada de N

    def calcular(self):
        """
        Realiza el cálculo de combinaciones o permutaciones según las entradas y las opciones seleccionadas.
        """
        orden = self.orden_var.get()  # Determina si el orden es importante
        repetir = self.repetir_var.get()  # Determina si se permiten repeticiones

        if self.isN:  # Si se usa un valor de N en lugar de una lista de objetos
            try:
                n = int(self.entry_n.get())  # Obtiene el valor de N
            except ValueError:
                n = None
            try:
                r = int(self.entry_r.get())  # Obtiene el valor de R
            except ValueError:
                r = None

            if n is not None and r is not None:
                cantidad = Combinatoria.calcular_cantidad(n, rep=repetir, orden=orden, r=r)
                resultado = f"Cantidad calculada con valor de n: {cantidad}"
            else:
                resultado = "Por favor, ingrese valores válidos para (n) y (r)."
        else:
            objetos = self.entry_objetos.get().split(",")  # Obtiene la lista de objetos
            try:
                r = int(self.entry_r.get())  # Obtiene el valor de R
            except ValueError:
                r = None

            posible, combinaciones = CombinatoriaAvanzada.evaluar(objetos, rep=repetir, orden=orden, r=r)
            resultado = f"Número de combinaciones/permutaciones: {posible}\nPosibilidades:\n{combinaciones}"

        # Muestra el resultado en el widget de texto
        self.text_resultado.delete(1.0, END)
        self.text_resultado.insert(END, resultado)

if __name__ == "__main__":
    # Inicia la aplicación
    root = Tk()
    app = UI(root)
    root.mainloop()

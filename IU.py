import tkinter as tk  # Importa la librería tkinter para crear interfaces gráficas
from tkinter import ttk  # Importa la librería ttk para estilos adicionales de widgets
from Evaluador import ModularEvaluator  # Importa la clase ModularEvaluator del archivo Evaluador.py

class CalculadoraGrafica:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Gráfica")  # Título de la ventana
        master.geometry("350x500")  # Tamaño de la ventana
        master.config(bg="#ACB6BE")  # Color de fondo de la ventana

        self.evaluador = ModularEvaluator()  # Inicializa el evaluador modular

        # Pantalla de la calculadora
        self.pantalla = ttk.Entry(master, width=30, justify="right", font=("Arial", 18))
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=15, pady=(20, 10), ipady=15)

        # Lista de botones (texto, estilo). "CBtn" para botones especiales y "OpBtn" para operadores
        botones = [
            ('C', "CBtn"), ('(', "OpBtn"), (')', "OpBtn"), ('^', "OpBtn"),
            ('7', "NumBtn"), ('8', "NumBtn"), ('9', "NumBtn"), ('/', "OpBtn"),
            ('4', "NumBtn"), ('5', "NumBtn"), ('6', "NumBtn"), ('*', "OpBtn"),
            ('1', "NumBtn"), ('2', "NumBtn"), ('3', "NumBtn"), ('-', "OpBtn"),
            ('0', "NumBtn"), ('=', "CBtn"), ('mod', "OpBtn"), ('+', "OpBtn")
        ]

        # Crear los botones en una cuadrícula
        row = 1
        col = 0
        for (boton, estilo) in botones:
            comando = lambda x=boton: self.click(x)  # Asigna la función click al botón
            btn = tk.Button(master, text=boton, command=comando, bg="#768592", fg="white", font=("Arial", 14))
            
            # Personalizar color según el tipo de botón
            if estilo == "CBtn":
                btn.config(bg="#335B78")  # Color para botones especiales
            elif estilo == "OpBtn":
                btn.config(bg="#62696F")  # Color para operadores

            # Posicionar el botón en la cuadrícula
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            master.grid_rowconfigure(row, weight=1)
            master.grid_columnconfigure(col, weight=1)

            col += 1
            if col > 3:  # Mover a la siguiente fila después de 4 columnas
                col = 0
                row += 1

    # Función que se ejecuta al hacer clic en un botón
    def click(self, key):
        if key.strip() == '=':
            try:
                expression = self.pantalla.get()  # Obtener la expresión de la pantalla
                resultado = self.evaluador.evaluate(expression)  # Evaluar la expresión usando el evaluador
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, str(resultado))  # Mostrar el resultado en la pantalla
            except Exception as e:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, "Error")
                print("Error en la evaluación:", e)  # Mensaje de error en consola
        elif key.strip() == 'C':
            self.pantalla.delete(0, tk.END)  # Limpiar la pantalla si se presiona 'C'
        else:
            self.pantalla.insert(tk.END, key)  # Agregar el valor del botón presionado a la pantalla

# Crear la ventana principal
root = tk.Tk()
calculadora = CalculadoraGrafica(root)

# Configurar el tamaño de cada fila y columna de la cuadrícula para que los botones sean uniformes
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()  # Iniciar el loop principal de la interfaz
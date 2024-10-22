import tkinter as tk
from tkinter import ttk

class CalculadoraGrafica:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Gráfica")
        master.geometry("350x500")
        master.config(bg="#ACB6BE")

        # Pantalla de la calculadora
        self.pantalla = ttk.Entry(master, width=30, justify="right", font=("Arial", 18))
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=15, pady=(20, 10), ipady=15)

        # Estilo de los botones
        style = ttk.Style()
        style.theme_use('clam') 
        
        # Definir colores para cada tipo de botón
        style.configure("CBtn", background="#335B78", foreground="white", font=("Arial", 14), padding=10)
        style.configure("NumBtn", background="#768592", foreground="white", font=("Arial", 14), padding=10)
        style.configure("OpBtn", background="#62696F", foreground="white", font=("Arial", 14), padding=10)
        
        # Lista de botones y sus estilos correspondientes
        botones = [
            ('C', "CBtn"), ('(', "OpBtn"), (')', "OpBtn"), ('^', "OpBtn"),
            ('7', "NumBtn"), ('8', "NumBtn"), ('9', "NumBtn"), ('/', "OpBtn"),
            ('4', "NumBtn"), ('5', "NumBtn"), ('6', "NumBtn"), ('*', "OpBtn"),
            ('1', "NumBtn"), ('2', "NumBtn"), ('3', "NumBtn"), ('-', "OpBtn"),
            ('0', "NumBtn"), ('=', "CBtn"), ('mod', "OpBtn"), ('+', "OpBtn")
        ]

        # Crear los botones
        row = 1
        col = 0
        for (boton, estilo) in botones:
            comando = lambda x=boton: self.click(x)
            btn = ttk.Button(master, text=boton, command=comando, style=estilo)
            
            # Posicionar el botón en la cuadrícula
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            master.grid_rowconfigure(row, weight=1)
            master.grid_columnconfigure(col, weight=1)

            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, key):
        if key == '=':
            try:
                resultado = eval(self.pantalla.get())
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, str(resultado))
            except:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, "Error")
        elif key == 'C':
            self.pantalla.delete(0, tk.END)
        else:
            self.pantalla.insert(tk.END, key)

# Crear la ventana principal
root = tk.Tk()
calculadora = CalculadoraGrafica(root)

# Configurar el tamaño de cada fila y columna de la cuadrícula para que los botones sean uniformes
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
from Utilerias import *
from Lisp3 import *

conjuntos = {"U": []}

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Programa de conjuntos")
        
        self.current_letter_index = -1  # Iniciamos en -1 para que el primer botón sea 'U'
        self.letters = ['U'] + [chr(i) for i in range(65, 91)]  # ['U', 'A', 'B', ..., 'Z']

        self.create_widgets()

    def create_widgets(self):
        # Crear un Notebook
        notebook = ttk.Notebook(self)
        notebook.pack(expand=1, fill="both")

        # Tab1
        tab1 = tk.Frame(notebook, bg="#6c95b3")
        notebook.add(tab1, text="Crear conjuntos")

        # Tab2
        tab2 = tk.Frame(notebook, bg="#6c95b3")
        notebook.add(tab2, text="Operaciones y Resultados")

        # Frames para tab1
        # Side de conjuntos creados
        self.frame_con = tk.Frame(tab1, bg="#335b78", bd=1, padx=10, pady=10)
        self.frame_con.grid(row=0, column=0, padx=10, pady=10, rowspan=3)
        label_con = tk.Label(self.frame_con, text="Conjuntos", font=("Arial", 16, "bold"), bg="#335b78", fg="white")
        label_con.grid(row=0, column=0, pady=(0, 10))
        self.conjunto_buttons = []

        # Frame para crear nuevos conjuntos
        frame_crear_conjuntos = tk.Frame(tab1, bg="#335b78")
        frame_crear_conjuntos.grid(row=0, column=1, pady=(10, 10), padx=10, sticky="nsew")
        label_crear = tk.Label(frame_crear_conjuntos, text="Pon elementos para crear conjuntos", font=("Arial", 16, "bold"), fg="white", bg="#335b78")
        label_crear.grid(row=0, column=1, columnspan=2, pady=(0, 10))
        self.entry_conjunto = ttk.Entry(frame_crear_conjuntos, font=("Arial", 12))
        self.entry_conjunto.grid(row=1, column=1, padx=(10, 10), pady=20, sticky="we")
        button_new1 = ttk.Button(frame_crear_conjuntos, text="New", command=self.create_con_manual)
        button_new1.grid(row=1, column=2, padx=(0, 10), pady=20, sticky="e")

        # Frame para crear nuevos conjuntos con operaciones
        frame_op_conjuntos = tk.Frame(tab1, bg="#335b78")
        frame_op_conjuntos.grid(row=2, column=1, pady=(0, 10),padx=10, sticky="nsew")
        label_op = tk.Label(frame_op_conjuntos, text="Crear conjuntos con operaciones", font=("Arial", 16, "bold"), fg="white", bg="#335b78")
        label_op.grid(row=0, column=1, columnspan=2, pady=(0, 10))
        label_instruc = tk.Label(frame_op_conjuntos, text="Asocia con parentesis y deja espacios entre\nlas operaciones: Ej(A uni B) int C", font=("Arial", 12, "bold"), fg="white", bg="#335b78")
        label_instruc.grid(row=1, column=1, columnspan=2, pady=(10, 10))
        self.entry_conjunto_op = ttk.Entry(frame_op_conjuntos, font=("Arial", 12))
        self.entry_conjunto_op.grid(row=2, column=1, padx=(10, 10), pady=20, sticky="we")
        self.button_new2 = ttk.Button(frame_op_conjuntos, text="New", command=self.create_con_op, state="disabled")
        self.button_new2.grid(row=2, column=2, padx=(0, 10), pady=20, sticky="e")

        # Frame para botones operandos tab1
        frame_botones = tk.Frame(tab1, relief="solid", padx=10, pady=10, bg="#335b78")
        frame_botones.grid(row=3, column=1, pady=(0, 10),padx=10, sticky="nsew")
        buttons_text = ["(", ")", "uni", "int", "dif", "com"]
        for i, text in enumerate(buttons_text):
            button = ttk.Button(frame_botones, text=text, command=lambda t=text: self.append_to_entry1(t))
            button.grid(row=0, column=i)
        
        #Frames para Tab2
        # Side de conjuntos creados
        self.frame_con2 = tk.Frame(tab2, bg="#335b78", bd=1, padx=10, pady=10)
        self.frame_con2.grid(row=0, column=0, padx=10, pady=10, rowspan=3)
        label_con2 = tk.Label(self.frame_con2, text="Conjuntos", font=("Arial", 16, "bold"), bg="#335b78", fg="white")
        label_con2.grid(row=0, column=0, pady=(0, 10))
        self.conjunto_buttons2 = []

        # Frame para colocar operaciones
        frame_cal_con = tk.Frame(tab2, bg="#335b78")
        frame_cal_con.grid(row=0, column=1, pady=(10, 10), padx=10, sticky="nsew")
        label_op = tk.Label(frame_cal_con, text="Operar conjuntos", font=("Arial", 16, "bold"), fg="white", bg="#335b78")
        label_op.grid(row=0, column=1, columnspan=2, pady=(0, 10))
        label_instruc = tk.Label(frame_cal_con, text="Asocia con parentesis y deja espacios entre\nlas operaciones: Ej(A uni B) int C", font=("Arial", 12, "bold"), fg="white", bg="#335b78")
        label_instruc.grid(row=1, column=1, columnspan=2, pady=(10, 10))
        self.entry_cal_con = ttk.Entry(frame_cal_con, font=("Arial", 12))
        self.entry_cal_con.grid(row=2, column=1, padx=(10, 10), pady=20, sticky="we")
        self.button_new3 = ttk.Button(frame_cal_con, text="Operar", state='disabled', command=self.calc_con)
        self.button_new3.grid(row=2, column=2, padx=(0, 10), pady=20, sticky="e")

        # Frame para botones operandos tab2
        frame_botones2 = tk.Frame(tab2, relief="solid", padx=10, pady=10, bg="#335b78")
        frame_botones2.grid(row=3, column=1, pady=(0, 10),padx=10, sticky="nsew")

        #Frame de botones de calculadora
        buttons_text1 = ["(", ")", "uni", "int", "dif", "com", "fun", "pro"]
        for i, text in enumerate(buttons_text1):
            row = i // 4
            column = i % 4
            button_cal = ttk.Button(frame_botones2, text=text, command=lambda t=text: self.append_to_entry2(t))
            button_cal.grid(row=row, column=column, padx=5, pady=5)
        
        #Frame resultado
        frame_result = tk.Frame(tab2, relief="solid", padx=10, pady=10, bg="#335b78")
        frame_result.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        label_TitR = tk.Label(frame_result, text="Resultado", font=("Arial", 16, "bold"), fg="white", bg="#335b78")
        label_TitR.grid(row=0,column=2, pady=(0, 10))
        self.text_resultado = tk.Text(frame_result, font=("Arial", 12), fg="white", wrap="word", height=8, width=30, bg="#2c2c2c")
        self.text_resultado.grid(row=1, column=2, pady=(0, 10), rowspan=2)
        self.text_resultado.insert(tk.END, "lista de conjuntos")

        # Configuración de la grid
        frame_crear_conjuntos.grid_columnconfigure(1, weight=1)
        frame_op_conjuntos.grid_columnconfigure(1, weight=1)
        frame_cal_con.grid_columnconfigure(1, weight=1)
        frame_result.grid_columnconfigure(1, weight=1)

    def create_con_manual(self):
        entrada = self.entry_conjunto.get()
        letter = self.know_letter()
        if letter == None:
            return
        elif letter == "U":
            self.manager = ConjuntoManager(conjuntos["U"])    
            entrada = entrada.replace('(', '').replace(')', '').replace(' ', '')

        conjunto = self.manager.convertir_entrada_a_lista(entrada)
        print(conjunto)
        success, _ = self.manager.agregar_conjunto(conjunto, letter, conjuntos)
        
        if success:
            self.create_con_btn(letter)
            self.entry_conjunto.delete(0, tk.END)
            self.button_new2['state'] = 'normal'
            self.button_new3['state'] = 'normal'
            self.manager.referencial = conjuntos["U"]
            self.calculadora_conjuntos = Conjuntos_Evaluator(conjuntos["U"])
        else:
            self.current_letter_index -= 1
            messagebox.showerror("Error", _)
        print(conjuntos)


    def create_con_op(self):
        entrada = self.entry_conjunto_op.get()
        letter = self.know_letter()
        if letter == None:
            return
        conjunto = self.calculadora_conjuntos.evaluate(entrada, conjuntos)
        success, _ = self.manager.agregar_conjunto(conjunto, letter, conjuntos)
        if success:
            self.create_con_btn(letter)
            self.entry_conjunto_op.delete(0, tk.END)
        else:
            self.current_letter_index -= 1
            messagebox.showerror("Error", _)
        print(conjuntos)

    def calc_con(self):
        entrada = f"{self.entry_cal_con.get()}"
        letter = self.know_letter()
        if letter == None:
            return
        print(entrada)
        conjunto = ", ".join(self.calculadora_conjuntos.evaluate(entrada, conjuntos))
        print(conjunto)
        self.text_resultado.delete(1.0, tk.END)
        self.text_resultado.insert(tk.END, conjunto)
        self.entry_cal_con.delete(0, tk.END)
        
    def create_con_btn(self, letter):
        # Crear un nuevo botón
        new_con_btn = ttk.Button(self.frame_con, text=letter, command=lambda: self.append_to_entry1(letter))
        new_con_btn.grid(row=self.current_letter_index + 2, column=0, pady=5, sticky="we")
        # Guardar el botón en la lista
        self.conjunto_buttons.append(new_con_btn)

        # Crear un nuevo botón en Tab2
        new_con_btn_tab2 = ttk.Button(self.frame_con2, text=letter, command= lambda: self.append_to_entry2(letter) )
        new_con_btn_tab2.grid(row=self.current_letter_index + 2, column=0, pady=5, sticky="we")
        # Guardar el botón en la lista de Tab2
        self.conjunto_buttons2.append(new_con_btn_tab2)

        self.entry_cal_con.delete(0, tk.END)  

    def know_letter(self):
        # Incrementar el índice de la letra actual
        self.current_letter_index += 1
        # Si nos quedamos sin letras, no hacer nada
        if self.current_letter_index >= len(self.letters):
            return None
        # Obtener la letra correspondiente
        return self.letters[self.current_letter_index]

    def append_to_entry1(self, text):
        current_text = self.entry_conjunto_op.get()
        self.entry_conjunto_op.delete(0, tk.END)
        self.entry_conjunto_op.insert(0, current_text + text)
    
    def append_to_entry2(self, text):
        current_text = self.entry_cal_con.get()
        self.entry_cal_con.delete(0, tk.END)
        self.entry_cal_con.insert(0, current_text + text)

    
if __name__ == "__main__":
    app = App()
    app.mainloop()

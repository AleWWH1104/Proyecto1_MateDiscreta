import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Programa de conjuntos")
        self.configure(bg="#6c95b3")

        self.current_letter_index = -1  # Iniciamos en -1 para que el primer botón sea 'U'
        self.letters = ['U'] + [chr(i) for i in range(65, 91)]  # ['U', 'A', 'B', ..., 'Z']

        self.create_widgets()

    def create_widgets(self):
        # Crear un Notebook
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both")

        # Frame principal
        frame_principal = tk.Frame(notebook, bg="#6c95b3", relief="solid", bd=1, padx=10, pady=10)
        notebook.add(frame_principal, text="Crear conjuntos")

        # Frame para los conjuntos
        frame_conjuntos = tk.Frame(frame_principal, bg="#335b78", bd=1, padx=10, pady=10)
        frame_conjuntos.grid(row=0, column=0, padx=10, pady=10, rowspan=3)

        label_conjuntos = tk.Label(frame_conjuntos, text="Conjuntos", font=("Arial", 16, "bold"), bg="#335b78", fg="white")
        label_conjuntos.grid(row=0, column=0, pady=(0, 10))

        self.conjunto_buttons = []
        self.frame_conjuntos = frame_conjuntos
        
        # Frame para crear nuevos conjuntos
        frame_crear_conjuntos = tk.Frame(frame_principal, bg="#335b78")
        frame_crear_conjuntos.grid(row=0, column=1, pady=(0, 10), sticky="nsew")

        label_crear = tk.Label(frame_crear_conjuntos, text="Crear conjuntos", font=("Arial", 16, "bold"), fg="white", bg="#335b78")
        label_crear.grid(row=0, column=1, columnspan=2, pady=(0, 10))

        self.entry_conjunto = ttk.Entry(frame_crear_conjuntos, font=("Arial", 12))
        self.entry_conjunto.grid(row=1, column=1, padx=(10, 10), pady=20, sticky="we")

        button_new1 = ttk.Button(frame_crear_conjuntos, text="New", command=self.add_conjunto)
        button_new1.grid(row=1, column=2, padx=(0, 10), pady=20, sticky="e")

        # Frame para crear conjuntos operados
        frame_op_conjuntos = tk.Frame(frame_principal, bg="#335b78")
        frame_op_conjuntos.grid(row=2, column=1, pady=(0, 10), sticky="nsew")

        label_op = tk.Label(frame_op_conjuntos, text="Crear conjuntos con operaciones", font=("Arial", 16, "bold"), fg="white", bg="#335b78")
        label_op.grid(row=0, column=1, columnspan=2, pady=(0, 10))

        self.entry_conjunto_op = ttk.Entry(frame_op_conjuntos, font=("Arial", 12))
        self.entry_conjunto_op.grid(row=1, column=1, padx=(10, 10), pady=20, sticky="we")

        button_new2 = ttk.Button(frame_op_conjuntos, text="New", command=self.add_conjunto)
        button_new2.grid(row=1, column=2, padx=(0, 10), pady=20, sticky="e")

        # Frame para botones operandos
        frame_botones = tk.Frame(frame_principal, relief="solid", padx=10, pady=10, bg="#335b78")
        frame_botones.grid(row=3, column=1, pady=(10, 0), sticky="nsew")

        buttons_text = ["(", ")", "uni", "int", "dif", "com"]
        for i, text in enumerate(buttons_text):
            button = ttk.Button(frame_botones, text=text, command=lambda t=text: self.append_to_entry(t))
            button.grid(row=0, column=i)

        # Configuración de la grid
        frame_crear_conjuntos.grid_columnconfigure(1, weight=1)
        frame_op_conjuntos.grid_columnconfigure(1, weight=1)

    def create_button(self, parent, text):
        button = ttk.Button(parent, text=text, width=10, command=lambda: self.append_to_entry(text))
        button.grid(pady=5)
        self.conjunto_buttons.append(button)

    def add_conjunto(self):
        if self.current_letter_index < len(self.letters) - 1:
            self.current_letter_index += 1
            new_conjunto = self.letters[self.current_letter_index]
            self.create_button(self.frame_conjuntos, new_conjunto)
            self.entry_conjunto.delete(0, tk.END)

    def append_to_entry(self, text):
        current_text = self.entry_conjunto_op.get()
        self.entry_conjunto_op.delete(0, tk.END)
        self.entry_conjunto_op.insert(0, current_text + text)

if __name__ == "__main__":
    app = App()
    app.mainloop()

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

    def agregar_conjunto(self, lista_elementos, nombre, conjuntos):
            print("lista", lista_elementos)
            if self.validar_elementos(lista_elementos) or nombre == "U":
                conjuntos[nombre] = lista_elementos
                return True, lista_elementos
            else:
                return False, "Error: Un elemento no pertenece al conjunto referencial."
            
    def lista_a_string(self, lista, es_exterior=True):
        # Si estamos en el nivel exterior usamos llaves {}, si no, usamos paréntesis ()
        if type(lista) == bool:
            return "True" if lista else "False"
        if es_exterior:
            delimitador_izquierdo = '{'
            delimitador_derecho = '}'
        else:
            delimitador_izquierdo = '('
            delimitador_derecho = ')'
        
        elementos = []
        for elemento in lista:
            if isinstance(elemento, list):  # Si el elemento es una lista, llamada recursiva
                elementos.append(self.lista_a_string(elemento, es_exterior=False))  # Interior usa ()
            else:
                elementos.append(str(elemento))  # Elementos normales se convierten a string

        return f"{delimitador_izquierdo}{','.join(elementos)}{delimitador_derecho}"
            

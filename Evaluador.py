from ModularArithmetic import ModularArithmetic  # Importa la clase para realizar operaciones modulares
import Utilerias  # Importa utilidades adicionales (como verificar si un número es primo)

class ModularEvaluator:
    def __init__(self):
        self.mod_arithmetic = ModularArithmetic()  # Instancia de aritmética modular

    # Función para evaluar expresiones
    def evaluate(self, expresion):

        # Función interna para aplicar operaciones
        def aplicar_operacion(op, a, b=None):
            if op == "+":
                return self.mod_arithmetic.mod_add(a, b)  # Suma modular
            elif op == "-":
                return self.mod_arithmetic.mod_subtract(a, b)  # Resta modular
            elif op == "*":
                return self.mod_arithmetic.mod_multiply(a, b)  # Multiplicación modular
            elif op == "/":
                return self.mod_arithmetic.mod_divide(a, b)  # División modular
            elif op == "^":
                return self.mod_arithmetic.mod_power(a, b)  # Potencia modular
        
        # Define la prioridad de los operadores
        def prioridad(op):
            if op in ["+", "-"]:
                return 1
            if op in ["*", "/"]:
                return 2
            if op == "^":
                return 3
            return -1
        
        # Realiza la operación utilizando el operador y los operandos
        def operar(operador, a, b=None):
            return aplicar_operacion(operador, a, b)

        # Tokeniza la expresión para separarla en números y operadores
        tokens = expresion.replace("(", " ( ").replace(")", " ) ").replace("^", " ^ ").replace("*", " * ").replace("/", " / ").replace("+", " + ").replace("-", " - ").replace("mod", " mod ").split()
        print("ln35", tokens)  # Debug para verificar los tokens

        # Buscar y aplicar el operador 'mod'
        if "mod" in tokens:
            mod_index = tokens.index("mod")
            new_mod = int(tokens[mod_index + 1])
            self.mod_arithmetic.set_modulo(new_mod)  # Configurar el nuevo módulo
            tokens = tokens[:mod_index]  # Elimina la parte "mod n"
            tokens.pop()
            if not(Utilerias.es_primo(new_mod)): raise Exception("No es primo")  # Validación del número primo

        # Pilas para operadores y operandos
        stack_operadores = []
        stack_operandos = []

        # Evaluación de la expresión
        for token in tokens:
            if token.isnumeric():
                stack_operandos.append(int(token))  # Agregar números al stack de operandos
            elif token in ["+", "-", "*", "/", "^"]:
                while (stack_operadores and prioridad(stack_operadores[-1]) >= prioridad(token)):
                    operador = stack_operadores.pop()
                    b = stack_operandos.pop()
                    a = stack_operandos.pop()
                    resultado = operar(operador, a, b)
                    stack_operandos.append(resultado)
                stack_operadores.append(token)
            elif token == "(":
                stack_operadores.append(token)
            elif token == ")":
                while stack_operadores and stack_operadores[-1] != "(":
                    operador = stack_operadores.pop()
                    b = stack_operandos.pop()
                    a = stack_operandos.pop()
                    resultado = operar(operador, a, b)
                    stack_operandos.append(resultado)
                stack_operadores.pop()  # Eliminar el '('

        # Aplicar cualquier operador restante
        while stack_operadores:
            operador = stack_operadores.pop()
            b = stack_operandos.pop()
            a = stack_operandos.pop()
            resultado = operar(operador, a, b)
            stack_operandos.append(resultado)
        
        # Realiza la operación final modular
        r = self.mod_arithmetic.mod_evaluate(stack_operandos[0], new_mod)
        return r


"""# Prueba de la evaluación
evaluador = ModularEvaluator()
expresion = "(7^3 + 4 * 5) * 2 (mod 23)"
resultado = evaluador.evaluate(expresion)
print(resultado)  # Imprime el resultado de la evaluación"""

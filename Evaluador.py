from ModularArithmetic import ModularArithmetic

class ModularEvaluator:
    def __init__(self):
        self.mod_arithmetic = ModularArithmetic()

    def evaluate(self, expresion):

        def aplicar_operacion(op, a, b=None):
            if op == "+":
                return self.mod_arithmetic.mod_add(a, b)
            elif op == "-":
                return self.mod_arithmetic.mod_subtract(a, b)
            elif op == "*":
                return self.mod_arithmetic.mod_multiply(a, b)
            elif op == "/":
                return self.mod_arithmetic.mod_divide(a, b)
            elif op == "^":
                return self.mod_arithmetic.mod_power(a, b)
        
        def prioridad(op):
            if op in ["+", "-"]:
                return 1
            if op in ["*", "/"]:
                return 2
            if op == "^":
                return 3
            return -1
        
        def operar(operador, a, b=None):
            return aplicar_operacion(operador, a, b)

        # Tokenizar la expresión
        tokens = expresion.replace("(", " ( ").replace(")", " ) ").replace("^", " ^ ").replace("*", " * ").replace("/", " / ").replace("+", " + ").replace("-", " - ").replace("mod", " mod ").split()
        print("ln35", tokens)


        # Buscar el mod
        if "mod" in tokens:
            mod_index = tokens.index("mod")
            print("ln41", mod_index)
            new_mod = int(tokens[mod_index + 1])
            print("ln43", new_mod)
            self.mod_arithmetic.set_modulo(new_mod)
            tokens = tokens[:mod_index]  # Remover la parte "mod n"
            print("ln46", tokens)
            tokens.pop()
            print("ln48", tokens)

        # Stacks
        stack_operadores = []
        stack_operandos = []

        # Evaluacion de la expresion
        for token in tokens:
            if token.isnumeric():
                stack_operandos.append(int(token))
                print("ln56", stack_operandos)
                print("ln57", stack_operadores)
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
                stack_operadores.pop()  # Remover el '('

        # Aplicar cualquier operador restante
        while stack_operadores:
            operador = stack_operadores.pop()
            b = stack_operandos.pop()
            a = stack_operandos.pop()
            resultado = operar(operador, a, b)
            stack_operandos.append(resultado)
        

        r = self.mod_arithmetic.mod_evaluate(stack_operandos[0],new_mod)
        print(r)

        return r


#pruebas
evaluador = ModularEvaluator()
expresion = "((6^2 * 3 + 7) / (2^3 - 5)) * (11 + 4^3) - 9 (mod 41)"
resultado = evaluador.evaluate(expresion)
print(resultado)

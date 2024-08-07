from Functions import FuncionesConjunto

class Conjuntos_Evaluator:
    def __init__(self, conjunto_referencial):
        self.fun = FuncionesConjunto(conjunto_referencial)
        self.conjuntos = None

    def evaluate(self, expresion, conjuntos):
        self.conjuntos = conjuntos
        
        def obtener_conjunto(nombre):
            return self.conjuntos[nombre]

        def aplicar_operacion(op, conjunto1, conjunto2=None):
            if op == "uni":
                return self.fun.union(conjunto1, conjunto2)
            elif op == "int":
                return self.fun.interseccion(conjunto1, conjunto2)
            elif op == "dif":
                return self.fun.diferencia(conjunto1, conjunto2)
            elif op == "com":
                return self.fun.complemento(conjunto1)
            elif op == "fun":
                return self.fun.is_funcion(conjunto1)
            elif op == "pro":
                return self.fun.producto_cartesiano(conjunto1, conjunto2)

        def prioridad(op):
            if op in ["uni", "int", "dif", "pro"]:
                return 1
            if op == "com":
                return 2
            if op == "fun":
                return 2
            return -1

        def operar(operador, conjunto1, conjunto2=None):
            return aplicar_operacion(operador, conjunto1, conjunto2)

        # Tokenizar la expresión
        tokens = expresion.replace("(", " ( ").replace(")", " ) ").split()
        
        # Stacks
        stack_operadores = []
        stack_operandos = []

        for token in tokens:
            if token in self.conjuntos:
                stack_operandos.append(obtener_conjunto(token))
            elif token in ["uni", "int", "dif", "com", "fun", "pro"]:
                while (stack_operadores and prioridad(stack_operadores[-1]) >= prioridad(token)):
                    operador = stack_operadores.pop()
                    if operador in ["com", "fun"]:
                        conjunto = stack_operandos.pop()
                        resultado = operar(operador, conjunto)
                    else:
                        conjunto2 = stack_operandos.pop()
                        conjunto1 = stack_operandos.pop()
                        resultado = operar(operador, conjunto1, conjunto2)
                    stack_operandos.append(resultado)
                stack_operadores.append(token)
            elif token == "(":
                stack_operadores.append(token)
            elif token == ")":
                while stack_operadores and stack_operadores[-1] != "(":
                    operador = stack_operadores.pop()
                    if operador in ["com", "fun"]:
                        conjunto = stack_operandos.pop()
                        resultado = operar(operador, conjunto)
                    else:
                        conjunto2 = stack_operandos.pop()
                        conjunto1 = stack_operandos.pop()
                        resultado = operar(operador, conjunto1, conjunto2)
                    stack_operandos.append(resultado)
                stack_operadores.pop()  # Quitar '('

        while stack_operadores:
            operador = stack_operadores.pop()
            if operador in ["com", "fun"]:
                conjunto = stack_operandos.pop()
                resultado = operar(operador, conjunto)
            else:
                conjunto2 = stack_operandos.pop()
                conjunto1 = stack_operandos.pop()
                resultado = operar(operador, conjunto1, conjunto2)
            stack_operandos.append(resultado)

        return stack_operandos[0]


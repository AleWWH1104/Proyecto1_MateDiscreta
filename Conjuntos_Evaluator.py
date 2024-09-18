from Functions import FuncionesConjunto

class Conjuntos_Evaluator:
    def __init__(self, conjunto_referencial):
        self.fun = FuncionesConjunto(conjunto_referencial)
        self.conjuntos = None

    def evaluate(self, expresion, conjuntos):
        self.conjuntos = conjuntos
        
        def obtener_conjunto(nombre):
            return self.conjuntos[nombre]

        def aplicar_operacion(op, conjunto1, conjunto2=None, conjunto3=None):
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
            elif op == "comp":
                return self.fun.compose(conjunto1, conjunto2)
            elif op == "pot":
                print("a", conjunto1)
                print("b", conjunto2)
                return self.fun.potencia(conjunto1, conjunto2)  #conjunto2 deberia ser el exponente
            elif op == "ref":
                return self.fun.ref(conjunto1, conjunto2)
            elif op == "sim":
                return self.fun.sim(conjunto1, conjunto2)
            elif op == "tra":
                return self.fun.tra(conjunto1, conjunto2)
            elif op == "bin":
                return self.fun.bin(conjunto3, conjunto2, conjunto1) #relacion es conjunto 1, conjunto2, conjunto3

        def prioridad(op):
            if op in ["uni", "int", "dif", "pro", "comp", "pot"]:
                return 1
            if op in ["com", "fun", "ref", "sim", "tra", "bin"]:
                return 2
            return -1

        def operar(operador, conjunto1, conjunto2=None, conjunto3=None):
            return aplicar_operacion(operador, conjunto1, conjunto2, conjunto3)

        # Tokenizar la expresión
        tokens = expresion.replace("(", " ( ").replace(")", " ) ").replace(",", " ").split()
        
        # Stacks
        stack_operadores = []
        stack_operandos = []

        print("tokens antes de for ln57", tokens)
        for token in tokens:
            print("Token cuando se crea ln58", token)
            if token in self.conjuntos:
                stack_operandos.append(obtener_conjunto(token))
                print("p creado stack operandos ln62", stack_operandos)
            elif token.isnumeric():
                stack_operandos.append(token)
            elif token in ["uni", "int", "dif", "com", "fun", "pro", "ref", "sim", "tra", "bin", "pot", "cps"]:
                print("p creado stack operandos ln65", stack_operandos)

                while (stack_operadores and prioridad(stack_operadores[-1]) >= prioridad(token)):
                    operador = stack_operadores.pop()
                    if operador in ["com", "fun", "ref", "sim", "tra"]:
                        conjunto = stack_operandos.pop()
                        resultado = operar(operador, conjunto)
                        print("op con lista com fun ref sim tra linea 69", stack_operandos)
                        print("Token ln 70", token)
                    elif operador in ["bin"]:
                        print("bin operador linea 75 ", stack_operandos)
                        conjunto2 = stack_operandos.pop()
                        conjunto1 = stack_operandos.pop()
                        conjunto3 = stack_operandos.pop() if stack_operandos else None
                        resultado = operar(operador, conjunto1, conjunto2, conjunto3)
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
                    if operador in ["com", "fun", "ref", "sim", "tra"]:
                        print("segundo op de fun linea 92", stack_operandos)
                        conjunto = stack_operandos.pop()
                        resultado = operar(operador, conjunto)

                    elif operador == "bin":
                        print("bin operador linea 101", stack_operandos)
                        print("antes de pop en bin", stack_operandos)
                        conjunto2 = stack_operandos.pop()
                        conjunto1 = stack_operandos.pop()
                        conjunto3 = stack_operandos.pop() if stack_operandos else None
                        resultado = operar(operador, conjunto1, conjunto2, conjunto3)
                        print("despues de pop en bin", stack_operandos)
                    else:
                        conjunto2 = stack_operandos.pop()
                        conjunto1 = stack_operandos.pop()
                        resultado = operar(operador, conjunto1, conjunto2)
                    stack_operandos.append(resultado)
                stack_operadores.pop()  # Quitar '('

        while stack_operadores:
            print(stack_operandos)
            operador = stack_operadores.pop()
            if operador in ["com", "fun"]:
                conjunto = stack_operandos.pop()
                resultado = operar(operador, conjunto)
                print("result de fun linea 121")
            elif operador in ["ref", "sim", "tra"]:
                exponente = stack_operandos.pop()
                conjunto = stack_operandos.pop()
                resultado = operar(operador, conjunto, exponente)
            elif operador == "bin":
                print("bin")
                
                conjunto2 = stack_operandos.pop()
                conjunto1 = stack_operandos.pop()
                conjunto3 = stack_operandos.pop() if stack_operandos else None
                resultado = operar(operador, conjunto1, conjunto2, conjunto3)
            else:
                conjunto2 = stack_operandos.pop()
                conjunto1 = stack_operandos.pop()
                resultado = operar(operador, conjunto1, conjunto2)
            stack_operandos.append(resultado)

        return stack_operandos[0]

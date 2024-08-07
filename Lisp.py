from Operaciones import *

def lisp(expr, conjuntos):
    def obtener_conjunto(nombre):
        return conjuntos[nombre]

    def aplicar_operacion(op, conjunto1, conjunto2=None):
        if op == "uni":
            return uni(conjunto1, conjunto2)
        elif op == "int":
            return int(conjunto1, conjunto2)
        elif op == "dif":
            return dif(conjunto1, conjunto2)
        elif op == "com":
            return com(conjuntos['U'], conjunto1)

    def prioridad(op):
        if op in ["uni", "int", "dif"]:
            return 1
        if op == "com":
            return 0
        return -1

    def operar(operador, conjunto1, conjunto2=None):
        return aplicar_operacion(operador, conjunto1, conjunto2)

    # Tokenizar la cosa
    tokens = expr.replace("(", " ( ").replace(")", " ) ").split()
    
    # Stacks
    stack_operadores = []
    stack_operandos = []

    for token in tokens:
        if token in conjuntos:
            stack_operandos.append(obtener_conjunto(token))
        elif token in ["uni", "int", "dif", "com"]:
            while (stack_operadores and prioridad(stack_operadores[-1]) >= prioridad(token)):
                operador = stack_operadores.pop()
                if operador == "com":
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
                if operador == "com":
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
        if operador == "com":
            conjunto = stack_operandos.pop()
            resultado = operar(operador, conjunto)
        else:
            conjunto2 = stack_operandos.pop()
            conjunto1 = stack_operandos.pop()
            resultado = operar(operador, conjunto1, conjunto2)
        stack_operandos.append(resultado)

    return stack_operandos[0]

# Ejemplo de uso
conjuntos = {
    'U': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    'A': [1, 2, 3, 4, 7],
    'B': [3, 4, 5, 6, 8],
    'C': [7, 8, 9, 10],
    'D': [11, 12],
    'E': [13, 14, 15],
    'F': [16,8]
}

expresion6 = "((A dif C) int D)"
resultado6 = lisp(expresion6, conjuntos)
print("Intersección ((A dif C) int D):", resultado6)

expresion7 = "((A uni B) dif (C int E))"
resultado7 = lisp(expresion7, conjuntos)
print("Unión y Diferencia combinadas ((A uni B) dif (C int E)):", resultado7)

expresion8 = "(com(A) dif B)"
resultado8 = lisp(expresion8, conjuntos)
print("Diferencia y Complemento combinados (com(A) dif B):", resultado8)

expresion9 = "((A int C) uni (B dif D))"
resultado9 = lisp(expresion9, conjuntos)
print("Intersección y Unión combinadas ((A int C) uni (B dif D)):", resultado9)

expresion10 = "((A uni (B int C)) dif (D uni E))"
resultado10 = lisp(expresion10, conjuntos)
print("Operaciones Anidadas Complejas ((A uni (B int C)) dif (D uni E)):", resultado10)





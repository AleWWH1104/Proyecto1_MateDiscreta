from Functions import *

# el conjunto_referencial
conjunto_referencial = ['a', 'b', 'c', 'd', 'e']
fun = FuncionesConjunto(conjunto_referencial)

def lisp(expr, conjuntos):
    def obtener_conjunto(nombre):
        return conjuntos[nombre]

    def aplicar_operacion(op, conjunto1, conjunto2=None):
        if op == "uni":
            return fun.union(conjunto1, conjunto2)
        elif op == "int":
            return fun.interseccion(conjunto1, conjunto2)
        elif op == "dif":
            return fun.diferencia(conjunto1, conjunto2)
        elif op == "com":
            return fun.complemento(conjunto1)
        elif op == "fun":
            return fun.is_funcion(conjunto1)
        elif op == "pro":
            return fun.producto_cartesiano(conjunto1, conjunto2)

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
    tokens = expr.replace("(", " ( ").replace(")", " ) ").split()
    
    # Stacks
    stack_operadores = []
    stack_operandos = []

    for token in tokens:
        if token in conjuntos:
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

# Ejemplo de uso
conjuntos = {
    'A': ['a', 'b', 'c'],
    'B': ['b', 'c', 'd'],
    'C': [['a', 1], ['b', 2], ['c', 3]]
}

# Ejemplo de expresiones
expr1 = "(A uni B)"
expr2 = "(A int B)"
expr3 = "(A dif B)"
expr4 = "(com A)"
expr5 = "(fun C)"
expr6 = "(A pro B)"
expr7 = "(C pro C)"

print(lisp(expr1, conjuntos))  # Unión de A y B
print(lisp(expr2, conjuntos))  # Intersección de A y B
print(lisp(expr3, conjuntos))  # Diferencia de A y B
print(lisp(expr4, conjuntos))  # Complemento de A
print(lisp(expr5, conjuntos))  # Verifica si C es una función
print(lisp(expr6, conjuntos))  # Producto cartesiano de A y B
print(lisp(expr7, conjuntos))  # Producto cartesiano de A y B

from Functions import *

# el u que estaba en el dic
#conjunto_referencial = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
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
        elif op == "is_funcion":
            return fun.is_funcion(conjunto1)
        elif op == "prod_cart":
            return fun.producto_cartesiano(conjunto1, conjunto2)

    def prioridad(op):
        if op in ["uni", "int", "dif", "prod_cart"]:
            return 1
        if op == "com":
            return 0
        if op == "is_funcion":
            return -1 
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
        elif token in ["uni", "int", "dif", "com", "is_funcion", "prod_cart", "com"]:
            while (stack_operadores and prioridad(stack_operadores[-1]) >= prioridad(token)):
                operador = stack_operadores.pop()
                if operador in ["is_funcion"]:
                    conjunto = stack_operandos.pop()
                    resultado = operar(operador, conjunto)
                else:
                    if len(stack_operandos) < 2:
                        print(f"Error: se esperaba al menos dos operandos para el operador {operador}, pero no hay suficientes operandos.")
                        return
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
                if operador in ["com", "is_funcion"]:
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
        if operador in ["com", "is_funcion"]:
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
expr1 = "(uni A B)"
expr2 = "(int A B)"
expr3 = "(dif A B)"
expr4 = "(com A)"
expr5 = "(is_funcion C)"
expr6 = "(prod_cart A B)"

print(lisp(expr1, conjuntos))  # Unión de A y B
print(lisp(expr2, conjuntos))  # Intersección de A y B
print(lisp(expr3, conjuntos))  # Diferencia de A y B
print(lisp(expr4, conjuntos))  # Complemento de A
print(lisp(expr5, conjuntos))  # Verifica si C es una función
print(lisp(expr6, conjuntos))  # Producto cartesiano de A y B
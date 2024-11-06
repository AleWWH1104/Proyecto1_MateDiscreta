from math import factorial

class Combinatoria:
    @staticmethod
    def calcular_cantidad(n, rep, orden, r=None):
        """
        Calcula la cantidad de combinaciones o permutaciones según las fórmulas específicas.
        
        Args:
            n (int): Cantidad de elementos en el conjunto original.
            rep (bool): Si True, permite repeticiones (con reemplazo).
            orden (bool): Si True, el orden importa (permutación).
            r (int, opcional): Número de elementos a seleccionar. Si no se proporciona, se usa el valor de n.
        
        Returns:
            int: Cantidad de combinaciones o permutaciones calculadas.
        """
        # Si no se especifica un valor para r, se iguala al total de elementos n.
        if r is None:
            r = n

        # Se elige la fórmula según si el orden importa o no (permutación o combinación).
        if orden:  # Caso de permutación
            if rep:  # Permutación con reemplazo: n^r
                cantidad = n ** r
            else:  # Permutación sin reemplazo: n! / (n - r)!
                cantidad = factorial(n) // factorial(n - r)
        else:  # Caso de combinación
            if rep:  # Combinación con reemplazo: (r + n - 1)! / (r!(n - 1)!)
                cantidad = factorial(r + n - 1) // (factorial(r) * factorial(n - 1))
            else:  # Combinación sin reemplazo: n! / (r!(n - r)!)
                cantidad = factorial(n) // (factorial(r) * factorial(n - r))

        return cantidad  # Devuelve el resultado de la combinación o permutación

# Ejemplos de uso de la función para mostrar los diferentes casos:

# Definimos el total de elementos y la cantidad a seleccionar
elementos = 4
r = 4

# Ejemplo 1: Combinación sin repetición, sin importar el orden
cantidad = Combinatoria.calcular_cantidad(elementos, rep=False, orden=False, r=r)
print(f"Combinación sin repetición, sin importar el orden: {cantidad}")

# Ejemplo 2: Combinación con repetición, sin importar el orden
cantidad = Combinatoria.calcular_cantidad(elementos, rep=True, orden=False, r=r)
print(f"Combinación con repetición, sin importar el orden: {cantidad}")

# Ejemplo 3: Permutación sin repetición, importando el orden
cantidad = Combinatoria.calcular_cantidad(elementos, rep=False, orden=True, r=r)
print(f"Permutación sin repetición, importando el orden: {cantidad}")

# Ejemplo 4: Permutación con repetición, importando el orden
cantidad = Combinatoria.calcular_cantidad(elementos, rep=True, orden=True, r=r)
print(f"Permutación con repetición, importando el orden: {cantidad}")

from math import factorial

class Combinatoria:
    @staticmethod
    def calcular_cantidad(lista, rep, orden, r=None):
        """
        Calcula la cantidad de combinaciones o permutaciones según las fórmulas específicas.
        
        Args:
            lista (list): Lista de elementos a combinar o permutar.
            rep (bool): Si True, permite repeticiones (con reemplazo).
            orden (bool): Si True, el orden importa (permutación).
            r (int, opcional): Número de elementos a seleccionar. Si no se proporciona, se usa el tamaño de la lista.
        
        Returns:
            int: Cantidad de combinaciones o permutaciones calculadas.
        """
        n = len(lista)
        if r is None:
            r = n

        if orden:  # Permutación
            if rep:  # Permutación con reemplazo: n^r
                cantidad = n ** r
            else:  # Permutación sin reemplazo: n! / (n - r)!
                cantidad = factorial(n) // factorial(n - r)
        else:  # Combinación
            if rep:  # Combinación con reemplazo: (r + n - 1)! / (r!(n - 1)!)
                cantidad = factorial(r + n - 1) // (factorial(r) * factorial(n - 1))
            else:  # Combinación sin reemplazo: n! / (r!(n - r)!)
                cantidad = factorial(n) // (factorial(r) * factorial(n - r))

        return cantidad

# Ejemplos de uso
elementos = ["a", "b", "c", "d"]
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

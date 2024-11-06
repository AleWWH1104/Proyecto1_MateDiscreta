import math

class Combinatoria:
    @staticmethod
    def permutaciones_diferentes(n, r):
        """Calcula permutaciones de objetos diferentes."""
        return math.perm(n, r)

    @staticmethod
    def permutaciones_iguales(n, grupos):
        """Calcula permutaciones de objetos iguales."""
        resultado = math.factorial(n)
        for g in grupos:
            resultado //= math.factorial(g)
        return resultado

    @staticmethod
    def combinaciones_diferentes(n, r):
        """Calcula combinaciones de objetos diferentes."""
        return math.comb(n, r)

    @staticmethod
    def combinaciones_iguales(n, r):
        """Calcula combinaciones de objetos iguales."""
        return math.comb(n + r - 1, r)


# Ejemplo de uso
n = 5  # Total de objetos
r = 3  # Número de objetos a seleccionar
grupos = [2, 2, 1]  # Ejemplo de grupos de objetos iguales

# Ejemplo para permutaciones y combinaciones de objetos diferentes
print("Permutaciones de objetos diferentes:", Combinatoria.permutaciones_diferentes(n, r))
print("Combinaciones de objetos diferentes:", Combinatoria.combinaciones_diferentes(n, r))

# Ejemplo para permutaciones de objetos iguales
print("Permutaciones de objetos iguales:", Combinatoria.permutaciones_iguales(n, grupos))

# Ejemplo para combinaciones de objetos iguales
print("Combinaciones de objetos iguales:", Combinatoria.combinaciones_iguales(n, r))

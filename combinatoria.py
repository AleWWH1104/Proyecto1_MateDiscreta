import math
from collections import Counter

class Combinatoria:
    @staticmethod
    def permutaciones_diferentes(n, r):
        """Calcula permutaciones de objetos diferentes, si n >= r."""
        if r > n:
            return "Error: r no puede ser mayor que n en permutaciones sin repetición."
        return math.perm(n, r)

    @staticmethod
    def permutaciones_iguales(n, grupos):
        """Calcula permutaciones de objetos iguales."""
        contador = Counter(grupos)
        resultado = math.factorial(n)
        for g in contador.values():
            resultado //= math.factorial(g)
        return resultado

    @staticmethod
    def combinaciones_diferentes(n, r):
        """Calcula combinaciones de objetos diferentes, si n >= r."""
        if r > n:
            return "Error: r no puede ser mayor que n en combinaciones sin repetición."
        return math.comb(n, r)

    @staticmethod
    def combinaciones_iguales(n, r):
        """Calcula combinaciones de objetos iguales."""
        return math.comb(n + r - 1, r)

# Ejemplo de uso
n = 4  # Total de objetos
r = 2  # Número de objetos a seleccionar (intencionalmente mayor para ver el mensaje de error)
grupos = ["a", "a", "b", "c"]  # Ejemplo de grupos de objetos iguales

# Ejemplo para permutaciones y combinaciones de objetos diferentes
print("Permutaciones de objetos diferentes:", Combinatoria.permutaciones_diferentes(n, r))
print("Combinaciones de objetos diferentes:", Combinatoria.combinaciones_diferentes(n, r))

# Ejemplo para permutaciones de objetos iguales
print("Permutaciones de objetos iguales:", Combinatoria.permutaciones_iguales(n, grupos))

# Ejemplo para combinaciones de objetos iguales
print("Combinaciones de objetos iguales:", Combinatoria.combinaciones_iguales(n, r))
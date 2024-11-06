from itertools import permutations, combinations, product, combinations_with_replacement

class CombinatoriaAvanzada:
    @staticmethod
    def evaluar(lista, muestreo, orden, r=None):
        """
        Calcula permutaciones o combinaciones de acuerdo con los parámetros.
        
        Args:
            lista (list): Lista de elementos a combinar o permutar.
            muestreo (bool): Si True, permite muestreo con reemplazo.
            orden (bool): Si True, importa el orden.
            r (int, opcional): Número de elementos a seleccionar. Si no se proporciona, se usa el tamaño de lista.
        
        Returns:
            list: Lista de combinaciones o permutaciones calculadas.
        """
        if r is None:
            r = len(lista)

        # Determinar si es permutación o combinación basándonos en muestreo y orden
        if orden:  # Importa el orden
            if muestreo:  # Con reemplazo
                resultado = list(set(product(lista, repeat=r)))  # Permutación con reemplazo
            else:  # Sin reemplazo
                resultado = list(set(permutations(lista, r)))  # Permutación sin reemplazo
        else:  # No importa el orden
            if muestreo:  # Con reemplazo
                resultado = list(set(combinations_with_replacement(lista, r)))  # Combinación con reemplazo
            else:  # Sin reemplazo
                resultado = list(set(combinations(lista, r)))  # Combinación sin reemplazo

        # Convertimos el resultado a lista de listas para que el formato sea consistente
        return [list(item) for item in resultado]


# Ejemplos de uso

# Ejemplo 1: Permutaciones de Objetos Diferentes
lista1 = ["a", "b", "c", "d"]
resultado1 = CombinatoriaAvanzada.evaluar(lista1, muestreo=False, orden=True)
print("Ejemplo 1 - Permutaciones de Objetos Diferentes:", resultado1)

# Ejemplo 2: Permutaciones de Objetos Iguales
lista2 = ["a", "a", "b", "c"]
resultado2 = CombinatoriaAvanzada.evaluar(lista2, muestreo=False, orden=True)
print("Ejemplo 2 - Permutaciones de Objetos Iguales:", resultado2)

# Ejemplo 3: Combinaciones de Objetos Diferentes
lista3 = ["a", "b", "c", "d"]
resultado3 = CombinatoriaAvanzada.evaluar(lista3, muestreo=False, orden=False, r=2)
print("Ejemplo 3 - Combinaciones de Objetos Diferentes:", resultado3)

# Ejemplo 4: Combinaciones de Objetos Iguales
lista4 = ["a", "a", "b", "c"]
resultado4 = CombinatoriaAvanzada.evaluar(lista4, muestreo=False, orden=False, r=2)
print("Ejemplo 4 - Combinaciones de Objetos Iguales:", resultado4)

from itertools import permutations, combinations, product, combinations_with_replacement

class CombinatoriaAvanzada:
    @staticmethod
    def evaluar(lista, rep, orden, r=None):
        """
        Calcula permutaciones o combinaciones de acuerdo con los parámetros proporcionados.
        
        Args:
            lista (list): Lista de elementos a combinar o permutar.
            rep (bool): Si True, permite repeticiones (con reemplazo).
            orden (bool): Si True, el orden importa (permutación).
            r (int, opcional): Número de elementos a seleccionar. Si no se proporciona, se usa el tamaño de la lista.
        
        Returns:
            tuple: Número de combinaciones o permutaciones calculadas y la lista de combinaciones o permutaciones.
        """
        # Si r no está especificado, se asigna el tamaño de la lista como valor por defecto.
        if r is None:
            r = len(lista)

        # Seleccionamos la fórmula según si el orden y la repetición importan.
        if orden:  # Caso donde el orden importa (permutaciones)
            if rep:  # Permutación con reemplazo: utiliza product
                resultado = list(set(product(lista, repeat=r)))  # Genera todas las permutaciones con reemplazo
            else:  # Permutación sin reemplazo: utiliza permutations
                resultado = list(set(permutations(lista, r)))  # Genera todas las permutaciones sin reemplazo
        else:  # Caso donde el orden no importa (combinaciones)
            if rep:  # Combinación con reemplazo: utiliza combinations_with_replacement
                resultado = list(set(combinations_with_replacement(lista, r)))  # Genera combinaciones con reemplazo
            else:  # Combinación sin reemplazo: utiliza combinations
                resultado = list(set(combinations(lista, r)))  # Genera combinaciones sin reemplazo

        # Convertimos el resultado a una lista de listas para formato consistente
        resultado = [list(item) for item in resultado]
        
        # Calculamos la cantidad de combinaciones o permutaciones posibles
        posible = len(resultado)

        # Devolvemos el número de resultados posibles y la lista de combinaciones/permutaciones
        return posible, resultado


# Ejemplos de uso de la función para diferentes casos:

# Ejemplo 1: Permutaciones de elementos diferentes sin repetición
lista1 = ["a", "b", "c", "d"]
resultado1 = CombinatoriaAvanzada.evaluar(lista1, rep=False, orden=True)
print("Ejemplo 1 - Permutaciones de Objetos Diferentes:", resultado1)

# Ejemplo 2: Permutaciones de elementos con algunos repetidos, sin repetición
lista2 = ["a", "a", "b", "c"]
resultado2 = CombinatoriaAvanzada.evaluar(lista2, rep=False, orden=True)
print("Ejemplo 2 - Permutaciones de Objetos Iguales:", resultado2)

# Ejemplo 3: Combinaciones de elementos diferentes sin repetición, sin importar el orden
lista3 = ["a", "b", "c", "d"]
resultado3 = CombinatoriaAvanzada.evaluar(lista3, rep=False, orden=False, r=2)
print("Ejemplo 3 - Combinaciones de Objetos Diferentes:", resultado3)

# Ejemplo 4: Combinaciones de elementos con algunos repetidos, sin repetición, sin importar el orden
lista4 = ["a", "a", "b", "c"]
resultado4 = CombinatoriaAvanzada.evaluar(lista4, rep=False, orden=False, r=2)
print("Ejemplo 4 - Combinaciones de Objetos Iguales:", resultado4)

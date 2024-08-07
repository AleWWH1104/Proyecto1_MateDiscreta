class FuncionesConjunto:
    """
    Clase que implementa diversas operaciones con conjuntos y funciones.

    Atributos:
    conjunto_referencial (list): El conjunto referencial para las operaciones de complemento.

    Métodos:
    union(conjunto1, conjunto2): Retorna la unión de dos conjuntos.
    interseccion(conjunto1, conjunto2): Retorna la intersección de dos conjuntos.
    diferencia(conjunto1, conjunto2): Retorna la diferencia de dos conjuntos.
    complemento(conjunto): Retorna el complemento de un conjunto respecto al conjunto referencial.
    is_funcion(conjunto_funcion): Verifica si un conjunto es una función (todos los elementos son listas con dominios únicos).
    producto_cartesiano(conjunto1, conjunto2): Retorna el producto cartesiano de dos conjuntos.
    """
    
    def __init__(self, conjunto_referencial):
        """
        Inicializa la clase FuncionesConjunto con un conjunto referencial.

        Parámetros:
        conjunto_referencial (list): El conjunto referencial para las operaciones de complemento.
        """
        self.conjunto_referencial = conjunto_referencial

    def union(self, conjunto1, conjunto2):
        """
        Retorna la unión de dos conjuntos.

        Parámetros:
        conjunto1 (list): El primer conjunto.
        conjunto2 (list): El segundo conjunto.

        Retorna:
        list: La unión de los dos conjuntos.
        """
        return list(set(conjunto1) | set(conjunto2))

    def interseccion(self, conjunto1, conjunto2):
        """
        Retorna la intersección de dos conjuntos.

        Parámetros:
        conjunto1 (list): El primer conjunto.
        conjunto2 (list): El segundo conjunto.

        Retorna:
        list: La intersección de los dos conjuntos.
        """
        return list(set(conjunto1) & set(conjunto2))

    def diferencia(self, conjunto1, conjunto2):
        """
        Retorna la diferencia de dos conjuntos.

        Parámetros:
        conjunto1 (list): El primer conjunto.
        conjunto2 (list): El segundo conjunto.

        Retorna:
        list: La diferencia de los dos conjuntos.
        """
        return list(set(conjunto1) - set(conjunto2))

    def complemento(self, conjunto):
        """
        Retorna el complemento de un conjunto respecto al conjunto referencial.

        Parámetros:
        conjunto (list): El conjunto para el cual se calculará el complemento.

        Retorna:
        list: El complemento del conjunto.
        """
        return list(set(self.conjunto_referencial) - set(conjunto))

    def is_funcion(self, conjunto_funcion):
        """
        Verifica si un conjunto es una función (todos los elementos son listas con dominios únicos).

        Parámetros:
        conjunto_funcion (list): El conjunto a verificar.

        Retorna:
        bool: True si el conjunto es una función, False en caso contrario.
        """
        if not all(isinstance(item, list) and len(item) == 2 for item in conjunto_funcion):
            return False
        dominios = [item[0] for item in conjunto_funcion]
        return [len(dominios) == len(set(dominios))]

    def producto_cartesiano(self, conjunto1, conjunto2):
        """
        Retorna el producto cartesiano de dos conjuntos.

        Parámetros:
        conjunto1 (list): El primer conjunto.
        conjunto2 (list): El segundo conjunto.

        Retorna:
        list: El producto cartesiano de los dos conjuntos.
        """
        conjunto1Xconjunto2 = []
        for i in conjunto1:
            for j in conjunto2:
                conjunto1Xconjunto2.append((i, j))
        return conjunto1Xconjunto2


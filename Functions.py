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
    compose relacion1, relacion2): Retorna la composición de dos relaciones.
    potencia(relacion, n): Calcula la potencia n-ésima de una relación.
    ref(relacion, conjunto): Verifica si una relación es reflexiva en un conjunto.
    sim(relacion, conjunto): Verifica si una relación es simétrica en un conjunto.
    tra(relacion, conjunto): Verifica si una relación es transitiva en un conjunto.
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
        return len(dominios) == len(set(dominios))

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

    def compose(self, relacion1, relacion2):
        """
        Retorna la composición de dos relaciones.

        Parámetros:
        relacion1 (list): La primera relación, una lista de pares.
        relacion2 (list): La segunda relación, una lista de pares.

        Retorna:
        list: La composición de las dos relaciones.
        """
        result = []
        for a, b in relacion1:
            for c, d in relacion2:
                if b == c:
                    result.append((a, d))
        return result

    def potencia(self, relacion, n):
        """
        Calcula la potencia n-ésima de una relación.

        Parámetros:
        relacion (list): La relación, una lista de pares.
        n (int): El exponente de la potencia.

        Retorna:
        list: La relación elevada a la potencia n.
        """
        if n < 1:
            return []  # No tiene sentido calcular potencia 0 o negativa
        resultado = relacion.copy()
        for _ in range(n - 1):
            resultado = self.compose(resultado, relacion)
        return resultado

    def ref(self, relacion, conjunto):
        """
        Verifica si una relación es reflexiva en un conjunto.

        Parámetros:
        relacion (list): La relación, una lista de pares.
        conjunto (list): El conjunto sobre el cual se define la reflexividad.

        Retorna:
        bool: True si la relación es reflexiva, False en caso contrario.
        """
        for a in conjunto:
            if [a, a] not in relacion:
                return False
        return True

    def sim(self, relacion, conjunto):
        """
        Verifica si una relación es simétrica en un conjunto.

        Parámetros:
        relacion (list): La relación, una lista de pares.
        conjunto (list): El conjunto sobre el cual se define la simetría.

        Retorna:
        bool: True si la relación es simétrica, False en caso contrario.
        """
        for (a, b) in relacion:
            if [b, a] not in relacion:
                return False
        return True

    def tra(self, relacion, conjunto):
        """
        Verifica si una relación es transitiva en un conjunto.

        Parámetros:
        relacion (list): La relación, una lista de pares.
        conjunto (list): El conjunto sobre el cual se define la transitividad.

        Retorna:
        bool: True si la relación es transitiva, False en caso contrario.
        """
        for (a, b) in relacion:
            for (c, d) in relacion:
                if b == c and [a, d] not in relacion:
                    return False
        return True
    
    def bin(self, relacion, conjunto1, conjunto2):
        """
        Verifica si la relación relacion es una función binaria de conjunto1 a conjunto2.
        
        Parámetros:
        relacion (list): La relación, una lista de pares.
        conjunto1 (list): El dominio (conjunto de partida).
        conjunto2 (list): El codominio (conjunto de llegada).

        Retorna:
        bool: True si la relación es binaria de conjunto1 a conjunto2, False en caso contrario.
        """
        rel_dict = {}
        for a, b in relacion:
            if a not in conjunto1 or b not in conjunto2:
                return False  # El elemento de la relación no está en conjunto1 o conjunto2
            if a in rel_dict:
                return False  # Un elemento de conjunto1 está relacionado con más de un elemento de conjunto2
            rel_dict[a] = b
        return len(rel_dict) == len(conjunto1)
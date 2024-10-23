class AritmeticaModular:
    """
    Clase que implementa operaciones de aritmética modular en Zp, donde p es un número primo.

    Atributos:
    p (int): El número primo que define el módulo.

    Métodos:
    suma_modular(a, b): Retorna la suma de a y b en Zp.
    resta_modular(a, b): Retorna la resta de a y b en Zp.
    multiplicacion_modular(a, b): Retorna el producto de a y b en Zp.
    division_modular(a, b): Retorna la división de a entre b en Zp, usando el inverso multiplicativo de b.
    potencia_modular(a, b): Retorna a elevado a la potencia b en Zp.
    evaluar_modulo(a): Retorna el valor de a módulo p.
    establecer_modulo(p): Establece el valor de p como el módulo para las operaciones.
    """

    def __init__(self, p=1):
        """
        Inicializa la clase con un valor de módulo p.

        Parámetros:
        p (int): El número primo que define el módulo. Por defecto es 1.
        """
        self.p = p

    def suma_modular(self, a, b):
        """
        Retorna la suma de a y b en Zp.

        Parámetros:
        a (int): El primer número.
        b (int): El segundo número.

        Retorna:
        int: La suma de a y b módulo p.
        """
        return (a + b) % self.p

    def resta_modular(self, a, b):
        """
        Retorna la resta de a y b en Zp.

        Parámetros:
        a (int): El primer número.
        b (int): El segundo número.

        Retorna:
        int: La resta de a y b módulo p.
        """
        return (a - b) % self.p

    def multiplicacion_modular(self, a, b):
        """
        Retorna el producto de a y b en Zp.

        Parámetros:
        a (int): El primer número.
        b (int): El segundo número.

        Retorna:
        int: El producto de a y b módulo p.
        """
        return (a * b) % self.p

    def division_modular(self, a, b):
        """
        Retorna la división de a entre b en Zp, utilizando el inverso multiplicativo de b.

        Parámetros:
        a (int): El numerador.
        b (int): El denominador.

        Retorna:
        int: El cociente de a entre b módulo p.
        """
        b_inv = pow(b, -1, self.p)  # Calcula el inverso multiplicativo de b en Zp
        return (a * b_inv) % self.p

    def potencia_modular(self, a, b):
        """
        Retorna a elevado a la potencia b en Zp.

        Parámetros:
        a (int): La base.
        b (int): El exponente.

        Retorna:
        int: a elevado a la potencia b módulo p.
        """
        return pow(a, b, self.p)

    def evaluar_modulo(self, a):
        """
        Retorna el valor de a módulo p.

        Parámetros:
        a (int): El número a evaluar.

        Retorna:
        int: a módulo p.
        """
        return a % self.p

    def establecer_modulo(self, p):
        """
        Establece el valor de p como el módulo para las operaciones.

        Parámetros:
        p (int): El número primo que define el módulo.
        """
        self.p = p

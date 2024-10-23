class ModularArithmetic:
    def __init__(self):
        self.p = 1

    def mod_add(self, a, b): #suma
        return (a + b)

    def mod_subtract(self, a, b): #resta
        return (a - b)

    def mod_multiply(self, a, b): #multiplicacion
        return (a * b)

    def mod_divide(self, a, b): #división
        return (a * pow(b,-1,self.p))

    def mod_power(self, a, b): #potencia
        return pow(a, b, self.p)

    def mod_evaluate(self, a, b): #modulo
        return a % b
    
    def set_modulo(self, p):
        self.p = p

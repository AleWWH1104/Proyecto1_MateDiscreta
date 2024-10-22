class ModularArithmetic:
    def __init__(self):
        self.p = 1

    def mod_add(self, a, b):
        return (a + b)

    def mod_subtract(self, a, b):
        return (a - b)

    def mod_multiply(self, a, b):
        return (a * b)

    def mod_divide(self, a, b):
        # Asumimos que b tiene inverso multiplicativo en Zp
        b_inv = pow(b, -1, self.p)
        return (a * b_inv)

    def mod_power(self, a, b):
        return pow(a, b, self.p)

    def mod_evaluate(self, a, b):
        return a % b
    
    def set_modulo(self, p):
        self.p = p

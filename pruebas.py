def compose(R1, R2):
    result = []
    for a, b in R1:
        for c, d in R2:
            if b == c:
                result.append((a, d))
    return result

def potencia(R, n):
    if n < 1:
        return []  # No tiene sentido calcular potencia 0 o negativa
    resultado = R.copy()
    for _ in range(n - 1):
        resultado = compose(resultado, R)
    return resultado

def ref(R, A):
    for a in A:
        if [a, a] not in R:
            return False
    return True

def sim(R,A):
    for (a, b)in R:
        if [b,a] not in R:
            return False
    return True
    
def tra(R,A):
    for (a, b) in R:
        for (c, d) in R:
            if b == c and [a, d] not in R:
                return False
    return True

R1 = [['1', '1'], ['2', '2'], ['3', '3'], ['0', '0'], ['1', '2'],['2', '1']]
conjunto = ['1', '2', '3', '0']

print("ref: ", ref(R1, conjunto))
print("sim: ", sim(R1, conjunto))
print("tra: ", tra(R1, conjunto))

S = [['1', '0'], ['2', '0'], ['3', '1'], ['3', '2'], ['4', '1']]
E = [['1', '1'], ['1', '4'], ['2', '3'], ['3', '1'], ['3', '4']]
print("comps RoS: ", compose(S, E))
print("comps SoR: ", compose(E, S))

M1 = [['1', '1'], ['1', '3'], ['2', '2'],['2', '1']]
M2 = [['1', '2'], ['2', '3'], ['3', '1'],['3', '3']]
print("comps M1oM2: ", compose(M1, M2))

M3 = [['1', '2'], ['3', '1'], ['2', '3'],['3', '2']]
print("pot M3^2: ", potencia(M3,2))
print("pot M3^3: ", potencia(M3,3))
print("pot M3^4: ", potencia(M3,4))
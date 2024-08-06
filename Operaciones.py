U = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Conjunto referencial
A = [1, 2, 3, 4]
B = [3, 4, 5, 6]

# Unión
def uni(conjunto1, conjunto2):
    return list(set(conjunto1) | set(conjunto2))

# Intersección
def int(conjunto1, conjunto2):
    return list(set(conjunto1) & set(conjunto2))

# Diferencia
def dif(conjunto1, conjunto2):
    return list(set(conjunto1) - set(conjunto2))

# Complemento
def com(conjunto_referencial, conjunto):
    return list(set(conjunto_referencial) - set(conjunto))

# Pruebas de las funciones
print("Unión (A o B):", uni(A, B))
print("Intersección (A y B):", int(A, B))
print("Diferencia (A - B):", dif(A, B))
print("Complemento (-A):", com(U, A))
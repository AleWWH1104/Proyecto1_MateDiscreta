L = [(1,2),(2,4),(3,6),(4,8 ),(5,10)] #funcion x=2x {x∈Z|x<=1&x>=1}
M = [(1,2),(2,4),(3,6),3]#algo no funcion

N = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
O = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def isFun(conjuntoFun):
    return all(isinstance(item, tuple) for item in conjuntoFun) #verifica que todos los objetos sean tuplas

def prodCart(conjunto1, conjunto2):#recibe dos conjuntos
    conjunto1Xconjunto2 = []
    for i in conjunto1:#para todos los elementos de conjunto1
        for j in conjunto2:#recorrer los elementos de conjunto2
            conjunto1Xconjunto2.append((i,j))#crear una tupla del recorrido anterios
    return conjunto1Xconjunto2#devuelve unicamente un conjunto


#pruebas
print(isFun(L))
print(isFun(M))
print(prodCart(N,O))
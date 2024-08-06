L = [(1,2),(2,4),(3,6),(4,8 ),(5,10)] #funcion x=2x {x∈Z|x<=1&x>=1}
M = [(1,2),(2,4),(3,6),3]#algo no funcion

N = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
O = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def isFun(conjuntoFun):
    return all(isinstance(item, tuple) for item in conjuntoFun)

def prodCart(conjunto1, conjunto2):
    conjunto1Xconjunto2 = []
    for i in conjunto1:
        for j in conjunto2:
            conjunto1Xconjunto2.append((i,j))
    return conjunto1Xconjunto2


#pruebas
print(isFun(L))
print(isFun(M))
print(prodCart(N,O))
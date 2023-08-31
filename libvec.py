import cmath

def sumaveccplx(c1,c2):
    """Adición de vectores complejos"""
    suma = []
    for i in range(0,len(c1)):
        suma.append(c1[i] + c2[i])
    return suma

def inverveccplx(c1):
    """Inverso (aditivo) de un vector complejos"""
    inver = []
    for i in range(0,len(c1)):
        inv = -c1[i]
        inver.append(inv)
    return inver

def multiescalcplx(c1,c2):
    """Multiplicación de un escalar por un vector complejo"""
    mult = []
    for i in range(0,len(c2)):
        mult.append(c1 * c2[i])
    return mult 

def sumamatcplx(c1,c2):
    """Adición de matrices complejas"""
    suma = []
    for i in range(0,len(c1)):
        for j in range(0,len(c1)):
            su = c1[i][j] + c2[i][j]
            suma.append(su)
    return(suma)

def invermatcplx(c1):
    """Inversa (aditiva) de una matriz compleja"""
    inversa = []
    for i in range(0,len(c1)):
        for j in range(0,len(c1)):
            inver = - c1[i][j]
            inversa.append(inver)
    return inversa

def multimatcplx(c1,c2):
    """Multiplicación de un escalar por una matriz compleja"""
    multi = []
    for i in range(0,len(c2)):
        for j in range(0,len(c2)):
            mu = c1 * c2[i][j]
            multi.append(mu)
    return multi 

def transmatcplx(c1):
    """Transpuesta de una matriz/vector"""
    m = len(c1)
    n = len(c1[0])
    trans = [[0 for i in range(m)] for j in range(n)]
    for i in range(len(trans)):
        for j in range(len(trans[0])):
            trans[i][j] = c1[j][i] 
    return trans
    
def conjumat(c1):
    """Conjugada de una matriz/vector"""
    c1 = c1.conjugate()
    return(c1)

if __name__ == '__main__':
    print(sumaveccplx((5,3),(9,2)))
    print(inverveccplx((2,7)))
    print(multiescalcplx((2),(-3,4)))
    print(sumamatcplx(([[1,2],[3,4]]),([[5,6],[7,8]])))
    print(invermatcplx([[1,2],[3,4]]))
    print(multimatcplx((5),([[1,2],[3,4]])))
    print(transmatcplx([[1,2],[3,4]]))
    print(conjumat(2 + 4j))

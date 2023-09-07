import cmath
import numpy as np

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

def adjuntamat(mat):
    """Adjunta (daga) de una matriz/vector"""
    return transmatcplx(conjumat(mat))

def productmat(mat1,mat2):
    """Producto de dos matrices (de tamaños compatibles)"""
    m1 = len(mat1)
    n1 = len(mat1[0])
    m2 = len(mat2)
    n2 = len(mat2[0])
    if n1 != m2:
        return "No son matrices compatibles"
    else:
        matri = [[0 for row in range(n2)] for col in range(m1)]
        for i in range(m1):
            for j in range(n2):
                for k in range(m2):
                    matri[i][j] += mat1[i][k] * mat2[k][j]
        return matri

def accionmat(mat, vect):
    """Función para calcular la "acción" de una matriz sobre un vector."""
    matriz = np.array(mat)
    vector = np.array(vect)
    rest = np.dot(matriz,vector)
    return str(rest)

def produinterno(vector_1,vector_2):
    """Producto interno de dos vectores"""
    sum = 0
    if len(vector_1) != len(vector_2):
        return "No son vectores compatibles. "
    else:
        for i in range(len(vector_1)):
            sum+= vector_1[i]*vector_2[i]
    return sum

def normvect(vec):
    """Norma de un vector."""
    sum = 0
    for i in range(len(vec)):
        sum+=abs(vec[i])**2
        print(sum)
    return round((sum)**0.5, 2)

def distvect(vect_1, vect_2):
    """Distancia entre dos vectores."""
    resta = []
    for i in range(0, len(vect_1)):
        resta.append((vect_1[i] - vect_2[i]))
    ver = str(resta[0])
    val = []
    for i in range(len(ver)):
        if ver[i] == "+" or ver[i] == "-":
            val.append(ver[i-1])
            val.append(ver[i+1])
            break
    su = 0
    for i in range(2):
        su+=int(val[i])**2
    return round(su**0.5, 2)

def valprop(mat):
    """Valores  y vectores propios de una matriz."""
    if len(mat) != len(mat[0]): return "No es una matriz cuadrada"
    matriz = np.array(mat)
    valores_propios, vectores_propios = np.linalg.eig(matriz)
    return "los valores propios para esta matriz o vector son {} y los vectores son {}".format(valores_propios, vectores_propios)

def matunita(mat):
    """Revisar si una matriz es unitaria."""
    long_f = len(mat)
    long_c = len(mat[0])
    if long_c != long_f:
        return "La matriz no es cuadrada"
    for i in range(long_f):
        for j in range(long_c):
            if i == j:
                if mat[i][j] == 1:
                    continue
            else:
                if mat[i][j] != 0:
                    return "No es unitaria"
    return "Si es matriz unitaria"

def mathermitiana(mat):
    """Revisar si una matriz es Hermitiana."""
    m = len(mat)
    n = len(mat[0])
    mat2 = transmatcplx(mat)
    for row in range(m):
        for column in range(n):
            if mat[row][column] != (mat2[row][column]).conjugate():
                return "No es hermitiana"
    return "Es hermimtiana"

def prodtensemat(mat1, mat2):
    """Producto tensor de dos matrices/vectores."""
    m = len(mat1)
    n = len(mat2)
    m1 = len(mat1[0])
    n1 = len(mat2[0])
    fil = m * n
    col = n1 * m1
    matriz = [[0 for row in range(fil)]for column in range(col)]
    for j in range(fil):
        for k in range(col):
            matriz[j][k] = (mat1[j//n][k//n1] * mat2[j%n][k%n1])
    return matriz



# Libreria CNYT OPERACIONES CON VECTORES Y MATRICES COMPLEJAS

## Autor: ***Juan Jose Mejia Celis***

Libreria creada con el objetivo de lograr operaciones de vectores y matrices complejas la cual cuenta con lo siguiente:

- Adición de vectores complejos.
- Inverso (aditivo) de un vector complejos.
- Multiplicación de un escalar por un vector complejo.
- Adición de matrices complejas.
- Inversa (aditiva) de una matriz compleja.
- Multiplicación de un escalar por una matriz compleja.
- Transpuesta de una matriz/vector
- Conjugada de una matriz/vector
- Adjunta (daga) de una matriz/vector
- Producto de dos matrices (de tamaños compatibles)
- Función para calcular la "acción" de una matriz sobre un vector.
- Producto interno de dos vectores
- Norma de un vector
- Distancia entre dos vectores
- Valores  y vectores propios de una matriz
- Revisar si una matriz es unitaria
- Revisar si una matriz es Hermitiana
- Producto tensor de dos matrices/vectores

## ¿Como se usa?

Se neceitan conocer los numeros complejos que se operaran y escoger las funciones que desea las cuales estan diseñadas 
para un proceso simple y funcional 

## Datos

Denotación

``` txt
(Numero Real, Numero Complejo)
```

Manera en que se representan los numeros complejos es necesario saber que para denotar numeros complejos es con la letra **j**.


``` txt
4 + 1j
```

Vectores complejos

``` txt
[3 + 5j, 2 -7j]
```

Matrices Complejas
``` txt
[[1 + 2j, 6 - 4j],
[3 - 9j, 9 - 2j],
[2 + 6j, 7 - 4j]]
```



## Parametos Generales

>Se uso la Funcion Round para aproximar los valores con una presicion de 2, se ve reflejado en los casos de prueba
```Python
round(Parametro,2)
```

## Contenido

### Archivos 

En esta libreria cuenta con 4 archivos:

- ***.gitignore*** -> Es el archivo que excluye que no queremos que se suba al repositorio GITHUB
- ***README.md*** -> El texto general de la libreria.
- ***libvec.py*** -> Es la libreria con todas sus funciones correctamente explicadas.
- ***test_libvec.py*** -> Este archivo contiene los correspondientes testeos los cuales pueden contiene casos
de prueba que pueden ser sustituidos de la manera que desee.

### test.py

Explicacion de como funciona el testeo lo probaremos con la suma de vectores

``` Python
def test_sumveccplx(self):
    """test 1: Adición de vectores complejos"""
    c1 = [1 + 5j, -4 - 9j] """En esta columnda se agregan 
    las variables de los vectores, si tienen mas variables se le agregan 
    dependendiendo de la funcion"""
    c2 = [1 + 5j, 5 + 17j]
    sum_ver = [(2 + 10j), (1 + 8j)] #En esta variable se pone la respuesta que a usted le dio
    sum_doc = lc.sumaveccplx(c1, c2) #En esta variable se tiene que cambiar la funcion a la cual se va a hacer el testeo
    self.assertEqual(sum_doc, sum_ver)
    #Al final devuelve la cantidad de casos que pasan correctamente 
```


## Requisitos para usar el sistema

Debe de poseer na version a ***Python*** superior a 3.5, adicionalmente debe de poseer la libreria math y numpy instaladas
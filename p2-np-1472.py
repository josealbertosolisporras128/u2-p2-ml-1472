import numpy as np
# jose solis nc 1472
# Ejemplos de numpy numerical python
print("-- especiado linealmente en array -- 1472")
arre= np.linspace(start=0,stop=1,num=10)
print(arre)
print("-- matriz identidad en array -- 1472")
matrix=np.eye(3)
print(matrix)
print("-- genera numeros al azar(aleatorios) en 2D array -- 1472")
numale= np.random.random((3,4)) # genera 12 numeros aleatorios
print(numale)
print("generar 9 numeros aleatorios entre 0 y 1")
numale= np.random.random((3,3)) # genera 9 numeros aleatorios
print(numale)
# como generar 9 numeros aleatorios comprendidos entre 1 y 20
# con numpy un arreglo de 3x3
print("generar 9 numeros aleatorios entre 1 y 20")
arre = np.random.randint(1, 21, size=9).reshape(3, 3)
print(arre)
print("jose solis porras nc 1472")

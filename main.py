import numpy as np
#Definicion de dimensiones de la matriz
num_filas = int(input("Ingrese el numero de filas de la matriz "))
num_col = int(input("Ingrese el numero de columnas de la matriz "))
#Ingresar los valores de la matriz R
print("Si su matriz se ve así")
print("1 2 3")
print("4 5 6")
print("7 8 9")
print("Ingrese los valores separados por espacios así: 1 2 3 4 5 6 7 8 9")
elementos = list(map(float, input("Ingrese los elementos de la matriz:").split()))
#Asignar los elementos a una matriz
R = np.array(elementos).reshape(num_filas,num_col)
#Ingresar los valores de la matriz S
num_filas = int(input("Ingrese el numero de filas de la matriz "))
num_col = int(input("Ingrese el numero de columnas de la matriz "))
elementos = list(map(float, input("Ingrese los elementos de la matriz:").split()))
#Asignar los elementos a una matriz
S = np.array(elementos).reshape(num_filas,num_col)
#Hallar la matriz de composición
C = np.zeros((len(R),len(S[0])))
for i in range(0,len(R)):
    for j in range(0,len(S[0])):
        lista=[]
        for k in range(0,len(R[0])):
            lista.append(min(R[i,k],S[k,j]))
        C[i,j] = max(lista)
print("La matriz composición R°S es:")
for i in range(0,len(R)):
    for j in range(0,len(S[0])):
        print("\t",C[i,j],end="")
    print()
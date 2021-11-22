import re
import numpy as np
import sys

n = int(input("Masukkan Banyaknya Variabel : "))
m = int(input("Masukkan Banyaknya Persamaan : "))

augmented_matrix = np.zeros((n, n+1))
result = np.zeros(n)

print("Masukkan Koefisien Persamaan : ")

# Input with Console
for i in range(m):
    temp = input()
    temp = temp.split()
    for j in range(n+1):
        augmented_matrix[i][j] = temp[j]

# Gauss Jordan Elimination
for i in range(n):
    if augmented_matrix[i][i] == 0.0: 
        sys.exit("Tidak ditemukan solusi")
    for j in range(n):
        if i != j:
            ratio = augmented_matrix[j][i] / augmented_matrix[i][i]

            for k in range(n+1):
                augmented_matrix[j][k] = augmented_matrix[j][k] - ratio * augmented_matrix[i][k]


# Obtaining
for i in range(n):
    result[i] = augmented_matrix[i][n]/augmented_matrix[i][i]


# Output Result
print("Hasil : ")
for i in range(n):
    print("X%d = %0.2f" %(i+1, result[i]), end = "\t") 
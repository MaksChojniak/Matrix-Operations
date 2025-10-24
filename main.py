import numpy as np

def mnozenie(A, B):
    m = A.shape[0]
    n = A.shape[1]
    k = B.shape[1]

    C = np.zeros((m, k), dtype=float)

    for i in range(m):
        for j in range(k):
            suma = 0
            for s in range(n):
                suma += A[i][s] * B[s][j]
            C[i][j] = suma
    return C


def wyznacznik(A):
    A = np.copy(A)

    n = A.shape[0]
    det = A[0][0]

    for s in range(n-1):
        for i in range(s+1, n):
            for j in range(s+1, n):
                A[i][j] = A[i][j] - A[i][s] * A[s][j] / A[s][s]
        det *= A[s+1][s+1]
    return det

# np.linalg.inv() odwrotna


print()
print(f"{'-'*15}Zad 1{'-'*15}")
print()

A = np.array([[10,	3,	7,	-8],	
              [0,	5,	8,	-8],
              [-4,	-8,	-4,	6],	
              [-7,	-1,	-10,	4],	
              [-3,	0,	8,	1]],
      dtype=float)

B = np.array([[1,	-8,	-10],	
              [4,	-7,	6],	
              [-4,	-6,	-10	],
              [-6,	0,	8]],
      dtype=float)

# print(f"wynik: \n{mnozenie(A, B)}")
# print(f"oczekiwany wynik: \n{np.matmul(A, B)}")

print(f"wynik: \n{np.array2string(mnozenie(A, B), formatter={'float_kind': lambda x: "%.10f" % x})}")
print(f"oczekiwany wynik: \n{np.array2string(np.matmul(A, B), formatter={'float_kind': lambda x: "%.10f" % x})}")
print(f"roznica: \n{np.array2string(np.matmul(A, B)-mnozenie(A,B), formatter={'float_kind': lambda x: "%.10f" % x})}")

print()
print(f"{'-'*15}Zad 2{'-'*15}")
print()

D = np.array([  [-7,	-2,	9,	5],	
                [5,	-7,	-9,	-8],	
                [1,	3,	2,	-3],	
                [-1,	6,	3,	9]], dtype=float)

print(f"wynik: {wyznacznik(D):.10f}")
print(f"oczekiwany wynik: {np.linalg.det(D):.10f}")
print(f"roznica: {np.abs(np.linalg.det(D)-wyznacznik(D)):.10f}")



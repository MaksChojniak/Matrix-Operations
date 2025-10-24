import numpy as np

def odwaracanie_macierzy(A):
    A = np.copy(A)

    n = A.shape[0]
    B = np.zeros((n, 2*n), dtype=float)

    for i in range(n):
        for j in range(n):
            B[i][j] = A[i][j]

            if i is j:
                B[i][j+n] = 1
            else:
                B[i][j+n] = 0

    print(f"macierz rozszerzona: \n{np.array2string(B, formatter={'float_kind': lambda x: "%.10f" % x})}")


    for s in range(0, n):
        c = B[s][s]
        B[s][s] = B[s][s] - 1
        for j in range(s+1, 2*n):
            d = B[s][j] / c
            for i in range(0, n):
                B[i][j] = B[i][j] - d * B[i][s]
    
    odwA = np.zeros(A.shape, dtype=float)

    for i in range(n):
        for j in range(n, 2*n):
            odwA[i][j-n] = B[i][j]
    return odwA



E = np.array([[-3,	-4,	1,	1]	,
[-5,	-1,	3,	5]	,
[-3,	-5,	-4,	3]	,
[-4,	3,	5,	2]], dtype=float)

print(f"macierz odwrotna: \n{np.array2string(odwaracanie_macierzy(E), formatter={'float_kind': lambda x: "%.10f" % x})}")

print(f"wynik mnozenia: \n{np.array2string(np.matmul(odwaracanie_macierzy(E), E), formatter={'float_kind': lambda x: "%.10f" % x})}")

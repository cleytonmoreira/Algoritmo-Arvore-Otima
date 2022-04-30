
freqs = [0, 0, 2, 1, 8, 7, 4, 3, 1]
freqs_interval = [1, 1, 5, 0, 8, 3, 1, 0, 3]

def build_F(freq, freq_int):
    n = len(freq)
    F = [[0 for i in range(n)] for j in range(n)]

    for j in range(n):
        for i in range(j + 1):
            F[i][j] = sum(freq[i + 1:j + 1]) + sum(freq_int[i:j + 1])

    return F

def build_C_and_K(F):
    n = len(F[0])
    C = [[0 for i in range(n)] for j in range(n)]
    K = [[0 for i in range(n)] for j in range(n)]

    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            C[i][j] = 1e12
            for k in range(i + 1, j + 1):
                if C[i][k - 1] + C[k][j] < C[i][j]:
                    C[i][j] = C[i][k - 1] + C[k][j]
                    K[i][j] = k
            C[i][j] += F[i][j]

    return C, K

if __name__ == "__main__":
    F = build_F(freqs, freqs_interval)
    C, K = build_C_and_K(F)

    print("MATRIZ DE FREQUÃŠNCIAS")
    for l in F:
        print(l)

    print()
    print("MATRIZ DE CUSTOS")
    for l in C:
        print(l)

    print()
    print("MATRIZ DE ÃNDICES")
    for l in K:
        print(l)

    print()
    print(f"CUSTO MÃNIMO DA ÃRVORE: {C[0][-1]}")
    input()

A = [9, 2, 3, 1, 4]
n = max(A)

# adiciona o numero se já nao esta presente
[A.append(i) for i in range(n) if i not in A]

# deixa em ordem crescente
A = sorted(A)
print(A)

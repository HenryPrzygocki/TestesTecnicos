def hasSum(array,x):
  # Verdade se para A[i] + A[j] = x com i de (0,j) com j de (0,numero de elementos)
  if [True for j in range(len(array)) for i in range(j) if (array[i] + array[j] == x)]:
    return True
  return False


A = [1, 15, 2, 7, 2, 5, 7, 1, 4]

# soma a ser verificada
soma = 1231
hasSum(A,soma)

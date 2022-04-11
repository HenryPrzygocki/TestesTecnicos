A = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
# numero que deve estar à esquerda
n = 1 

# encontra multiplos indices onde o numero pode ser encontrado na lista
get_ones = lambda A, xs: [i for (y,i) in zip(xs, range(len(xs))) if A==y] 

# indices onde o numero desejado, n, se encontra na lista, A
indxs = get_ones(n,A) 

# como os indices estao ordenados crescentemente, podemos remover o item e move-lo sem ter que corigir os indices para as posteriores remocoes
for i in indxs: 
  # remove o item do dado indice
  A.pop(i) 
  # insere-o na primeira posicao
  A.insert(0,n) 
print(A)

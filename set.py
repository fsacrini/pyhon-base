conjunto_a = set([1,2,3,4,5])
conjunto_b = set([4,5,6,7,8])

# União [1,2,3,4,5,6,7,8]
print(conjunto_a | conjunto_b)
print(conjunto_a.union(conjunto_b)) 

# Intercção [4,5]
print(conjunto_a & conjunto_b)
print(conjunto_a.intersection(conjunto_b))

# Differece a and b [1,2,3] - Order matter
print(conjunto_a.difference(conjunto_b))
print(conjunto_a - conjunto_b)

# Symetric Difference [1,2,3,6,7,8]
print(conjunto_a.symmetric_difference(conjunto_b))
print(conjunto_a ^ conjunto_b)

# ----------------------------

c1 = set()

c1.add(1)
c1.add(2)
c1.add(3)

print(c1) # {1,2,3} -> Adiciona dinamico

# Hash Table

numeros = [1,2,3,5,1,1,1,7,8,9]

1 in numeros # True
8 in numeros # True -> Depende do tamanho da lista pode demorar muito
6 in numeros # False

# No caso do 8 essa busca chama de O(n) - compleximada ciclomatica

# Quado criarmos a a mesma lista usando set ele já remove os dados duplicados,
# reduzindo o tamanho da lista e é usado o processo O(1) - Operação constante
# Ele guarda os dados usando Hash Table (Rapido)

numeros = set([1,2,3,5,1,1,1,7,8,9])
print(numeros) # {1,2,3,4,7,8,9}

# set não pode ser acessado usando a posição, pois não garante a posição dos items


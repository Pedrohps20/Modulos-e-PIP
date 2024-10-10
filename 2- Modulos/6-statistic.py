import statistics

# 1 - Aplicar a média
print(statistics.mean([3, 2, 5, 8, 9])) # valores em forma de lista por causa dos []

# 2 - Aplicar a mediana
print(statistics.median([1, 2, 3, 8, 9]))
print(statistics.median([1, 2, 4, 7, 8, 9])) # soma os dois valores centrais e aplica a média

# 3 - Aplicar a moda - é o que mais se repete
print(statistics.mode([2, 5, 3, 2, 8, 3, 9, 4, 1, 5, 6]))

# 4 - Desvio padrão
"""
- Quanto mais próximo de 0 for o desvio padrão, significa que o dados do conjunto estão menos dispersos
"""
print(statistics.stdev([1, 2.5, 2, 2.5, 3, 3.5, 4, 4.5]))
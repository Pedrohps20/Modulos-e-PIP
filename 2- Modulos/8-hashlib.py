import hashlib

# 1 - Verificar os algorítmos disponíveis
print(hashlib.algorithms_available)

# 2 - Algoritmos disponíveis de acordo com o SO
print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o sha256
algoritmo = hashlib.sha256()
print(algoritmo.digest())
mensagem = "A melhor forma de prever o futuro é criá-lo".encode()
algoritmo.update(mensagem)
print(algoritmo.hexdigest())

# 4 - Utilizando o MD5
md5 = hashlib.md5()
md5.update(mensagem)
print(md5.hexdigest())
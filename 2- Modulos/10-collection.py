from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Contar itens de uma lista
frutas = ["Maçã", "Banana", "uva", "pera", "Uva", "Maçã", 
          "Abacaxi", "Melancia", "Mamão", "Maçã", "Banana", 
          "Uva", "Abacaxi", "Banana"]
print(frutas)
print(Counter(frutas))

# 2 - Utilizando tupla nomeada
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game ("Fifa23", 90.50, 8.5)
g2 = game("Residente Evil 4 Remake", 300, 10.0)
print(g1)
print(g2)

# 3 - Ordenando dicionários
students = {"Pedro":23, "Ana": 22, "Ronaldo": 26, "janaina":25}
a = sorted(students.items(), key=itemgetter(0))
print(students)
print(a)

# 4 - Utilizando fila ambas extremidades
deq = deque ([20, 40, 60, 80])
print(deq)
deq.appendleft(10)
print(deq)
deq.append(90)
print(deq)
deq.popleft()
print(deq)
deq.pop()
print(deq)
import calc

from calc import div # Aqui vai estar importando só um pedaço do modulo, no caso só a div

print(calc.sum(8, 3))
print(calc.sub(9, 2))
print(calc.div(5, 2))
print(calc.mult(8, 3))

print(div(10, 5)) # esse é o módulo importado do from
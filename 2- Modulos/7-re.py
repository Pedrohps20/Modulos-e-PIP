import re

text = "OneBitCode: Tranformamos pessoas em programadores sem limites"

# 1 - Índice inicial e final de palavras
# O "r" significa que estamos trabalhando com uma string bruta (row string)

match = re.search(r'pessoas em programadores',text)
print('Índice inicial', match.start())
print('Índice final', match.end())

# 2 - Buscando o índice que possui o ponto
site = 'https://onebitcode.com'
# match = re.search(r'.',site)
match = re.search(r'\.',site)
print(match)

# 3 - Buscando uma lista de caracteres dentro de uma frase
padrao = "[a-m]"
result = re.findall(padrao, text)
print(text)
print(result)

# 4 - Verificando o inicio de uma string
rule = r'^A'
phrases=['A casa está suja', 'O dia está lindo', 'Vamos passear']
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não corresponde: {f}")
        
# 5 - Verrifcando o final de uma string
rule_end = r'!$'
phrases2= 'O dia está lindo!'
match=re.search(rule_end, phrases2)
if match:
    print("Sim, corresponde")
else:
    print("Não corresponde")
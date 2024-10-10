import json

# 1 - String para dicionários
person = '{"name": "Rodrigo", "linguagens":["Python", "JavaScript"]}'
person_dict = json.loads(person)
print(person_dict)
print(person_dict['linguagens'])

# 2 - Convertendo dicionários para json
person_json = json.dumps(person_dict)
print(person_json)
print(type(person_json))
print(type(person_dict))

# 3 - Formatando json
print(json.dumps(person_dict, indent=4, sort_keys=True))

# 4 - Salvando json em txt
with open("person.txt", "w") as json_file:
    json.dump(person_dict, json_file)
    
# 5 - Lendo json externo
with open ("nome do arquivo", "r") as f:
    data = json.load(f)
    print(data)
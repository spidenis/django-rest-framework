import requests
import jsonpath

base_url = 'http://localhost:8000'

avaliacoes = requests.get(base_url + '/api/v2/avaliacoes/')

# results = jsonpath.jsonpath(avaliacoes.json(), 'results')

# print(results)

# first = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')

# print(first)

# nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')

# print(nome)

#Todos os nomes que avaliaram

# nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')

# print(nomes)

notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')

print(notas)
import requests

base_url = 'http://localhost:8000'

#GET Avaliações

# avaliacoes = requests.get(base_url + '/api/v2/avaliacoes/')

#Codigo de status HTTP
# print(avaliacoes.status_code)

#Acesso aos dados da resposta
# print(avaliacoes.json())

#Acessar a quantidade de registros
# print(avaliacoes.json()['count'])

# Acessar proxima pagina
# print(avaliacoes.json()['next'])

# Acessando dados da pagina
# print(avaliacoes.json()['results'])

# Acesso primeiro elemento da lista
# print(avaliacoes.json()['results'][0])

# Acesso ultimo elemento da lista
# print(avaliacoes.json()['results'][-1]['nome'])

# Get Avaliacao

# avaliacao = requests.get(base_url + '/api/v2/avaliacoes/31/')
# print(avaliacao.json())

# Get Cursos

headers = {"Authorization": "Token 35bba4817ba8011cf9200e49e6e3bca9c1dccf4a"}

cursos = requests.get(url=base_url + '/api/v2/cursos/c', headers=headers)
print(cursos.json())

import requests

headers = {"Authorization": "Token 35bba4817ba8011cf9200e49e6e3bca9c1dccf4a"}

base_url_cursos = 'http://localhost:8000/api/v2/cursos/'

base_url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

results = requests.get(url=base_url_cursos, headers=headers)

# print(results.json())

assert results.status_code == 200
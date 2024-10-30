import requests


class TestCursos:
    headers = {"Authorization": "Token df472793418ed0412eaef5c18ed4c3c3bf43e2f2"}
    base_url_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.base_url_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.base_url_cursos}1/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso de Jogos de Animação com muita curtição ou não",
            "url": "https://www.geekuniverity.com.br/animation"
        }

        resposta = requests.post(url=self.base_url_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Curso de Jogos de Animação-Act",
            "url": "https://www.geekuniverity.com.br/cosme"
        }

        resposta = requests.put(url=f'{self.base_url_cursos}4/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200
    
    def test_put_titulo(self):
        atualizado = {
            "titulo": "Curso de Jogos de Animação com Python2",
            "url": "https://www.geekuniverity.com.br/cjap2"
        }

        resposta = requests.put(url=f'{self.base_url_cursos}8/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.base_url_cursos}7/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursoAPIView(APIView):
    """
        API de cursos Geek
    """

    def get(self, request):
        #cursos = Curso.objects.raw('SELECT "cursos_curso"."id", "cursos_curso"."criacao", "cursos_curso"."atualizacao", "cursos_curso"."ativo", "cursos_curso"."titulo", "cursos_curso"."url" FROM "cursos_curso" WHERE "cursos_curso"."ativo" ORDER BY "cursos_curso"."id" ASC')
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)

        #print([m.name for m in Curso._meta.fields])

        #data = serializer.data
        #print(data)
        return Response(serializer.data)
    
class  AvaliacaoAPIView(APIView):
    """
        API de avaliações da Geek
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
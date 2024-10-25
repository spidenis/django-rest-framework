from rest_framework import serializers #Trasnformar objetos python em JSON e vice versa
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):

    #class Meta em que adicionamos configurações extras
    class Meta:
        extra_kwargs = {
            'email': {'write_only':True}
        }
        model = Avaliacao
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    #Nested Relationship (Traz o objeto DJSON)
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    
    #HyperLinked Related Field (Link de acesso ao recurso)
    """
    avaliacoes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='avaliacao-detail'
    )    
    """
    #Primary Key Related Field (Chaves primarias - Maxima performance)
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )
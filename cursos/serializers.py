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
    
    class Meta:
        model = Curso
        fields = '__all__'
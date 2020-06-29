from rest_framework.serializers import ModelSerializer
from lojaApp.models import *


class SuaCompraSerializer(ModelSerializer):
    class Meta:
        model = SuaCompra
        fields = '__all__'


class RedeSerializer(ModelSerializer):
    class Meta:
        model = Rede
        fields = '__all__'


class PanosDePratoSerializer(ModelSerializer):
    class Meta:
        model = PanosDePrato
        fields = '__all__'


class MantasSerializer(ModelSerializer):
    class Meta:
        model = Mantas
        fields = '__all__'
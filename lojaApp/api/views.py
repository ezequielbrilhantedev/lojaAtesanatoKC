from rest_framework import viewsets
from lojaApp.models import *
from .serializers import *


class SuaCompraViewSet(viewsets.ModelViewSet):
    queryset = SuaCompra.objects.all()
    serializer_class = SuaCompraSerializer


class RedeViewSet(viewsets.ModelViewSet):
    queryset = Rede.objects.all()
    serializer_class = RedeSerializer


class PanosDePratoViewSet(viewsets.ModelViewSet):
    queryset = PanosDePrato.objects.all()
    serializer_class = PanosDePratoSerializer


class MantasViewSet(viewsets.ModelViewSet):
    queryset = Mantas.objects.all()
    serializer_class = MantasSerializer
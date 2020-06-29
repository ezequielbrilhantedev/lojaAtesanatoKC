from django.contrib import admin
from .models import SuaCompra, Rede, PanosDePrato, Mantas

# Register your models here.
admin.site.register(SuaCompra)
admin.site.register(Rede)
admin.site.register(PanosDePrato)
admin.site.register(Mantas)
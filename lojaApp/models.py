from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# REDES
rede_cor = [
    ('VERMELHA', 'Vermelha'),
    ('AMARELA', 'Amarela'),
    ('VERDE', 'Verde'),
    ('AZUL', 'Azul'),
]

rede_preco = [
    (1, '60.00'),
    (2, '80.00')
]

rede_tipo = [
    ('SIMPLES', 'Simples'),
    ('PREMIUM', 'Premium')
]

# PANOS DE PRATO
panos_preco = [
    ('R$ 10.00', '10.00')
]

# MANTAS
mantas_cor = [
    ('VERMELHA', 'Vermelha'),
    ('AMARELA', 'Amarela'),
    ('VERDE', 'Verde'),
    ('AZUL', 'Azul'),
]

mantas_preco = [
    ('R$ 30.00', '30.00')
]


class SuaCompra(models.Model):
    rede = models.ForeignKey('Rede', on_delete=models.CASCADE)
    panos = models.ForeignKey('PanosDePrato', on_delete=models.CASCADE)
    mantas = models.ForeignKey('Mantas', on_delete=models.CASCADE)


class Rede(models.Model):
    tipo = models.CharField(choices=rede_tipo, max_length=10)
    cor = models.CharField('Cor', choices=rede_cor, max_length=10)
    valor = models.CharField('Valor', choices=rede_preco, max_length=10)

    def __str__(self):
        return self.cor


class PanosDePrato(models.Model):
    valor = models.CharField('Valor', choices=panos_preco, max_length=10)

    def __str__(self):
        return self.valor


class Mantas(models.Model):
    cor = models.CharField('Cor', choices=mantas_cor, max_length=10)
    valor = models.CharField('Valor', choices=mantas_preco, max_length=10)

    def __str__(self):
        return self.cor
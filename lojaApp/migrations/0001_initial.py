# Generated by Django 3.0.7 on 2020-06-28 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonteSuaCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Rede',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(choices=[('VERMELHA', 'Vermelha'), ('AMARELA', 'Amarela'), ('VERDE', 'Verde'), ('VERDE', 'Verde'), ('AZUL', 'Azul')], max_length=10, verbose_name='Cor')),
            ],
        ),
    ]

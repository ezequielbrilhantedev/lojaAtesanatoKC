# Generated by Django 3.0.7 on 2020-06-28 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lojaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='montesuacompra',
            name='rede',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lojaApp.Rede', verbose_name='Redes'),
            preserve_default=False,
        ),
    ]
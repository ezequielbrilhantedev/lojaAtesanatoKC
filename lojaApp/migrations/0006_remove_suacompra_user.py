# Generated by Django 3.0.7 on 2020-06-28 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lojaApp', '0005_auto_20200628_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suacompra',
            name='user',
        ),
    ]
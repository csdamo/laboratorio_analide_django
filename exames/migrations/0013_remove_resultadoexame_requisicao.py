# Generated by Django 3.2.8 on 2021-11-15 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exames', '0012_alter_resultadoexame_requisicao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultadoexame',
            name='requisicao',
        ),
    ]

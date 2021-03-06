# Generated by Django 3.2.8 on 2021-11-26 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exames', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultadoexame',
            name='indice_colesterol',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resultadoexame',
            name='indice_glicose',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resultadoexame',
            name='resultado_teste_covid',
            field=models.CharField(choices=[('positivo', 'positivo'), ('negativo', 'negativo')], default='negativo', max_length=100),
        ),
        migrations.AddField(
            model_name='resultadoexame',
            name='resultado_teste_toxicológico',
            field=models.CharField(choices=[('positivo', 'positivo'), ('negativo', 'negativo')], default='negativo', max_length=100),
        ),
        migrations.AlterField(
            model_name='resultadoexame',
            name='tipo_exame',
            field=models.CharField(choices=[('glicose', 'glicose'), ('colesterol', 'colesterol'), ('teste covid', 'teste Covid'), ('testetoxicologico', 'teste toxicológico')], default='glicose', max_length=100),
        ),
    ]

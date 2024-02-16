# Generated by Django 5.0.1 on 2024-02-16 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('ing', 'Ingenieria'), ('TSU', 'Tecnico Superior Universitario'), ('M', 'Maestría')], max_length=10, verbose_name='Nivel')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('short_name', models.CharField(max_length=20, verbose_name='Abreviatura')),
            ],
            options={
                'verbose_name': 'carreras',
            },
        ),
    ]
# Generated by Django 5.1.1 on 2024-10-25 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avaliacao',
            options={'ordering': ['id'], 'verbose_name': ('Avaliacao',), 'verbose_name_plural': 'Avaliacoes'},
        ),
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ['id'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
    ]

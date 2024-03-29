# Generated by Django 5.0.2 on 2024-02-20 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('publicacao', models.CharField(max_length=4)),
                ('genero', models.CharField(max_length=20)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autor.autor')),
            ],
        ),
    ]

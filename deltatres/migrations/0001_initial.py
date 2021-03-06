# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-17 21:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('data_nasc', models.DateTimeField(default=django.utils.timezone.now)),
                ('venc_habilitacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('rg', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=6)),
                ('bairro', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=10)),
                ('cidade', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=100)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(max_length=200)),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]

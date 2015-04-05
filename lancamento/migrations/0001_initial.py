# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lancamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=70, verbose_name='descri\xe7\xe3o')),
                ('valor', models.DecimalField(verbose_name='valor', max_digits=10, decimal_places=2)),
                ('situacao', models.CharField(default=None, max_length=1, verbose_name='situa\xe7\xe3o', choices=[(b'P', 'Projetado'), (b'C', 'Concretizado')])),
                ('observacao', models.TextField(null=True, verbose_name='observa\xe7\xe3o', blank=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='data do cadastro')),
                ('data_lancamento', models.DateTimeField(default=None, null=True, verbose_name='data', blank=True)),
                ('conta', models.ForeignKey(to='conta.Conta')),
            ],
            options={
                'ordering': ['data_lancamento'],
                'verbose_name': 'lan\xe7amento',
                'verbose_name_plural': 'lan\xe7amentos',
            },
        ),
    ]

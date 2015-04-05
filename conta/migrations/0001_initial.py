# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=30, verbose_name='descri\xe7\xe3o')),
                ('ativa', models.BooleanField(default=True, verbose_name='ativa')),
            ],
            options={
                'ordering': ['descricao'],
                'verbose_name': 'conta',
                'verbose_name_plural': 'contas',
            },
        ),
    ]

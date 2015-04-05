# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancamento', '0003_lancamento_classificacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lancamento',
            name='classificacao',
            field=models.CharField(default=None, max_length=1, verbose_name='classifica\xe7\xe3o', choices=[(b'F', 'Despesa Fixa'), (b'V', 'Despesa Vari\xe1vel')]),
        ),
    ]

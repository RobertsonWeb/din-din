# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancamento', '0002_auto_20150405_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='lancamento',
            name='classificacao',
            field=models.CharField(default=b'V', max_length=1, verbose_name='classifica\xe7\xe3o', choices=[(b'F', 'Despesa Fixa'), (b'V', 'Despesa Vari\xe1vel')]),
        ),
    ]

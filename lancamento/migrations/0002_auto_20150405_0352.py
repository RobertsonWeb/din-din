# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lancamento',
            name='data_lancamento',
            field=models.DateField(default=None, null=True, verbose_name='data', blank=True),
        ),
    ]

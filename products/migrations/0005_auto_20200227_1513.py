# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-27 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_commentperfume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentperfume',
            name='score',
            field=models.IntegerField(verbose_name=(1, 2, 3, 4)),
        ),
    ]

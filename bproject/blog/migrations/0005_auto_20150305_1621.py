# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150305_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=5000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=5000),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150305_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upd_date',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]

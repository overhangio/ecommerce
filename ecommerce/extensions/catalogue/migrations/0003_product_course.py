# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('catalogue', '0002_auto_20150223_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='course',
            field=models.ForeignKey(related_name='products', blank=True, to='courses.Course', null=True),
            preserve_default=True,
        ),
    ]

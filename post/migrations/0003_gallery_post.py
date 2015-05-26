# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_gallery_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='post',
            field=models.ForeignKey(default=0, to='post.Post'),
            preserve_default=False,
        ),
    ]

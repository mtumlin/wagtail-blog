# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogindexrelatedlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexrelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='related_links', to='blog.BlogPage'),
        ),
    ]

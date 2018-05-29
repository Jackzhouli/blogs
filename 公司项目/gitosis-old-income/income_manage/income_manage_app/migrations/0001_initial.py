# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('LoginID', models.CharField(max_length=20, verbose_name='\u767b\u9646\u540d')),
                ('Name', models.CharField(max_length=10, verbose_name='\u59d3\u540d')),
                ('Sex', models.BooleanField(default=True)),
                ('Birthday', models.CharField(max_length=20, null=True)),
                ('JoinTime', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('built_from', models.CharField(default='CC', max_length=2, choices=[('FA', 'Factory'), ('CC', 'Command Centre'), ('BA', 'Barracks'), ('SA', 'Starport')])),
                ('supply_cost', models.IntegerField(default=1)),
                ('mineral_cost', models.IntegerField(default=0)),
                ('vespene_cost', models.IntegerField(default=0)),
                ('build_time', models.IntegerField()),
                ('life', models.IntegerField()),
                ('armor', models.IntegerField(default=0)),
            ],
        ),
    ]

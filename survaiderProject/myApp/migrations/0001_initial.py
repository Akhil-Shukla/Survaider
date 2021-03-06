# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-07-23 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdultDataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=0)),
                ('work', models.CharField(max_length=50)),
                ('fnlwgt', models.IntegerField(default=0)),
                ('education', models.CharField(max_length=50)),
                ('education_num', models.IntegerField(default=0)),
                ('marital_status', models.CharField(max_length=20)),
                ('occupation', models.CharField(max_length=20)),
                ('relationship', models.CharField(max_length=20)),
                ('race', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=20)),
                ('capital_gain', models.IntegerField(default=0)),
                ('capital_loss', models.IntegerField(default=0)),
                ('hours_per_week', models.IntegerField(default=0)),
                ('native_country', models.CharField(max_length=20)),
                ('salary', models.CharField(max_length=10)),
            ],
        ),
    ]

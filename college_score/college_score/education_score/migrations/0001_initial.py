# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name=b'name')),
                ('location', models.CharField(max_length=100, verbose_name=b'address')),
                ('university', models.CharField(max_length=500, verbose_name=b'University1')),
            ],
        ),
        migrations.CreateModel(
            name='CourseRank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('courses', models.CharField(max_length=100, verbose_name=b'course_name')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee', models.CharField(max_length=200)),
                ('emplocation', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='IncomeBoost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('annualsalary', models.DecimalField(max_digits=12, decimal_places=2)),
                ('dependents', models.DecimalField(max_digits=2, decimal_places=0)),
                ('kids', models.DecimalField(max_digits=1, decimal_places=0)),
                ('certification', models.CharField(max_length=500, verbose_name=b'certification_name')),
            ],
        ),
    ]

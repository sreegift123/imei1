# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-26 03:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Detail',
            new_name='Users',
        ),
    ]

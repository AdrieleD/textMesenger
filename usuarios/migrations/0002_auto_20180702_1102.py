# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-02 14:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserConta',
            new_name='User',
        ),
    ]

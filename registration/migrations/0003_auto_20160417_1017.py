# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 10:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20160410_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='Shipment_ID',
        ),
        migrations.AddField(
            model_name='delivery',
            name='Shipment_ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='registration.Shipment'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shipment',
            name='Shipment_ID',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='\u0410\u0447\u0430\u0430\u043d\u044b \u0434\u0443\u0433\u0430\u0430\u0440'),
        ),
    ]

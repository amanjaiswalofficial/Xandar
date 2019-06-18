# Generated by Django 2.1.7 on 2019-06-14 04:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190614_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupons',
            name='valid_till',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 14, 4, 31, 58, 567415)),
        ),
        migrations.AlterField(
            model_name='productsubcategory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ProductCategory'),
        ),
    ]

# Generated by Django 2.1.7 on 2019-06-11 09:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ColorDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=10)),
                ('code', models.CharField(max_length=8)),
            ],
        ),
        migrations.AlterField(
            model_name='coupons',
            name='valid_till',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 9, 43, 46, 466787)),
        ),
    ]

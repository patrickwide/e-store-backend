# Generated by Django 3.2.10 on 2022-01-21 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0005_auto_20220121_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shopLocation',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='shop',
            name='shopName',
            field=models.CharField(default='N/A', max_length=64),
        ),
    ]

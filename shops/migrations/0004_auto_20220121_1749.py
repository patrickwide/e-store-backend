# Generated by Django 3.2.10 on 2022-01-21 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_auto_20220115_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productPrice',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='productPhoto1',
            field=models.FileField(max_length=255, upload_to='pictures/%Y/%m/%d'),
        ),
    ]
# Generated by Django 3.2.10 on 2022-01-21 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0013_auto_20220122_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='shop',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]

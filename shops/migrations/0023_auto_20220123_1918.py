# Generated by Django 3.2.10 on 2022-01-23 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0022_auto_20220123_0519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='shopOwner',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]

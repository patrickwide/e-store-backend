# Generated by Django 3.2.10 on 2022-01-21 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0010_auto_20220121_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopname',
            name='shopProfile',
            field=models.FileField(default='/media/pictures/2022/01/08/project-2.jpg', max_length=255, upload_to='pictures/%Y/%m/%d'),
        ),
    ]

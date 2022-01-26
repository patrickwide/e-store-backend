# Generated by Django 3.2.10 on 2022-01-23 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productCategoryName', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopName', models.CharField(max_length=64)),
                ('shopProfile', models.FileField(max_length=255, upload_to='pictures/%Y/%m/%d')),
                ('shopBio', models.CharField(max_length=255)),
                ('shopLocation', models.CharField(max_length=255)),
                ('shopOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopOwner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=64)),
                ('productPrice', models.IntegerField()),
                ('productDescription', models.CharField(max_length=500)),
                ('productPhoto1', models.FileField(default='/media/pictures/2022/01/08/project-2.jpg', max_length=255, upload_to='pictures/%Y/%m/%d')),
                ('productPhoto2', models.FileField(default='/media/pictures/2022/01/08/project-2.jpg', max_length=255, upload_to='pictures/%Y/%m/%d')),
                ('productPhoto3', models.FileField(default='/media/pictures/2022/01/08/project-2.jpg', max_length=255, upload_to='pictures/%Y/%m/%d')),
                ('productPhoto4', models.FileField(default='/media/pictures/2022/01/08/project-2.jpg', max_length=255, upload_to='pictures/%Y/%m/%d')),
                ('productPhoto5', models.FileField(default='/media/pictures/2022/01/08/project-2.jpg', max_length=255, upload_to='pictures/%Y/%m/%d')),
                ('productCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productCategory', to='database.productcategory')),
                ('shop', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, related_name='shop', to='database.shop')),
            ],
        ),
    ]
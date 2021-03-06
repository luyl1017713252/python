# Generated by Django 3.1.7 on 2021-05-11 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='icon',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='图标'),
        ),
        migrations.AddField(
            model_name='permission',
            name='is_menu',
            field=models.BooleanField(default=False, verbose_name='是否菜单'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-05-14 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0003_auto_20210512_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='别名'),
        ),
    ]

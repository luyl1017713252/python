# Generated by Django 3.1.7 on 2021-05-07 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_auto_20210507_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='permissions',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='roles',
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.campuses'),
        ),
        migrations.DeleteModel(
            name='Permission',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]

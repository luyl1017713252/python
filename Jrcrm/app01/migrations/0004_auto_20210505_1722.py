# Generated by Django 3.1.7 on 2021-05-05 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20210505_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app01.customer', verbose_name='跟进人'),
        ),
    ]

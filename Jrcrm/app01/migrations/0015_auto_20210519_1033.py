# Generated by Django 3.1.7 on 2021-05-19 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0014_auto_20210518_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='部门名称')),
                ('coutent', models.IntegerField(verbose_name='人数')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='deal_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='departments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.department'),
        ),
    ]

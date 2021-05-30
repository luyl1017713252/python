# Generated by Django 3.1.7 on 2021-03-23 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20210323_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(max_length=32)),
                ('tel', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='ad',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.authordetail'),
        ),
    ]

# Generated by Django 3.2.5 on 2022-05-06 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-09 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=50, verbose_name='ФИО')),
                ('phone_number', models.CharField(max_length=13, verbose_name='Номер телефона')),
                ('type_of_learning', models.BooleanField(default=True)),
                ('sr_mark', models.FloatField(verbose_name='Средний балл')),
            ],
        ),
    ]

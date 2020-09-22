# Generated by Django 3.0.3 on 2020-09-11 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('roll', models.IntegerField(max_length=70)),
                ('city', models.CharField(max_length=70)),
                ('marks', models.IntegerField()),
                ('passdate', models.DateField()),
                ('admdatetime', models.DateTimeField()),
            ],
        ),
    ]

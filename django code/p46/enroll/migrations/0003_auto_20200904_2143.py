# Generated by Django 3.0.3 on 2020-09-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_auto_20200904_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=70),
        ),
    ]

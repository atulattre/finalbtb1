# Generated by Django 4.2 on 2023-06-23 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user1',
            name='space',
            field=models.IntegerField(),
        ),
    ]

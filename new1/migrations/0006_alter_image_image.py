# Generated by Django 4.2 on 2023-06-23 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new1', '0005_user1_imagess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='img/%y'),
        ),
    ]

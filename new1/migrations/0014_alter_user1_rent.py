# Generated by Django 4.2 on 2023-07-04 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new1', '0013_alter_user1_images1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user1',
            name='rent',
            field=models.IntegerField(),
        ),
    ]

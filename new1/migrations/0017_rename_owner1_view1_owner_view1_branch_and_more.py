# Generated by Django 4.2 on 2023-08-06 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new1', '0016_view1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='view1',
            old_name='owner1',
            new_name='owner',
        ),
        migrations.AddField(
            model_name='view1',
            name='branch',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='view1',
            name='ownername',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='view1',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='view1',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]

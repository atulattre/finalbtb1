# Generated by Django 4.2 on 2023-08-05 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new1', '0015_alter_user1_rent'),
    ]

    operations = [
        migrations.CreateModel(
            name='View1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner1', models.CharField(max_length=100)),
                ('rentp', models.CharField(max_length=100)),
                ('flatid', models.IntegerField()),
            ],
        ),
    ]

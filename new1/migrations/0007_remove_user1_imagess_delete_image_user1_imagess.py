# Generated by Django 4.2 on 2023-06-23 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new1', '0006_alter_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user1',
            name='imagess',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='user1',
            name='imagess',
            field=models.FileField(null=True, upload_to='files/'),
        ),
    ]

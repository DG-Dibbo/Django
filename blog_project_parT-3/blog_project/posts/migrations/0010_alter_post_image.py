# Generated by Django 5.1.7 on 2025-03-24 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_remove_post_photo_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/media/uploads/'),
        ),
    ]

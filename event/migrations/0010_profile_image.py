# Generated by Django 2.0.2 on 2018-03-21 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_remove_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='settings.MEDIA_ROOT/default_user.jpg', upload_to=''),
        ),
    ]

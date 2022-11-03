# Generated by Django 2.0.2 on 2018-03-05 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='wallet_balance',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='wallet_pin',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
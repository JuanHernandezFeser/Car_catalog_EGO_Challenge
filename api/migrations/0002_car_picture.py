# Generated by Django 5.0.3 on 2024-03-11 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='cars_pictures/'),
        ),
    ]

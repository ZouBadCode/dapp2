# Generated by Django 5.0 on 2024-12-04 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AD_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='uploaded_at',
            new_name='upload_at',
        ),
    ]

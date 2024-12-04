# Generated by Django 5.0 on 2024-12-04 14:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AD_api', '0003_remove_video_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='picture/')),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
        ),
    ]
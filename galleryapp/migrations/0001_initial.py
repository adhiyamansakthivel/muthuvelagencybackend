# Generated by Django 4.2.3 on 2023-08-04 03:27

from django.db import migrations, models
import galleryapp.models
import galleryapp.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(upload_to=galleryapp.models.RandomFileName('gallery'), validators=[galleryapp.validators.validate_file_size])),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Gallery',
            },
        ),
    ]

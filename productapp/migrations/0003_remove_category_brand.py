# Generated by Django 4.2.3 on 2023-07-29 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0002_remove_brand_category_category_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='brand',
        ),
    ]
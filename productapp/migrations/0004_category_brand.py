# Generated by Django 4.2.3 on 2023-07-29 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0003_remove_category_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='brand',
            field=models.ManyToManyField(blank=True, related_name='Category', to='productapp.brand'),
        ),
    ]
# Generated by Django 5.0.6 on 2024-07-07 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0004_rename_image_subcategory_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='images',
            new_name='image',
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-07 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0003_alter_products_specification_alter_subcategory_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='image',
            new_name='images',
        ),
    ]

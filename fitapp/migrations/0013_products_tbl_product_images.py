# Generated by Django 4.2.1 on 2023-06-21 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0012_alter_memberregistration_tbl_package_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='products_tbl',
            name='product_images',
            field=models.FileField(null=True, upload_to='media'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-28 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0020_scheduletime_tbl_trainer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduletime_tbl',
            name='StarTime',
        ),
        migrations.AddField(
            model_name='scheduletime_tbl',
            name='StartTime',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='scheduletime_tbl',
            name='EndTime',
            field=models.TimeField(null=True),
        ),
    ]
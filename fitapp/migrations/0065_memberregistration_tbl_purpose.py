# Generated by Django 4.2.1 on 2023-08-02 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0064_remove_workoutlist_tbl_membername'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberregistration_tbl',
            name='purpose',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

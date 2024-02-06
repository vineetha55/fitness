# Generated by Django 4.2.1 on 2023-06-12 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_Name', models.CharField(max_length=20, null=True)),
                ('doctor_Email', models.EmailField(max_length=20, null=True)),
                ('doctor_Contact', models.IntegerField(max_length=20, null=True)),
                ('doctor_Gender', models.CharField(max_length=10, null=True)),
                ('doctor_id_proof', models.CharField(max_length=30, null=True)),
                ('doctor_qualification', models.DateField(max_length=10, null=True)),
                ('doctor_experience', models.IntegerField(max_length=20, null=True)),
                ('doctor_Password', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
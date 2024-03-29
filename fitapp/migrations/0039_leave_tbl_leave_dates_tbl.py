# Generated by Django 4.2.1 on 2023-07-17 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0038_alter_memberbooking_tbl_memberid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave_Tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_name', models.CharField(max_length=100, null=True)),
                ('trainer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitapp.trainer_tbl')),
            ],
        ),
        migrations.CreateModel(
            name='leave_dates_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates', models.DateField(null=True)),
                ('leave_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitapp.leave_tbl')),
                ('trainer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitapp.trainer_tbl')),
            ],
        ),
    ]

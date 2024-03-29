# Generated by Django 4.2.1 on 2023-07-19 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0039_leave_tbl_leave_dates_tbl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leave_dates_tbl',
            name='trainer_id',
        ),
        migrations.CreateModel(
            name='workoutlist_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membername', models.CharField(max_length=100, null=True)),
                ('wrktype', models.CharField(max_length=100, null=True)),
                ('week', models.CharField(max_length=100, null=True)),
                ('excname', models.CharField(max_length=100, null=True)),
                ('reps', models.IntegerField(null=True)),
                ('sets', models.IntegerField(null=True)),
                ('memberid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitapp.memberregistration_tbl')),
            ],
        ),
        migrations.CreateModel(
            name='TrainerSalary_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_Name', models.CharField(max_length=100, null=True)),
                ('month', models.CharField(max_length=100, null=True)),
                ('total_leave', models.IntegerField(null=True)),
                ('total_working_days', models.IntegerField(null=True)),
                ('basic_pay', models.IntegerField(null=True)),
                ('total_salary', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('trainer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitapp.trainer_tbl')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorSalary_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_Name', models.CharField(max_length=100, null=True)),
                ('month', models.CharField(max_length=100, null=True)),
                ('total_leave', models.IntegerField(null=True)),
                ('total_working_days', models.IntegerField(null=True)),
                ('basic_pay', models.IntegerField(null=True)),
                ('total_salary', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('doctor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitapp.trainer_tbl')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor_Leave_Tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_Name', models.CharField(max_length=100, null=True)),
                ('doctor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitapp.doctor_tbl')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor_leave_dates_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates', models.DateField(null=True)),
                ('leave_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitapp.doctor_leave_tbl')),
            ],
        ),
    ]

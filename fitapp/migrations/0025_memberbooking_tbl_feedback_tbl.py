# Generated by Django 4.2.1 on 2023-07-11 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0024_viewcart_tbl'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberBooking_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full', models.CharField(max_length=20, null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=20, null=True)),
                ('country', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=20, null=True)),
                ('house', models.CharField(max_length=20, null=True)),
                ('road', models.CharField(max_length=20, null=True)),
                ('state', models.CharField(max_length=20, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('pincode', models.CharField(max_length=20, null=True)),
                ('near', models.CharField(max_length=20, null=True)),
                ('con_name', models.CharField(max_length=20, null=True)),
                ('con_mob', models.IntegerField(null=True)),
                ('del_add', models.CharField(max_length=20, null=True)),
                ('build', models.CharField(max_length=20, null=True)),
                ('area', models.CharField(max_length=20, null=True)),
                ('states', models.CharField(max_length=20, null=True)),
                ('town', models.CharField(max_length=20, null=True)),
                ('code', models.CharField(max_length=20, null=True)),
                ('place', models.CharField(max_length=20, null=True)),
                ('product_totalprice', models.IntegerField(null=True)),
                ('product_delivery_charge', models.IntegerField(null=True)),
                ('pay', models.IntegerField(null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('time', models.TimeField(auto_now_add=True, null=True)),
                ('memberid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitapp.products_tbl')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, null=True)),
                ('Email', models.EmailField(max_length=30, null=True)),
                ('Message', models.CharField(max_length=300, null=True)),
                ('star1', models.CharField(max_length=300, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitapp.memberregistration_tbl')),
            ],
        ),
    ]
# Generated by Django 4.2.1 on 2023-08-07 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0069_regpayment_tbl_paid_amount_monthlyfeepayment_tbl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monthlyfeepayment_tbl',
            old_name='reg_payment_id',
            new_name='reg_payment',
        ),
    ]
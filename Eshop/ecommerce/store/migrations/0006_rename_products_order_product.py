# Generated by Django 4.1 on 2022-09-05 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_order_landmark_remove_order_pincode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='products',
            new_name='product',
        ),
    ]
# Generated by Django 4.1 on 2022-09-05 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_products_order_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
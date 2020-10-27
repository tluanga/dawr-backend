# Generated by Django 3.0 on 2020-10-27 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0010_auto_20201027_0721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='date',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='total_amount',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='total_discount',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='total_tax',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='warehouse',
        ),
        migrations.RemoveField(
            model_name='purchaseorderitem',
            name='active',
        ),
        migrations.RemoveField(
            model_name='purchaseorderitem',
            name='bulk',
        ),
        migrations.RemoveField(
            model_name='purchaseorderitem',
            name='cost_price',
        ),
        migrations.RemoveField(
            model_name='purchaseorderitem',
            name='cost_price_bulk',
        ),
        migrations.RemoveField(
            model_name='purchaseorderitem',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='purchaseorderitem',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='purchaseorderitem',
            name='sell_price',
        ),
        migrations.RemoveField(
            model_name='purchaseorderitem',
            name='sell_price_bulk',
        ),
    ]
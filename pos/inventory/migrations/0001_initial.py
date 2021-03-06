# Generated by Django 3.0 on 2020-10-23 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('warehouse', '0001_initial'),
        ('product', '0014_auto_20201023_1611'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellItem',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('sell_rate', models.FloatField(null=True)),
                ('mrp', models.IntegerField()),
                ('cost_price', models.IntegerField()),
                ('gst_code', models.CharField(max_length=255)),
                ('gst_rate', models.FloatField()),
                ('amount', models.IntegerField()),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('discount', models.IntegerField()),
                ('quantity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('invoice_no', models.CharField(max_length=255)),
                ('customer_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('gst_no', models.CharField(max_length=255)),
                ('total_tax', models.FloatField()),
                ('total_discount', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('sell_item', models.ManyToManyField(blank=True, default=None, related_name='sell', to='inventory.SellItem')),
            ],
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('stock_type', models.CharField(choices=[('Box', 'box'), ('Bundle', 'bundle')], max_length=100)),
                ('bulkmode', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('current', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productstock', to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bulk', models.BooleanField(default=False)),
                ('buy_rate', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('quantity', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productpurchase', to='product.Product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productpurchase', to='supplier.Supplier')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productpurchase', to='warehouse.WareHouse')),
            ],
        ),
    ]

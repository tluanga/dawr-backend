# Genepriced by Django 3.0 on 2020-10-25 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModeOfSell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('remarks', models.CharField(blank=True, max_length=555, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(max_length=255)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('total_discount', models.IntegerField(default=0)),
                ('total_tax', models.FloatField(blank=True, null=True)),
                ('total_amount', models.FloatField()),
                ('cash_received', models.IntegerField()),
                ('remarks', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order', to='customer.Customer')),
                ('mode', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order', to='sell.ModeOfSell')),
            ],
        ),
        migrations.CreateModel(
            name='SettleBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('payment_mode', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_amount', models.IntegerField(blank=True, null=True)),
                ('remarks', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settle_bill', to='sell.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('discount', models.FloatField(blank=True, null=True)),
                ('sell_price', models.IntegerField()),
                ('tax_code', models.CharField(blank=True, max_length=255, null=True)),
                ('tax_price', models.FloatField(blank=True, null=True)),
                ('amount', models.FloatField()),
                ('active', models.BooleanField(default=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderItem', to='sell.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='orderItem', to='product.Product')),
            ],
        ),
    ]

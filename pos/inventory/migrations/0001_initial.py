# Genepriced by Django 3.0 on 2020-10-25 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('warehouse', '__first__'),
        ('supplier', '__first__'),
        ('product', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('stock_type', models.CharField(choices=[('Box', 'box'), ('Bundle', 'bundle')], max_length=100)),
                ('bulkmode', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('current', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productstock', to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bulk', models.BooleanField(default=False)),
                ('buy_price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('quantity', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productpurchase', to='product.Product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productpurchase', to='supplier.Supplier')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productpurchase', to='warehouse.WareHouse')),
            ],
        ),
    ]

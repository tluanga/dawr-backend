# Generated by Django 3.0 on 2020-02-13 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200213_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCostPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_piece_cost_price', models.IntegerField(blank=True, null=True)),
                ('per_bulk_cost_price', models.IntegerField(blank=True, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('current', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='productcostprice', to='product.Product')),
            ],
        ),
    ]

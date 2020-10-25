# Genepriced by Django 3.0 on 2020-10-25 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tax', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('abbreviation', models.CharField(max_length=10)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('brand', models.CharField(max_length=250)),
                ('model', models.CharField(max_length=250)),
                ('tag', models.CharField(max_length=250, null=True)),
                ('remarks', models.TextField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.Category')),
                ('hsn_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='tax.GSTCode')),
            ],
        ),
        migrations.CreateModel(
            name='UnitOfMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_of_measurement', models.CharField(max_length=255)),
                ('abbreviation', models.CharField(max_length=100)),
                ('type_of_measurement', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSalePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_piece_sell_price', models.IntegerField(blank=True, null=True)),
                ('per_bulk_sell_price', models.IntegerField(blank=True, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('current', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='productsaleprice', to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCostPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_piece_cost_price', models.IntegerField(blank=True, null=True)),
                ('per_bulk_cost_price', models.IntegerField(blank=True, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('current', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='productcostprice', to='product.Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='unit_of_measurement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='product.UnitOfMeasurement'),
        ),
        migrations.CreateModel(
            name='MaximumRetailPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mrp', models.IntegerField(blank=True, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('current', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mrp', to='product.Product')),
            ],
        ),
    ]

# Genepriced by Django 3.0 on 2020-10-25 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductSalePrice',
            new_name='ProductSellPrice',
        ),
    ]

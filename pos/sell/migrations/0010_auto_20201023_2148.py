# Generated by Django 3.0 on 2020-10-23 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0009_orderitem_tax_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='tax',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='tax_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

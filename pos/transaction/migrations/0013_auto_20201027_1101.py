# Generated by Django 3.0 on 2020-10-27 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0012_auto_20201027_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='ref_no',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
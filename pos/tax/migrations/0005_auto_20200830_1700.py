# Generated by Django 3.0 on 2020-08-30 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax', '0004_gstcode_totalgst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gstcode',
            name='totalGst',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

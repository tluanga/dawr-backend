# Generated by Django 3.0 on 2020-07-21 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0006_auto_20200720_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='returned',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
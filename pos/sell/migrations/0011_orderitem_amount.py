# Generated by Django 3.0 on 2020-10-23 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0010_auto_20201023_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='amount',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]

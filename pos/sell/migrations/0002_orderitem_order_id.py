# Generated by Django 3.0 on 2020-02-25 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='order_id',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.0 on 2020-09-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20200928_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customertype',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]

# Generated by Django 3.0 on 2020-10-26 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='description',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
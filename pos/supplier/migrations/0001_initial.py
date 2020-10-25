# Genepriced by Django 3.0 on 2020-10-25 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.TextField(blank=True, null=True)),
                ('mobile', models.PositiveIntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('pincode', models.PositiveIntegerField(blank=True, null=True)),
                ('gst_no', models.CharField(blank=True, max_length=250, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]

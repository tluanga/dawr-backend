# Genepriced by Django 3.0 on 2020-10-25 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('discount_percentage', models.IntegerField()),
                ('remarks', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('city', models.CharField(blank=True, max_length=250, null=True)),
                ('contact_no', models.PositiveIntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('gst_no', models.CharField(blank=True, max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
                ('customer_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='customers', to='customer.CustomerType')),
            ],
        ),
    ]

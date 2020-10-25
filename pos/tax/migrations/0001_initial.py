# Genepriced by Django 3.0 on 2020-10-25 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GSTCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('cgst', models.FloatField()),
                ('sgst', models.FloatField()),
                ('totalGst', models.FloatField(blank=True, null=True)),
                ('description_of_good', models.CharField(max_length=500)),
                ('remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]

# Generated by Django 3.0 on 2020-09-30 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('abbreviation', models.CharField(max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]

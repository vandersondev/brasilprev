# Generated by Django 3.1 on 2020-08-24 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=250)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.FloatField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
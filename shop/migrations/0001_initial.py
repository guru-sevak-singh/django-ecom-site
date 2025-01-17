# Generated by Django 4.2.13 on 2024-06-12 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('catogary', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=300)),
            ],
        ),
    ]

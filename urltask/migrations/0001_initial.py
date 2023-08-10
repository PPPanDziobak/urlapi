# Generated by Django 4.2.4 on 2023-08-09 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_url', models.URLField(max_length=300)),
                ('output_url', models.URLField(blank=True, max_length=300, unique=True)),
            ],
        ),
    ]

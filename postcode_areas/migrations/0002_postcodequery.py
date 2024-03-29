# Generated by Django 4.1.3 on 2023-02-16 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postcode_areas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostcodeQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.IntegerField()),
                ('queried_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Postcode Query',
                'verbose_name_plural': 'Postcode Queries',
                'db_table': 'postcode_queries',
            },
        ),
    ]

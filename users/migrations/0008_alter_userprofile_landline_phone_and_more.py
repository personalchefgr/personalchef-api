# Generated by Django 4.1.3 on 2022-12-19 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_userprofile_landline_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='landline_phone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile_phone',
            field=models.CharField(max_length=15),
        ),
    ]

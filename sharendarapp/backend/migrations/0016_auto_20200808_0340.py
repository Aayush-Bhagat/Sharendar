# Generated by Django 2.2 on 2020-08-08 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_auto_20200808_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='contact1',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='contact2',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='contact3',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='contact4',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-20 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20211020_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='user',
        ),
        migrations.AddField(
            model_name='appointments',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='appointments',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='appointments',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

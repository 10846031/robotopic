# Generated by Django 3.2 on 2022-05-08 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='accounts',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

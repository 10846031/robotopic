# Generated by Django 3.2 on 2022-05-13 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_user_identity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['last_name', 'first_name']},
        ),
    ]

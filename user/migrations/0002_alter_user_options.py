# Generated by Django 4.2.5 on 2023-09-20 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['surname']},
        ),
    ]

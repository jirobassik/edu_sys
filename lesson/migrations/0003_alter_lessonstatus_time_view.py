# Generated by Django 4.2.5 on 2023-09-20 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_alter_lesson_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonstatus',
            name='time_view',
            field=models.PositiveBigIntegerField(default=0, verbose_name='View time'),
        ),
    ]

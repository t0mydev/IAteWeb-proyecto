# Generated by Django 4.1.3 on 2022-11-20 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_datosnuevos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datosnuevos',
            old_name='datoimp',
            new_name='submission',
        ),
    ]
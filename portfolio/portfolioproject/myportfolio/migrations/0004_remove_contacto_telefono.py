# Generated by Django 4.2.13 on 2024-06-11 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0003_contacto_telefono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='telefono',
        ),
    ]

# Generated by Django 4.1 on 2022-10-31 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('rut', 'first_name', 'last_name'), 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
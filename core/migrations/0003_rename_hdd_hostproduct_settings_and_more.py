# Generated by Django 4.0.4 on 2022-04-21 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_aboutus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostproduct',
            old_name='hdd',
            new_name='settings',
        ),
        migrations.RemoveField(
            model_name='hostproduct',
            name='data',
        ),
        migrations.RemoveField(
            model_name='hostproduct',
            name='panel',
        ),
        migrations.RemoveField(
            model_name='hostproduct',
            name='support',
        ),
        migrations.RemoveField(
            model_name='hostproduct',
            name='theme',
        ),
    ]

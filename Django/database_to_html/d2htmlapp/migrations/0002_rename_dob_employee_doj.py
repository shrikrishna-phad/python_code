# Generated by Django 3.2.8 on 2021-11-13 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('d2htmlapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='dob',
            new_name='doj',
        ),
    ]
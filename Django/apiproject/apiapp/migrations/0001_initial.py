# Generated by Django 3.2.9 on 2021-12-14 08:31

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('E_id', models.IntegerField(primary_key=True, serialize=False)),
                ('E_Name', models.CharField(blank=True, max_length=225)),
                ('E_Address', models.CharField(blank=True, max_length=225)),
                ('E_Mobile', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeModel2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('E_Salary', models.IntegerField(blank=True)),
                ('E_Position', models.CharField(blank=True, max_length=225)),
                ('E_Department', models.CharField(blank=True, max_length=225)),
                ('E_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiapp.employeemodel')),
            ],
        ),
    ]

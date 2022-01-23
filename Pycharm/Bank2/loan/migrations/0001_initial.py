# Generated by Django 3.2.8 on 2021-11-19 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('middle_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('mobile_no', models.BigIntegerField()),
                ('loan_amount', models.IntegerField()),
                ('ref_no', models.BigIntegerField()),
                ('type_loan', models.CharField(max_length=5)),
                ('condition', models.CharField(help_text='used/new', max_length=4)),
                ('car_brand', models.CharField(max_length=10)),
                ('car_model', models.CharField(max_length=10)),
                ('city_home', models.CharField(max_length=15)),
                ('address_home', models.CharField(max_length=50)),
                ('type_business', models.CharField(max_length=10)),
                ('city_business', models.CharField(max_length=15)),
            ],
        ),
    ]

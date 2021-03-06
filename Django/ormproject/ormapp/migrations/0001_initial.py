# Generated by Django 3.2.8 on 2021-11-25 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.IntegerField(unique=True)),
                ('stu_name', models.CharField(max_length=50)),
                ('stu_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('stu_stream', models.CharField(choices=[('Mech', 'Mechanical'), ('IT', 'Information & Technology'), ('CSE', 'Computer Science'), ('EnT', 'Electronics & Telecommunication')], max_length=5)),
                ('stu_avgmarks', models.FloatField()),
            ],
        ),
    ]

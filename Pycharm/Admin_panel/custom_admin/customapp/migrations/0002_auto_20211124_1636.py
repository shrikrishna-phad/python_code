# Generated by Django 3.2.9 on 2021-11-24 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('customadminmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='customapp.customadminmodel')),
            ],
            bases=('customapp.customadminmodel', models.Model),
        ),
        migrations.AddField(
            model_name='customadminmodel',
            name='query1',
            field=models.TextField(default=1, help_text='Write your Query here'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.1 on 2020-01-08 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Need_Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_1', models.CharField(max_length=75)),
                ('location_2', models.CharField(max_length=75)),
                ('city', models.CharField(max_length=35)),
                ('state', models.CharField(max_length=35)),
                ('rent', models.FloatField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Have_Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=75)),
                ('city', models.CharField(max_length=35)),
                ('state', models.CharField(max_length=35)),
                ('rent', models.FloatField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Profile')),
            ],
        ),
    ]

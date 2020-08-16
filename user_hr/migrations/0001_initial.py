# Generated by Django 3.0.7 on 2020-07-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=2)),
                ('department', models.CharField(max_length=25)),
                ('mail', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]

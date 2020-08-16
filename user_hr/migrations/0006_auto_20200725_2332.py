# Generated by Django 3.0.7 on 2020-07-25 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_hr', '0005_auto_20200725_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='name',
            new_name='first',
        ),
        migrations.AddField(
            model_name='employee',
            name='last',
            field=models.CharField(default=-1.0, max_length=20),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='HrCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_hr.Employee')),
            ],
        ),
    ]
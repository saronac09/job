# Generated by Django 4.0.5 on 2022-09-19 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=50),
        ),
    ]

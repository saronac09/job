# Generated by Django 4.0.5 on 2022-09-27 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_requestform'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestform',
            name='salary',
            field=models.TextField(default='Null'),
        ),
    ]

# Generated by Django 3.0.3 on 2020-05-24 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_auto_20200524_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='p_payment',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

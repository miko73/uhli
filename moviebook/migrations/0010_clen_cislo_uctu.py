# Generated by Django 2.0.4 on 2020-10-06 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviebook', '0009_auto_20201002_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='clen',
            name='cislo_uctu',
            field=models.CharField(default='', max_length=30, unique=True),
        ),
    ]
# Generated by Django 2.0.4 on 2020-10-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviebook', '0011_auto_20201006_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akce',
            name='datum_konani',
            field=models.DateTimeField(),
        ),
    ]

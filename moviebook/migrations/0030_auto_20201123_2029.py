# Generated by Django 3.1.3 on 2020-11-23 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviebook', '0029_auto_20201123_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clen',
            name='klub_id',
            field=models.IntegerField(default=10),
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-10 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviebook', '0034_prichozi_platby_facr_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clen',
            name='narozen',
        ),
    ]
# Generated by Django 2.0.4 on 2020-10-06 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviebook', '0013_akce_vedouci'),
    ]

    operations = [
        migrations.AddField(
            model_name='akce',
            name='trener',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trenerp', to='moviebook.Clen', verbose_name='trener'),
        ),
    ]

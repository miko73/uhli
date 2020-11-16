# Generated by Django 2.0.4 on 2020-10-02 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviebook', '0008_ucastnici'),
    ]

    operations = [
        migrations.AddField(
            model_name='akce',
            name='trener',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trenerp', to='moviebook.Clen', verbose_name='trener'),
        ),
        migrations.AddField(
            model_name='akce',
            name='vedouci',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vedoucip', to='moviebook.Clen', verbose_name='Vedouci'),
        ),
        migrations.AlterField(
            model_name='ucastnici',
            name='akce',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='moviebook.Akce', verbose_name='Akce'),
        ),
        migrations.AlterField(
            model_name='ucastnici',
            name='clen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='moviebook.Clen', verbose_name='Clen'),
        ),
    ]
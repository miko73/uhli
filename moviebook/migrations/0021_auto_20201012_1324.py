# Generated by Django 2.0.4 on 2020-10-12 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviebook', '0020_clen_prijmeni_rodic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Naplanovane_platby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('splatnost', models.DateField()),
                ('objem', models.FloatField()),
                ('popis_platby', models.CharField(default='', max_length=160)),
                ('sdelelni', models.CharField(default='', max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='Prichozi_platby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateField()),
                ('objem', models.FloatField()),
                ('protiucet', models.CharField(default='', max_length=100)),
                ('kod_banky', models.CharField(default='', max_length=6)),
                ('zprava_pro_prijemce', models.CharField(default='', max_length=160)),
                ('poznamka', models.CharField(default='', max_length=160)),
                ('nazev_protiuctu', models.CharField(default='', max_length=100)),
                ('typ_platby', models.CharField(default='', max_length=2)),
                ('cislo_uctu_prichozi', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='clen',
            name='typ_clena',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='clen',
            name='ucet_kod_banky',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AddField(
            model_name='clen',
            name='ucet_nazev_protiuctu',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='clen',
            name='ucet_poznamka',
            field=models.CharField(default='', max_length=160),
        ),
        migrations.AddField(
            model_name='clen',
            name='ucet_protiucet',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='clen',
            name='ucet_zprava_pro_prijemce',
            field=models.CharField(default='', max_length=160),
        ),
        migrations.AlterField(
            model_name='clen',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='email',
            field=models.EmailField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='clen',
            name='rc',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='prichozi_platby',
            name='clen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clen_pp', to='moviebook.Clen', verbose_name='Člen'),
        ),
        migrations.AddField(
            model_name='naplanovane_platby',
            name='clen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clen_np', to='moviebook.Clen', verbose_name='Člen'),
        ),
        migrations.AddField(
            model_name='naplanovane_platby',
            name='sparovano',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parovani', to='moviebook.Prichozi_platby', verbose_name='Párování'),
        ),
        migrations.AddField(
            model_name='naplanovane_platby',
            name='trener',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trener', to='moviebook.Clen', verbose_name='Trenér'),
        ),
    ]
# Generated by Django 3.1.3 on 2020-11-23 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviebook', '0025_clen_ucet_protiucet2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clen',
            name='active',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='cislo_uctu',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='clenem_od',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='facr_id',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='jmeno',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='klub_id',
            field=models.IntegerField(blank=True, default=1050181, null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='narozen',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='prijmeni',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='prijmeni_rodic',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='rc',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='rok_narozeni',
            field=models.CharField(blank=True, default='2010', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='telefonni_cislo',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='typ_clena',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='ucet_kod_banky',
            field=models.CharField(blank=True, default='', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='ucet_nazev_protiuctu',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='ucet_poznamka',
            field=models.CharField(blank=True, default='', max_length=160, null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='ucet_protiucet',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='ucet_protiucet2',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='ucet_zprava_pro_prijemce',
            field=models.CharField(blank=True, default='', max_length=160, null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='var_symbol',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
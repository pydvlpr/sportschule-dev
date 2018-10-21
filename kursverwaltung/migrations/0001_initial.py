# Generated by Django 2.1.2 on 2018-10-20 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buchung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Kunde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nachname', models.CharField(max_length=100)),
                ('vorname', models.CharField(max_length=100)),
                ('strasse', models.CharField(max_length=100)),
                ('hausnummer', models.CharField(max_length=5)),
                ('plz', models.CharField(max_length=5)),
                ('stadt', models.CharField(max_length=100)),
                ('handy', models.CharField(max_length=30)),
                ('festnetz', models.CharField(max_length=30)),
                ('fax', models.CharField(max_length=30)),
                ('e_mail', models.EmailField(max_length=254)),
                ('ansprechpartner', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Kurs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('beschreibung', models.CharField(default=' ', max_length=32767)),
                ('anfangszeit', models.DateTimeField()),
                ('endzeit', models.DateTimeField()),
                ('teilnehmerzahl', models.IntegerField()),
                ('max_teilnehmer', models.IntegerField()),
                ('gebuehr', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'ordering': ['-id', '-anfangszeit'],
            },
        ),
        migrations.CreateModel(
            name='Raum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raum_nr', models.IntegerField()),
                ('gebaeude', models.CharField(max_length=100)),
                ('bemerkung', models.CharField(max_length=32767)),
                ('sitzplaetze', models.IntegerField()),
                ('ansprechpartner', models.CharField(max_length=100)),
                ('geraeteverantwortlicher', models.CharField(max_length=100)),
                ('strasse', models.CharField(max_length=100)),
                ('hausnummer', models.CharField(max_length=100)),
                ('stadt', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nachname', models.CharField(max_length=100)),
                ('vorname', models.CharField(max_length=100)),
                ('strasse', models.CharField(max_length=100)),
                ('hausnummer', models.CharField(max_length=5)),
                ('plz', models.CharField(max_length=5)),
                ('stadt', models.CharField(max_length=100)),
                ('handy', models.CharField(max_length=30)),
                ('festnetz', models.CharField(max_length=30)),
                ('fax', models.CharField(max_length=30)),
                ('e_mail', models.EmailField(max_length=254)),
                ('bemerkung', models.CharField(max_length=32767)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Zertifizierung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gueltig_bis', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='trainer',
            name='zertifizierung',
            field=models.ManyToManyField(to='kursverwaltung.Zertifizierung'),
        ),
        migrations.AddField(
            model_name='kurs',
            name='raum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kursverwaltung.Raum'),
        ),
        migrations.AddField(
            model_name='kurs',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kursverwaltung.Trainer'),
        ),
    ]
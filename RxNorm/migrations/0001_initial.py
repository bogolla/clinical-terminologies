# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rxnatomarchive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rxaui', models.CharField(max_length=8, db_column='RXAUI')),
                ('aui', models.CharField(max_length=10, null=True, db_column='AUI', blank=True)),
                ('str', models.CharField(max_length=4000, db_column='STR')),
                ('archive_timestamp', models.CharField(max_length=280, db_column='ARCHIVE_TIMESTAMP')),
                ('created_timestamp', models.CharField(max_length=280, db_column='CREATED_TIMESTAMP')),
                ('updated_timestamp', models.CharField(max_length=280, db_column='UPDATED_TIMESTAMP')),
                ('code', models.CharField(max_length=50, null=True, db_column='CODE', blank=True)),
                ('is_brand', models.CharField(max_length=1, null=True, db_column='IS_BRAND', blank=True)),
                ('lat', models.CharField(max_length=3, null=True, db_column='LAT', blank=True)),
                ('last_released', models.CharField(max_length=30, null=True, db_column='LAST_RELEASED', blank=True)),
                ('saui', models.CharField(max_length=50, null=True, db_column='SAUI', blank=True)),
                ('vsab', models.CharField(max_length=40, null=True, db_column='VSAB', blank=True)),
                ('rxcui', models.CharField(max_length=8, null=True, db_column='RXCUI', blank=True)),
                ('sab', models.CharField(max_length=20, null=True, db_column='SAB', blank=True)),
                ('tty', models.CharField(max_length=20, null=True, db_column='TTY', blank=True)),
                ('merged_to_rxcui', models.CharField(max_length=8, null=True, db_column='MERGED_TO_RXCUI', blank=True)),
            ],
            options={
                'db_table': 'RXNATOMARCHIVE',
            },
        ),
        migrations.CreateModel(
            name='Rxnconso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rxcui', models.CharField(max_length=8, db_column='RXCUI')),
                ('lat', models.CharField(max_length=3, db_column='LAT')),
                ('ts', models.CharField(max_length=1, null=True, db_column='TS', blank=True)),
                ('lui', models.CharField(max_length=8, null=True, db_column='LUI', blank=True)),
                ('stt', models.CharField(max_length=3, null=True, db_column='STT', blank=True)),
                ('sui', models.CharField(max_length=8, null=True, db_column='SUI', blank=True)),
                ('ispref', models.CharField(max_length=1, null=True, db_column='ISPREF', blank=True)),
                ('rxaui', models.CharField(max_length=8, db_column='RXAUI')),
                ('saui', models.CharField(max_length=50, null=True, db_column='SAUI', blank=True)),
                ('scui', models.CharField(max_length=50, null=True, db_column='SCUI', blank=True)),
                ('sdui', models.CharField(max_length=50, null=True, db_column='SDUI', blank=True)),
                ('sab', models.CharField(max_length=20, db_column='SAB')),
                ('tty', models.CharField(max_length=20, db_column='TTY')),
                ('code', models.CharField(max_length=50, db_column='CODE')),
                ('str', models.CharField(max_length=3000, db_column='STR')),
                ('srl', models.CharField(max_length=10, null=True, db_column='SRL', blank=True)),
                ('suppress', models.CharField(max_length=1, null=True, db_column='SUPPRESS', blank=True)),
                ('cvf', models.CharField(max_length=50, null=True, db_column='CVF', blank=True)),
            ],
            options={
                'db_table': 'RXNCONSO',
            },
        ),
        migrations.CreateModel(
            name='Rxncui',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cui1', models.CharField(max_length=8, null=True, blank=True)),
                ('ver_start', models.CharField(max_length=40, null=True, blank=True)),
                ('ver_end', models.CharField(max_length=40, null=True, blank=True)),
                ('cardinality', models.CharField(max_length=8, null=True, blank=True)),
                ('cui2', models.CharField(max_length=8, null=True, blank=True)),
            ],
            options={
                'db_table': 'RXNCUI',
            },
        ),
        migrations.CreateModel(
            name='Rxncuichanges',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rxaui', models.CharField(max_length=8, null=True, db_column='RXAUI', blank=True)),
                ('code', models.CharField(max_length=50, null=True, db_column='CODE', blank=True)),
                ('sab', models.CharField(max_length=20, null=True, db_column='SAB', blank=True)),
                ('tty', models.CharField(max_length=20, null=True, db_column='TTY', blank=True)),
                ('str', models.CharField(max_length=3000, null=True, db_column='STR', blank=True)),
                ('old_rxcui', models.CharField(max_length=8, db_column='OLD_RXCUI')),
                ('new_rxcui', models.CharField(max_length=8, db_column='NEW_RXCUI')),
            ],
            options={
                'db_table': 'RXNCUICHANGES',
            },
        ),
        migrations.CreateModel(
            name='Rxndoc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dockey', models.CharField(max_length=50, db_column='DOCKEY')),
                ('value', models.CharField(max_length=1000, null=True, db_column='VALUE', blank=True)),
                ('type', models.CharField(max_length=50, db_column='TYPE')),
                ('expl', models.CharField(max_length=1000, null=True, db_column='EXPL', blank=True)),
            ],
            options={
                'db_table': 'RXNDOC',
            },
        ),
        migrations.CreateModel(
            name='Rxnrel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rxcui1', models.CharField(max_length=8, null=True, db_column='RXCUI1', blank=True)),
                ('rxaui1', models.CharField(max_length=8, null=True, db_column='RXAUI1', blank=True)),
                ('stype1', models.CharField(max_length=50, null=True, db_column='STYPE1', blank=True)),
                ('rel', models.CharField(max_length=4, null=True, db_column='REL', blank=True)),
                ('rxcui2', models.CharField(max_length=8, null=True, db_column='RXCUI2', blank=True)),
                ('rxaui2', models.CharField(max_length=8, null=True, db_column='RXAUI2', blank=True)),
                ('stype2', models.CharField(max_length=50, null=True, db_column='STYPE2', blank=True)),
                ('rela', models.CharField(max_length=100, null=True, db_column='RELA', blank=True)),
                ('rui', models.CharField(max_length=10, null=True, db_column='RUI', blank=True)),
                ('srui', models.CharField(max_length=50, null=True, db_column='SRUI', blank=True)),
                ('sab', models.CharField(max_length=20, db_column='SAB')),
                ('sl', models.CharField(max_length=1000, null=True, db_column='SL', blank=True)),
                ('dir', models.CharField(max_length=1, null=True, db_column='DIR', blank=True)),
                ('rg', models.CharField(max_length=10, null=True, db_column='RG', blank=True)),
                ('suppress', models.CharField(max_length=1, null=True, db_column='SUPPRESS', blank=True)),
                ('cvf', models.CharField(max_length=50, null=True, db_column='CVF', blank=True)),
            ],
            options={
                'db_table': 'RXNREL',
            },
        ),
        migrations.CreateModel(
            name='Rxnsab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vcui', models.CharField(max_length=8, null=True, db_column='VCUI', blank=True)),
                ('rcui', models.CharField(max_length=8, null=True, db_column='RCUI', blank=True)),
                ('vsab', models.CharField(max_length=40, null=True, db_column='VSAB', blank=True)),
                ('rsab', models.CharField(max_length=20, db_column='RSAB')),
                ('son', models.CharField(max_length=3000, null=True, db_column='SON', blank=True)),
                ('sf', models.CharField(max_length=20, null=True, db_column='SF', blank=True)),
                ('sver', models.CharField(max_length=20, null=True, db_column='SVER', blank=True)),
                ('vstart', models.CharField(max_length=10, null=True, db_column='VSTART', blank=True)),
                ('vend', models.CharField(max_length=10, null=True, db_column='VEND', blank=True)),
                ('imeta', models.CharField(max_length=10, null=True, db_column='IMETA', blank=True)),
                ('rmeta', models.CharField(max_length=10, null=True, db_column='RMETA', blank=True)),
                ('slc', models.CharField(max_length=1000, null=True, db_column='SLC', blank=True)),
                ('scc', models.CharField(max_length=1000, null=True, db_column='SCC', blank=True)),
                ('srl', models.IntegerField(null=True, db_column='SRL', blank=True)),
                ('tfr', models.IntegerField(null=True, db_column='TFR', blank=True)),
                ('cfr', models.IntegerField(null=True, db_column='CFR', blank=True)),
                ('cxty', models.CharField(max_length=50, null=True, db_column='CXTY', blank=True)),
                ('ttyl', models.CharField(max_length=300, null=True, db_column='TTYL', blank=True)),
                ('atnl', models.CharField(max_length=1000, null=True, db_column='ATNL', blank=True)),
                ('lat', models.CharField(max_length=3, null=True, db_column='LAT', blank=True)),
                ('cenc', models.CharField(max_length=20, null=True, db_column='CENC', blank=True)),
                ('curver', models.CharField(max_length=1, null=True, db_column='CURVER', blank=True)),
                ('sabin', models.CharField(max_length=1, null=True, db_column='SABIN', blank=True)),
                ('ssn', models.CharField(max_length=3000, null=True, db_column='SSN', blank=True)),
                ('scit', models.CharField(max_length=4000, null=True, db_column='SCIT', blank=True)),
            ],
            options={
                'db_table': 'RXNSAB',
            },
        ),
        migrations.CreateModel(
            name='Rxnsat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rxcui', models.CharField(max_length=8, null=True, db_column='RXCUI', blank=True)),
                ('lui', models.CharField(max_length=8, null=True, db_column='LUI', blank=True)),
                ('sui', models.CharField(max_length=8, null=True, db_column='SUI', blank=True)),
                ('rxaui', models.CharField(max_length=8, null=True, db_column='RXAUI', blank=True)),
                ('stype', models.CharField(max_length=50, null=True, db_column='STYPE', blank=True)),
                ('code', models.CharField(max_length=50, null=True, db_column='CODE', blank=True)),
                ('atui', models.CharField(max_length=11, null=True, db_column='ATUI', blank=True)),
                ('satui', models.CharField(max_length=50, null=True, db_column='SATUI', blank=True)),
                ('atn', models.CharField(max_length=1000, db_column='ATN')),
                ('sab', models.CharField(max_length=20, db_column='SAB')),
                ('atv', models.CharField(max_length=4000, null=True, db_column='ATV', blank=True)),
                ('suppress', models.CharField(max_length=1, null=True, db_column='SUPPRESS', blank=True)),
                ('cvf', models.CharField(max_length=50, null=True, db_column='CVF', blank=True)),
            ],
            options={
                'db_table': 'RXNSAT',
            },
        ),
        migrations.CreateModel(
            name='Rxnsty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rxcui', models.CharField(max_length=8, db_column='RXCUI')),
                ('tui', models.CharField(max_length=4, null=True, db_column='TUI', blank=True)),
                ('stn', models.CharField(max_length=100, null=True, db_column='STN', blank=True)),
                ('sty', models.CharField(max_length=50, null=True, db_column='STY', blank=True)),
                ('atui', models.CharField(max_length=11, null=True, db_column='ATUI', blank=True)),
                ('cvf', models.CharField(max_length=50, null=True, db_column='CVF', blank=True)),
            ],
            options={
                'db_table': 'RXNSTY',
            },
        ),
    ]

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Rxnatomarchive(models.Model):
    rxaui = models.CharField(db_column='RXAUI', max_length=8)
    aui = models.CharField(db_column='AUI', max_length=10, blank=True, null=True)
    str = models.CharField(db_column='STR', max_length=4000)
    archive_timestamp = models.CharField(db_column='ARCHIVE_TIMESTAMP', max_length=280)
    created_timestamp = models.CharField(db_column='CREATED_TIMESTAMP', max_length=280)
    updated_timestamp = models.CharField(db_column='UPDATED_TIMESTAMP', max_length=280)
    code = models.CharField(db_column='CODE', max_length=50, blank=True, null=True)
    is_brand = models.CharField(db_column='IS_BRAND', max_length=1, blank=True, null=True)
    lat = models.CharField(db_column='LAT', max_length=3, blank=True, null=True)
    last_released = models.CharField(db_column='LAST_RELEASED', max_length=30, blank=True, null=True)
    saui = models.CharField(db_column='SAUI', max_length=50, blank=True, null=True)
    vsab = models.CharField(db_column='VSAB', max_length=40, blank=True, null=True)
    rxcui = models.CharField(db_column='RXCUI', max_length=8, blank=True, null=True)
    sab = models.CharField(db_column='SAB', max_length=20, blank=True, null=True)
    tty = models.CharField(db_column='TTY', max_length=20, blank=True, null=True)
    merged_to_rxcui = models.CharField(db_column='MERGED_TO_RXCUI', max_length=8, blank=True, null=True)

    class Meta:
        db_table = 'RXNATOMARCHIVE'


class Rxnconso(models.Model):
    rxcui = models.CharField(db_column='RXCUI', max_length=8)
    lat = models.CharField(db_column='LAT', max_length=3)
    ts = models.CharField(db_column='TS', max_length=1, blank=True, null=True)
    lui = models.CharField(db_column='LUI', max_length=8, blank=True, null=True)
    stt = models.CharField(db_column='STT', max_length=3, blank=True, null=True)
    sui = models.CharField(db_column='SUI', max_length=8, blank=True, null=True)
    ispref = models.CharField(db_column='ISPREF', max_length=1, blank=True, null=True)
    rxaui = models.CharField(db_column='RXAUI', max_length=8)
    saui = models.CharField(db_column='SAUI', max_length=50, blank=True, null=True)
    scui = models.CharField(db_column='SCUI', max_length=50, blank=True, null=True)
    sdui = models.CharField(db_column='SDUI', max_length=50, blank=True, null=True)
    sab = models.CharField(db_column='SAB', max_length=20)
    tty = models.CharField(db_column='TTY', max_length=20)
    code = models.CharField(db_column='CODE', max_length=50)
    str = models.CharField(db_column='STR', max_length=3000)
    srl = models.CharField(db_column='SRL', max_length=10, blank=True, null=True)
    suppress = models.CharField(db_column='SUPPRESS', max_length=1, blank=True, null=True)
    cvf = models.CharField(db_column='CVF', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'RXNCONSO'


class Rxncui(models.Model):
    cui1 = models.CharField(max_length=8, blank=True, null=True)
    ver_start = models.CharField(max_length=40, blank=True, null=True)
    ver_end = models.CharField(max_length=40, blank=True, null=True)
    cardinality = models.CharField(max_length=8, blank=True, null=True)
    cui2 = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        db_table = 'RXNCUI'


class Rxncuichanges(models.Model):
    rxaui = models.CharField(db_column='RXAUI', max_length=8, blank=True, null=True)
    code = models.CharField(db_column='CODE', max_length=50, blank=True, null=True)
    sab = models.CharField(db_column='SAB', max_length=20, blank=True, null=True)
    tty = models.CharField(db_column='TTY', max_length=20, blank=True, null=True)
    str = models.CharField(db_column='STR', max_length=3000, blank=True, null=True)
    old_rxcui = models.CharField(db_column='OLD_RXCUI', max_length=8)
    new_rxcui = models.CharField(db_column='NEW_RXCUI', max_length=8)

    class Meta:
        db_table = 'RXNCUICHANGES'


class Rxndoc(models.Model):
    dockey = models.CharField(db_column='DOCKEY', max_length=50)
    value = models.CharField(db_column='VALUE', max_length=1000, blank=True, null=True)
    type = models.CharField(db_column='TYPE', max_length=50)
    expl = models.CharField(db_column='EXPL', max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'RXNDOC'


class Rxnrel(models.Model):
    rxcui1 = models.CharField(db_column='RXCUI1', max_length=8, blank=True, null=True)
    rxaui1 = models.CharField(db_column='RXAUI1', max_length=8, blank=True, null=True)
    stype1 = models.CharField(db_column='STYPE1', max_length=50, blank=True, null=True)
    rel = models.CharField(db_column='REL', max_length=4, blank=True, null=True)
    rxcui2 = models.CharField(db_column='RXCUI2', max_length=8, blank=True, null=True)
    rxaui2 = models.CharField(db_column='RXAUI2', max_length=8, blank=True, null=True)
    stype2 = models.CharField(db_column='STYPE2', max_length=50, blank=True, null=True)
    rela = models.CharField(db_column='RELA', max_length=100, blank=True, null=True)
    rui = models.CharField(db_column='RUI', max_length=10, blank=True, null=True)
    srui = models.CharField(db_column='SRUI', max_length=50, blank=True, null=True)
    sab = models.CharField(db_column='SAB', max_length=20)
    sl = models.CharField(db_column='SL', max_length=1000, blank=True, null=True)
    dir = models.CharField(db_column='DIR', max_length=1, blank=True, null=True)
    rg = models.CharField(db_column='RG', max_length=10, blank=True, null=True)
    suppress = models.CharField(db_column='SUPPRESS', max_length=1, blank=True, null=True)
    cvf = models.CharField(db_column='CVF', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'RXNREL'


class Rxnsab(models.Model):
    vcui = models.CharField(db_column='VCUI', max_length=8, blank=True, null=True)
    rcui = models.CharField(db_column='RCUI', max_length=8, blank=True, null=True)
    vsab = models.CharField(db_column='VSAB', max_length=40, blank=True, null=True)
    rsab = models.CharField(db_column='RSAB', max_length=20)
    son = models.CharField(db_column='SON', max_length=3000, blank=True, null=True)
    sf = models.CharField(db_column='SF', max_length=20, blank=True, null=True)
    sver = models.CharField(db_column='SVER', max_length=20, blank=True, null=True)
    vstart = models.CharField(db_column='VSTART', max_length=10, blank=True, null=True)
    vend = models.CharField(db_column='VEND', max_length=10, blank=True, null=True)
    imeta = models.CharField(db_column='IMETA', max_length=10, blank=True, null=True)
    rmeta = models.CharField(db_column='RMETA', max_length=10, blank=True, null=True)
    slc = models.CharField(db_column='SLC', max_length=1000, blank=True, null=True)
    scc = models.CharField(db_column='SCC', max_length=1000, blank=True, null=True)
    srl = models.IntegerField(db_column='SRL', blank=True, null=True)
    tfr = models.IntegerField(db_column='TFR', blank=True, null=True)
    cfr = models.IntegerField(db_column='CFR', blank=True, null=True)
    cxty = models.CharField(db_column='CXTY', max_length=50, blank=True, null=True)
    ttyl = models.CharField(db_column='TTYL', max_length=300, blank=True, null=True)
    atnl = models.CharField(db_column='ATNL', max_length=1000, blank=True, null=True)
    lat = models.CharField(db_column='LAT', max_length=3, blank=True, null=True)
    cenc = models.CharField(db_column='CENC', max_length=20, blank=True, null=True)
    curver = models.CharField(db_column='CURVER', max_length=1, blank=True, null=True)
    sabin = models.CharField(db_column='SABIN', max_length=1, blank=True, null=True)
    ssn = models.CharField(db_column='SSN', max_length=3000, blank=True, null=True)
    scit = models.CharField(db_column='SCIT', max_length=4000, blank=True, null=True)

    class Meta:
        db_table = 'RXNSAB'


class Rxnsat(models.Model):
    rxcui = models.CharField(db_column='RXCUI', max_length=8, blank=True, null=True)
    lui = models.CharField(db_column='LUI', max_length=8, blank=True, null=True)
    sui = models.CharField(db_column='SUI', max_length=8, blank=True, null=True)
    rxaui = models.CharField(db_column='RXAUI', max_length=8, blank=True, null=True)
    stype = models.CharField(db_column='STYPE', max_length=50, blank=True, null=True)
    code = models.CharField(db_column='CODE', max_length=50, blank=True, null=True)
    atui = models.CharField(db_column='ATUI', max_length=11, blank=True, null=True)
    satui = models.CharField(db_column='SATUI', max_length=50, blank=True, null=True)
    atn = models.CharField(db_column='ATN', max_length=1000)
    sab = models.CharField(db_column='SAB', max_length=20)
    atv = models.CharField(db_column='ATV', max_length=4000, blank=True, null=True)
    suppress = models.CharField(db_column='SUPPRESS', max_length=1, blank=True, null=True)
    cvf = models.CharField(db_column='CVF', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'RXNSAT'


class Rxnsty(models.Model):
    rxcui = models.CharField(db_column='RXCUI', max_length=8)
    tui = models.CharField(db_column='TUI', max_length=4, blank=True, null=True)
    stn = models.CharField(db_column='STN', max_length=100, blank=True, null=True)
    sty = models.CharField(db_column='STY', max_length=50, blank=True, null=True)
    atui = models.CharField(db_column='ATUI', max_length=11, blank=True, null=True)
    cvf = models.CharField(db_column='CVF', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'RXNSTY'

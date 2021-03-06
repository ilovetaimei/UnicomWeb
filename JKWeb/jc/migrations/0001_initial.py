# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-15 06:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jc.util


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bigbusiness',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, null=True)),
                ('type', models.CharField(max_length=50, null=True)),
                ('linkman', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'bigbusiness',
            },
        ),
        migrations.CreateModel(
            name='bueqlink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('businessid', models.IntegerField(null=True)),
                ('type', models.CharField(max_length=50, null=True)),
                ('mainstartid', models.IntegerField(null=True)),
                ('mainstopid', models.IntegerField(null=True)),
                ('ordernumer', models.IntegerField(null=True)),
                ('currenteqid', models.IntegerField(null=True)),
                ('portid', models.IntegerField(null=True)),
                ('upeqid', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'bueqlink',
            },
        ),
        migrations.CreateModel(
            name='businessression',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('businessid', models.IntegerField(null=True)),
                ('type', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'businessression',
            },
        ),
        migrations.CreateModel(
            name='cabinet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'cabinet',
            },
        ),
        migrations.CreateModel(
            name='equipment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, null=True)),
                ('type', models.CharField(max_length=50, null=True)),
                ('brand', models.CharField(max_length=50, null=True)),
                ('model', models.CharField(max_length=50, null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('superpassword', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=80, null=True)),
                ('role', models.CharField(max_length=50, null=True)),
                ('loginmode', models.CharField(max_length=50, null=True)),
                ('edition', models.CharField(max_length=50, null=True)),
                ('wbstopdate', models.DateTimeField(null=True)),
                ('personliable', models.CharField(max_length=50, null=True)),
                ('liablephone', models.CharField(max_length=50, null=True)),
                ('buytime', models.DateTimeField(null=True)),
                ('serialnumber', models.CharField(max_length=80, null=True)),
                ('tradename', models.CharField(max_length=50, null=True)),
                ('startusetime', models.DateTimeField(null=True)),
                ('purpose', models.CharField(max_length=50, null=True)),
                ('wbcs', models.CharField(max_length=50, null=True)),
                ('wbstart', models.DateTimeField(null=True)),
                ('ip', models.CharField(max_length=100, null=True)),
                ('os', models.CharField(max_length=50, null=True)),
                ('bitsize', models.CharField(max_length=50, null=True)),
                ('hostname', models.CharField(max_length=50, null=True)),
                ('totalmemory', models.CharField(max_length=50, null=True)),
                ('totaldisk', models.CharField(max_length=50, null=True)),
                ('cabinetid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jc.cabinet')),
            ],
            options={
                'db_table': 'equipment',
            },
        ),
        migrations.CreateModel(
            name='grouper',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('fathergroup', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'grouper',
            },
        ),
        migrations.CreateModel(
            name='hostmonitoring',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cpuavailability', models.CharField(max_length=50, null=True)),
                ('ramavailability', models.CharField(max_length=50, null=True)),
                ('cardstatu', models.CharField(max_length=50, null=True)),
                ('monitoringtime', models.DateTimeField(null=True)),
                ('equipmentstatu', models.CharField(max_length=50, null=True)),
                ('diskspaceavailability', jc.util.JsonField()),
                ('netdelay', models.CharField(max_length=50, null=True)),
                ('netcardtraffic', jc.util.JsonField()),
                ('diskio', jc.util.JsonField()),
                ('equipmentid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jc.equipment')),
            ],
            options={
                'db_table': 'hostmonitoring',
            },
        ),
        migrations.CreateModel(
            name='motorroom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, null=True)),
                ('layoutmap', models.CharField(max_length=80, null=True)),
            ],
            options={
                'db_table': 'motorroom',
            },
        ),
        migrations.CreateModel(
            name='netreportforms',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('avgportflow', models.CharField(max_length=20, null=True)),
                ('peakvalueportflow', models.CharField(max_length=20, null=True)),
                ('avgportuse', models.FloatField(max_length=20, null=True)),
                ('peakvalueportuse', models.FloatField(max_length=20, null=True)),
                ('reportfromscycle', models.CharField(max_length=50, null=True)),
                ('reportfromtime', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'netreportforms',
            },
        ),
        migrations.CreateModel(
            name='networkdevicemonitor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('portid', models.IntegerField(null=True)),
                ('portstatu', models.CharField(max_length=20, null=True)),
                ('linkbandwidth', models.CharField(max_length=50, null=True)),
                ('avgdelay', models.FloatField(max_length=20, null=True)),
                ('packetloss', models.CharField(max_length=20, null=True)),
                ('portavguse', models.CharField(max_length=20, null=True)),
                ('portpeakvalueuse', models.CharField(max_length=20, null=True)),
                ('netdelay', models.FloatField(max_length=20, null=True)),
                ('rateout', models.CharField(max_length=50, null=True)),
                ('ratein', models.CharField(max_length=50, null=True)),
                ('portdescribe', models.CharField(max_length=200, null=True)),
                ('equipmentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jc.equipment')),
            ],
            options={
                'db_table': 'networkdevicemonitor',
            },
        ),
        migrations.CreateModel(
            name='schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('timeregexp', models.CharField(max_length=80, null=True)),
                ('taskidlist', models.IntegerField(null=True)),
                ('statu', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'schedule',
            },
        ),
        migrations.CreateModel(
            name='smallbusiness',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, null=True)),
                ('type', models.CharField(max_length=50, null=True)),
                ('linkman', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('whetherbusiness', models.CharField(max_length=50, null=True)),
                ('branch', models.IntegerField(null=True)),
                ('fatherbusiness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jc.bigbusiness')),
            ],
            options={
                'db_table': 'smallbusiness',
            },
        ),
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, null=True)),
                ('target', models.CharField(max_length=50, null=True)),
                ('whetherdispatch', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='taskexecute',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('excuteresult', models.CharField(max_length=50, null=True)),
                ('excutetime', models.DateTimeField(null=True)),
                ('usetime', models.FloatField(max_length=20, null=True)),
                ('scheduleid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jc.schedule')),
                ('taskid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jc.task')),
            ],
            options={
                'db_table': 'taskexecute',
            },
        ),
        migrations.CreateModel(
            name='warninglog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('linkman', models.CharField(max_length=80, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('correlationeq', models.IntegerField(null=True)),
                ('correlationport', models.IntegerField(null=True)),
                ('correlationtask', models.IntegerField(null=True)),
                ('faultdescription', models.CharField(max_length=200, null=True)),
                ('urgency', models.CharField(max_length=100, null=True)),
                ('date', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'warninglog',
            },
        ),
        migrations.CreateModel(
            name='warningthreshold',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50, null=True)),
                ('target', models.CharField(max_length=50, null=True)),
                ('number', models.CharField(max_length=50, null=True)),
                ('groupid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jc.grouper')),
            ],
            options={
                'db_table': 'warningthreshold',
            },
        ),
        migrations.AddField(
            model_name='equipment',
            name='groupid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jc.grouper'),
        ),
        migrations.AddField(
            model_name='cabinet',
            name='motorroomid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jc.motorroom'),
        ),
        migrations.AddField(
            model_name='businessression',
            name='equipmentid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jc.equipment'),
        ),
    ]

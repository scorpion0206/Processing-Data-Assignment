# Generated by Django 3.0.6 on 2020-06-10 23:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MappedSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('account', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SyncBag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('source', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SyncItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('grade', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1)),
                ('syncBag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.SyncBag')),
            ],
        ),
        migrations.CreateModel(
            name='HistoryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_dataString6', models.UUIDField(default=uuid.uuid4)),
                ('status', models.IntegerField(choices=[(-1, 'Discarded'), (0, 'Current'), (1, 'Readonly')])),
                ('created', models.DateTimeField()),
                ('dataString0', models.URLField()),
                ('dataString1', models.DateTimeField()),
                ('dataString2', models.TextField(blank=True)),
                ('dataString3', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('[0-9][ ]*[0-9][ ]*[0-9][ ]*[0-9][ ]*[A-Za-z][ ]*[A-Za-z]')])),
                ('dataString4', models.CharField(blank=True, max_length=40)),
                ('dataString5', models.IntegerField(blank=True)),
                ('syncItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.SyncItem')),
            ],
        ),
        migrations.CreateModel(
            name='CurrentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_dataString6', models.UUIDField(default=uuid.uuid4)),
                ('status', models.IntegerField(choices=[(-1, 'Discarded'), (0, 'Current'), (1, 'Readonly')])),
                ('created', models.DateTimeField()),
                ('dataString0', models.URLField()),
                ('dataString1', models.DateTimeField()),
                ('dataString2', models.TextField(blank=True)),
                ('dataString3', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('[0-9][ ]*[0-9][ ]*[0-9][ ]*[0-9][ ]*[A-Za-z][ ]*[A-Za-z]')])),
                ('dataString4', models.CharField(blank=True, max_length=40)),
                ('dataString5', models.IntegerField(blank=True)),
                ('syncItem', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='application.SyncItem', verbose_name='current data')),
            ],
        ),
    ]

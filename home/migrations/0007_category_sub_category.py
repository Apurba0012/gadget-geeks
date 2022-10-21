# Generated by Django 4.1.1 on 2022-10-21 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('ca_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ca_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('sc_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sc_name', models.CharField(max_length=20)),
            ],
        ),
    ]
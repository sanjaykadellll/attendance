# Generated by Django 5.0.2 on 2024-02-17 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname1', models.CharField(blank=True, max_length=200, null=True)),
                ('lastname2', models.CharField(blank=True, max_length=100, null=True)),
                ('email1', models.CharField(blank=True, max_length=200, null=True)),
                ('address1', models.CharField(blank=True, max_length=200, null=True)),
                ('remark1', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]

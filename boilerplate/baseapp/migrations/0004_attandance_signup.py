# Generated by Django 5.0.2 on 2024-02-18 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0003_test2'),
    ]

    operations = [
        migrations.CreateModel(
            name='attandance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('userid', models.IntegerField(blank=True, null=True)),
                ('breaktime', models.IntegerField(blank=True, null=True)),
                ('entry', models.IntegerField(blank=True, null=True)),
                ('exit', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('password', models.IntegerField(blank=True, null=True)),
                ('confirmpassword', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
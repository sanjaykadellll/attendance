# Generated by Django 5.0.2 on 2024-02-18 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0004_attandance_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='confirmpassword',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

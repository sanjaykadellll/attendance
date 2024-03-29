# Generated by Django 4.2.6 on 2024-02-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0006_remove_attandance_breaktime_remove_attandance_entry_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attandance',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attandance',
            name='checkin',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attandance',
            name='checkout',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

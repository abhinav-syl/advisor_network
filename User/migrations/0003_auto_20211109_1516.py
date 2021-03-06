# Generated by Django 3.2.8 on 2021-11-09 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20211109_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='advisor',
        ),
        migrations.AddField(
            model_name='booking',
            name='advisor_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.CharField(max_length=20),
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-09 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_time', models.DateTimeField()),
                ('advisor', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='register',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.0.2 on 2020-01-10 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=20, verbose_name='イベント名')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='開始時刻')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='終了時刻')),
                ('is_active', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='images/')),
                ('contents', models.TextField()),
            ],
        ),
    ]

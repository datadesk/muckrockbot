# Generated by Django 2.1.2 on 2019-01-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muckrockbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muckrock_id', models.IntegerField()),
                ('title', models.CharField(max_length=2000)),
                ('slug', models.CharField(max_length=2000)),
                ('status', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=2000)),
                ('datetime_submitted', models.DateTimeField()),
                ('absolute_url', models.CharField(max_length=2000)),
            ],
        ),
    ]

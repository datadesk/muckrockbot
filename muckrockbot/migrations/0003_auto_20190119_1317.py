# Generated by Django 2.1.2 on 2019-01-19 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muckrockbot', '0002_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='datetime_submitted',
            field=models.DateTimeField(null=True),
        ),
    ]

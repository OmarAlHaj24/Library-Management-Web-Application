# Generated by Django 3.2.4 on 2021-07-11 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_alter_booking_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together=set(),
        ),
    ]

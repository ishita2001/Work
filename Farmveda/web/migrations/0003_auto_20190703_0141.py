# Generated by Django 2.2.1 on 2019-07-03 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20190701_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='contact_no',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='contact_no',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='name',
        ),
    ]

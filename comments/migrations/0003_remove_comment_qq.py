# Generated by Django 2.2 on 2019-05-03 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20190503_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='QQ',
        ),
    ]

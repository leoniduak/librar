# Generated by Django 2.1 on 2018-09-01 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20180901_0036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'permissions': (('can_create_author', 'Can create author'),)},
        ),
    ]

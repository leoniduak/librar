# Generated by Django 2.1 on 2018-08-31 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20180901_0029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Can view all lean books'),)},
        ),
    ]

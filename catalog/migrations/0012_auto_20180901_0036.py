# Generated by Django 2.1 on 2018-08-31 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20180901_0034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('all_lean', 'Can view all lean books'), ('can_mark_returned', 'Can view all lean books 222'))},
        ),
    ]

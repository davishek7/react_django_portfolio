# Generated by Django 3.2 on 2022-03-06 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avishek', '0002_auto_20220306_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='details',
            new_name='message',
        ),
    ]

# Generated by Django 3.1 on 2020-09-06 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200906_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='categery',
            new_name='category',
        ),
    ]
# Generated by Django 2.2.1 on 2019-06-10 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='interested_in',
            new_name='intrested',
        ),
    ]

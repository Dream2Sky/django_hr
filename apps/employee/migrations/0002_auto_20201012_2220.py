# Generated by Django 3.1.2 on 2020-10-12 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertoemployee',
            old_name='employee_id',
            new_name='employee',
        ),
        migrations.RenameField(
            model_name='usertoemployee',
            old_name='user_id',
            new_name='user',
        ),
    ]
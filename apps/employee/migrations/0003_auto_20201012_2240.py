# Generated by Django 3.1.2 on 2020-10-12 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20201012_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='number',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-15 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0018_auto_20201014_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='entry_status',
            field=models.PositiveIntegerField(choices=[(0, '未入职'), (1, '已入职')], default=0),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['user'], name='employee_user_id_7ab7e5_idx'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['mobile'], name='employee_mobile_1d49db_idx'),
        ),
    ]

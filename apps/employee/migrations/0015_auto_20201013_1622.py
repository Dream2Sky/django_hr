# Generated by Django 3.1.2 on 2020-10-13 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0014_orgunit_is_root'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgdepartment',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.orgunit'),
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-12 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('creator_id', models.CharField(max_length=100, verbose_name='创建人')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('modifier_id', models.CharField(max_length=100, verbose_name='修改人')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('delete_time', models.DateTimeField(null=True, verbose_name='删除时间')),
                ('deleter_id', models.CharField(max_length=100, verbose_name='删除人')),
                ('id', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField()),
                ('identity_card', models.CharField(max_length=18)),
                ('telephone', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='UserToEmployee',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('creator_id', models.CharField(max_length=100, verbose_name='创建人')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('modifier_id', models.CharField(max_length=100, verbose_name='修改人')),
                ('id', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('employee_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_to_employee',
            },
        ),
    ]
# Generated by Django 3.1.2 on 2020-10-18 09:43

from django.db import migrations, models
import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('creator_id', models.CharField(max_length=100, verbose_name='创建人')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('modifier_id', models.CharField(max_length=100, verbose_name='修改人')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('delete_time', models.DateTimeField(null=True, verbose_name='删除时间')),
                ('deleter_id', models.CharField(max_length=100, verbose_name='删除人')),
                ('id', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]

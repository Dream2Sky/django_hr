# Generated by Django 3.1.2 on 2020-10-13 07:12

import apps.base.models
from django.db import migrations, models
import django.db.models.deletion
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_auto_20201013_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrgDepartment',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('creator_id', models.CharField(max_length=100, verbose_name='创建人')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('modifier_id', models.CharField(max_length=100, verbose_name='修改人')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('delete_time', models.DateTimeField(null=True, verbose_name='删除时间')),
                ('deleter_id', models.CharField(max_length=100, verbose_name='删除人')),
                ('id', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.orgdepartment')),
            ],
            options={
                'abstract': False,
            },
            bases=(apps.base.models.NameNumberMixin, models.Model),
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='number',
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('creator_id', models.CharField(max_length=100, verbose_name='创建人')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('modifier_id', models.CharField(max_length=100, verbose_name='修改人')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('delete_time', models.DateTimeField(null=True, verbose_name='删除时间')),
                ('deleter_id', models.CharField(max_length=100, verbose_name='删除人')),
                ('id', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.orgdepartment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrgUnit',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('creator_id', models.CharField(max_length=100, verbose_name='创建人')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('modifier_id', models.CharField(max_length=100, verbose_name='修改人')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('delete_time', models.DateTimeField(null=True, verbose_name='删除时间')),
                ('deleter_id', models.CharField(max_length=100, verbose_name='删除人')),
                ('id', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.orgunit')),
            ],
            options={
                'abstract': False,
            },
            bases=(apps.base.models.NameNumberMixin, models.Model),
        ),
        migrations.AddField(
            model_name='orgdepartment',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.orgunit'),
        ),
        migrations.CreateModel(
            name='JobInformation',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('creator_id', models.CharField(max_length=100, verbose_name='创建人')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('modifier_id', models.CharField(max_length=100, verbose_name='修改人')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('delete_time', models.DateTimeField(null=True, verbose_name='删除时间')),
                ('deleter_id', models.CharField(max_length=100, verbose_name='删除人')),
                ('id', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
                ('position_type', models.IntegerField(choices=[(0, '主任职'), (1, '兼职'), (2, '借调'), (3, '委派'), (4, '助勤'), (5, '挂职')])),
                ('position_status', models.IntegerField(choices=[(0, '在职'), (1, '试用'), (2, '离职')])),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.orgdepartment')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.position')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.orgunit')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

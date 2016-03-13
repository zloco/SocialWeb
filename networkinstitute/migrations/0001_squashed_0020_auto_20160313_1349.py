# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-13 17:32
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone
import djchoices.choices


class Migration(migrations.Migration):

    replaces = [(b'networkinstitute', '0001_initial'), (b'networkinstitute', '0002_auto_20160306_1854'), (b'networkinstitute', '0003_project_status'), (b'networkinstitute', '0004_auto_20160308_2351'), (b'networkinstitute', '0005_auto_20160309_0118'), (b'networkinstitute', '0006_auto_20160309_0126'), (b'networkinstitute', '0007_auto_20160309_0129'), (b'networkinstitute', '0008_auto_20160309_0139'), (b'networkinstitute', '0009_auto_20160309_1233'), (b'networkinstitute', '0010_auto_20160309_1255'), (b'networkinstitute', '0011_auto_20160309_1522'), (b'networkinstitute', '0012_auto_20160309_2127'), (b'networkinstitute', '0013_auto_20160311_1255'), (b'networkinstitute', '0014_auto_20160311_1258'), (b'networkinstitute', '0015_customuser_username'), (b'networkinstitute', '0016_auto_20160312_2357'), (b'networkinstitute', '0017_auto_20160313_0228'), (b'networkinstitute', '0018_auto_20160313_0313'), (b'networkinstitute', '0019_auto_20160313_0952'), (b'networkinstitute', '0020_auto_20160313_1349')]

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Faculty', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('facebook', models.CharField(blank=True, default=None, max_length=100)),
                ('twitter', models.CharField(blank=True, default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('deadline', models.DateField()),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectOwner',
            fields=[
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='networkinstitute.ProjectOwner'),
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='password',
            field=models.CharField(default=datetime.datetime(2016, 3, 8, 22, 51, 25, 297000, tzinfo=utc), max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='facebook',
            field=models.CharField(blank=True, default=None, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='twitter',
            field=models.CharField(blank=True, default=None, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateField(help_text='Please state the last date for applying to the project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(help_text='Please provide a description, be sure to mention skills required, number of jobs available etc.'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to=b'auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to=b'auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'default_permissions': ('add', 'change', 'delete'), 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='twitter',
        ),
        migrations.AddField(
            model_name='project',
            name='faculties',
            field=models.ManyToManyField(help_text='To select more faculties, hold ctrl for Windows or command for Mac', related_name='faculties', to=b'networkinstitute.Faculty'),
        ),
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateField(help_text='Please state the last date for applying to the project as yyyy-mm-dd'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('O', b'Operative'), ('A', b'Approved'), ('D', b'Declined')], default='O', max_length=1, validators=[djchoices.choices.ChoicesValidator({'A': b'Approved', 'D': b'Declined', 'O': b'Operative'})])),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='networkinstitute.Project')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
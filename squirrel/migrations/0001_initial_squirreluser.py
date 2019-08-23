# Generated by Django 2.2.1 on 2019-08-21 06:06

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# squirrel.migrations.0012_article_thumbnail_url

class Migration(migrations.Migration):

    replaces = [('squirrel', '0001_initial'), ('squirrel', '0002_auto_20190602_1117'), ('squirrel', '0003_auto_20190602_1119'), ('squirrel', '0004_auto_20190602_1120'), ('squirrel', '0005_auto_20190602_1121'), ('squirrel', '0006_auto_20190610_1920'), ('squirrel', '0007_auto_20190610_1929'), ('squirrel', '0008_auto_20190611_0634'), ('squirrel', '0009_auto_20190626_1232'), ('squirrel', '0010_auto_20190626_1234'), ('squirrel', '0011_auto_20190626_1235'), ('squirrel', '0012_article_thumbnail_url'), ('squirrel', '0013_squirreluser')]

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('teaser_text', models.TextField(blank=True, editable=False, max_length=500)),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='date published')),
                ('download_date', models.DateTimeField(blank=True, null=True, verbose_name='date downloaded')),
                ('author', models.CharField(blank=True, max_length=250, null=True)),
                ('publisher', models.CharField(blank=True, max_length=250, null=True)),
                ('copyright', models.CharField(blank=True, max_length=250, null=True)),
                ('download_url', models.URLField(blank=True)),
                ('source_html', models.TextField()),
                ('source_markdown', models.TextField(editable=False)),
                ('wordcount', models.BigIntegerField(blank=True, editable=False, null=True)),
                ('thumbnail_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SquirrelUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
# Generated by Django 2.2.1 on 2019-08-21 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0001_initial_squirreluser'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='isRead',
            field=models.BooleanField(default=False),
        ),
    ]
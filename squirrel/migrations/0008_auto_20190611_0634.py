# Generated by Django 2.2.1 on 2019-06-11 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0007_auto_20190610_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='source_html',
            field=models.TextField(),
        ),
    ]

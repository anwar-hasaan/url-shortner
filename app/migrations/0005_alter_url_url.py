# Generated by Django 4.1.2 on 2022-10-26 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_url_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.URLField(editable=False, max_length=1000),
        ),
    ]
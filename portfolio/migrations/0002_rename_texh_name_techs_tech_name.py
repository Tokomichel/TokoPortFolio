# Generated by Django 4.1.1 on 2022-10-17 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='techs',
            old_name='texh_name',
            new_name='tech_name',
        ),
    ]

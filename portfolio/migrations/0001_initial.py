# Generated by Django 4.1.1 on 2022-10-17 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=300)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField(blank=True)),
                ('imageP', models.ImageField(upload_to='photo/')),
                ('image2', models.ImageField(blank=True, upload_to='photo/')),
                ('image3', models.ImageField(blank=True, upload_to='photo/')),
                ('en_equipe', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Techs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texh_name', models.CharField(max_length=25)),
                ('project', models.ManyToManyField(to='portfolio.projects')),
            ],
        ),
    ]

# Generated by Django 3.1.6 on 2021-07-19 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('don', '0002_donneur_montant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donneur',
            name='montant',
        ),
        migrations.AlterField(
            model_name='donneur',
            name='pays',
            field=models.CharField(default='fr', max_length=40),
        ),
    ]
# Generated by Django 3.1.6 on 2021-03-14 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0025_remove_menu_produits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='nom',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]
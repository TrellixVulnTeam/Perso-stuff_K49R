# Generated by Django 3.1.6 on 2021-07-22 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adhesion', '0003_adherent_vu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adherent',
            name='vu',
        ),
        migrations.AddField(
            model_name='adhesion',
            name='vu',
            field=models.BooleanField(default=False),
        ),
    ]
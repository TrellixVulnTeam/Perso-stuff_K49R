# Generated by Django 3.1.6 on 2021-03-14 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0017_auto_20210314_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulairecontact',
            name='prestations',
            field=models.CharField(default='Autres', max_length=20),
        ),
    ]
# Generated by Django 3.2.4 on 2021-06-09 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paiement', '0029_auto_20210608_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='panier_produit',
            name='boisson',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='panier_produit',
            name='garniture',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='panier_produit',
            name='sauce',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='panier_produit',
            name='supplement',
            field=models.TextField(blank=True, null=True),
        ),
    ]
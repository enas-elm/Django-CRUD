# Generated by Django 4.1.4 on 2022-12-16 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
    ]

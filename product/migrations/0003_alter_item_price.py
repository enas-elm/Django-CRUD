# Generated by Django 4.1.4 on 2022-12-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
# Generated by Django 5.0.7 on 2024-07-15 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegitables', '0005_alter_product_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.CharField(choices=[('vegetables', 'vegetables'), ('fruits', 'fruits'), ('meat', 'meat')], max_length=70, verbose_name='Category'),
        ),
    ]

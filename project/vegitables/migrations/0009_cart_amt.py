# Generated by Django 5.0.7 on 2024-07-16 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegitables', '0008_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='amt',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

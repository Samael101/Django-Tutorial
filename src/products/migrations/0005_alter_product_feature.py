# Generated by Django 4.1.2 on 2022-10-15 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_alter_product_summary"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="feature",
            field=models.BooleanField(default=False),
        ),
    ]
